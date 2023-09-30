import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import WordNetLemmatizer


nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Initialize the WordNet lemmatizer
lemmatizer = WordNetLemmatizer()

# Sample corpus with special symbols and brackets as you said  in the class
corpus = """
 The quick brown fox (jumped) over the lazy dogs.
 A red apple fell from the tree.
 She always enjoyed reading books by the fireplace.
 The sunsets at the beach are stunning.
 In a galaxy far, far $ away,@ there was a brave hero.
 The ancient # ruins stood tall against the test of time. 
After a long day at work, he just wanted to relax.
 Birds chirped merrily in the morning.
 Cooking a !delicious meal takes time and patience.
1 The cityscape glittered with lights at night.
1 Mountains ^ covered in snow make for a beautiful sight.
1 Music has the & power to touch our souls.
 The old oak tree provided shade on hot summer days.
1 Traveling to $ new places broadens your perspective.
1She gazed at the stars, lost in thought.
1 The river flowed % peacefully through the valley.
1 Children laughed and played in the park.
1 Learning a new language can be # a rewarding experience.
1 Raindrops danced on the windowpane{.
2 The (professor) gave an insightful }{ lecture on literature.
"""

# Tokenize the corpus into sentences
sentences = sent_tokenize(corpus)

# Tokenize each sentence into word lemmatize and filter  stop words
stop_words = set(stopwords.words("english"))
filtered_corpus = []

for sentence in sentences:
    words = word_tokenize(sentence)
    filtered_words = [lemmatizer.lemmatize(word.lower()) for word in words if word.lower() not in stop_words and word.isalpha()]
    filtered_sentence = " ".join(filtered_words)
    if filtered_sentence:
        filtered_corpus.append(filtered_sentence)


    print(f"Tokenized Words for Sentence: {words}")

# Display the filtered corpus sentences final output
for cop, sentence in enumerate(filtered_corpus, start=1):
    print(f"{cop}. {sentence}")
