import nltk
import re
import string

punctuation = set(string.punctuation)
punctuation.update(['...', '£', '•'])
punctuation = ''.join(punctuation)

stopwords = set(nltk.corpus.stopwords.words('english'))


def remove_extra_spaces(text):
    return ' '.join(text.split())


def remove_punctuation(word_list, word_list_type="list"):
    pattern = re.compile("^([%s]|([%s]+))$" % (re.escape(punctuation), re.escape(punctuation)))

    if word_list_type == "list":
        punctuations_removed = [pattern.sub('', term) for term in word_list if pattern.sub('', term)]
    else:
        punctuations_removed = [(pattern.sub('', term), tag) for term, tag in word_list if pattern.sub('', term)]

    return punctuations_removed


def remove_digits(word_list, word_list_type="list"):
    pattern = re.compile("^[0-9]{4}-[0-9]{4}$")

    if word_list_type == "list":
        digits_removed = [term for term in word_list if not (term.isdigit() or pattern.match(term))]
    else:
        digits_removed = [(term, tag) for term, tag in word_list if not (term.isdigit() or pattern.match(term))]

    return digits_removed


def remove_stopwords(word_list, word_list_type="list"):
    if word_list_type == "list":
        stopwords_removed = [term for term in word_list if term not in stopwords]
    else:
        stopwords_removed = [(term, tag) for term, tag in word_list if term not in stopwords]

    return stopwords_removed


def write_to_file():
    return False
