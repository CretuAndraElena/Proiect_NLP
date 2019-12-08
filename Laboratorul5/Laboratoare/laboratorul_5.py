import nltk
from nltk.stem import WordNetLemmatizer 

f = open("corpus.txt", encoding="utf8")
text = f.read()
#1
tokens = nltk.word_tokenize(text)

#print(tokens)

#2
lemmatizer = WordNetLemmatizer() 
new_tokens = []

for token in tokens:
    new_tokens.append(lemmatizer.lemmatize(token))

#print(new_tokens)

#3
part_of_speech = nltk.pos_tag(tokens)

#print(part_of_speech)


#4
from nltk import FreqDist

word_frequent = FreqDist(tokens)
#print(word_frequent.most_common(100))

#5
part_of_speech_frequent = nltk.FreqDist(tag for (word, tag) in part_of_speech)
#print(part_of_speech_frequent.most_common(5))

#6
from nltk.tokenize.regexp import RegexpTokenizer

#email_pattern = r'\S+@[^\s.]+\.[a-zA-Z]+|\w+|[^\w\s]'
#tokeniser=RegexpTokenizer(email_pattern)
#print(tokeniser.tokenize(text))

url_pattern = r'^(http:\/\/www\.|https:\/\/www\.|http:\/\/|https:\/\/)?[a-z0-9]+([\-\.]{1}[a-z0-9]+)*\.[a-z]{2,5}(:[0-9]{1,5})?(\/.*)?$'
tokeniser=RegexpTokenizer(url_pattern)
print(tokeniser.tokenize(text))