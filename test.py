import csv

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

# Load questions from a CSV file
load_questions_from_file('questions.csv')

print(questions)