import os
import io
import base64

from flask import Blueprint
from flask import jsonify, request, make_response, render_template, send_file
from werkzeug.utils import secure_filename

from onportrait import app
from onportrait.exceptions import *
from onportrait.models import Portrait
from onportrait.utils.facetagger import FaceTagger
from onportrait.utils.serialize import serialize

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
UPLOAD_FOLDER = './files/uploads'
logger = app.logger

index_blueprint = Blueprint('index', __name__)
upload_blueprint = Blueprint('upload', __name__)
add_portrait_blueprint = Blueprint('add_portrait', __name__)
get_portrait_image_blueprint = Blueprint('get_portrait_image', __name__)
get_portrait_blueprint = Blueprint('get_portrait', __name__)


@upload_blueprint.errorhandler(500)
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

@index_blueprint.route("/", methods=["GET"])
def index():
    return render_template('index2.html')


def _allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@upload_blueprint.route("/api/upload", methods=["POST"])
def upload():
    """
    From request get the file and save on UPLOAD_FOLDER, create a referency
    on database, after that process the image om opencv and return the faces
    detection
    :return:
    """

    # salvar imagem local ou no db
    if 'image_file' not in request.files:
        logger.debug(request.files)
        raise ImageUploadError

    logger.debug(request.files)
    image_file = request.files['image_file']
    if image_file.filename == '':
        raise ImageUploadError

    if image_file and _allowed_file(image_file.filename):
        try:
            filename = secure_filename(image_file.filename)
            filepath = os.path.join(UPLOAD_FOLDER, filename)
            image_file.save(os.path.join(filepath))
        except Exception as e:
            raise internal_exception_handler("error to save image!")

        # se não error, processar imagem usando opencv
        ft = FaceTagger()
        try:
            faces = ft.image_process(filepath)
        except Exception as e:
            logger.error("Error: {0}".format(e))
            raise internal_exception_handler("process image failed")

        # salvar imagem no db
        try:
            pt = Portrait.add(file_name=filename, faces_coods=faces)
            logger.info("{}".format(pt.id))
        except Exception as e:
            logger.error(e)
            raise internal_exception_handler(
                "error to save image ref on db!")

        # TODO: return image id (string) unique
        return jsonify({'data': {'id': pt.id, 'faces': faces}}), 200
    else:
        return jsonify({'errors':
                        {'file_error': ['file format not allowed, ' +
                                        'only {0}'.format(
                                                ALLOWED_EXTENSIONS)]}}), 422


@add_portrait_blueprint.route("/api/add/portrait/<int:image_id>", methods=["PUT"])
def add_portrait(image_id):
    """
    Get infos of portrait and save on database
    :param image_id:
    :return:
    """

    name = request.json['name']
    instagram = request.json['instagram']

    try:
        Portrait.update(id=image_id, name=name, social_media=instagram)
    except Exception as e:
        logger.error(e)
        raise internal_exception_handler("error to update image ref on db!")

    return "", 200


def _get_portrait(id):
    try:
        pt = Portrait.query.get(id)
    except Exception as e:
        logger.error(e)
        raise internal_exception_handler("error to update image ref on db!")

    return pt


# return image infos: face_coods, name, social_media, image file
@get_portrait_image_blueprint.route("/api/get/portrait/image/<int:image_id>",
                                    methods=["GET"])
def get_portrait_image(image_id):
    """
    Return binary image
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

    :param image_id:
    :return:
    """
    pt = _get_portrait(image_id)

    if pt:
        return jsonify({'data': {'faces': pt.faces_coods, 'name': pt.name,
                                 'instagram': pt.social_media}}), 200
    else:
        raise PortraitNotFound
