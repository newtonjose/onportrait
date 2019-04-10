import logging
from flask import Blueprint, render_template
from flask import jsonify
from onportrait import app
from onportrait.utils.facetagger import FaceTagger
from onportrait.exceptions import *


logger = logging.getLogger(__name__)
index_blueprint = Blueprint('index', __name__)
upload_blueprint = Blueprint('upload', __name__)

@upload_blueprint.errorhandler(500)
def internal_exception_handler(error):
    logger.error(error)
    return jsonify({'errors': {'internal_error': [str(error)]}}), 500

@upload_blueprint.errorhandler(ImageProcessFailedError)
def image_process_exception_handler(error):
    return jsonify({'errors': {'internal_error': ['process image failed']}}), 500


@index_blueprint.route("/", methods=["GET"])
def index():
    return render_template('index.html')


@upload_blueprint.route("/upload", methods=["POST"])
def upload():
    """
    Salva referencia do arquino na base e salva localmente retorna error no
    servidor
    :return:
    """
    ov2 = FaceTagger()

    # salvar imagem local ou no db
    if None:
        return internal_exception_handler("Error to save image!")

    # se não error, processar imagem usando opencv
    try:
        faces = ov2.image_process("./files/arnold.jpg")
    except Exception as e:
        logger.error("Error: {0}".format(e))
        raise ImageProcessFailedError

    return jsonify({'data': {'faces': faces}}), 200
