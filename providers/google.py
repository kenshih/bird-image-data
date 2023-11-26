from googleapiclient.discovery import build
import json
import os
import subprocess
import uuid
import zipfile
from datetime import datetime

api_key = os.getenv('GOOGLE_API_KEY')
cse_id="305333fdcdf3b4f00"

def google_search(search_term, api_key, cse_id, start, **kwargs):
 service = build("customsearch", "v1", developerKey=api_key)
 res = service.cse().list(q=search_term, cx=cse_id, searchType='image', start=start, **kwargs).execute()
 return res

def download_metadata(meta_file):
   # todo add cn & sex to google results
   search_terms = [
   "female house finch",
   "female cassin's finch",
   "female pine siskin",
   "female purple finch"
   ]
   all_results = []
   for search_term in search_terms:
      for start in range(1, 101, 10):
         results = google_search(
         search_term=search_term,
         api_key=api_key,
         cse_id=cse_id,
         start=start,
         num=10
         )
      all_results.extend(results['items'])
   with open(meta_file, 'w') as f:
      f.write(json.dumps(all_results, indent=2))

def download_images(results, output_dir):
 for result in results:
   # deterministic id
   id = str(uuid.uuid3(uuid.NAMESPACE_URL, result['link']))[:16]
   link = result['link']
   common_name = result['cn']
   sex = result['sex']
   file_extension = 'jpeg'
   parts = result['fileFormat'].split('/')
   if len(parts) > 1 and parts[1]:
       file_extension = parts[1]
   file_name = f'{common_name}-{sex}-{id}.{file_extension}'
   file_path = os.path.join(output_dir, file_name)
   command = ["curl", "-o", file_path, link]
   try:
      subprocess.run(command, check=True)
   except subprocess.CalledProcessError:
      print(f"Failed to download {link}")

def zip_directory(directory_path, zip_path):
   # Create the zip file
   with zipfile.ZipFile(zip_path, 'w') as zipf:
       # Walk through the directory
       for root, dirs, files in os.walk(directory_path):
           for file in files:
               # Create a full filepath
               full_path = os.path.join(root, file)
               # Add the file to the zip
               zipf.write(full_path, arcname=os.path.relpath(full_path, directory_path))

def main():
   # 1. download metadata and save in file
   #download_metadata('data-meta/google-finch-metadata.json')
   # 2. download images from metadata file
   # download_images(
   #   json.load(open('data-meta/google-finch-metadata.json')),
   #   'data-images')
   # 3. zip images
    current_date = datetime.now().strftime('%Y-%m-%d')
    zip_directory('data-images', f'finch_images_{current_date}.zip')

if __name__ == "__main__":
    main()
