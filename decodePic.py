from ultralytics import YOLO
import cv2
import numpy as np
from pylibdmtx.pylibdmtx import decode as qr_decode
from pyzbar.pyzbar import decode as barcode_decode
from concurrent.futures import ThreadPoolExecutor, as_completed


# def decode_main(model_path: str, img_path: str, is_qr_detection: bool):
#     # find model and image files using their paths as method args
#     model = YOLO(model_path)
#     img = cv2.imread(img_path)
#     crop_img_2D = None
#     crop_img_PPID = None

#     matrixCode = None

#     results = model(img)
#     result = results[0]

#     highest_confidence = 0
#     for box in result.boxes:
#         class_idx = int(box.cls[0].item())  # Convert tensor to integer
#         label = result.names[class_idx]

#         # model identifies QR/barcode label, crop it out and create a new image
#         if label == '2DMatrix' :
            

#             confidence = box.conf.item()
#             if confidence > highest_confidence:
#                 highest_confidence = confidence
#                 # Extract bounding box coordinates and convert to list
#                 x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())

#                 # Crop the image
#                 crop_img_2D = img[(y1 - 10):(y2 + 10), (x1 - 10):(x2 + 10)]
#         if label == 'PPID' :
#              confidence = box.conf.item()
#              if confidence > highest_confidence:
#                  highest_confidence = confidence
#                  # Extract bounding box coordinates and convert to list
#                  x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())

#                  # Crop the image
#                  crop_img_PPID = img[(y1 - 10):(y2 + 10), (x1 - 10):(x2 + 10)]
#     # checks whether the cropped image including the QR/barcode even exists
#     if crop_img_2D is not None:
#         # Load the image
#         zoomed_frame = crop_img_2D
#         # Initialize variables for the loop
#         brightness_range = range(0, -101, -20)  # From 0 to -100 with -10 step
#         contrast_range = np.arange(0, 1.21, 0.3)  # From 0 to 1.2 with 0.2 step
#         sharpness_values = range(4, 10)  # From 4 to 9 for the kernel center value
#         rotation_steps = [15, -15, 30, -30, 45, -45, 60, -60, 75, -75, 90, -90]

#         found = False
#         futures = []
#         # Add a loop for rotation
        
#         for angle in rotation_steps:
#             rotated_image = rotate_image(zoomed_frame, angle)
#             for beta in brightness_range:
#                 for alpha in contrast_range:
#                     for sharpness in sharpness_values:
#                         decoded, matrixCode, modified_image = try_decode(rotated_image, alpha, beta, sharpness, is_qr_detection)
#                         if decoded:
#                             print(f"Decoded Matrix Code: {matrixCode}")
#                             print(
#                                 f"Rotation: {angle} degrees, Brightness: {beta}, Contrast: {alpha}, Sharpness: {sharpness}")
#                             # comment-out to view successful decode
#                             # cv2.imwrite(f'successful_decode_{angle}_{beta}_{alpha}_{sharpness}.png', modified_image)
#                             found = True
#                             break  # Exit sharpness loop
#                     if found:
#                         break  # Exit contrast loop
#                 if found:
#                     break  # Exit brightness loop
#             if found:
#                 break  # Exit rotation loop

#         if not found:
#             decoded_data = barcode_decode(zoomed_frame)
#             if decoded_data is not None:
#                 matrixCode=decoded_data[0].data.decode('utf-8')
#                 print(f"Decoded Matrix Code: {matrixCode}")
#                 return True, matrixCode
#             else:
#                 print("No successful decode with the tried parameters.")
#                 return False, None
#         else:
#             return True, matrixCode

#     # cropped image does not exist
#     else:
#         print(f'QR/Barcode not detected within {img_path}.')
#         return False, None

def decode_main(model_path: str, img_path: str, is_qr_detection: bool):
    model = YOLO(model_path)
    img = cv2.imread(img_path)
    crop_img_2D = None

    results = model(img)
    result = results[0]

    highest_confidence = 0
    for box in result.boxes:
        class_idx = int(box.cls[0].item())
        label = result.names[class_idx]
        confidence = box.conf.item()
        
        if label == '2DMatrix' and confidence > highest_confidence:
            highest_confidence = confidence
            x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())
            crop_img_2D = img[(y1 - 10):(y2 + 10), (x1 - 10):(x2 + 10)]

    if crop_img_2D is not None:
        zoomed_frame = crop_img_2D
        brightness_range = range(0, -101, -20)
        contrast_range = np.arange(0, 1.21, 0.3)
        sharpness_values = range(4, 10)
        rotation_steps = [15, -15, 30, -30, 45, -45, 60, -60, 75, -75, 90, -90]

        with ThreadPoolExecutor(max_workers=8) as executor:
            futures = []
            for angle in rotation_steps:
                for beta in brightness_range:
                    for alpha in contrast_range:
                        for sharpness in sharpness_values:
                            futures.append(executor.submit(try_decode, rotate_image(zoomed_frame, angle), alpha, beta, sharpness, is_qr_detection))
            
            # Process the results as they complete
            for future in as_completed(futures):
                decoded, matrixCode, modified_image = future.result()
                if decoded:
                    print(f"Decoded Matrix Code: {matrixCode}")
                    print(f"Details: Rotation: {angle}, Brightness: {beta}, Contrast: {alpha}, Sharpness: {sharpness}")
                    return True, matrixCode

        print("No successful decode with the tried parameters.")
        return False, None
    else:
        print(f'QR/Barcode not detected within {img_path}.')
        return False, None
# Function to rotate the image
def rotate_image(image, angle):
    # Get the image dimensions (height, width)
    height, width = image.shape[:2]

    # Calculate the center of the image for rotation
    center = (width / 2, height / 2)

    # Calculate the rotation matrix for the current angle
    rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)

    # Calculate the sine and cosine (these are the rotation matrix components)
    abs_cos = abs(rotation_matrix[0, 0])
    abs_sin = abs(rotation_matrix[0, 1])

    # Compute the new bounding dimensions of the image
    bound_w = int(height * abs_sin + width * abs_cos)
    bound_h = int(height * abs_cos + width * abs_sin)

    # Adjust the rotation matrix to consider the translation
    rotation_matrix[0, 2] += bound_w / 2 - center[0]
    rotation_matrix[1, 2] += bound_h / 2 - center[1]

    # Rotate the image without losing significant quality
    rotated_image = cv2.warpAffine(image, rotation_matrix, (bound_w, bound_h), flags=cv2.INTER_LANCZOS4)
    return rotated_image


# Function to apply modifications and attempt decoding
def try_decode(image, alpha, beta, kernel_value, is_qr_detection):
    modified_image = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)
    kernel = np.array([[0, -1, 0], [-1, kernel_value, -1], [0, -1, 0]])
    sharpened_image = cv2.filter2D(modified_image, -1, kernel)

    # check whether qr or barcode detection here
    if is_qr_detection:
        decoded_data = qr_decode(sharpened_image)

    if decoded_data:
        return True, decoded_data[0].data.decode('utf-8'), sharpened_image
    else:
        return False, "", sharpened_image
