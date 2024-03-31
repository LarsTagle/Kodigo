import spacy
import pytextrank
import sys
import os
import json

def summarize(document_text):
    nlp = spacy.load("en_core_web_sm")
    nlp.add_pipe("textrank")
    doc = nlp(document_text)

    total_sentences = len(list(doc.sents))
    target_sentences = int(total_sentences * 0.6)  #70% of the total sentences

    summarized_text = ""
    sentences = []
    
    og_sents = []
    summarized_sents = []
    summarized_text = ""
    
    for sent in list(doc.sents):
        og_sents.append(sent.text)
    
    for sent in list(doc._.textrank.summary(limit_sentences = target_sentences)):
        summarized_sents.append(sent.text)
    
    ranked_sents = ' '.join(summarized_sents)
    
    # Create a dictionary to store the indices of each sentence in the longer list
    indices_dict = {sentence: index for index, sentence in enumerate(og_sents)}

    # Sort the shorter list based on the indices in the longer list
    summarized_sents = sorted(summarized_sents, key=lambda x: indices_dict[x])
    
    summarized_text = ' '.join(summarized_sents)
      
    return summarized_text, summarized_sents, ranked_sents

fn = sys.argv[1]
document_text = sys.argv[2]

base_path = os.getcwd()
relative_path = f"kodigo\\game\\python\\temp\\{fn}.json"
fp = os.path.join(base_path, relative_path)#r"D:\renpy-8.1.3-sdk\Kodigo\game\python\docs\Quiz 1.json"#

summarized_text, summarized_sents, ranked_sents = summarize(document_text)

#read the json file
with open(fp, 'r') as file:
    quiz = json.load(file)

quiz["notes"] = summarized_text
quiz["sentences"] = summarized_sents
quiz["ranked_sentences"] = ranked_sents

#save the updated data back to json
with open(fp, 'w') as file:
    json.dump(quiz, file)