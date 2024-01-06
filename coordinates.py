import cv2

# Function to print coordinates on click
def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f'x={x}, y={y}')

# Load the image
img = cv2.imread('heatmap.jpg')

# Get the screen size
screen_res = 1280, 720  # replace with your screen resolution
scale_width = screen_res[0] / img.shape[1]
scale_height = screen_res[1] / img.shape[0]
scale = min(scale_width, scale_height)

# Resized window width and height
window_width = int(img.shape[1] * scale)
window_height = int(img.shape[0] * scale)

# Create a window and set the click event
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.resizeWindow('image', window_width, window_height)

cv2.setMouseCallback('image', click_event)

# Display the image
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
