import cv2
import os
from werkzeug.utils import secure_filename

# Directory to save uploaded and processed images
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

def detect_faces(image_file):
    """
    Detect faces in the given uploaded image file.
    
    Args:
        image_file: File object (from Flask's request.files) representing the uploaded image.
    
    Returns:
        tuple: (number_of_faces, output_path)  
            - number_of_faces (int): How many faces were detected  
            - output_path (str): Path to the processed image with rectangles drawn  
    """
    # Sanitize filename and save uploaded file
    filename = secure_filename(image_file.filename)
    filepath = os.path.join(UPLOAD_DIR, filename)
    image_file.save(filepath)

    # Load OpenCV's pre-trained face detector
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )

    # Read and convert to grayscale
    img = cv2.imread(filepath)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

    # Draw rectangles around detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Save result image
    output_path = os.path.join(UPLOAD_DIR, "result_" + filename)
    cv2.imwrite(output_path, img)

    return len(faces), output_path
