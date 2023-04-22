import cv2
import numpy as np

def add_gaussian_noise(image):
    mean = 0
    var = 100
    sigma = var
    gaussian = np.random.normal(mean, sigma, image.shape)
    noisy_image = image + gaussian
    noisy_image = np.clip(noisy_image, 0, 255)
    return noisy_image.astype(np.uint8)

# Read the image
image = cv2.imread('image.jpg')

# Add Gaussian noise to the image
noisy_image = add_gaussian_noise(image)

# Save the resulting image
cv2.imwrite('noisy_image.jpg', noisy_image)
