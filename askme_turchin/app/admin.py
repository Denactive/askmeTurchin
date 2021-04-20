from django.contrib import admin
from app.models import Question, Answer, Tag, User

# Register your models here.

class AnswerAdmin(admin.ModelAdmin):
    fields = ['fk_question', 'fk_user', 'text', 'marked_correct']
    list_filter = ['date']

class QuestionInline(admin.StackedInline):
    #TODO: forbid rating change here
    model = Answer
    extra = 1

class QuestionAdmin(admin.ModelAdmin):
    fields = ['fk_user', 'fk_tags', 'answers_num', 'title', 'text']
    inlines = [QuestionInline]
    list_filter = ['date']

class UserAdmin(admin.ModelAdmin):
    list_filter = ['reg_date']

# admin.site.register(Question)
admin.site.register(Question, QuestionAdmin)
# admin.site.register(Answer)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(Tag)
# admin.site.register(User)
admin.site.register(User, UserAdmin)


