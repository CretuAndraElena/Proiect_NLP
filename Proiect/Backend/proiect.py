from nltk.corpus import wordnet
from googletrans import Translator
from translate import Translator

def get_synonyms_antonyms(word):
    synonyms = [] 
    antonyms = [] 
    
    for syn in wordnet.synsets(word): 
        for l in syn.lemmas(): 
            synonyms.append(l.name()) 
            if l.antonyms(): 
                antonyms.append(l.antonyms()[0].name()) 
    return(synonyms,antonyms)
    
def get_definitions(word):
    syns = wordnet.synsets(word)
    return syns[0].definition()

def translate_text(text):
    translator= Translator(to_lang="ro")
    translation = translator.translate(text)
    return translation

def get_question(word):
    synonyms_antonyms = get_synonyms_antonyms(word)
    question = { "word": word, 
                "definition" : get_definitions(word), 
                "synonyms" : list(set(synonyms_antonyms[0])), 
                "antonyms" : list(set(synonyms_antonyms[1])), 
                "translate" : translate_text(word)
                }
    return question

# extract word from wornet
words = [x.name().split(".")[0] for x in wordnet.all_synsets()]

# get main domains
s = wordnet.synsets('dog')[0]
animal_domain = s.hypernym_paths()[1][6]

s = wordnet.synsets('orange')[0]
fruits_domain = s.hypernym_paths()[0][8]

s = wordnet.synsets('potato')[0]
vegetables_domain = s.hypernym_paths()[0][6]

s = wordnet.synsets('green')[0]
colors_domain = s.hypernym_paths()[0][5]

s = wordnet.synsets('cook')[0]
occupations_domain = s.hypernym_paths()[0][4]

s = wordnet.synsets('football')[0]
sports_domain = s.hypernym_paths()[0][7]

data = {}
data['animals']=[]
data['fruits']=[]
data['vegetables']=[]
data['colors']=[]
data['occupations']=[]
data['sports']=[]

for word in words:
    s = wordnet.synsets(word)
    if s:
        if any(animal_domain in sublist for sublist in s[0].hypernym_paths()):
           data['animals'].append(get_question(word))
        if any(fruits_domain in sublist for sublist in s[0].hypernym_paths()):
            data['fruits'].append(get_question(word))
        if any(vegetables_domain in sublist for sublist in s[0].hypernym_paths()):
            data['vegetables'].append(get_question(word))
        if any(colors_domain in sublist for sublist in s[0].hypernym_paths()):
            data['colors'].append(get_question(word))
        if any(occupations_domain in sublist for sublist in s[0].hypernym_paths()):
            data['occupations'].append(get_question(word))
        if any(sports_domain in sublist for sublist in s[0].hypernym_paths()):
            data['sports'].append(get_question(word))

# Import the json module
import json

with open('Data/list.json', 'w') as outfile:
        json.dump(data, outfile, indent=4)



