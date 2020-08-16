import src.helpers as helpers


def keyword_selection(pp_tokens, pp_tags):
    """Creates chunks of words (suitable phrases) using the POS tags and adds them to the list of tokens. As well as
    removing all irrelevant punctuation and stop words which will not be needed for the final index. Finally creating
    a table of frequency used in calculating the tf.idf.

    :param pp_tokens: a list of tokens
    :param pp_tags: a list of POS tagged tokens
    """
    # Remove punctuation
    wo_punct_tokens = helpers.remove_punctuation(pp_tokens)
    wo_punct_tags = helpers.remove_punctuation(pp_tags, word_list_type="tuple")

    # Remove digits

    # Remove stopwords

    return False
