import cv2
import numpy as np

# Load the image
img = cv2.imread('2_pencils.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Canny edge detection
edges = cv2.Canny(gray, 50, 150)

# Find contours in the edge map
contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Filter out contours that are not pencil-like
pencil_contours = []
for contour in contours:
    area = cv2.contourArea(contour)
    x, y, w, h = cv2.boundingRect(contour)
    aspect_ratio = float(w)/h
    if area > 50 and aspect_ratio > 1:
        pencil_contours.append(contour)

# Find the length of each pencil
pencil_lengths = []
for contour in pencil_contours:
    rect = cv2.minAreaRect(contour)
    (x, y), (w, h), angle = rect
    length = max(w, h)
    pencil_lengths.append(length * 0.1)  # convert px to mm

# Find the angle between the two pencils
pencil_angles = []
for contour in pencil_contours:
    rect = cv2.minAreaRect(contour)
    (x, y), (w, h), angle = rect
    pencil_angles.append(angle)
angle_between_pencils = abs(pencil_angles[0] - pencil_angles[1])

# Create a mask image
mask1 = np.zeros_like(img)
cv2.drawContours(mask1, [pencil_contours[0]], -1, (255, 255, 255), -1)
mask2 = np.zeros_like(img)
cv2.drawContours(mask2, [pencil_contours[1]], -1, (255, 255, 255), -1)
intersection = cv2.bitwise_and(mask1, mask2)

# Highlight the region of interference and draw the pencil lengths
cv2.drawContours(img, pencil_contours, -1, (0, 255, 0), 2)
cv2.drawContours(img, [pencil_contours[0]], -1, (0, 0, 255), 2)
cv2.putText(img, f"Pencil A: {pencil_lengths[0]:.2f} mm", (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
cv2.putText(img, f"Pencil B: {pencil_lengths[1]:.2f} mm", (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
cv2.putText(img, f"Angle: {angle_between_pencils:.2f} deg", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)

# Display the output
cv2.imshow('Pencils', img)
cv2.waitKey(0)
cv2.destroyAllWindows()