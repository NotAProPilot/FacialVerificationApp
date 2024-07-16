from tkinter import filedialog, messagebox, Tk, Canvas, Button, PhotoImage, Label, Frame
from pathlib import Path
from PIL import Image, ImageTk
from main import FaceVerification

# Initialize the FaceVerification object
face_verifier = FaceVerification()

def upload_photo():
    """Handles the uploading of a photo ID, shows the image, and checks for face detection."""
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
    if file_path:
        success = face_verifier.upload_photo_id(file_path)
        if success:
            show_image(file_path, photo_id_label)
            messagebox.showinfo("Success", "Photo ID uploaded and face extracted successfully.")
        else:
            messagebox.showerror("Error", "No face detected in the photo ID or file could not be read.")

def capture_photo():
    """Captures a photo using the webcam, shows the captured image, and checks for face detection."""
    success = face_verifier.capture_webcam_images()
    if success:
        show_image(face_verifier.captured_image_path, captured_image_label)
        messagebox.showinfo("Success", "Image captured successfully.")
    else:
        messagebox.showerror("Error", "Failed to capture image from webcam.")

def verify_faces():
    """Verifies if the uploaded photo ID and the captured image from webcam match."""
    result = face_verifier.verify_faces()
    if result is None:
        messagebox.showerror("Error", "Missing images for verification.")
    elif result:
        messagebox.showinfo("Success", "Faces match!")
    else:
        messagebox.showinfo("Failure", "Faces do not match.")

def show_image(image_path, label):
    """Displays an image on the specified label.

    Args:
        image_path (str): Path to the image file.
        label (tk.Label): The label widget to display the image.
    """
    image = Image.open(image_path)
    image = image.resize((300, 300))  # Adjust size to 300x300 pixels
    photo = ImageTk.PhotoImage(image)

    label.config(image=photo, width=300, height=300)  # Set label size
    label.image = photo

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\FIT\Junior Year\Official classes\SPRING 2024\Image Processing\IPR_Final Project\Finalv3\Final_Assignment_IPR\assets\frame0")

def relative_to_assets(path: str) -> Path:
    """Converts a relative path to an absolute path within the assets directory.

    Args:
        path (str): Relative path to the asset.

    Returns:
        Path: Absolute path to the asset.
    """
    return ASSETS_PATH / Path(path)

# Initialize main window
window = Tk()
window.geometry("1124x697")
window.configure(bg="#01005E")

# Configure the main frame
frame = Frame(window, bg="#01005E")
frame.grid(row=0, column=0, sticky="nsew")

# Configure the canvas
canvas = Canvas(
    frame,
    bg="#01005E",
    height=697,
    width=1124,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.grid(row=0, column=0, columnspan=2, rowspan=4)

canvas.create_rectangle(
    0.0,
    0.0,
    1124.0,
    697.0,
    fill="#01004B",
    outline=""
)

# Load and place background image
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png")
)
image_1 = canvas.create_image(
    500,
    300,
    image=image_image_1
)

# Configure labels for the uploaded photo ID and captured image
photo_id_label = Label(frame, bg=frame.cget("bg"))  # Match frame background color
photo_id_label.grid(row=0, column=0, padx=(90, 20), pady=20, sticky="n")
photo_id_text = Label(frame, text="Uploaded Photo ID", bg=frame.cget("bg"), fg="white")  # Match frame background color
photo_id_text.grid(row=1, column=0, padx=(100, 20), sticky="n")

captured_image_label = Label(frame, bg=frame.cget("bg"))  # Match frame background color
captured_image_label.grid(row=0, column=1, padx=(0, 20), pady=20, sticky="n")
captured_image_text = Label(frame, text="Captured Image From Camera", bg=frame.cget("bg"), fg="white")  # Match frame background color
captured_image_text.grid(row=1, column=1, padx=(0, 20), sticky="n")

# Load and place buttons
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png")
)
button_1 = Button(
    frame,
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=upload_photo,
    relief="flat"
)
button_1.grid(row=2, column=0, padx=(100, 20), pady=20, sticky="n")

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png")
)
button_2 = Button(
    frame,
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=verify_faces,
    relief="flat"
)
button_2.grid(row=3, column=0, columnspan=2, pady=20 , sticky="n")

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png")
)
button_3 = Button(
    frame,
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=capture_photo,
    relief="flat"
)
button_3.grid(row=2, column=1, padx=(0, 30), pady=20, sticky="n")

# Configure padding for text labels
photo_id_text.grid_configure(pady=(0, 20))
captured_image_text.grid_configure(pady=(0, 20))

# Center the window on the screen
window.update_idletasks()
window_width = window.winfo_width()
window_height = window.winfo_height()

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))

window.geometry(f'{window_width}x{window_height}+{x}+{y}')

# Prevent window resizing
window.resizable(False, False)
window.mainloop()

