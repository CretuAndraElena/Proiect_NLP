from nltk.corpus import wordnet

wordlist = [x.name().split(".")[0] for x in wordnet.all_synsets()]
lines = [line.rstrip('\n') for line in open('Data/frequent_words.txt')]
words = [x for x in wordlist if x in lines]
words = list(set(words))

from yandex.Translater  import Translater
tr = Translater()
tr.set_key('trnsl.1.1.20200110T204012Z.aced353ec92e75ae.c22065bc688827a0cd8fcc8e5c4a0a6ccf0cc15b')
tr.set_from_lang('en')
tr.set_to_lang('ro')

for word in words:
    with open("test.txt", "a",  encoding="utf-8") as myfile:
        print(word)
        tr.set_text(word)
        text = word + ','
        try:
            text = text + tr.translate() + '\n'
        except:
            text = text + '\n'
        myfile.write(text)
