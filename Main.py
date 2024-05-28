import tkinter as tk
from tkinter import filedialog, messagebox
import customtkinter as ctk
import cv2
from deepface import DeepFace
import os

# Initialize customtkinter
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class FaceVerificationApp(ctk.CTk):
    """Main application class for face verification using customtkinter."""

    def __init__(self):
        """Initialize the FaceVerificationApp class."""
        super().__init__()

        self.title("Face Verification Tool")
        self.geometry("400x300")

        # Button to upload photo ID
        self.upload_button = ctk.CTkButton(self, text="Upload Photo ID", command=self.upload_photo_id)
        self.upload_button.pack(pady=20)

        # Button to capture image from webcam
        self.capture_button = ctk.CTkButton(self, text="Capture Image from Webcam", command=self.capture_webcam_image)
        self.capture_button.pack(pady=20)

        # Button to verify faces
        self.verify_button = ctk.CTkButton(self, text="Verify", command=self.verify_faces)
        self.verify_button.pack(pady=20)

        self.photo_id_path = None
        self.captured_image_path = "captured.png"
        self.extracted_image_path = "extracted.png"

        # Load the pre-trained Haar Cascade for face detection
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    def upload_photo_id(self):
        """Handle uploading of the photo ID."""
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
        if file_path:
            self.photo_id_path = file_path
            if self.extract_face_from_photo_id():
                messagebox.showinfo("Success", "Photo ID uploaded and face extracted successfully")
            else:
                messagebox.showwarning("Warning", "No face detected in the uploaded photo ID.")

    def extract_face_from_photo_id(self):
        """Extract face from the uploaded photo ID."""
        image = cv2.imread(self.photo_id_path)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
        
        if len(faces) == 0:
            return False

        # Assuming the first detected face is the one we want
        (x, y, w, h) = faces[0]
        x = x - 25  # Padding to include more of the face
        y = y - 40
        w = w + 50
        h = h + 70
        
        face = image[y:y+h, x:x+w]
        cv2.imwrite(self.extracted_image_path, face)
        return True

    def capture_webcam_image(self):
        """Capture an image from the webcam."""
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        cap.release()

        if ret:
            cv2.imwrite(self.captured_image_path, frame)
            messagebox.showinfo("Success", "Image captured from webcam successfully")
        else:
            messagebox.showerror("Error", "Failed to capture image from webcam")

    def verify_faces(self):
        """Verify the uploaded photo ID and the captured image."""
        if not self.photo_id_path:
            messagebox.showwarning("Warning", "Please upload a photo ID first")
            return

        if not os.path.exists(self.captured_image_path):
            messagebox.showerror("Error", "Captured image not found. Please capture an image from the webcam.")
            return

        if not os.path.exists(self.extracted_image_path):
            messagebox.showerror("Error", "Extracted image from photo ID not found. Please upload a photo ID.")
            return

        try:
            result = DeepFace.verify(img1_path=self.extracted_image_path, img2_path=self.captured_image_path)
            verified = result['verified']
            if verified:
                messagebox.showinfo("Verification Result", "Verification successful!")
            else:
                messagebox.showinfo("Verification Result", "Verification failed: Not the same person")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

if __name__ == "__main__":
    app = FaceVerificationApp()
    app.mainloop()
