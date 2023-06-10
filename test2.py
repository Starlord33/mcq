from flask import Flask, render_template, request

app = Flask(__name__)

# Define the custom enumerate filter
def enumerate_filter(sequence):
    return enumerate(sequence)

app.jinja_env.filters['enumerate'] = enumerate_filter

# Define the quiz questions
questions = [
    {
        'question': 'What is the capital of France?',
        'options': ['Paris', 'London', 'Berlin', 'Madrid']
    },
    {
        'question': 'What is the largest planet in our solar system?',
        'options': ['Jupiter', 'Saturn', 'Mars', 'Venus']
    },
    {
        'question': 'What is the highest mountain in the world?',
        'options': ['Mount Everest', 'K2', 'Kangchenjunga', 'Lhotse']
    }
]

# Define the correct answers
answers = ['Paris', 'Jupiter', 'Mount Everest']

# Define the route for the home page
@app.route('/')
def home():
    return render_template('home.html', questions=questions)

# Define the route for the result page
@app.route('/result', methods=['POST'])
def result():
    score = 0
    results = []
    for index, question in enumerate(questions):
        user_answer = request.form.get('question-{}'.format(index))
        is_correct = user_answer == answers[index]
        if is_correct:
            score += 1
        results.append({
            'question': question['question'],
            'user_answer': user_answer,
            'correct_answer': answers[index],
            'is_correct': is_correct
        })
    return render_template('result.html', score=score, results=results)

if __name__ == '__main__':
    app.run(debug=True)
