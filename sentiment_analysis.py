# Hi I am really struggling with this;
# I am aware it has issues and would be grateful for any pointers.

# modules etc installation
import pandas as pd
import spacy
from textblob import TextBlob
nlp = spacy.load('en_core_web_sm')

# create dataframe from csv

dataframe = pd.read_csv('amazon_product_reviews.csv')

# text cleaning

reviews_data = dataframe[['reviews.text']]

reviews_data = reviews_data.dropna(subset=['reviews.text'])
#reviews_data = dataframe['reviews.text'].str.lower()


# function for sentiment analysis: input is product review
text = reviews_data

# Processing/cleaning text data
def preprocess_text(text):
    doc = nlp(text)

    # Lowercasing and removing punctuation
    tokens = [token.text.lower() for token in doc if token.is_alpha]

    # Removing stop words and punctuation
    tokens = [token for token in tokens if not nlp.vocab[token].is_stop]

    return tokens

nlp_data = reviews_data['reviews.text'].apply(preprocess_text)

# Function to analyse polarity and sentiment
def analyse_polarity(doc):
    polarity = doc._.blob.polarity

    sentiment = doc._.blob.sentiment

    polarity_score = polarity(text)

    if polarity_score > 0:
        sentiment = 'positive'
    elif polarity_score < 0:
        sentiment = 'negative'
    else:
        sentiment = 'neutral'

    print(f"Text: {text}\nPolarity score: {polarity_score}\nSentiment: {sentiment}")

analyse_polarity(nlp_data)

# -1 to 1

# test model on sample reviews using similarity() and polarity()
# select and compare sentiments

first_choice_review = reviews_data['reviews.text'][0]
second_choice_review = reviews_data['reviews.text'][1]

first_tokens = preprocess_text(first_choice_review)
second_tokens = preprocess_text(second_choice_review)

first_doc = nlp(' '.join(first_tokens))
second_doc = nlp(' '.join(second_tokens))

similarity = first_doc.similarity(second_doc)
print(f"Review similarity: {similarity:.2f}")
