from question_model import Question
from data import question_data


question_bank = []

for question in question_data:
    question_bank.append(Question(question["text"], question["answer"]))

for question_nr in range(0, len(question_bank)):
    print(question_bank[question_nr].text, ":", question_bank[question_nr].answer)
