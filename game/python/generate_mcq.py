from mcq_utils import summarize, keywords, clean_keywords, map, options, questions, dictionary, save_json

#1. Get text from file.
with open('D:/renpy-8.1.3-sdk/kodigo/game/python/docs/Intro-to-OS-1.txt', 'r', encoding='utf-8') as file:
    document_text = file.read()

#2. Summarize text.
summarized_text, sentences = summarize(document_text)
print("Test summarization is successful!\n")

#3. Get keywords.
keywords = keywords(summarized_text, len(sentences)+40)
print("Keywords extraction is  successful!\n")

#4. Clean keywords.
keywords = clean_keywords(keywords)
print("Cleaning the keywords is successful!\n")

#5. Map keywords to sentences to get answers.
sentences, answers = map(sentences, keywords)
print("Sentences-keywords mapping is successful!\n")

#6. Get distractors.
options = options(answers)
print("Distractor extraction is successful!\n")

#7. Get questions.
questions = questions(sentences, answers)
print("Generated questions successful!\n")

#8. Add the questions, answers, options to dictionary.
dict = dictionary(questions, answers, options)
print("Creating dictionary is successful!\n")

#9. Save the dictionary to a .txt file.
save_json(dict)
print("Saving to json is successful!\n")
