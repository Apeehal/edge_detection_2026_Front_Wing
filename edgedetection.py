import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image_path = 'front wing.png'  # Replace with the path to your front wing image
image = cv2.imread(image_path)

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to reduce noise
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Apply Canny edge detection
edges = cv2.Canny(blurred, threshold1=50, threshold2=150)

# Display the results
plt.figure(figsize=(10, 6))

plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(1, 2, 2)
plt.title('Edge Detection')
plt.imshow(edges, cmap='gray')

plt.show()

