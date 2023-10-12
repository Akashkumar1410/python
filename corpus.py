import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize

nltk.download('punkt')
nltk.download('stopwords')

# Sample corpus with special symbols and brackets
corpus = """🎓🏛️ My university, ⭐️𝗠𝘆 𝗨𝗻𝗶𝘃𝗲𝗿𝘀𝗶𝘁𝘆⭐️, is a place of 📚🔬✨knowledge and discovery, where every day is a new adventure. Located in the heart of 🌆🌳🏞️, our campus is a vibrant hub of 🌟💡💼learning and innovation. With a diverse community of 🧑‍🎓👩‍🏫👨‍🔬students, 🌍🌎🌏faculty, and 🌐🤝🌟staff from all corners of the world, we embrace and celebrate our differences, fostering an environment of 🤝🌈🎉inclusivity and mutual respect.

At ⭐️𝗠𝘆 𝗨𝗻𝗶𝘃𝗲𝗿𝘀𝗶𝘁𝘆⭐️, we are committed to 📚🧠🌱academic excellence, providing a wide range of 📖📊🔍programs and resources to help students reach their full potential. Our state-of-the-art 🏫🔬🖥️facilities and 🌆🏞️🏛️beautiful campus create the perfect backdrop for a rich and fulfilling educational experience.

But it's not just about the classroom; we also value 💼🤝🌱community engagement and 🌟🏆🌍global awareness. Students at ⭐️𝗠𝘆 𝗨𝗻𝗶𝘃𝗲𝗿𝘀𝗶𝘁𝘆⭐️ have countless opportunities to get involved in 🌏🌱🤝extracurricular activities, from 🏀🎶🎭sports and 🎨🎉🎤arts to 💼🌍🌐internships and 🌱📣🌟volunteer work.

In conclusion, ⭐️𝗠𝘆 𝗨𝗻𝗶𝘃𝗲𝗿𝘀𝗶𝘁𝘆⭐️ is not just a university; it's a place where dreams are nurtured, knowledge is cherished, and friendships are forged. It's a symbol of 📚🌟🌈hope and a beacon of 🧠💡🌍intellectual growth in an ever-changing world.

"""


sentences = sent_tokenize(corpus)


stop_words = set(stopwords.words("english"))
filtered_corpus = []

for sentence in sentences:
    words = word_tokenize(sentence)
    filtered_words = [word.lower() for word in words if word.lower() not in stop_words and word.isalpha()]
    if filtered_words:
        filtered_sentence = " ".join(filtered_words)
        filtered_corpus.append(filtered_sentence)


output_paragraph = " ".join(filtered_corpus)

# Display the paragraph
print(output_paragraph)
