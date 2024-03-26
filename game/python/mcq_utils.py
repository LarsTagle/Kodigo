import spacy
import pytextrank
import nltk
import pke
import string
import random
import json
nltk.download('stopwords')
from nltk.corpus import stopwords
from flashtext import KeywordProcessor
from sense2vec import Sense2Vec
from question_generator import get_question

def summarize(document_text):
    nlp = spacy.load("en_core_web_sm")
    nlp.add_pipe("textrank")
    doc = nlp(document_text)

    total_sentences = len(list(doc.sents))
    target_sentences = int(total_sentences * 0.7)  #70% of the total sentences

    summarized_text = ""
    sentences = []

    for sent in doc._.textrank.summary(limit_sentences = target_sentences):
      summarized_text += " " + sent.text
      sentences.append(sent.text)

    return summarized_text, sentences

def keywords(text, n):
    out = []

    extractor = pke.unsupervised.MultipartiteRank()
    extractor.load_document(input=text, language='en')
    pos = {'PROPN', 'NOUN', 'VERB'}
    stoplist = list(string.punctuation)
    stoplist += stopwords.words('english')
    extractor.candidate_selection(pos=pos)
    # 4. build the Multipartite graph and rank candidates using random walk,
    #    alpha controls the weight adjustment mechanism, see TopicRank for
    #    threshold/method parameters.
    try:
        extractor.candidate_weighting(alpha=1.1,
                                      threshold=0.75,
                                      method='average')
    except:
        return out

    keyphrases = extractor.get_n_best(n)

    for key in keyphrases:
        out.append(key[0])

    return out

def tag_word(keywords, keyword):
  nlp = spacy.load('en_core_web_sm')

  doc = nlp(keywords)

  for token in doc:
    if token.text.lower() == keyword.lower():
      return token.pos_

def clean_keywords(keywords):
    for i in range(len(keywords)):
        if ' ' in keywords[i]:
            phrase = keywords[i].split()
            key_tags = []
            for word in phrase:
                key_tags.append(tag_word(keywords[i], word))
            if len(key_tags) < 4:
                if key_tags == ['VERB', 'NOUN', 'NOUN']:
                    phrase.pop(0)
                    keywords[i] =  ' '.join(phrase)
                if key_tags == ['NOUN', 'NOUN', 'VERB']:
                    phrase.pop(2)
                    keywords[i] =  ' '.join(phrase)
                if key_tags == ['NOUN', 'VERB']:
                    phrase.pop(1)
                    keywords[i] =  ' '.join(phrase)
                if key_tags == ['VERB', 'NOUN', 'VERB']:
                    phrase.pop(2)
                    keywords[i] =  ' '.join(phrase)
            else:
                if key_tags[0] == 'VERB':
                    phrase.pop(0)
                    keywords[i] =  ' '.join(phrase)
                    continue
                for j in range(len(key_tags)):
                    if key_tags[j] == 'VERB':
                        phrase = phrase[:j]
                        keywords[i] =  ' '.join(phrase)
                        break

    return keywords

def map_sentences(sentence, keywords):
    keyword_processor = KeywordProcessor()
    keyword_processor.add_keywords_from_list(keywords)

    keywords_found = keyword_processor.extract_keywords(sentence)

    answer = ""

    if len(keywords_found) != 0:
        answer = keywords_found[0]

    return answer

def map(sentences, keywords):
    answers = []

    for sentence in sentences:
        answers.append(map_sentences(sentence, keywords))

    sentences_final = []
    answers_final = []

    for i in range(len(sentences)):
        if answers[i] != "":
            sentences_final.append(sentences[i])
            answers_final.append(answers[i])

    return sentences_final, answers_final

def clean_option(option):
    option = option.strip("/u/")
    option = option.strip("\\*")
    option = option.strip("~~")
    return option
def distractors(word, s2v):
    options = []

    word = word.lower()
    word = word.replace(' ','_')

    sense = s2v.get_best_sense(word)

    if sense == None:
        return None

    pos = sense.split("|")[1]
    most_similar = s2v.most_similar(sense,n=12)

    max = 0
    while max != 3:
        option = random.choices(most_similar)
        p = option[0][0].split('|')[1]
        option = option[0][0].split('|')[0]
        if option.lower() not in [word.lower() for word in options] and pos == p and option.lower() != word:
            #print(f"{pos} : {p}")
            option = clean_option(option)
            options.append(option.replace('_',' '))
            max += 1

    return options

def options(answers):
    options = []
    s2v = Sense2Vec().from_disk('s2v_old')

    for answer in answers:
        options.append(distractors(answer, s2v))

    return options

def questions(sentences, answers):
    questions = []

    for i in range(len(sentences)):
        questions.append(get_question(sentences[i], answers[i]))

    return questions

def dictionary(questions, answers, options):
    dict = {"Questions": [],
            "Answers": [],
            "Options": [],}

    dict["Questions"] = questions
    dict["Answers"] = answers
    dict["Options"] = options

    return dict

def save_json(dict):
    with open("questions_dict.json", "w") as json_file:
        json.dump(dict, json_file)