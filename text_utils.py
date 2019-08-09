import re
import string

from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize


def clean_text(text):
    if type(text) != str:
        print(text)

    text = str(text)

    # lower
    text = text.lower()

    # Remove Punctuation
    punct = string.punctuation
    trantab = str.maketrans(punct, len(punct) * ' ')
    text = text.translate(trantab)

    # Remove Digits
    text = re.sub('\d+', '', text)

    # Remove Urls
    text = re.sub(r'http.?://[^\s]+[\s]?', '', text)

    tokens = word_tokenize(text)
    lemmatizer = WordNetLemmatizer()

    # Lemmatizer
    tokens = [lemmatizer.lemmatize(t) for t in tokens]
    text = " ".join(tokens)

    return text


if __name__ == "__main__":
    text = " If the solar system were used as a model of an"
    print("text:", text)
    print("cleaned text:", clean_text(text))
