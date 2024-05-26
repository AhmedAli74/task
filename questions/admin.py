from django.contrib import admin
from .models import Question,Answrer,QuestionMCQ
# Register your models here.
@admin.register(QuestionMCQ)
class AnswerAdmin(admin.ModelAdmin):
    list_display=['questions','is_active']
@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display=['subjects','is_active']
@admin.register(Answrer)
class AnswerAdmin(admin.ModelAdmin):
    list_display=['question','is_active']