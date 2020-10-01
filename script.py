import requests
from bs4 import BeautifulSoup as BeSo
import sys
import urllib.parse as urlparse

assert len(sys.argv) == 3, 'There should be 3 arguments, <anime_name> <start_ep> <end_ep>'
assert sys.argv[2].isnumeric() == True, '<start_ep> should be an integer'
assert sys.argv[3].isnumeric() == True, '<end_ep> should be an integer'

name = sys.argv[1]
start = int(sys.argv[2])
end = int(sys.argv[3])
rapidx = True


def get_bs(link):
        print(f'Getting link for {link}')
        res = requests.get(link)
        return BeSo(res.text, 'lxml')


def generate_links(name, start, end):
        print('Generating links')
        links = [(f'https://www2.chia-anime.cc/watch/{name.lower}-episode-{i}.html', i) for i in range(start, end + 1)]
        return links


links = generate_links(name, start, end)

for link, index in links:
        print(f'Searching for episode {index}')
        bs = get_bs(link)
        bs = get_bs(bs.find(class_='plugins_true').find_all('ul')[1].find_all('li')[4].find('a').attrs['href'])
        #if not rapidx:
        #       link = bs.find_all(class_='dowload'fast)[2].find('a').attrs['href']
        #       parsed = urlparse.urlparse(link)
        #       print('-' * 100 + f'\n\n{parsed.scheme}://{parsed.netloc}{parsed.path}?{parsed.query[:parsed.query.find("title")]}title={name}{index}.mp4\n\n' + '-' * 100)
        #       continue
        link = get_bs(bs.find_all(class_='mirror_find_all(class_='dowload')[2].find('a').attrs['href'])).find(class_='is-info').attrs['href']
        parsed = urlparse.urlparse(link)
        print('-' * 100 + f'\n\n{parsed.scheme}://{parsed.netloc}{parsed.path}?name={name}{index}.mp4\n\n' + '-' * 200)
