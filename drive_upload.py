from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


def upload_encrypted_images(location):

    google_auth = GoogleAuth()
    print("Establishing Connection with Google Drive ....")
    drive = GoogleDrive(google_auth)

    upload_file = location

    drive_file_object = drive.CreateFile({'parents': [{'id': '1rnheo0nFGC4uOqeZszq29fC1CrLCQtsX'}]})
    print("Uploading " + upload_file)
    drive_file_object.SetContentFile(upload_file)
    drive_file_object.Upload()
    print("Upload Successful !!")
