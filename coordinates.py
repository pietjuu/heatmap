import cv2

# Load your image
image = cv2.imread("blueprint2.jpg")  # replace with the path to your image

# Define the callback function that will be called by OpenCV when the user clicks on the image
def print_coordinates(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f'Point: ({x}, {y})')

# Create a named window
cv2.namedWindow('image', cv2.WINDOW_NORMAL)

# Connect the callback function to the window
cv2.setMouseCallback('image', print_coordinates)

# Display the image
cv2.imshow('image', image)
cv2.resizeWindow('image', 600, 600)  # Adjust the size as needed

# Wait for the user to close the window
cv2.waitKey(0)
cv2.destroyAllWindows()
