import math

def main(text):
    # split the text first into lines and then into lists of words
    docs = [line.split() for line in text.splitlines()]

    N = len(docs)

    # create the vocabulary: the list of words that appear at least once
    vocabulary = list(set(text.split()))

    df = {}
    tf = {}
    for word in vocabulary:
        # tf: number of occurrences of word w in document divided by document length
        tf[word] = [doc.count(word)/len(doc) for doc in docs]

        # df: number of documents containing word w
        df[word] = sum([word in doc for doc in docs])/N

    # loop through documents to calculate the tf-idf values
    for doc_index, doc in enumerate(docs):
        tfidf = []
        for word in vocabulary:
            # Calculate tf-idf using the formula
            tf_value = tf[word][doc_index]
            df_value = df[word]
            tfidf_value = tf_value * math.log(N / (df_value * N), 10)  # Correct formula for tf-idf
            tfidf.append(tfidf_value)

        print(tfidf)

text = '''he really really loves coffee
my sister dislikes coffee
my sister loves tea'''

main(text)
