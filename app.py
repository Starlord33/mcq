# from flask import Flask, render_template
# from flask import request, redirect

# app = Flask(__name__)

# # Example list of questions and options
# questions = [
#     {
#         "question": "What is the capital of France?",
#         "options": ["Paris", "London", "Berlin", "Rome"],
#         "answer": "Paris"
#     },
#     {
#         "question": "Who invented the telephone?",
#         "options": ["Alexander Graham Bell", "Thomas Edison", "Nikola Tesla", "Albert Einstein"],
#         "answer": "Alexander Graham Bell"
#     },
#     # Add more questions here
# ]

# # Initialize a dictionary to store user responses
# user_responses = {}

# @app.route('/', methods=['GET', 'POST'])
# def home():
#     if request.method == 'POST':
#         # Retrieve the submitted form data
#         for question in questions:
#             question_number = questions.index(question)
#             user_answer = request.form.get(f'question-{question_number}')
#             user_responses[question_number] = user_answer

#         # Perform scoring or other actions with user responses

#         return redirect('/result')

#     return render_template('home.html', questions=questions)

# @app.route('/result')
# def result():
#     # Calculate the score or perform other actions based on user responses

#     return render_template('result.html', user_responses=user_responses)

# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

questions = []

def load_questions_from_file(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        # next(reader)  # Skip the header row if it exists

        for row in reader:
            question = {
                "question": row[0],
                "options": row[1:5],
                "answer": row[5]
            }
            questions.append(question)

# Load questions from a CSV file on application startup
load_questions_from_file('questions.csv')

user_responses = {}

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        for question in questions:
            question_number = questions.index(question)
            user_answer = request.form.get(f'question-{question_number}')
            user_responses[question_number] = user_answer

        return redirect('/result')

    return render_template('home.html', questions=questions)

@app.route('/result')
def result():
    score = 0
    for question_number, question in enumerate(questions):
        user_answer = user_responses.get(question_number)
        if user_answer == question['answer']:
            score += 1

    return render_template('result.html', questions=questions, user_responses=user_responses, score=score)

if __name__ == '__main__':
    app.run(debug=True)

