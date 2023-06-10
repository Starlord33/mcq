# import csv
# import random
# from flask import Flask, render_template, request, redirect

# app = Flask(__name__)

# # List to store the questions
# questions = []

# def enumerate_filter(sequence):
#     return enumerate(sequence)

# app.jinja_env.filters['enumerate'] = enumerate_filter

# def load_questions_from_file(filename):
#     with open(filename, 'r') as file:
#         reader = csv.reader(file)
#         # next(reader)  # Skip the header row if it exists

#         for row in reader:
#             question = {
#                 "question": row[0],
#                 "options": row[1:5],
#                 "answer": row[5]  # Store the correct answer
#             }
#             questions.append(question)

# # Load questions from a CSV file
# load_questions_from_file('questions.csv')

# @app.route('/', methods=['GET', 'POST'])
# def home():
#     if request.method == 'POST':
#         # Retrieve the submitted form data
#         user_responses = {}
#         for question in questions:
#             question_number = questions.index(question)
#             user_answer = request.form.get(f'question-{question_number}')
#             user_responses[question_number] = user_answer

#         return redirect('/result')

#     # Randomize the order of questions and options for each user request
#     randomized_questions = random.sample(questions, len(questions))
#     for question in randomized_questions:
#         random.shuffle(question['options'])

#     return render_template('home.html', questions=randomized_questions)

# @app.route('/result', methods=['POST'])
# def result():
#     # Retrieve the user responses
#     user_responses = {}
#     for question in questions:
#         question_number = questions.index(question)
#         user_answer = request.form.get(f'question-{question_number}')
#         user_responses[question_number] = user_answer

#     # Calculate the score based on user responses
#     score = 0
#     results = []

#     for question in questions:
#         question_number = questions.index(question)
#         user_answer = user_responses[question_number]
#         options = question['options']
#         correct_answer = question['answer']

#         is_correct = user_answer == correct_answer

#         if is_correct:
#             score += 1

#         result = {
#             'question': question['question'],
#             'user_answer': user_answer,
#             'correct_answer': correct_answer,
#             'is_correct': is_correct
#         }
#         results.append(result)

#     return render_template('result.html', score=score, results=results)

# if __name__ == '__main__':
#     app.run(debug=True)

import csv
import random
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# List to store the questions
questions = []

def enumerate_filter(sequence):
    return enumerate(sequence)

app.jinja_env.filters['enumerate'] = enumerate_filter

def load_questions_from_file(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        # next(reader)  # Skip the header row if it exists

        for row in reader:
            question = {
                "question": row[0],
                "options": row[1:5],
                "answer": row[5]  # Store the correct answer
            }
            questions.append(question)

# Load questions from a CSV file
load_questions_from_file('questions.csv')

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Retrieve the submitted form data
        user_responses = {}
        for question in questions:
            question_number = questions.index(question)
            user_answer = request.form.get(f'question-{question_number}')
            user_responses[question_number] = user_answer

        return redirect('/result')

    # Randomize the order of questions and options for each user request
    randomized_questions = random.sample(questions, len(questions))
    for question in randomized_questions:
        random.shuffle(question['options'])

    return render_template('home.html', questions=randomized_questions)

#Question and its answer correct but correct_option is not calculated
# @app.route('/result', methods=['POST'])
# def result():
#     # Retrieve the user responses
#     user_responses = {}
#     for question in questions:
#         question_number = questions.index(question)
#         user_answer = request.form.get(f'question-{question_number}')
#         user_responses[question_number] = user_answer

#     # Calculate the score based on user responses
#     score = 0
#     results = []

#     for question in questions:
#         question_number = questions.index(question)
#         user_answer = user_responses[question_number]
#         options = question['options']
#         correct_answer = question['answer']

#         is_correct = user_answer == correct_answer

#         if is_correct:
#             score += 1

#         result = {
#             'question': question['question'],
#             'user_answer': user_answer,
#             'correct_answer': correct_answer,
#             'is_correct': is_correct
#         }
#         results.append(result)

#     return render_template('result.html', score=score, results=results)


# OPTION Correct but different question
@app.route('/result', methods=['GET','POST'])
def result():
    # Retrieve the user responses
    user_responses = {}
    for question in questions:
        question_number = questions.index(question)
        user_answer = request.form.get(f'question-{question_number}')
        user_responses[question_number] = user_answer

    # Calculate the score based on user responses
    score = 0
    results = []

    for question in questions:
        question_number = questions.index(question)
        user_answer = user_responses[question_number]
        options = question['options']
        correct_answer = question['answer']

        # Shuffle the options for the question
        random.shuffle(options)

        # Update the index of the correct answer to reflect the new order of the options
        correct_answer_index = options.index(correct_answer)

        is_correct = user_answer == correct_answer

        if is_correct:
            score += 1

        result = {
            'question': question['question'],
            'user_answer': user_answer,
            'correct_answer': correct_answer,
            'is_correct': is_correct
        }
        results.append(result)

    return render_template('result.html', score=score, results=results)



if __name__ == '__main__':
    app.run(debug=True)
