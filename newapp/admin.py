from django.contrib import admin

# ---------------------------------[edit]---------------------------------- #
from .models import Question

class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['q_subject']

admin.site.register(Question, QuestionAdmin)


# Register your models here.
