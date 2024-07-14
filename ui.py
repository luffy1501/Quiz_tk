from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_lable = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_lable.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125,
                                                     text="S",
                                                     width=290,
                                                     fill=THEME_COLOR,
                                                     font=("Arial", 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        right = PhotoImage(file="./images/true.png")
        wrong = PhotoImage(file="./images/false.png")
        right_button = Button(image=right, highlightthickness=0, command=self.true_pressed)
        right_button.grid(column=0, row=2)

        wrong_button = Button(image=wrong, highlightthickness=0, command=self.false_pressed)
        wrong_button.grid(column=1, row=2)

        self.next_question()
        self.window.mainloop()

    def next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            self.score_lable.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f"You have reached the goal.Your score is above")

    def true_pressed(self):

        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.next_question)
