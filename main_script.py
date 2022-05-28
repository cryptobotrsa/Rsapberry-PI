from encryption import img_encrypt
from drive_upload import upload_encrypted_images

# All the files should be in same folder (pwd)
image_name = "cute_bot.jpg"

# This function is called to encrypt the image & place in same folder
img_encrypt(image_name)

# This function is called to upload the specified image into Google Drive
upload_encrypted_images(image_name)
