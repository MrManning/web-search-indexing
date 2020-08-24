import operator

import nltk

import src.helpers as helpers


def keyword_selection(tokens, tags):
    filtered_tokens, filtered_tags = token_filtration(tokens, tags)
    stemmed_tokens, stemmed_tags = stemming(filtered_tokens, filtered_tags)
    chunking(stemmed_tokens, stemmed_tags)


def token_filtration(pp_tokens, pp_tags):
    """Creates chunks of words (suitable phrases) using the POS tags and adds them to the list of tokens. As well as
    removing all irrelevant punctuation and stop words which will not be needed for the final index. Finally creating
    a table of frequency used in calculating the tf.idf.

    :param pp_tokens: a list of tokens
    :param pp_tags: a list of POS tagged tokens
    """
    # Remove punctuation
    tokens_punctuation_removed = helpers.remove_punctuation(pp_tokens, word_list_type="list")
    tags_punctuation_removed = helpers.remove_punctuation(pp_tags, word_list_type="tuple")

    # Remove digits
    tokens_digits_removed = helpers.remove_digits(tokens_punctuation_removed, word_list_type="list")
    tags_digits_removed = helpers.remove_digits(tags_punctuation_removed, word_list_type="tuple")

    # Remove stopwords
    tokens_stopwords_removed = helpers.remove_stopwords(tokens_digits_removed, word_list_type="list")
    tags_stopwords_removed = helpers.remove_stopwords(tags_digits_removed, word_list_type="tuple")

    return tokens_stopwords_removed, tags_stopwords_removed


def stemming(tokens, tags):
    stem_token_list = [nltk.PorterStemmer().stem(term) for term in tokens]
    stem_tagged_list = [(nltk.PorterStemmer().stem(term), tag) for term, tag in tags]

    return stem_token_list, stem_tagged_list


def chunking(tokens, tags):
    # Calculate the frequency of the terms
    token_frequency = nltk.FreqDist(tokens)

    # Chunk all the words using the grammar from POS tags
    chunked_list = []
    grammar = r"""
                NP: {<JJ><NN|NNS>}
                    {<NN><IN><JJ|NN>{1,2}}
                    {<NN><NN>}
                    {<WP><NN>{0,2}}
                    {<NNP>?<NN>{0,2}<NNS>?}
                    {<DT|JJ|NN.*>+}
            """
    chunk_parser = nltk.RegexpParser(grammar)
    tree = chunk_parser.parse(tags)

    # Loops tree of phrases and adds them to a list
    for subtree in tree.subtrees(filter=lambda t: t.label() == 'NP'):
        if len(' '.join(x[0] for x in subtree).split()) > 1:
            chunked_list.append(' '.join(x[0] for x in subtree))

    # Creates a list of frequencies for all phrases and chooses the top 30 most common
    chunked_frequency = nltk.FreqDist(chunked_list).most_common(30)
    for chunky, frequency in chunked_frequency:
        token_frequency[chunky] = frequency

    # Sorts the list of tokens from highest to smallest
    sorted_token_frequency = sorted(token_frequency.items(), key=operator.itemgetter(1), reverse=True)
