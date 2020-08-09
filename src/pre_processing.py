def pre_processing(html):
    """Minimises the HTML into individual sentences removing additional whitespace, then word tokens in lowercase form

    :param html:
    :return: the list of tokens and part-of-speech tags generated
    """
    stripped = remove_extra_spaces(html)

    return html


def remove_extra_spaces(text):
    return ' '.join(text.split())
