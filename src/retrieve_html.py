import requests
from bs4 import BeautifulSoup


def get_html(url):
    """Creates a response object with the raw HTML from the URL.

    :param str url: the website being requested
    :return: a nicely formatted string of the HTML retrieved
    """
    # Gets the raw HTML with the tags
    response = requests.get(url)
    beau_soup = BeautifulSoup(response.content, 'html.parser')

    return beau_soup


def extract_relevant_html(html):
    """Extracts all potentially relevant text from the raw HTML whilst removing all script tags.

    :param html: the raw HTML collected from the previous function
    :return: the stripped HTML with the meta and img content
    """
    all_text = ""

    # Find all meta tags and add their content to the text
    for meta in html.find_all('meta'):
        try:
            if meta.has_attr('name') and meta['name'] in "description":
                all_text += meta['content'] + ". "
            else:
                continue
        except KeyError:
            continue

    # Remove all script tags
    [script.extract() for script in html.find_all('script')]

    # Add extracted text to main text
    all_text += html.get_text()
    return all_text
