from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizzUserInterface:

    def __init__(self, quiz_brain: QuizBrain):

        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.true_img = PhotoImage(file="images/true.png")
        self.false_img = PhotoImage(file="images/false.png")

        self.canvas = Canvas(width=300, height=250,
                             bg="aliceblue", highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125, text=f"", font=(
            "Arial", 20, "italic"), fill=THEME_COLOR, width=280)

        self.score_text = Label(text=f"Score: 0", font=(
            "Arial", 15, "normal"), background=THEME_COLOR, fg="aliceblue")

        self.true_button = Button(
            image=self.true_img, highlightthickness=0, command=self.user_true)
        self.false_button = Button(
            image=self.false_img, highlightthickness=0, command=self.user_false)

        self.score_text.grid(row=0, column=1,  padx=20, pady=20)
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=20)
        self.true_button.grid(row=2, column=0, padx=20, pady=20)
        self.false_button.grid(row=2, column=1, padx=20, pady=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(background="aliceblue")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
            self.canvas.itemconfig(self.question_text,text="You've reached the end of the quiz.")

    def user_true(self):
        user_correct = self.quiz.check_answer("true")
        self.give_feedback(user_correct)

    def user_false(self):
        user_correct = self.quiz.check_answer("false")
        self.give_feedback(user_correct)

    def give_feedback(self, user_correct):
        if user_correct:
            self.canvas.config(background="green")
            self.score_text.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.config(background="red")
        self.window.after(1000, self.get_next_question)
        
