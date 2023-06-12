import requests
from bs4 import BeautifulSoup
import os
from PIL import Image
from io import BytesIO
import urllib.parse

# Define the URL of the web page containing the images
url = "https://www.nettruyenco.vn/truyen-tranh/mashle-magic-and-muscles/chuong-1/372895"

# Send a GET request to the URL
response = requests.get(url)

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Find all <img> tags on the page
image_tags = soup.find_all("img")

# Create a directory to save the images
save_directory = "./images/"
# Create the directory if it doesn't exist
os.makedirs(save_directory, exist_ok=True)

# Download and save each image
for image in image_tags:
    image_url = image["src"]
    image_name = image["alt"]

    # Sanitize the image name by removing invalid characters
    sanitized_name = urllib.parse.quote_plus(image_name)

    image_path = os.path.join(save_directory, sanitized_name + ".jpg")
    response = requests.get(image_url)

    # Check if the response contains image data
    if "image" in response.headers["Content-Type"]:
        # Save the image to the specified path
        with open(image_path, "wb") as file:
            file.write(response.content)
        print("Downloaded:", image_path)
    else:
        print("Skipped:", image_url, "- Not an image")
