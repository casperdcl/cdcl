import re

import bs4
import requests


def get_soup(url):
    req = requests.get(url, headers={'User-Agent': 'Python/3 requests'})
    return bs4.BeautifulSoup(req.text, 'html.parser')


def test_psf_sponsor():
    soup = get_soup('https://www.python.org/psf/fiscal-sponsorees/')
    headers = [i.text for i in soup.find_all('h1')]
    if "At this time, the Python Software Foundation is not accepting new fiscal sponsoree requests." not in headers:
        raise ValueError("The PSF is accepting new fiscal sponsoree requests")


def test_kingkiller_chronicle():
    soup = get_soup('https://en.wikipedia.org/wiki/The_Kingkiller_Chronicle')
    years = sorted(set(re.findall(r"The Doors of Stone\s+\(([TBA0-9]+)\)", soup.text)))
    if any(year != "TBA" for year in years):
        raise ValueError(f"The Doors of Stone ({', '.join(years)})")


def test_dark_profit_saga():
    soup = get_soup('https://jzacharypike.com/pages/shop')
    if re.findall('Crypt Currency', soup.text, flags=re.I):
        raise ValueError("Crypt Currency is available.")


def test_dungeon_crawler_carl():
    soup = get_soup('https://en.wikipedia.org/wiki/Dungeon_Crawler_Carl')
    if cell := soup.find(['th', 'tr'], string=re.compile(r"^9$")):
        raise ValueError(" ".join(i.text for i in cell.next_siblings).replace("\xa0", " "))
