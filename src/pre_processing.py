import nltk

from src.helpers import remove_extra_spaces


def pre_processing(html):
    """Minimises the HTML into individual sentences removing additional whitespace, then word tokens in lowercase form

    :param html:
    :return: the list of tokens and part-of-speech tags generated
    """
    stripped = remove_extra_spaces(html)

    # Creates a list for every variable using a loop
    sent_list, token_list, pos_list = ([] for _ in range(3))

    # For loop tokenizes the html into sentences
    for sentences in nltk.sent_tokenize(stripped):
        sent_list.append(sentences)

        # For loop tokenizes sentences into words
        words = [x.lower() for x in nltk.word_tokenize(sentences.replace("/", " "))]
        for token in words:
            token_list.append(token)

        # Creates part of speech tags for every word
        pos_list.extend(nltk.pos_tag(words))

    return token_list, pos_list

