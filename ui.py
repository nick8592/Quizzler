from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.window = Tk()
        self.quiz = quiz_brain
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        # score label
        self.score_label = Label(self.window, text="Score: 0", font=('Arial', 20),
                                 bg=THEME_COLOR, fg="white", padx=20, pady=20)
        self.score_label.grid(column=1, row=0)
        # white background
        self.canvas = Canvas(width=300, height=250)
        self.canvas.grid(column=0, row=1, columnspan=2, padx=20, pady=50)
        # question text
        self.question_text = self.canvas.create_text(
            150, 125, text='TEST', width=280, font=('Arial', 20, 'italic'), fill=THEME_COLOR)

        # check image
        check_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=check_img, padx=20, pady=20,
                                  highlightthickness=0, command=self.true_button_pressed)
        self.true_button.grid(column=0, row=2)
        # cross image
        cross_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=cross_img, padx=20, pady=20,
                                   highlightthickness=0, command=self.false_button_pressed)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_button_pressed(self):
        answer = self.quiz.check_answer("true")
        self.give_feedback(answer)

    def false_button_pressed(self):
        answer = self.quiz.check_answer("false")
        self.give_feedback(answer)

    def give_feedback(self, answer):
        if answer:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)





