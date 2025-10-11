import os
from werkzeug.utils import secure_filename

# Directory to save uploaded and processed images
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

def save_uploaded_file(file) -> str:
    """
    Save the uploaded file securely inside the uploads directory.

    Args:
        file: The uploaded file object (e.g., from Flask's request.files).

    Returns:
        str: The absolute path where the file was saved.
    """
    filename = secure_filename(file.filename)
    filepath = os.path.join(UPLOAD_DIR, filename)
    file.save(filepath)
    return filepath


def get_result_path(filename: str) -> str:
    """
    Generate a safe file path for processed images.

    Args:
        filename (str): Original uploaded filename.

    Returns:
        str: Path where the processed (result) file should be stored.
    """
    safe_name = secure_filename(filename)
    result_name = "result_" + safe_name
    return os.path.join(UPLOAD_DIR, result_name)
