import time


class QuizLogic:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        users_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False):").lower()
        self.check_answer(users_answer, current_question.answer)

    def check_answer(self, users_answer, current_answer):
        if users_answer.lower() == current_answer.lower():
            print("checking your answer... Please Wait!")
            time.sleep(0.8)
            print("\n")
            print("YAY! You got the write answer")
            self.score += 1
        else:
            print("checking your answer... Please Wait!")
            time.sleep(0.8)
            print("\n")
            print("oh no! that's not the correct answer\n")
        print(f"Current Score is: {self.score}/{self.question_number}")
        print(f"the correct answer is: {current_answer}")