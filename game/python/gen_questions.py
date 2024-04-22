import sys
import json
import os
import re

from question_generator import get_questions

fn = sys.argv[1]
base_path = os.getcwd()
relative_path = f"kodigo\\game\\python\\temp\\{fn}.json"
fp = os.path.join(base_path, relative_path)

#read the json file
with open(fp, 'r') as file:
    quiz = json.load(file)

answers = quiz["answers"]
sentences = quiz["sentences"].copy()
numbers = []
questions = []

for i in range(len(sentences)):
    numbers.append(i)
    questions.append("")

# Sort sentences based on their lengths

# Zip the sentences and another_list together and sort based on the length of sentences in descending order
sorted_data = sorted(zip(sentences, numbers, answers), key=lambda x: len(x[0]), reverse=True)

# Unzip the sorted pairs back into separate lists
sorted_sentences, sorted_numbers, sorted_answers= zip(*sorted_data)

#sort the numbers by sorted_sentence?

#get the 1/4 of the sentences

# Calculate the length of one-fourth of the sentences
quarter_length = len(sorted_sentences) // 4
# Get the first one-fourth of the sorted sentences
quarter_sentences = sorted_sentences[:quarter_length]
quarter_numbers = sorted_numbers[:quarter_length]
quarter_answers = sorted_answers[:quarter_length]

#get the questions
quarter_questions = get_questions(quarter_sentences, quarter_answers)

for i in range(len(sentences)):
    for j in range(len(quarter_numbers)):
        if i == quarter_numbers[j]:
            questions[quarter_numbers[j]] = quarter_questions[j]

#get fill in the blank questions

blank_space = '___'

for i in range(len(sentences)):
     if questions[i] == "":
        pattern = re.compile(answers[i], re.IGNORECASE)
        questions[i] = pattern.sub(blank_space, sentences[i], count=1)

quiz["questions"] = questions

#save the updated data back to json
with open(fp, 'w') as file:
    json.dump(quiz, file)

print(questions)