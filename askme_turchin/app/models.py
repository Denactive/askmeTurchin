from django.db import models
from django.db.models import ObjectDoesNotExist
from django.db.models import Sum, Count
from django.http import HttpResponse, Http404
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from datetime import datetime
from django.db.models import Sum
# Create your models here.

    # TODO: metod returning userlink

        
    # @receiver(post_save, sender=User)
    # def create_user_profile(sender, instance, created, **kwargs):
    #     if created:
    #         Profile.objects.create(user=instance)


    # @receiver(post_save, sender=User)
    # def save_user_profile(sender, instance, **kwargs):
    #     instance.profile.save()



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    avatarlink = models.CharField(max_length = 255, default=None)#models.ImageField(upload_to='img/', null=True, blank=True)
    # login = models.CharField(primary_key = True, max_length = 80)
    # email = models.CharField(max_length = 200)
    # password = models.CharField(max_length = 80)
    # avatarlink = models.CharField(max_length = 80)
    # nickname = models.CharField(max_length = 80)
    # reg_date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        if self.user.username == None:
            return "ERROR-LOGIN IS NULL"
        return self.user.username

    class Meta:
        verbose_name = 'User profile'
        verbose_name_plural = 'User profiles'

    @property   
    def userlink(self):
        return "user/" + self.user.username


class Tag(models.Model):
    
    def __str__(self):
        if self.tagname == None:
            return "ERROR-TAG NAME IS NULL"
        return self.tagname

    class Meta:
        db_table = 'tags'
        managed = True
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    tagname = models.CharField(primary_key = True, max_length = 255)
    # TODO: metod returning tag_search_link

class QuestionManager(models.Manager):
    def get_new(self):
        return self.select_related().order_by("-date").prefetch_related('fk_profile', 'fk_tags')
    
    def get_popular(self):
        return self.order_by("-_rating").select_related('fk_profile')
        # db = MySQLdb.connect(user='admin', db='db', passwd='secret', host='localhost')
        # cursor = db.cursor()
        # cursor.execute('SELECT name FROM books ORDER BY name')
        # names = [row[0] for row in cursor.fetchall()]
        # db.close()

    # def get_popular(self):
    #     #update
    #     q = Question.objects.all()
    #     for i in q:
    #         i.rating
        
    #     return q.order_by('_rating').prefetch_related('fk_profile', 'fk_tags')

    # def get_new(self):
    #     return self.all().order_by('-date').prefetch_related('fk_profile', 'fk_tags')

    def get_by_tag(tag):
        questions_tagged = self.all().filter(tags__tag__iexact=search_tag).prefetch_related('fk_profile')
        if not questions:
            raise Http404
        return questions_tagged

    def get_by_id(id):
        try:
            question = self.prefetch_related('fk_profile', 'fk_tags').get(pk=id)
        except ObjectDoesNotExist:
            raise Http404
        return question


class Question(models.Model):
        
    def __str__(self):
        if self.title == None:
            return "ERROR-QUESTION TITLE IS NULL"
        return self.title

    class Meta():
        db_table = 'questions'
        managed = True
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'

    objects = QuestionManager()

    fk_profile = models.ForeignKey(Profile, on_delete = models.CASCADE)
    fk_tags = models.ManyToManyField(Tag)

    _rating = models.IntegerField(default = 0)
    _answers_num = models.IntegerField(default = 0)
    title = models.CharField(max_length = 255)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add = True)

    @property
    def answers_num(self):
        _answers_num = Answer.objects.all().filter(fk_question=self.id).count()
        print("answers_num changed to: ", _answers_num)
        return _answers_num

    @property
    def rating(self):
        q = QuestionRatingMark.objects.all().filter(fk_question=self.id)
        sum = 0
        for i in q:
            sum += i.vote
        _rating = sum
        print("Q-rating changed to: ", _rating)
        return _rating

    # 'id': ,
    #     'userlink': f'#',
    #     'username': f'',
    #     'avatarlink': f'',
    #     'title': f'',
    #     'rating': 15,
    #     'answers_num': 3,
    #     'text': f'',
    #     'tags': [
    #     ]


class AnswerManager(models.Manager):
    def get_new(self):
        return self.all().order_by('-date').prefetch_related('user')

    def get_by_question_id(self, q_id):
        try:
            answers = self.all().prefetch_related('fk_profile').filter(fk_question=q_id)
        except ObjectDoesNotExist:
            raise Http404
        return answers

class Answer(models.Model):
    
    def __str__(self):
        if self.text == None:
            return "ERROR-ANSWER TEXT IS NULL"
        return self.text[:50]

    # def __init__(self):
    #     q = self.all().filter(fk_question=this.fk_question).annotate(Count())
    #     print(q)
    #     fk_question.answers_num = q
    #     return


    class Meta:
        db_table = 'answers'
        managed = True
        verbose_name = 'Answer'
        verbose_name_plural = 'Answers'

    objects = AnswerManager()

    fk_question = models.ForeignKey(Question, on_delete = models.CASCADE)
    fk_profile = models.ForeignKey(Profile, on_delete = models.CASCADE)

    _rating = models.IntegerField(default = 0)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add = True)
    marked_correct = models.BooleanField(default = False)

    @property
    def rating(self):
        q = AnswerRatingMark.objects.all().filter(fk_answer=self.id)
        sum = 0
        for i in q:
            sum += i.vote
        _rating = sum
        print("A-rating changed to: ", _rating)
        return _rating

    # {
    #     'id': ,
    #     'userlink': f'#',
    #     'username': f'',
    #     'avatarlink': f'',
    #     'correction_rating': ,
    #     'text': f''
    # }

    # likes
class QuestionRatingMark(models.Model):
    votes = [(1, 'like'), (-1, 'dislike'), (0, 'none'), ]

    vote = models.IntegerField(choices=votes, default=0)
    fk_profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    fk_question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.fk_question.title + '-' + self.fk_profile.user.username + ': ' + str(self.vote)

    class Meta:
        verbose_name = 'Q-VoteMark'
        verbose_name_plural = 'Q-VoteMarks'
    
    def update_rating(self):
            self.question.rating += self.vote


class AnswerRatingMark(models.Model):
    votes = [(1, 'like'), (-1, 'dislike'), (0, 'none'), ]

    vote = models.IntegerField(choices=votes, default=0)
    fk_profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    fk_answer = models.ForeignKey(Answer, on_delete=models.CASCADE)

    def __str__(self):
        return self.fk_answer.text[:10] + '-' + self.fk_profile.user.username+ ': ' + str(self.vote)

    class Meta:
        verbose_name = 'A-VoteMark'
        verbose_name_plural = 'A-VoteMarks'