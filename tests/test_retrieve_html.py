from bs4 import BeautifulSoup, NavigableString
from src import retrieve_html


def test_get_html():
    url = "https://www.google.co.uk"
    soup = retrieve_html.get_html(url, 0)

    assert soup.__module__ == BeautifulSoup.__module__
