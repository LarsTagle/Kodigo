from flashtext import KeywordProcessor
import os
import sys
import json

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

fn = sys.argv[1]
base_path = os.getcwd()
relative_path = f"kodigo\\game\\python\\docs\\{fn}.json"
fp = os.path.join(base_path, relative_path)#####r"D:\renpy-8.1.3-sdk\Kodigo\game\python\docs\Text.json"#

#read the json file
with open(fp, 'r') as file:
    quiz = json.load(file)

keywords = quiz["keywords"]
sentences = quiz["sentences"]
    
sentences, answers = map(sentences, keywords)

for i in range(len(sentences)):
    print(f"{sentences[i]}: {answers[i]}")

quiz["answers"] = answers
quiz["sentences"] = sentences 

#save the updated data back to json
with open(fp, 'w') as file:
    json.dump(quiz, file)
    
print("done")