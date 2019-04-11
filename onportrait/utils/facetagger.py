import cv2
import logging

logger = logging.getLogger(__name__)


class FaceTagger:
    def __init__(self,
                 casc_path="./files/haarcascade_frontalface_default.xml"):
        self.casc_path = casc_path
        self.faceCasc = cv2.CascadeClassifier(casc_path)

    def image_process(self, image_path):
        """
        process image and return faces coordens
        :return:
        """

        image = cv2.imread(image_path)
        image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        faces = self.faceCasc.detectMultiScale(
            image_gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv2.CASCADE_SCALE_IMAGE
        )


        # for (x, y, w, h) in faces:
        #     cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        #
        # cv2.imshow("Faces found", image)
        # cv2.waitKey(0)

        # convert faces to list of face coordinates
        faces_list = []
        for i in range(len(faces)):
            f = faces[i]
            faces_list.append({
                'x': int(f[0]),
                'y': int(f[1]),
                'hight': int(f[2]),
                'leght': int(f[3]),
             },)

        logger.error(
            "Found {0} faces at coords {1}!".format(len(faces), faces_list))
        return faces_list
