
from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz: QuizBrain):
        self.window = Tk()
        self.quiz_brain = quiz
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125,
                                                     text="placeholder",
                                                     fill=THEME_COLOR,
                                                     width=250,
                                                     font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)
        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, command=self.true)
        self.true_button.grid(row=2, column=1)
        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, command=self.false)
        self.false_button.grid(row=2, column=0)
        self.quiz_brain.still_has_questions()
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        q_text = self.quiz_brain.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)

    # def check_my_answer(self, guess):
    #     guess = guess
    #     correct_answer = self.quiz_brain.current_question.correct_answer
    #     if guess.lower() == correct_answer.lower():
    #         self.quiz_brain.score += 1
    #         print("You got it right!")
    #     else:
    #         print("That's wrong.")
    #
    #     print(f"Your current score is: {self.quiz_brain.score}/{self.quiz_brain.question_number}")
    #     print("\n")
    def true(self):
        correct = self.quiz_brain.check_answer("true")
        self.user_feedback(correct)

    def false(self):
        self.quiz_brain.check_answer("false")

    def user_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(500, self.get_next_question())


