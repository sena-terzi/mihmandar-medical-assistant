"""
YOLO + OCR based identity information extraction pipeline.

Used to simplify patient appointment workflows.
"""

# Capture patient ID image
frame = capture_camera_frame()

# Detect ID region using YOLO
detections = yolo_model.predict(frame)

# Extract detected region
roi = crop_detected_region(frame, detections)

# OCR text extraction
text = ocr_engine.read(roi)

# Parse identity information
patient_id = extract_identity_number(text)

print("Detected ID:", patient_id)
