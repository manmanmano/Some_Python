class QuizBrain():

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list

    def ask_question(self):
        asked_question = self.question_list[self.question_number]
        self.question_number += 1
        input(f"Q.{self.question_number}: {asked_question.text} (True/False): ")

    def still_has_questions(self):
        return self.question_number < len(self.question_list)
