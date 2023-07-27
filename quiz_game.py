import tkinter as tk
from tkinter import messagebox
import random

# Quiz questions in the format: "Question": "Correct Answer"
quiz_questions = {
    "What is the capital of France?": "Paris",
    "Who wrote the play 'Romeo and Juliet'?": "William Shakespeare",
    "What is the chemical symbol for water?": "H2O",
    "What is the largest planet in our solar system?": "Jupiter",
    "What is the main component of air?": "Nitrogen",
}

class QuizGame(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Quiz Game")
        self.geometry("400x300")
        self.configure(bg="lightblue")

        self.score = 0
        self.questions = list(quiz_questions.keys())
        random.shuffle(self.questions)
        self.current_question = 0

        self.create_widgets()
        self.present_question()

    def create_widgets(self):
        self.label_question = tk.Label(self, text="", wraplength=350, font=("Arial", 14), bg="lightblue")
        self.label_question.pack(pady=10)

        self.answer_var = tk.StringVar()
        self.entry_answer = tk.Entry(self, textvariable=self.answer_var, font=("Arial", 12))
        self.entry_answer.pack(pady=10)

        self.btn_submit = tk.Button(self, text="Submit", command=self.evaluate_answer, font=("Arial", 12), bg="green", fg="white")
        self.btn_submit.pack(pady=5)

        self.label_feedback = tk.Label(self, text="", font=("Arial", 12), bg="lightblue")
        self.label_feedback.pack(pady=10)

        self.label_score = tk.Label(self, text="Score: 0", font=("Arial", 14), bg="lightblue")
        self.label_score.pack(pady=5)

        self.btn_next = tk.Button(self, text="Next Question", command=self.next_question, font=("Arial", 12), bg="blue", fg="white")
        self.btn_next.pack(pady=5)

    def present_question(self):
        if self.current_question < len(self.questions):
            question_text = self.questions[self.current_question]
            self.label_question.config(text=question_text)
            self.answer_var.set("")
            self.btn_submit.config(state=tk.NORMAL)
            self.label_feedback.config(text="")
            self.btn_next.config(state=tk.DISABLED)

    def evaluate_answer(self):
        user_answer = self.answer_var.get().strip().lower()
        correct_answer = quiz_questions[self.questions[self.current_question]].lower()

        if user_answer == correct_answer:
            self.score += 1
            self.label_feedback.config(text="Correct!", fg="green")
        else:
            self.label_feedback.config(text=f"Wrong. The correct answer is: {correct_answer}", fg="red")

        self.label_score.config(text=f"Score: {self.score}")
        self.btn_submit.config(state=tk.DISABLED)
        self.btn_next.config(state=tk.NORMAL)

    def next_question(self):
        self.current_question += 1
        self.present_question()

        if self.current_question == len(self.questions):
            self.show_final_results()

    def show_final_results(self):
        performance_message = "Congratulations! You performed well." if (self.score / len(self.questions)) >= 0.7 else "Keep practicing to improve your knowledge."
        messagebox.showinfo("Quiz Finished", f"Quiz Finished!\nYour score: {self.score}/{len(self.questions)}\n{performance_message}")
        self.quit()

if __name__ == "__main__":
    app = QuizGame()
    app.mainloop()
