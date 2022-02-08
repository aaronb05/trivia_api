
import config
import ui
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []
for question in config.connect_to_api()["results"]:
    index = 0
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)


# while quiz.still_has_questions():
# question = quiz.next_question()
quiz_ui = ui.QuizInterface(quiz)

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")




