import os
import requests
import shutil
from duckduckgo_search import DDGS
import imghdr
import hashlib

def download_images(search_term, file_prefix, target_directory, max_results=10):
    with DDGS() as ddgs:
        results = [r for r in ddgs.images(search_term, max_results=max_results)]
        count = 0
        for i, result in enumerate(results):
            image_url = result['image']

            try:
                response = requests.get(image_url, stream=True)
            except Exception as e:
                print(f"... Could not download image {file_prefix} {i}, skipping")
                print(e)
                continue
            content = response.content

            #Determine the image format
            image_format = imghdr.what(None, h=content)
            if image_format is None:
                print(f"... Could not determine format for {file_prefix} {i}, skipping")
                continue

            # just use 8 characters of the hash
            content_hash = hashlib.sha256(content).hexdigest()[:8]

            file_name = os.path.join(target_directory, f"{file_prefix}-{i}-{content_hash}.{image_format}")

            with open(file_name, 'wb') as out_file:
                out_file.write(content)
            del response
            count += 1
        print(f"Downloaded {count} images for {file_prefix}")

def main():
    print("duckduck.py#main() does nothing")

if __name__ == "__main__":
    main()