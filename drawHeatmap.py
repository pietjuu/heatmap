import matplotlib.pyplot as plt
import pandas as pd
import cv2
import numpy as np
from matplotlib.colors import LinearSegmentedColormap

# Read the CSV file
data = pd.read_csv('coordinates.csv')

# Load your image
image = cv2.imread("blueprint2.jpg")  # replace with the path to your image

# Get the screen size
screen_res = 1280, 720  # replace with your screen resolution
scale_width = screen_res[0] / image.shape[1]
scale_height = screen_res[1] / image.shape[0]
scale = min(scale_width, scale_height)

# Resized window width and height
window_width = int(image.shape[1] * scale)
window_height = int(image.shape[0] * scale)

# Resize the image
resized_image = cv2.resize(image, (window_width, window_height))

fig, ax = plt.subplots(figsize=(window_width/80, window_height/80))  # 80 is a conversion factor from pixels to inches
ax.imshow(resized_image, cmap=plt.cm.gray)

# Create a green-to-yellow-to-red colormap
colors = [(0, 1, 0), (1, 1, 0), (1, 0, 0)]  # green -> yellow -> red
cmap_name = 'green_yellow_red'
n_bins = 1000
cm = LinearSegmentedColormap.from_list(cmap_name, colors, N=n_bins)

# Create a 2D histogram for the heatmap
heatmap, xedges, yedges = np.histogram2d(data['x'], data['y'], bins=(64,64))
extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]

# Display the heatmap using the custom colormap
plt.imshow(heatmap.T, extent=extent, origin='lower', cmap=cm, alpha=0.5)

# Save the image
plt.savefig("blueprintWithHeatmap.jpg")
plt.show()
