import os
import json
from dotenv import load_dotenv
from PIL import Image
from pillow_heif import register_heif_opener  # for that iphone demo
import requests

load_dotenv()


LOGMEAL_URL = "https://api.logmeal.es/v2/image/segmentation/complete/v1.0?language=eng"
LOGMEAL_COMPANY_KEY = os.getenv("LOGMEAL_API_KEY")
LOGMEAL_USER_KEY = os.getenv("LOGMEAL_API_USER_TOKEN")

token = os.getenv("token")
chalk = os.getenv("LOGMEAL_CHALK")

cache_file_path = "./data/cache.json"


def load_cache():
    if os.path.exists(cache_file_path):
        with open(cache_file_path, "r") as f:
            return json.load(f)
    else:
        return {}


def save_cache(cache):
    with open(cache_file_path, "w") as f:
        json.dump(cache, f)


def process_image(filepath):
    # Define the output directory
    output_dir = "./data/processed_images/"

    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Extract file name and extension from the filepath
    file_name, file_extension = os.path.splitext(os.path.basename(filepath))

    if (
        file_extension == ".heic"
        or file_extension == ".HEIC"
        or file_extension == ".heif"
        or file_extension == ".HEIF"
    ):
        register_heif_opener()  # for that iphone demo

    with Image.open(filepath).convert("RGB") as img:
        # make aspect ratio square by cropping into the center
        small_dim = min(img.width, img.height)
        left = (img.width - small_dim) // 2
        top = (img.height - small_dim) // 2
        right = (img.width + small_dim) // 2
        bottom = (img.height + small_dim) // 2

        img = img.crop((left, top, right, bottom))  # make it square!
        img = img.resize((512, 512))  # resize

        # check if image size is > 1MB
        quality = 90
        outpath = output_dir + f"{file_name}.jpg"

        while os.path.getsize(filepath) > 1024 * 1024:
            # compress image
            # note: this does it in place, so the uploaded image is overwritten
            # could be annoying if you want to keep the original
            # whatever, it's a hackathon
            print(f"Compressing {filepath}...")
            img.save(filepath, quality=quality)
            print(f"New size: {os.path.getsize(filepath)}")
            quality -= 5
            print(f"New quality: {quality}")

        img.save(outpath)
        return outpath


def caption_image(filepath):
    headers = {"Authorization": "Bearer " + chalk}

    cache = load_cache()
    cache_key = os.path.basename(filepath)

    if cache_key in cache:
        print(
            f"\n\n------------------------Result for {filepath} served from cache.------------------------\n\n"
        )
        return cache[cache_key]

    params = {
        # "apiKey": LOGMEAL_USER_KEY,  # always required
        "apiKey": token,
        "language": "eng",
    }

    files = {
        "image": (filepath, open(filepath, "rb"), "image/jpeg"),
    }

    response = requests.post(
        "https://api.logmeal.es/v2/image/segmentation/complete/v1.0",
        params=params,
        headers=headers,
        files=files,
    )

    if response.status_code == 200:
        dishes = response.json()

        # cache it (don't rate limit me bro)
        cache[cache_key] = dishes
        save_cache(cache)
        print(
            f"\n\n------------------------Result for {filepath} saved to cache.------------------------\n\n"
        )

        return dishes
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return f"Error: {response.status_code} - {response.text}"


# def confirm_dish(dish):


# TODO: make version that has "confirm dish" dialog
def process_and_caption(filepath):
    """Returns a JSON response containing dishes and their associated probabilities."""
    outpath = process_image(filepath)
    return caption_image(outpath)


if __name__ == "__main__":
    process_image("./data/uploads/steak.jpg")
    # process_and_caption("./data/uploads/flan.jpeg")
