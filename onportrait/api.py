import os
import io
import base64

from flask import Blueprint
from flask import jsonify, request, send_file
from werkzeug.utils import secure_filename

from onportrait import app
from onportrait.exceptions import *
from onportrait.models import Portrait
from onportrait.utils.facetagger import FaceTagger

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
UPLOAD_FOLDER = './files/uploads'
logger = app.logger

index_blueprint = Blueprint('index', __name__)
upload_blueprint = Blueprint('upload', __name__)
add_portrait_blueprint = Blueprint('add_portrait', __name__)
get_portrait_image_blueprint = Blueprint('get_portrait_image', __name__)
get_portrait_blueprint = Blueprint('get_portrait', __name__)


def internal_exception_handler(error):
    logger.error(error)
    return jsonify({'errors': {'internal_error': [str(error)]}}), 500


@upload_blueprint.errorhandler(ImageUploadError)
def image_upload_exception_handler(error):
    return jsonify(
        {'errors': {'file_error': ['error on uploading image']}}), 422


@get_portrait_blueprint.errorhandler(PortraitNotFound)
def get_portrait_exception_handler(error):
    return jsonify(
        {'errors': {'not_found_error':
                    ['portrait not found on the database']}}), 404


def _allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@upload_blueprint.route("/api/upload", methods=["POST"])
def upload():
    """
    From request get the file and save on UPLOAD_FOLDER, save image name on
    database, after that process the image using opencv and return the faces
    detection coordinates.
    :return:
    """

    # sa imagem local ou no db
    if 'file' not in request.files:
        raise ImageUploadError

    image_file = request.files['file']
    if image_file.filename == '':
        raise ImageUploadError

    if image_file and _allowed_file(image_file.filename):

        filename = secure_filename(image_file.filename)
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        try:
            image_file.save(os.path.join(filepath))
        except Exception as e:
            return internal_exception_handler("error to save image: {}".format(e))

        # object to process using OpenCV2
        ft = FaceTagger()
        try:
            faces = ft.image_process(filepath)
        except Exception as e:
            return internal_exception_handler(
                "process image failed: {}".format(e))

        # save image face coordinate on simple DB
        try:
            pt = Portrait.add(file_name=filename, faces_coods=faces)
        except Exception as e:
            logger.error(e)
            return internal_exception_handler(
                "error to save image coordinates on db!")

        return jsonify({'data': {'id': pt.id, 'faces': faces}}), 200
    else:
        return jsonify({'errors':
                        {'file_error': ['file format not allowed, ' +
                                        'only {0}'.format(
                                                ALLOWED_EXTENSIONS)]}}), 422


@add_portrait_blueprint.route("/api/add/portrait/<int:image_id>",
                              methods=["PUT"])
def add_portrait(image_id):
    """
    Get name of face on "portrait" and save on database to this specific image

    :param image_id: is number int returned on upload URI
    :return:
    """

    name = request.json['name']
    instagram = request.json['instagram']

    try:
        Portrait.update(id=image_id, name=name, social_media=instagram)
    except Exception as e:
        logger.error(e)
        internal_exception_handler("error to update image ref on db!")

    return "", 200


def _get_portrait(id):
    pt = None
    try:
        pt = Portrait.query.get(id)
    except Exception as e:
        logger.error(e)
        internal_exception_handler("error to update image ref on db!")

    return pt


@get_portrait_image_blueprint.route("/api/get/portrait/image/<int:image_id>",
                                    methods=["GET"])
def get_portrait_image(image_id):
    """
    From DB, get image infos and open image from local dir and return the image
    as binary file.

    :param image_id:
    :return:
    """
    pt = _get_portrait(image_id)
    image_path = os.path.join(UPLOAD_FOLDER, '{}'.format(pt.file_name))
    try:
        with open(image_path, 'rb') as image:
            return send_file(
                io.BytesIO(image.read()),
                attachment_filename='{}.jpeg'.format(pt.file_name),
                mimetype='image/jpg'
            )
    except Exception as e:
        logger.error(e)
        raise internal_exception_handler("error to open image on db!")


@get_portrait_blueprint.route("/api/get/portrait/<int:image_id>",
                              methods=["GET"])
def get_portrait(image_id):
    """
    From DB, return Return image infos: face_coods, name, social_media, image
    file

    :param image_id:
    :return:
    """
    pt = _get_portrait(image_id)

    if pt:
        return jsonify({'data': {'faces': pt.faces_coods, 'name': pt.name,
                                 'instagram': pt.social_media}}), 200
    else:
        raise PortraitNotFound