from random import choice
from itertools import islice
from django.core.management.base import BaseCommand
from app.models import Profile, Tag, Question, Answer, QuestionRatingMark, AnswerRatingMark
from django.contrib.auth.models import User
from faker import Faker
import glob
import random
from random import shuffle, seed
from faker.providers.person.en import Provider

class Command(BaseCommand):
    help = "filling db with random data"

    def add_arguments(self, parcer):
        parcer.add_argument("-u", "--users", type=int)
        parcer.add_argument("-t", "--tags", type=int)
        parcer.add_argument("-q", "--questions", type=int)
        parcer.add_argument("-a", "--answers", type=int)
        parcer.add_argument("-ql", "--question_likes", type=int)
        parcer.add_argument("-al", "--answer_likes", type=int)
        # parcer.add_argument("-amc", "--answer_marked_correct", type=int)
        parcer.add_argument("-all", "--all", type=int)
        

    def handle(self, *args, **options):
        users_amount = options["users"]
        questions_amount = options["questions"]
        answers_amount = options["answers"]
        tags_amount = options["tags"]
        question_votes_amount = options["question_likes"]
        answer_votes_amount = options["answer_likes"]
        total_amount = options["all"]

        if total_amount:
            self.fill_tags(total_amount * 10)
            self.fill_users(total_amount * 10)
            self.fill_questions(total_amount * 100)
            self.fill_answers(total_amount * 300)
            self.fill_question_likes(total_amount * 600)
            self.fill_answer_likes(total_amount * 500)
        if tags_amount:
            self.fill_tags(tags_amount * 10)
        if users_amount:
            self.fill_users(users_amount * 10)
        if questions_amount:
            self.fill_questions(questions_amount * 100)
        if answers_amount:
            self.fill_answers(answers_amount * 300)
        if question_votes_amount:
            self.fill_question_likes(question_votes_amount * 600)
        if answer_votes_amount:
            self.fill_answer_likes(answer_votes_amount * 500)
        

    def fill_questions(self, n):
        users = list(Profile.objects.values_list('id', flat=True))
        tags = list(Tag.objects.values_list('tagname', flat=True))
        for i in range(n):
            question = Question.objects.create(
                fk_profile_id=choice(users),
                title=Faker().sentence()[:200],
                text=". ".join(
                    Faker().sentences(
                        Faker().random_int(min=2, max=5)
                    )
                ),
                date=Faker().date_between("-100d", "today"),
            )
            question.fk_tags.add(choice(tags))


    def fill_answers(self, n):
        print("filling ", n, " answers")

        questions = list(Question.objects.values_list("id", flat=True))
        users = list(Profile.objects.values_list("id", flat=True))
        answers = []

        for i in range(n):
            answer = Answer(
                fk_question_id=choice(questions),
                fk_profile_id=choice(users),
                text=". ".join(Faker().sentences(Faker().random_int(min=2, max=5))),
            )
            if (Faker().random_int(min=0, max=5) == 0):
                answer.marked_correct = True
            answers.append(answer)

        batch_size = 100
        n_batches = len(answers) // batch_size
        if len(answers) % batch_size != 0:
            n_batches += 1
        for i in range(n_batches):
            start = batch_size * i
            end = batch_size * (i + 1)
            Answer.objects.bulk_create(answers[start:end], batch_size)

    def fill_users(self, n):
        usernames = set()

        file_path_type = "img/*.png"
        images = glob.glob(file_path_type)


        while len(usernames) != n:
            usernames.add(Faker().user_name() + "№" + str(Faker().random.randint(0, 1000000)))

        for name in usernames:
            user = User.objects.create(
                username=name,
                password=Faker().password(),
                email=Faker().email()
            )
            Profile.objects.create(
                user = user,
                avatarlink = choice(images)
            )
        

    def fill_tags(self, n):
        first_names = list(set(Provider.first_names))
        seed(4321)
        shuffle(first_names)

        for i in range(n):
            Tag.objects.create(tagname=Faker().word() + "№" + str(Faker().random.randint(0,100000)))


    def fill_question_likes(self, n):
        questions = list(Question.objects.values_list("id", flat=True))
        users = list(Profile.objects.values_list("id", flat=True))
        votes = []

        for i in range(n):
            vote = QuestionRatingMark(
                fk_question_id=choice(questions),
                fk_profile_id=choice(users),
                vote=Faker().random.randint(-1, 1)
            )
            votes.append(vote)

        batch_size = 100
        n_batches = len(votes) // batch_size
        if len(votes) % batch_size != 0:
            n_batches += 1
        for i in range(n_batches):
            start = batch_size * i
            end = batch_size * (i + 1)
            QuestionRatingMark.objects.bulk_create(votes[start:end], batch_size)

    def fill_answer_likes(self, n):
        answers = list(Answer.objects.values_list("id", flat=True))
        users = list(Profile.objects.values_list("id", flat=True))
        votes = []

        for i in range(n):
            vote = AnswerRatingMark(
                fk_answer_id=choice(answers),
                fk_profile_id=choice(users),
                vote=Faker().random.randint(-1, 1))
            votes.append(vote)

        batch_size = 100
        n_batches = len(votes) // batch_size
        if len(votes) % batch_size != 0:
            n_batches += 1
        for i in range(n_batches):
            start = batch_size * i
            end = batch_size * (i + 1)
            AnswerRatingMark.objects.bulk_create(votes[start:end], batch_size)