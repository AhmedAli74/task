import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import json

# Download NLTK resources
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Initialize NLTK components
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

# Function to preprocess text
def preprocess_text(text):
    tokens = word_tokenize(text.lower())
    words = [lemmatizer.lemmatize(word) for word in tokens if word.isalnum() and word not in stop_words]
    return words

# Function to evaluate submitted answers for MCQs and written questions
def evaluate_answers(questions, submitted_answers):
    score_mcq = 0
    score_written = 0
    for question, submitted_answer in zip(questions, submitted_answers):
        if question["type"] == "mcq":
            if submitted_answer.lower() == question["answer"]:
                score_mcq += 1
        elif question["type"] == "written":
            question_tokens = preprocess_text(question["answer"])
            submitted_tokens = preprocess_text(submitted_answer)
            if set(submitted_tokens) == set(question_tokens):
                score_written += 1
    return score_mcq, score_written

# Function to run the exam
def run_exam(questions):
    mcq_questions = [question for question in questions if question["type"] == "mcq"]
    written_questions = [question for question in questions if question["type"] == "written"]

    submitted_answers = []

    print("Multiple Choice Questions:")
    for i, question in enumerate(mcq_questions, start=1):
        print(f"Question {i}: {question['question']}")
        for option in question['options']:
            print(option)
        submitted_answer = input("Your answer (Enter the option number): ")
        submitted_answers.append(submitted_answer)

    print("\nWritten Questions:")
    for i, question in enumerate(written_questions, start=len(mcq_questions) + 1):
        print(f"\nQuestion {i}: {question['question']}")
        submitted_answer = input("Your answer: ")
        submitted_answers.append(submitted_answer)
    
    score_mcq, score_written = evaluate_answers(questions, submitted_answers)
    total_mcq_questions = len(mcq_questions)
    total_written_questions = len(written_questions)
    
    print(f"\nYour score for MCQs is {score_mcq}/{total_mcq_questions}.")
    print(f"Your score for written questions is {score_written}/{total_written_questions}.")

# Function to load questions from a file
def load_questions_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data['questions']

# Run the exam
file_path = r"E:\New folder\New folder (2)\intents.json"
questions = load_questions_from_file(file_path)
run_exam(questions)
