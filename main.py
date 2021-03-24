# Requests allows you to send HTTP/1.1 requests extremely easily.
import requests
# bs4: Beautiful Soup(bs4) is a Python library for pulling data out of HTML and XML files.
from bs4 import BeautifulSoup


def crawl_site(url):
    reqs = requests.get(url)
    soup = BeautifulSoup(reqs.text, 'html.parser')

    urls = []
    for link in soup.find_all('a'):
        print(link.get('href'))



if __name__ == '__main__':
    url = "https://www.afiniti.com/"
    crawl_site(url)

