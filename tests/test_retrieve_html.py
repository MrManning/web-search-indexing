from bs4 import BeautifulSoup
from src import retrieve_html


def test_get_html():
    url = "https://www.google.co.uk"
    soup = retrieve_html.get_html(url)

    assert soup.__module__ == BeautifulSoup.__module__


def test_extract_relevant_html():
    url = "https://www.reddit.com/"
    content = "Reddit is a network of communities based on people's interests."

    soup = retrieve_html.get_html(url)

    assert content not in soup.get_text()
    html = retrieve_html.extract_relevant_html(soup)
    assert content in html
