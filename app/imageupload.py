from dotenv import load_dotenv
from imagekitio import ImageKit
import os

load_dotenv()

imagekit = ImageKit(
    private_key=os.getenv("IMAGEKIT_PRIVATE_KEY"),
)

URL_ENDPOINT = os.getenv("IMAGEKIT_URL_ENDPOINT")


def upload_file(file, file_name: str, folder: str = "/"):
    response = imagekit.files.upload(
        file=file,
        file_name=file_name,
        folder=folder,
        use_unique_file_name=True,
    )
    return response  # response.url, response.file_id, etc.