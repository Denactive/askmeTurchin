from django.contrib import admin
from app.models import Question, Answer, Tag, Profile, QuestionRatingMark, AnswerRatingMark

# Register your models here.

class AnswerRatingInline(admin.StackedInline):
    model = AnswerRatingMark
    extra = 1

class AnswerAdmin(admin.ModelAdmin):
    fields = ['fk_question', 'fk_profile', 'text', 'marked_correct' ]
    list_filter = ['date']
    inlines = [AnswerRatingInline]

class QuestionAnswerInline(admin.StackedInline):
    #TODO: forbid rating change here
    model = Answer
    extra = 1

class QuestionRatingInline(admin.StackedInline):
    model = QuestionRatingMark
    extra = 1

class QuestionAdmin(admin.ModelAdmin):
    fields = ['fk_profile', 'fk_tags', 'title', 'text']
    inlines = [QuestionAnswerInline, QuestionRatingInline]
    list_filter = ['date']

class UserAdmin(admin.ModelAdmin):
    list_filter = ['reg_date']


admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(Tag)
admin.site.register(Profile)
admin.site.register(QuestionRatingMark)
admin.site.register(AnswerRatingMark)
