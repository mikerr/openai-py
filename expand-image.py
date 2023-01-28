# take a 256x256 image and use AI outpainting to make a 512x512 image
import cv2
import numpy as np
import openai
import webbrowser

openai.api_key = "openai-api-key"

# load a 256x256 image
s_img = cv2.imread("image.png")
h, w, c = s_img.shape
# make a 512x512 image (or double input image)
img_size = w * 2;
l_img = np.zeros((img_size,img_size,3), np.uint8)

#place small image in middle of large frame

x_offset= int(w / 2)
y_offset= 0
l_img[y_offset:y_offset + h, x_offset:x_offset + w] = s_img

alpha = np.full((img_size,img_size), 255, dtype=np.uint8)
result = np.dstack((l_img, alpha))

# Make mask of black pixels - mask is True where image is black
black = [0,0,0]
white = [255,255,255]
mBlack = (result[:, :, 0:3] == black).all(2)

# Make all pixels matched by mask into transparent ones
result[mBlack] = (0,0,0,0)

cv2.imwrite("image1.png",result)

response = openai.Image.create_edit(
    image= open("image1.png",mode="rb"),
    mask= open("image1.png",mode="rb"),
    prompt="underwater world with jellyfish and coral",
    n=1,
    size="512x512",
)
image_url = response['data'][0]['url']
print (image_url)
webbrowser.open(image_url)
