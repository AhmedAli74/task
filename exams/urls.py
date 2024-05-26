from django.urls import path
from . import views
app_name='exams'
urlpatterns = [
    path('',views.exam,name='Exams'),
    path('<str:category_slug>/',views.grade_exams,name='category_slug'),
    path('<str:category_slug>/<str:subject_slug>/',views.exam_detail,name='subjects_slug'),
    path('<str:category_slug>/<str:subject_slug>/<int:score_id>',views.score_details,name='score_id'),
]