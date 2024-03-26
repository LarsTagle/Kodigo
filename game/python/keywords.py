import pke
import string
from nltk.corpus import stopwords

import sys
import json
import os

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

fn = sys.argv[1]
text = sys.argv[2]
n = int(sys.argv[3])
keywords = keywords(text, n)

base_path = os.getcwd()
relative_path = f"kodigo\\game\\python\\docs\\{fn}_keys.json"
fp = os.path.join(base_path, relative_path) #f"D:\\renpy-8.1.3-sdk\\kodigo\\game\\python\\docs\\{filename}.json"
    
with open(fp, "w") as json_file:
    json.dump(keywords, json_file)