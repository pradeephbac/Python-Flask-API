from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from string import punctuation
from nltk.probability import FreqDist
from heapq import nlargest
from collections import defaultdict

def sumerize(text,n):
    sents = sent_tokenize(text)

    assert n <= len(sents)
    word_sents = word_tokenize(text.lower())
    _stopwords = set(stopwords.words('english') + list(punctuation))

    word_sent = [word for word in word_sents if word not in _stopwords]
    freq = FreqDist(word_sent)

    ranking = defaultdict(int)

    for i,sent in enumerate(sents):
        for w in word_tokenize(sent.lower()):
            if w in freq:
                ranking[i] += freq[w]


    sents_idx = nlargest(n, ranking, key = ranking.get)
    final_test = ""
    for j in sorted(sents_idx):
        final_test = final_test + sents[j]

    return final_test