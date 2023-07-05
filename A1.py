import os
import requests

# Function to download an image from a given URL
def download_image(url, directory, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(os.path.join(directory, filename), 'wb') as file:
            file.write(response.content)

# Function to search and download images of a specific person
def download_person_photos(person_name, num_photos, directory):
    # Replace 'YOUR_BING_API_KEY' with your actual Bing Image Search API key
    api_key = 'YOUR_BING_API_KEY'
    endpoint = 'https://api.bing.microsoft.com/v7.0/images/search'

    headers = {
        'Ocp-Apim-Subscription-Key': api_key,
    }

    params = {
        'q': person_name,
        'count': num_photos,
        'license': 'public',
        'imageType': 'photo'
    }

    response = requests.get(endpoint, headers=headers, params=params)
    data = response.json()

    if 'value' in data:
        for i, image in enumerate(data['value']):
            image_url = image['contentUrl']
            file_extension = os.path.splitext(image_url)[1]
            filename = f'{person_name}_{i}{file_extension}'
            download_image(image_url, directory, filename)
            print(f'Downloaded image {i + 1}/{num_photos}')
    else:
        print('No images found.')

# Prompt the user to enter the name of the person
person_name = input('Enter the name of the person: ')

# Create a directory to save the downloaded photos
directory = 'person_photos'
if not os.path.exists(directory):
    os.makedirs(directory)

# Download 50 photos of the specified person
num_photos = 50
download_person_photos(person_name, num_photos, directory)
