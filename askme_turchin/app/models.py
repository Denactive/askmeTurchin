from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from datetime import datetime
from django.db.models import Sum
# Create your models here.

    # TODO: metod returning userlink

        
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)


    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    class Profile(models.Model):
        user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
        avatarlink = models.ImageField(upload_to='img/', null=True, blank=True)
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

    tagname = models.CharField(primary_key = True, max_length = 80)
    # TODO: metod returning tag_search_link


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

    fk_user = models.ForeignKey(User, on_delete = models.CASCADE)
    fk_tags = models.ManyToManyField(Tag)

    rating = models.IntegerField(default = 0)
    # TODO: updating answers_num
    answers_num = models.IntegerField()
    title = models.CharField(max_length = 200)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add = True)
    
    class QuestionManager(models.Manager):
        def get_popular(self):
            return self.all().order_by('-rating').prefetch_related('user', 'tags')

        def get_new(self):
            return self.all().order_by('-date').prefetch_related('user', 'tags')

        def get_by_tag(tag):
            questions_tagged = self.all().filter(tags__tag__iexact=search_tag).prefetch_related('user')
            if not questions:
                raise Http404
            return questions_tagged

        def get_by_id(id):
            try:
                question = self.get(pk=id)
            except ObjectDoesNotExist:
                raise Http404

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


class Answer(models.Model):
    
    def __str__(self):
        if self.text == None:
            return "ERROR-ANSWER TEXT IS NULL"
        return self.text[:50]

    class Meta:
        db_table = 'answers'
        managed = True
        verbose_name = 'Answer'
        verbose_name_plural = 'Answers'

    fk_question = models.ForeignKey(Question, on_delete = models.CASCADE)
    fk_user = models.ForeignKey(User, on_delete = models.CASCADE)

    rating = models.IntegerField(default = 0)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add = True)
    marked_correct = models.BooleanField(default = False)

    # {
    #     'id': ,
    #     'userlink': f'#',
    #     'username': f'',
    #     'avatarlink': f'',
    #     'correction_rating': ,
    #     'text': f''
    # }