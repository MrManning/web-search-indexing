import nltk
import re
import string

nltk.download('stopwords')

punctuation = set(string.punctuation)
punctuation.update(['...', '£', '•'])
punctuation = ''.join(punctuation)

stopwords = set(nltk.corpus.stopwords.words('english'))


def remove_extra_spaces(text):
    return ' '.join(text.split())


def remove_punctuation(word_list, word_list_type="list"):
    # regex = re.compile("[%s]" % re.escape(punctuation))
    regex = re.compile("^([%s]|([%s]+))$" % (re.escape(punctuation), re.escape(punctuation)))

    if word_list_type == "list":
        punctuation_less = [regex.sub('', term) for term in word_list if regex.sub('', term)]
    else:
        punctuation_less = [(regex.sub('', term), tag) for term, tag in word_list if regex.sub('', term)]

    return punctuation_less


def remove_digits(word_list):
    return False


def remove_stopwords(word_list):
    return False


def write_to_file():
    return False
