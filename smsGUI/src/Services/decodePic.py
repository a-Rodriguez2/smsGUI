import threading
from ultralytics import YOLO
import cv2
import numpy as np
from pylibdmtx.pylibdmtx import decode as qr_decode
from pyzbar.pyzbar import decode as barcode_decode

def decode_main(model_path: str, img_path: str, is_qr_detection: bool):
    model = YOLO(model_path)
    img = cv2.imread(img_path)
    results = model(img)
    result = results[0]

    highest_confidence = 0
    crop_img = None

    for box in result.boxes:
        class_idx = int(box.cls[0].item())
        label = result.names[class_idx]
        if label in ['2DMatrix', 'PPID']:
            confidence = box.conf.item()
            if confidence > highest_confidence:
                highest_confidence = confidence
                x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())
                crop_img = img[(y1 - 10):(y2 + 10), (x1 - 10):(x2 + 10)]

    if crop_img is not None:
        successful_decode_event = threading.Event()
        decode_data = []
        threads = []
        rotation_steps = [0, 15, -15, 30, -30, 45, -45, 60, -60, 75, -75, 90, -90]
        brightness_range = range(0, -101, -10)
        contrast_range = np.arange(0, 1.21, 0.2)
        sharpness_values = range(4, 10)

        for angle in rotation_steps:
            thread = threading.Thread(target=process_image, args=(crop_img, angle, brightness_range, contrast_range, sharpness_values, is_qr_detection, successful_decode_event, decode_data))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        if successful_decode_event.is_set():
            print("Successfully decoded.")
            return True, decode_data[0]  # Return the first successful decode
        else:
            print("No successful decode with the tried parameters.")
            return False, None
    else:
        print(f'QR/Barcode not detected within {img_path}.')
        return False, None

def process_image(crop_img, angle, brightness_range, contrast_range, sharpness_values, is_qr_detection, successful_decode_event, decode_data):
    if successful_decode_event.is_set():
        return

    rotated_image = rotate_image(crop_img, angle)
    for beta in brightness_range:
        for alpha in contrast_range:
            for sharpness in sharpness_values:
                if successful_decode_event.is_set():
                    return

                decoded, matrix_code, modified_image = try_decode(rotated_image, alpha, beta, sharpness, is_qr_detection)
                if decoded:
                    print(f"Decoded Matrix Code: {matrix_code}")
                    print(f"Rotation: {angle} degrees, Brightness: {beta}, Contrast: {alpha}, Sharpness: {sharpness}")
                    successful_decode_event.set()
                    decode_data.append(matrix_code)  # Store the decoded code
                    break
#res
def rotate_image(image, angle):
    height, width = image.shape[:2]
    center = (width / 2, height / 2)
    rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
    abs_cos = abs(rotation_matrix[0, 0])
    abs_sin = abs(rotation_matrix[0, 1])
    bound_w = int(height * abs_sin + width * abs_cos)
    bound_h = int(height * abs_cos + width * abs_sin)
    rotation_matrix[0, 2] += bound_w / 2 - center[0]
    rotation_matrix[1, 2] += bound_h / 2 - center[1]
    return cv2.warpAffine(image, rotation_matrix, (bound_w, bound_h), flags=cv2.INTER_LANCZOS4)

def try_decode(image, alpha, beta, kernel_value, is_qr_detection):
    modified_image = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)
    kernel = np.array([[0, -1, 0], [-1, kernel_value, -1], [0, -1, 0]])
    sharpened_image = cv2.filter2D(modified_image, -1, kernel)
    decoded_data = qr_decode(sharpened_image) if is_qr_detection else barcode_decode(sharpened_image)
    if decoded_data:
        decoded_string = decoded_data[0].data.decode('utf-8')
        if decoded_string.isalnum() and len(decoded_string) > 10:  # Check if the decoded string is alphanumeric
            return True, decoded_string, sharpened_image
    # Ensure there is always a return statement providing a tuple of three values
    return False, "", sharpened_image