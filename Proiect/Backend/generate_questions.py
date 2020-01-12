import json
import random

with open('Data/list.json') as f:
    data = json.load(f)

def generate_multiple_choice_question(text, posible_answers, corect_asnwer, category):
    question = { "question": text, 
                "category": category,
                "corect" : corect_asnwer,
                "wrong_answers":random.choices(posible_answers, k=3)
                }
    return question

def generate_input_question(text, asnwer, category):
    question = { "question": text, 
                "category": category,
                "corect" : asnwer,
                }
    return question

def extract_word_by_category(category):
    synonyms=[]
    words = []
    for index in range(len(data[category])):
        word = data[category][index]['word']
        synonyms += data[category][index]["synonyms"]
        if len(data[category][index]["synonyms"]) > 0 :
            corect_asnwer = data[category][index]["synonyms"][0]
        words.append((word,corect_asnwer))
    
    return words, list(set(synonyms))

def extract_word_and_definition(category):
    words_def= []
    for index in range(len(data[category])):
        word = data[category][index]['word']
        definition = data[category][index]['definition']
        words_def.append((word,definition))
    return words_def

def get_wors_from_a_category(category):
    words = []
    for index in range(len(data[category])):
        words.append(data[category][index]['word'])
    return words

def get_word_and_translate(category):
    words = []
    for index in range(len(data[category])):
        words.append((data[category][index]['word'],data[category][index]['translate']))
    return words

animals , animals_synonyms = extract_word_by_category('animals')

fruits, fruits_synonyms = extract_word_by_category('fruits')

vegetables, vegetables_synonyms =extract_word_by_category('vegetables')

colors, colors_synonyms = extract_word_by_category('colors')

sports, sports_synonyms = extract_word_by_category('sports')

questions = dict()

for word, corect_asnwer in animals:
    question = generate_multiple_choice_question(word, animals_synonyms, corect_asnwer, 'animals')
    questions.update(question)

questions = dict()
questions['multiple_choice'] = []
questions['input'] = []
questions['translate'] = []

#Questions with multiple choice from sport
for word, definition in extract_word_and_definition('sports'):
    question = generate_multiple_choice_question(definition, get_wors_from_a_category('sports'), word, 'sports')
    questions['multiple_choice'].append(question)

#Questions with multiple choice from colors
for word in get_wors_from_a_category('colors'):
    question = generate_multiple_choice_question('Choice the corect color : ' + word, get_wors_from_a_category('colors'), word, 'colors')
    questions['multiple_choice'].append(question)

occupations, occupations_synonyms = extract_word_by_category('occupations')
#Questions with multiple choice from occupations
for word, synonym in occupations:
    if synonym and synonym!=word:
        question = generate_multiple_choice_question('Select the synonym for  : ' + word, occupations_synonyms, synonym, 'occupations')
        questions['multiple_choice'].append(question)

#Questions with multiple choice from sport
for word, definition in extract_word_and_definition('animals'):
    question = generate_multiple_choice_question(definition, get_wors_from_a_category('animals'), word, 'animals')
    questions['multiple_choice'].append(question)


#Questions with input from animals and definition
for word, definition in extract_word_and_definition('animals'):
    question = generate_input_question(definition, word, 'animals')
    questions['input'].append(question)

#Questions with input from sports and definition
for word, definition in extract_word_and_definition('sports'):
    question = generate_input_question(definition, word, 'sports')
    questions['input'].append(question)



#Questions with input from animals with translate
for word, translate in get_word_and_translate('sports'):
    question = generate_input_question("Translate the word :" + word, translate, 'sports')
    questions['translate'] .append(question)

#Questions with input from animals with translate
for word, translate in get_word_and_translate('animals'):
    question = generate_input_question("Translate the word :" + word, translate, 'animals')
    questions['translate'] .append(question)

import json

with open('Data/questions.json', 'w') as outfile:
        json.dump(questions, outfile, indent=4)


