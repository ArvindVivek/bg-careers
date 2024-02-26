import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

website_urls = ["https://www.paulawrzecionowska.com/", "https://www.peternoah.com/"]

def extract_images(url):

    response = requests.get(url)
    html_content = response.text

    soup = BeautifulSoup(html_content, 'html.parser')

    image_tags = soup.find_all('img')

    images = []
    for image_tag in image_tags:
        image_url = image_tag.get('src')

        absolute_image_url = urljoin(url, image_url)

        images.append(absolute_image_url)
    
    return images
    

if __name__ == "__main__":
    for website_url in website_urls:
        if website_url[-1] == "/":
            website_url = website_url[:-1]
        save_directory = "data/" + website_url.split("//")[-1].replace("/", "_") + "/images"
        print(extract_images(website_url))