from tkinter import *
from tkinter import PhotoImage

import quiz_brain
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class Quizeller():

    def __init__(self, quiz: QuizBrain):
        self.window = Tk()
        self.canvas = Canvas()
        self.window.title("Quizzer")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)
        self.canvas.config(width=300, height=270, background="WHITE", )
        self.h = quiz
        question_text = quiz.next_question()
        self.user_answer = quiz.check_answer('True')

        # self.canvas.create_text(122,122, text='A wonderful', font=('Ariel',20,'italic'), fill='red',anchor="center")
        canvas2 = self.canvas.create_text(152, 122, font=('Ariel', 18, 'italic'), fill='red', anchor="center",
                                          width=250)
        self.canvas.itemconfig(canvas2, text=question_text)

        self.score_label = Label(background=THEME_COLOR, fg="white", text=f"SCORE ={quiz.update_score()}",
                                 font=('Ariel', 15, 'italic'))
        true_pict = PhotoImage(file="images/true.png/")
        false_pict = PhotoImage(file="images/false.png")
        #
        self.true_button = Button(image=true_pict, command=(self.True_button))

        self.false_button = Button(image=false_pict, )

        self.score_label.grid(row=0, column=0, columnspan=2, pady=30)
        self.canvas.grid(row=1, column=1)
        self.true_button.grid(row=3, column=0, sticky='w', columnspan=2, pady=22)
        self.false_button.grid(row=3, column=1, columnspan=1, sticky='e', pady=22)

        self.window.mainloop()
    
    def True_button(self):
        self.h.check_answer('True')
        self.score_label.config(text=self.h.update_score())
        self.h.next_question()
         




# def change_quastion(self):


# BACKGROUND_COLOR = "#B1DDC6"Q

# window.title("FLASH CARD GAME")
# window.config(padx=50, pady=50, background=BACKGROUND_COLOR)
#
# canvas = tk.Canvas(window, width=800, height=526)
# back_photo = tk.PhotoImage(file="card_back.png")
# front_photo = tk.PhotoImage(file="card_front.png")
# canvas.create_image(400, 263, image=front_photo)
# canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
# canvas.grid(row=0, column=0, columnspan=2)
# # create texts
# test_text = canvas.create_text(400, 162, text="French", font=("Ariel", 20, "italic"))
#
# # buttons design
# right_image = PhotoImage(file='right.png')
# left_image = PhotoImage(file="wrong.png")
#
# right_button = tk.Button(window, image=right_image, text="right", bg='pink', width=100, highlightthickness=0,
#                          background=BACKGROUND_COLOR, command=clean_text)
# right_button.grid(row=1, column=1)
#
# left_button = tk.Button(image=left_image, text="left", bg='pink', width=100, highlightthickness=0,
#                         background=BACKGROUND_COLOR, command=words_to_learn_button)
# left_button.grid(row=1, column=0)
#
