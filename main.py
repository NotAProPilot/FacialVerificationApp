import cv2
from deepface import DeepFace
import os

class FaceVerification:
    """Class for handling face verification logic."""
    
    def __init__(self):
        """Initialize the FaceVerification class."""
        self.photo_id_path = None
        self.captured_image_path = "captured.png"
        self.extracted_image_path = "extracted.png"
        self.face_cascade = cv2.CascadeClassifier(
            cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
        )

    def upload_photo_id(self, file_path):
        """Handle the upload of the photo ID and extract face.

        Args:
            file_path (str): The path to the photo ID image.

        Returns:
            bool: True if face is extracted successfully, False otherwise.
        """
        self.photo_id_path = file_path
        return self.extract_face_from_photo_id()

    def extract_face_from_photo_id(self):
        """Extract face from the uploaded photo ID.

        Returns:
            bool: True if face is extracted successfully, False otherwise.
        """
        image = cv2.imread(self.photo_id_path)
        if image is None:
            return False

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
        
        if len(faces) == 0:
            return False

        # Assuming the first detected face is the one we want
        (x, y, w, h) = faces[0]
        x, y, w, h = x - 25, y - 40, w + 50, h + 70
        face = image[y:y+h, x:x+w]
        cv2.imwrite(self.extracted_image_path, face)
        return True

    def capture_webcam_images(self):
        """Capture images from the webcam until manually stopped.

        Returns:
        bool: True if image is captured successfully, False otherwise.
        """
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            return False

        while True:
            ret, frame = cap.read()
            if ret:
                cv2.imshow('Webcam', frame)
                if cv2.waitKey(1) & 0xFF == 13:  # ASCII code for Enter key is 13
                    cv2.imwrite(self.captured_image_path, frame)
                    break
            else:
                return False
        cap.release()
        cv2.destroyAllWindows()
        return True

    def verify_faces(self):
        """Verify the uploaded photo ID and the captured image.

        Returns:
            bool: True if the faces match, False otherwise, or None if images are missing.
        """
        if not self.photo_id_path or not os.path.exists(self.captured_image_path) or not os.path.exists(self.extracted_image_path):
            return None
        result = DeepFace.verify(img1_path=self.extracted_image_path, img2_path=self.captured_image_path)
        return result['verified']
