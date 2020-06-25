from bs4 import BeautifulSoup
import requests


def get_html(url, file_count):
    """Creates a response object with the raw HTML from the URL.

    :param str url: the website being requested
    :param int file_count_a: the current url number
    :return: a nicely formatted string of the HTML retrieved
    """
    # Gets the raw HTML with the tags
    response = requests.get(url)
    beau_soup = BeautifulSoup(response.content, 'html.parser')

    return beau_soup
