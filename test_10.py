import csv
import random
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# List to store the questions
questions = []

def load_questions_from_file(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        # Skip the header row if it exists
        # next(reader)

        for row in reader:
            question = {
                "question": row[0],
                "options": row[1:5],
                "answer": row[5]
            }
            questions.append(question)

# Load questions from a CSV file
load_questions_from_file('questions.csv')

# Initialize a dictionary to store user responses
user_responses = {}

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Retrieve the submitted form data
        for question in questions:
            question_number = question['shuffled_index']
            user_answer_index = int(request.form.get(f'question-{question_number}'))
            user_responses[question_number] = user_answer_index

        return redirect('/result')

    # Randomize the order of questions and options for each user request
    randomized_questions = random.sample(questions, len(questions))
    for index, question in enumerate(randomized_questions):
        question['shuffled_index'] = index
        random.shuffle(question['options'])

    return render_template('home.html', questions=randomized_questions)

@app.route('/result', methods=['POST'])
def result():
    # Calculate the score based on user responses
    score = 0
    results = []

    for question in questions:
        question_number = question['shuffled_index']
        user_answer_index = user_responses.get(question_number)
        options = question['options']
        correct_answer_index = int(question['answer']) - 1

        user_answer = options[user_answer_index] if user_answer_index is not None else ""
        correct_answer = options[correct_answer_index]

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
