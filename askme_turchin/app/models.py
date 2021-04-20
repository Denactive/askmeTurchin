from django.db import models

# Create your models here.

class User(models.Model):
    
    def __str__(self):
        self.login

    class Meta:
        db_table = 'users'
        managed = True
        verbose_name = 'User'
        verbose_name_plural = 'Users'
    
    # id = models.CharField(primary_key = True, max_length = 80)
    login = models.CharField(unique = True, max_length = 80)
    email = models.CharField(max_length = 200)
    password = models.CharField(max_length = 80)
    avatarlink = models.CharField(max_length = 80)
    nickname = models.CharField(max_length = 80)
    reg_date = models.DateTimeField(auto_now_add = True)

    # TODO: metod returning userlink


class Tag(models.Model):
    
    def __str__(self):
        self.tagname

    class Meta:
        db_table = 'tags'
        managed = True
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    tagname = models.CharField(primary_key = True, max_length = 80)
    # TODO: metod returning tag_search_link


class Question(models.Model):
    
    def __str__(self):
        self.title

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
        self.text[:50]

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