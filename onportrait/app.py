import os
import logging

from flask import Flask, Blueprint, render_template
from flask import jsonify
from flask import request
from werkzeug.utils import secure_filename

from config import ALLOWED_EXTENSIONS, UPLOAD_FOLDER
from onportrait.exceptions import *
from onportrait.models import Portrait
from onportrait.utils.facetagger import FaceTagger

app = Flask(__name__, static_folder='./public', template_folder='./static')

index_blueprint = Blueprint('index', __name__)
upload_blueprint = Blueprint('upload', __name__)
add_portrait_blueprint = Blueprint('add_portrait', __name__)


@upload_blueprint.errorhandler(500)
def internal_exception_handler(error):
    logger.error(error)
    return jsonify({'errors': {'internal_error': [str(error)]}}), 500


# ref: https://stackoverflow.com/questions/40920163/http-status-code-for-invalid-format
@upload_blueprint.errorhandler(ImageUploadError)
def image_upload_exception_handler(error):
    return jsonify(
        {'errors': {'file_error': ['error on uploading image']}}), 422


@index_blueprint.route("/", methods=["GET"])
def index():
    return render_template('index2.html')


def _allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@upload_blueprint.route("/upload", methods=["POST"])
def upload():
    """
    From request get the file and save on UPLOAD_FOLDER, create a referency
    on database, after that process the image om opencv and return the faces
    detection
    :return:
    """

    # salvar imagem local ou no db
    if 'file' not in request.files:
        raise ImageUploadError

    file = request.files['file']
    if file.filename == '':
        raise ImageUploadError

    if file and _allowed_file(file.filename):
        try:
            filename = secure_filename(file.filename)
            filepath = os.path.join(UPLOAD_FOLDER, filename)
            file.save(os.path.join(filepath))
        except Exception as e:
            logger.error("Error: {0}".format(e))
            raise internal_exception_handler("error to save image!")

        # se não error, processar imagem usando opencv
        ft = FaceTagger()
        try:
            faces = ft.image_process(filepath)
        except Exception as e:
            logger.error("Error: {0}".format(e))
            raise internal_exception_handler("process image failed")

        # TODO: return image id (string) unique
        return jsonify({'data': {'faces': faces}}), 200
    else:
        return jsonify({'errors':
                        {'file_error': ['file format not allowed, ' +
                                        'only {0}'.format(
                                                ALLOWED_EXTENSIONS)]}}), 422


@add_portrait_blueprint.route("/add/portrait/<int:id>", methods=["PUT"])
def add_portrait(id):
    """
    Get infos of portrait and save on database
    :param id:
    :return:
    """

    name = request.json['name']
    social_media = request.json['instagram']

    try:
        pt = Portrait(id)
    except Exception as e:
        pass

    logger.info("{}, {}".format(name, social_media))

    return "", 405
