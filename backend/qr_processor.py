import io
import qrcode
from PIL import Image
import cv2
import numpy as np

def generate_qr_code(data: str) -> bytes:
    """Generates a QR code image from input text/URL and returns bytes."""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    byte_im = buf.getvalue()
    return byte_im

def decode_qr_code(image_bytes: bytes) -> str:
    """Decodes a QR code from uploaded image bytes using OpenCV."""
    nparr = np.frombuffer(image_bytes, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    
    detector = cv2.QRCodeDetector()
    data, bbox, straight_qrcode = detector.detectAndDecode(img)
    
    if data:
        return data
    else:
        return "Error: Could not detect a valid QR code in the uploaded image."
