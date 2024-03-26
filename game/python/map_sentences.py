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

filename = sys.argv[1]

with open(r"D:\renpy-8.1.3-sdk\Kodigo\game\python\docs\Quiz_keys.json", 'r') as json_file:
    keywords = json.load(json_file)
    
with open(r"D:\renpy-8.1.3-sdk\Kodigo\game\python\docs\Quiz.json", 'r') as json_file:
    sentences = json.load(json_file)
    
sentences, answers = map(sentences, keywords)

for i in range(len(sentences)):
    print(f"{sentences[i]}: {keywords[i]}")
    
base_path = os.getcwd()
relative_path = f"kodigo\\game\\python\\docs\\{filename}_mapped.json"
fp = os.path.join(base_path, relative_path)#r"D:\renpy-8.1.3-sdk\Kodigo\game\python\docs\quiz_mapped.json"

data = {
    'sentences': sentences,
    'answers': answers
}

with open(fp, "w") as json_file:
    json.dump(data, json_file)