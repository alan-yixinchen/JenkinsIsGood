import nltk
nltk.download('punkt')
sentence = "Jenkins is so good!"

def process():
    tokens = nltk.word_tokenize(sentence)
    print(tokens)

if __name__ == "__main__":
    process()