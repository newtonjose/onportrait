import os
import logging

from flask import Blueprint, render_template
from flask import jsonify
from flask import request
from flask import redirect, url_for
from werkzeug.utils import secure_filename

from onportrait.utils.facetagger import FaceTagger
from config import ALLOWED_EXTENSIONS, UPLOAD_FOLDER
# from onportrait.utils.
from onportrait.exceptions import *

# ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

logger = logging.getLogger(__name__)
index_blueprint = Blueprint('index', __name__)
upload_blueprint = Blueprint('upload', __name__)


@upload_blueprint.errorhandler(500)
def internal_exception_handler(error):
    logger.error(error)
    return jsonify({'errors': {'internal_error': [str(error)]}}), 500


# ref: https://stackoverflow.com/questions/40920163/http-status-code-for-invalid-format
@upload_blueprint.errorhandler(ImageUploadError)
def image_upload_exception_handler(error):
    return jsonify(
        {'errors': {'file_error': ['error on uploading image']}}), 422


@upload_blueprint.errorhandler(ImageProcessFailedError)
def image_process_exception_handler(error="process image failed"):
    return jsonify({'errors': {'internal_error': [error]}}), 500


@index_blueprint.route("/", methods=["GET"])
def index():
    return render_template('index.html')


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@upload_blueprint.route("/upload", methods=["POST"])
def upload():
    """
    Salva referencia do arquino na base e salva localmente retorna error no
    servidor
    :return:
    """

    # salvar imagem local ou no db
    if 'file' not in request.files:
        raise ImageUploadError

    file = request.files['file']
    if file.filename == '':
        raise ImageUploadError

    if file and allowed_file(file.filename):
        try:
            filename = secure_filename(file.filename)
            filepath = os.path.join(UPLOAD_FOLDER, filename)
            file.save(os.path.join(filepath))
        except Exception as e:
            logger.error("Error: {0}".format(e))
            raise internal_exception_handler("Error to save image!")

        # se não error, processar imagem usando opencv
        ft = FaceTagger()
        try:
            faces = ft.image_process(filepath)
        except Exception as e:
            logger.error("Error: {0}".format(e))
            raise ImageProcessFailedError

        return jsonify({'data': {'faces': faces}}), 200
    else:
        return jsonify({'errors':
                        {'file_error': ['file format not allowed, ' +
                                        'only {0}'.format(
                                                ALLOWED_EXTENSIONS)]}}), 422
