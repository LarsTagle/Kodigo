import spacy
import pytextrank
import sys
import os

def summarize(document_text):
    nlp = spacy.load("en_core_web_sm")
    nlp.add_pipe("textrank")
    doc = nlp(document_text)

    total_sentences = len(list(doc.sents))
    target_sentences = int(total_sentences * 0.7)  #70% of the total sentences

    summarized_text = ""
    sentences = []
    
    og_sents = []
    summarized_sents = []
    summarized_text = ""
    
    for sent in list(doc.sents):
        og_sents.append(sent.text)
    
    for sent in list(doc._.textrank.summary(limit_sentences = target_sentences)):
        summarized_sents.append(sent.text)
    
    # Create a dictionary to store the indices of each sentence in the longer list
    indices_dict = {sentence: index for index, sentence in enumerate(og_sents)}

    # Sort the shorter list based on the indices in the longer list
    summarized_sents = sorted(summarized_sents, key=lambda x: indices_dict[x])
    
    for sent in summarized_sents:
      summarized_text += " " + sent
      
    return summarized_text

filename = sys.argv[1]
document_text = sys.argv[2]

base_path = os.getcwd()
relative_path = f"kodigo\\game\\python\\docs\\{filename}.txt"
fp = os.path.join(base_path, relative_path)

summarized_text = summarize(document_text)
print(summarized_text)

with open(fp, "w") as file:
        file.write(summarized_text)