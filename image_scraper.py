import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

website_urls = ["https://www.paulawrzecionowska.com/", "https://www.peternoah.com/"]

def download_images(url, save_dir):
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    else:
        for file in os.listdir(save_dir):
            os.remove(os.path.join(save_dir, file))

    response = requests.get(url)
    html_content = response.text

    soup = BeautifulSoup(html_content, 'html.parser')

    image_tags = soup.find_all('img')
    for image_tag in image_tags:
        image_url = image_tag.get('src')

        absolute_image_url = urljoin(url, image_url)

        image_filename = os.path.basename(urlparse(absolute_image_url).path)

        image_save_path = os.path.join(save_dir, image_filename)
        try:
            image_response = requests.get(absolute_image_url, stream=True)
            with open(image_save_path, 'wb') as image_file:
                for chunk in image_response.iter_content(chunk_size=1024):
                    image_file.write(chunk)
            #print(f"Image saved: {image_save_path}")
        except Exception as e:
            print(f"Error downloading image from {absolute_image_url}: {str(e)}")

if __name__ == "__main__":
    for website_url in website_urls:
        if website_url[-1] == "/":
            website_url = website_url[:-1]
        save_directory = "data/" + website_url.split("//")[-1].replace("/", "_") + "/images"
        download_images(website_url, save_directory)