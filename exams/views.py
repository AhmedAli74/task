from django.http import HttpResponse
from django.shortcuts import render
from .models import Category
from subjects.models import Subject
from django.contrib.auth.decorators import login_required
from questions.models import Question,Answrer
from django.core.paginator import Paginator
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Download NLTK resources
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Initialize NLTK components
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))


@login_required(login_url='accounts:login')
def exam(request):
    grades = Category.objects.all()      
    context = {'grades': grades}
    return render(request, 'exam/Exam.html', context)

def grade_exams(request, category_slug):
    grade = Category.objects.get(slug=category_slug) 
    subjects = Subject.objects.filter(category=grade)     
    context = {'subjects': subjects}
    return render(request, 'subjects/subjects.html', context)

def exam_detail(request, category_slug, subject_slug):
    grade = Category.objects.get(slug=category_slug)
    subject = Subject.objects.get(category=grade, slugy=subject_slug) 
    questions = Question.objects.filter(subjects=subject)
    paginator = Paginator(questions, 1)  # Show 1 question per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {'subject': subject, 'questions': page_obj}
    return render(request, 'subjects/exam_setion.html', context)
def score_details(request, score_id, category_slug, subject_slug):
    # تحميل مكتبة NLTK وتهيئة المكونات
    nltk.download('punkt')
    nltk.download('stopwords')
    nltk.download('wordnet')
    
    lemmatizer = WordNetLemmatizer()
    stop_words = set(stopwords.words('english'))

    def preprocess_text(text):
        tokens = word_tokenize(text.lower())
        words = [lemmatizer.lemmatize(word) for word in tokens if word.isalnum() and word not in stop_words]
        return words

    # دالة لتحليل الإجابات
    def evaluate_answers(questions, submitted_answers):
        score_mcq = 0
        score_written = 0
        for question, submitted_answer in zip(questions, submitted_answers):
            if question.question_type == "mcq":
                if submitted_answer.lower() == question.answer.lower():
                    score_mcq += 1
            elif question.question_type == "written":
                question_tokens = preprocess_text(question.answer)
                submitted_tokens = preprocess_text(submitted_answer)
                if set(submitted_tokens) == set(question_tokens):
                    score_written += 1
        return score_mcq, score_written

    if request.method == 'POST':
        submitted_answers = request.POST['answer']
        for answer_text in submitted_answers:
            nlp_answer = Answrer(answer_text=answer_text)
            nlp_answer.save()

        questions = Question.objects.filter(category=category_slug, slugy=subject_slug, id=score_id)
        answers = Answrer.objects.filter(question__in=questions)
        score_written = evaluate_answers(answers, submitted_answers)

        context = {'score_written': score_written}
        return render(request, 'subjects/score_details.html', context)
    else:
        return HttpResponse("Method not allowed")