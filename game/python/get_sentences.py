import spacy
import json
import sys
import os

fn = sys.argv[1]
text = sys.argv[2]

nlp = spacy.load("en_core_web_sm")
doc = nlp(text)

sentences = []
for sent in list(doc.sents):
    sentences.append(sent.text)
    
base_path = os.getcwd()
relative_path = f"kodigo\\game\\python\\docs\\{fn}.json"
fp = os.path.join(base_path, relative_path) 
    
#read the json file
with open(fp, 'r') as file:
    quiz = json.load(file)

quiz["sentences"] = sentences

#save the updated data back to json
with open(fp, 'w') as file:
    json.dump(quiz, file)