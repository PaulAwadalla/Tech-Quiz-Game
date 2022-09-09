from question_model import Question
from data import question_data
from data import easy_questions_data
from quiz_logic import QuizLogic

question_bank = [
]
user_difficulty = input("which questions would you like normal or easy?: ")
if user_difficulty == "easy":
    for question in easy_questions_data:
        question_text = question['question']
        question_answer = question['correct_answer']
        new_question = Question(question_text, question_answer)
        question_bank.append(new_question)
else:
    for question in question_data:
        question_text = question['text']
        question_answer = question['answer']
        new_question = Question(question_text, question_answer)
        question_bank.append(new_question)

quiz = QuizLogic(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
    print('\n')

print("------------------------------------")
print("------------------------------------")
print("------------------------------------")
print("------------------------------------")
print("You've Completed the quiz")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")