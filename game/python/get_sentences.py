import spacy
import json
import sys
import os

filename = sys.argv[1]
text = sys.argv[2]

nlp = spacy.load("en_core_web_sm")
doc = nlp(text)

sentences = []
for sent in list(doc.sents):
    sentences.append(sent.text)
    
base_path = os.getcwd()
relative_path = f"kodigo\\game\\python\\docs\\{filename}.json"
fp = os.path.join(base_path, relative_path) #f"D:\\renpy-8.1.3-sdk\\kodigo\\game\\python\\docs\\{filename}.json"
    
with open(fp, "w") as json_file:
    json.dump(sentences, json_file, indent=4)