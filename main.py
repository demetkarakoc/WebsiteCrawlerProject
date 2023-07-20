import requests
from bs4 import BeatifulSoup

target_url= "https://atilsamancioğlu.com"
foundLinks = []

def make_request(url):
    response = requests.get(url)
    soup = BeatifulSoup(response.text, "html.parser")
    return soup

def crawl(url):
    links = make_request()
    for link in soup.find_all('a'):
        found_link = link.get('href')
        if found_link:
            if "#" in found_link:
                found_link = found_link.splint("#")[0]
                if target_url in found_link and found_link not in foundLinks:
                    foundLinks.append(found_link)
                    print(found_link)
                    crawl(found_link)

crawl(target_url)






