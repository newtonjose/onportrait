import cv2
import logging
from PIL import Image
from resizeimage import resizeimage

logger = logging.getLogger(__name__)
UPLOAD_FOLDER = './files/uploads'


class FaceTagger:
    def __init__(self,
                 casc_path="./files/haarcascade_frontalface_default.xml"):

        self.casc_path = casc_path
        self.faceCasc = cv2.CascadeClassifier(casc_path)

    @staticmethod
    def _resize_image(image_path):

        with open(image_path, 'r+b') as f:
            with Image.open(f) as image:
                cover = resizeimage.resize_cover(image, [700, 400])
                cover.save(image_path, image.format)

    def image_process(self, image_path):
        """
        process image and return faces coordens
        :return:
        """

        self._resize_image(image_path)

        image = cv2.imread(image_path)
        image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        faces = self.faceCasc.detectMultiScale(
            image_gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv2.CASCADE_SCALE_IMAGE
        )

        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

        cv2.imwrite(image_path, image)
        #
        # cv2.imshow("Faces found", image)
        # cv2.waitKey(0)

        # convert faces to list of face coordinates
        faces_list = []
        for i in range(len(faces)):
            f = faces[i]
            faces_list.append({
                'x': int(f[1]),
                'y': int(f[0]),
                'width': int(f[2]),
                'height': int(f[3])
             })

        if not faces_list:
            raise Exception("NotFound faces on Image!")

        return faces_list
