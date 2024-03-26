from transformers import T5ForConditionalGeneration, T5Tokenizer

question_model = T5ForConditionalGeneration.from_pretrained('ramsrigouthamg/t5_squad_v1')
question_tokenizer = T5Tokenizer.from_pretrained('t5-base')

def get_question(sentence, answer):
    text = "context: {} answer: {} ".format(sentence, answer)
    max_len = 256
    encoding = question_tokenizer.encode_plus(text, max_length = max_len, padding = True, return_tensors = "pt", truncation=True)

    input_ids, attention_mask = encoding["input_ids"], encoding["attention_mask"]

    outs = question_model.generate(input_ids = input_ids,
                                    attention_mask = attention_mask,
                                    early_stopping = True,
                                    #numb_beams = 5,
                                    num_return_sequences = 1,
                                    no_repeat_ngram_size = 2,
                                    max_length = 200)

    dec  = [question_tokenizer.decode(ids) for ids in outs]

    Question = dec[0].replace("<pad> question: ", "").replace("</s>", "")
    Question = Question.strip()

    return Question
