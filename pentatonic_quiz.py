import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import random
import os

class PentatonicQuiz:
    def __init__(self, root):
        self.root = root
        self.root.title("Pentatonic Shapes Quiz")
        self.root.geometry("800x700")
        self.root.configure(bg='#2c3e50')
        
        # Quiz data
        self.total_questions = 50
        self.current_question = 0
        self.correct_answers = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
        self.wrong_answers = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
        self.current_shape = None
        self.quiz_active = False
        
        # Check if image files exist
        self.image_files = []
        for i in range(1, 6):
            filename = f"shape{i}.jpg"
            if os.path.exists(filename):
                self.image_files.append((i, filename))
            else:
                messagebox.showerror("Error", f"Image file '{filename}' not found!")
                return
        
        self.setup_ui()
        self.start_quiz()
    
    def setup_ui(self):
        # Title
        title_label = tk.Label(
            self.root, 
            text="Pentatonic Shapes Quiz", 
            font=('Arial', 24, 'bold'),
            fg='white',
            bg='#2c3e50'
        )
        title_label.pack(pady=20)
        
        # Progress label
        self.progress_label = tk.Label(
            self.root,
            text="Question 1 of 50",
            font=('Arial', 14),
            fg='white',
            bg='#2c3e50'
        )
        self.progress_label.pack(pady=5)
        
        # Image frame
        self.image_frame = tk.Frame(self.root, bg='#2c3e50')
        self.image_frame.pack(pady=20)
        
        # Image label
        self.image_label = tk.Label(
            self.image_frame,
            bg='white',
            relief='solid',
            borderwidth=2
        )
        self.image_label.pack()
        
        # Question label
        self.question_label = tk.Label(
            self.root,
            text="Which pentatonic shape is this? (Enter 1-5)",
            font=('Arial', 16),
            fg='white',
            bg='#2c3e50'
        )
        self.question_label.pack(pady=20)
        
        # Answer entry frame
        answer_frame = tk.Frame(self.root, bg='#2c3e50')
        answer_frame.pack(pady=10)
        
        self.answer_var = tk.StringVar()
        self.answer_entry = tk.Entry(
            answer_frame,
            textvariable=self.answer_var,
            font=('Arial', 16),
            width=5,
            justify='center'
        )
        self.answer_entry.pack(side=tk.LEFT, padx=5)
        self.answer_entry.bind('<Return>', self.check_answer)
        
        # Submit button
        self.submit_btn = tk.Button(
            answer_frame,
            text="Submit",
            font=('Arial', 14),
            bg='#3498db',
            fg='white',
            command=self.check_answer,
            padx=20
        )
        self.submit_btn.pack(side=tk.LEFT, padx=5)
        
        # Feedback label
        self.feedback_label = tk.Label(
            self.root,
            text="",
            font=('Arial', 14, 'bold'),
            bg='#2c3e50'
        )
        self.feedback_label.pack(pady=15)
        
        # Next button (initially hidden)
        self.next_btn = tk.Button(
            self.root,
            text="Next Question",
            font=('Arial', 14),
            bg='#27ae60',
            fg='white',
            command=self.next_question,
            padx=20
        )
        self.next_btn.pack(pady=10)
        self.next_btn.pack_forget()
        
        # Results frame (initially hidden)
        self.results_frame = tk.Frame(self.root, bg='#2c3e50')
        
        # Focus on entry field
        self.answer_entry.focus_set()
    
    def load_and_display_image(self, shape_number):
        """Load and display the image for the given shape number"""
        try:
            filename = f"shape{shape_number}.jpg"
            
            # Open and resize image
            pil_image = Image.open(filename)
            
            # Randomly rotate 180 degrees (50% chance)
            if random.choice([True, False]):
                pil_image = pil_image.rotate(180)
            
            # Calculate size while maintaining aspect ratio
            max_width, max_height = 400, 300
            pil_image.thumbnail((max_width, max_height), Image.Resampling.LANCZOS)
            
            # Convert to PhotoImage
            photo = ImageTk.PhotoImage(pil_image)
            
            # Update label
            self.image_label.configure(image=photo)
            self.image_label.image = photo  # Keep a reference
            
        except Exception as e:
            messagebox.showerror("Error", f"Could not load image: {e}")
    
    def start_quiz(self):
        """Start or restart the quiz"""
        self.quiz_active = True
        self.current_question = 0
        self.correct_answers = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
        self.wrong_answers = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
        self.results_frame.pack_forget()
        self.show_next_question()
    
    def show_next_question(self):
        """Display the next question"""
        if self.current_question >= self.total_questions:
            self.show_results()
            return
        
        self.current_question += 1
        self.current_shape = random.randint(1, 5)
        
        # Update UI
        self.progress_label.config(text=f"Question {self.current_question} of {self.total_questions}")
        self.load_and_display_image(self.current_shape)
        self.answer_var.set("")
        self.feedback_label.config(text="")
        self.next_btn.pack_forget()
        self.submit_btn.config(state='normal')
        self.answer_entry.config(state='normal')
        self.answer_entry.focus_set()
        
        # Rebind Enter key to check answer for new question
        self.root.bind('<Return>', self.check_answer)
    
    def check_answer(self, event=None):
        """Check if the answer is correct"""
        if not self.quiz_active:
            return
        
        try:
            user_answer = int(self.answer_var.get())
            if user_answer < 1 or user_answer > 5:
                raise ValueError
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a number between 1 and 5")
            return
        
        # Disable entry and submit button
        self.answer_entry.config(state='disabled')
        self.submit_btn.config(state='disabled')
        
        # Check if correct
        if user_answer == self.current_shape:
            self.correct_answers[self.current_shape] += 1
            self.feedback_label.config(text="Correct! ✓", fg='#27ae60')
        else:
            self.wrong_answers[self.current_shape] += 1
            self.feedback_label.config(
                text=f"Incorrect! The correct answer is {self.current_shape}", 
                fg='#e74c3c'
            )
        
        # Show next button
        if self.current_question < self.total_questions:
            self.next_btn.pack(pady=10)
        else:
            # Last question - show results button
            self.next_btn.config(text="Show Results")
            self.next_btn.pack(pady=10)
        
        # Bind Enter key to next question after showing result
        self.root.bind('<Return>', self.next_question_key)
    
    def next_question(self):
        """Move to next question or show results"""
        if self.current_question >= self.total_questions:
            self.show_results()
        else:
            self.show_next_question()
    
    def next_question_key(self, event=None):
        """Handle Enter key press to go to next question"""
        # Only proceed if we're showing the result (submit button is disabled)
        if self.submit_btn['state'] == 'disabled':
            self.next_question()
    
    def show_results(self):
        """Display the final results"""
        self.quiz_active = False
        
        # Hide quiz elements
        self.image_frame.pack_forget()
        self.question_label.pack_forget()
        self.answer_entry.master.pack_forget()
        self.feedback_label.pack_forget()
        self.next_btn.pack_forget()
        
        # Show results
        self.progress_label.config(text="Quiz Complete!")
        
        # Results frame
        self.results_frame = tk.Frame(self.root, bg='#2c3e50')
        self.results_frame.pack(pady=20, fill='both', expand=True)
        
        # Results title
        results_title = tk.Label(
            self.results_frame,
            text="Results Summary",
            font=('Arial', 20, 'bold'),
            fg='white',
            bg='#2c3e50'
        )
        results_title.pack(pady=10)
        
        # Calculate total correct and wrong
        total_correct = sum(self.correct_answers.values())
        total_wrong = sum(self.wrong_answers.values())
        accuracy = (total_correct / self.total_questions) * 100
        
        # Overall stats
        overall_label = tk.Label(
            self.results_frame,
            text=f"Overall: {total_correct}/{self.total_questions} correct ({accuracy:.1f}%)",
            font=('Arial', 16, 'bold'),
            fg='white',
            bg='#2c3e50'
        )
        overall_label.pack(pady=10)
        
        # Individual shape results
        for shape in range(1, 6):
            correct = self.correct_answers[shape]
            wrong = self.wrong_answers[shape]
            total_shape = correct + wrong
            
            if total_shape > 0:
                shape_accuracy = (correct / total_shape) * 100
                result_text = f"Shape {shape}: {correct}/{total_shape} correct ({shape_accuracy:.1f}%)"
            else:
                result_text = f"Shape {shape}: Not shown in this quiz"
            
            shape_label = tk.Label(
                self.results_frame,
                text=result_text,
                font=('Arial', 14),
                fg='white',
                bg='#2c3e50'
            )
            shape_label.pack(pady=2)
        
        # Restart button
        restart_btn = tk.Button(
            self.results_frame,
            text="Start New Quiz",
            font=('Arial', 16),
            bg='#3498db',
            fg='white',
            command=self.restart_quiz,
            padx=30,
            pady=10
        )
        restart_btn.pack(pady=20)
        
        # Quit button
        quit_btn = tk.Button(
            self.results_frame,
            text="Quit",
            font=('Arial', 16),
            bg='#e74c3c',
            fg='white',
            command=self.root.quit,
            padx=30,
            pady=10
        )
        quit_btn.pack(pady=5)
    
    def restart_quiz(self):
        """Restart the quiz"""
        # Show quiz elements again
        self.image_frame.pack(pady=20)
        self.question_label.pack(pady=20)
        self.answer_entry.master.pack(pady=10)
        self.feedback_label.pack(pady=15)
        
        # Hide results
        self.results_frame.pack_forget()
        
        # Start new quiz
        self.start_quiz()

def main():
    root = tk.Tk()
    app = PentatonicQuiz(root)
    root.mainloop()

if __name__ == "__main__":
    main()
