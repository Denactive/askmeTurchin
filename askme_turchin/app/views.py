from django.core.paginator import Paginator
from django.shortcuts import render

# data
question_contents = [
    {
        'id': 1,
        'userlink': f'#',
        'username': f'Optimus',
        'title': f'Desipticons should be killed',
        'avatarlink': f'img/optimus.png',
        'rating': 15,
        'answers_num': 3,
        'text': f'До начала времен был Куб.\
            Мы не знаем, откуда он появился.\
            Знаем только, что он обладает силой\
            создавать миры и населять их жизнью.\
            Так и родилась наша раса.\
            Сначала мы жили в гармонии,\
            но испокон веков одни стремятся к великой\
            власти ради добра, другие ради зла.\
            Так и началась война...\
            Война, терзавшая нашу планету,\
            пока ее не уничтожила смерть.\
            А Куб затерялся где-то\
            в бескрайнем Космосе.\
            Мы прочесывали Галактику,\
            чтобы найти его и возродить нашу Родину.\
            Обыскали каждую звезду, каждый уголок.\
            И когда надежды наши совсем угасли,\
            новые сведения привели нас...\
            ...к неизвестной планете по имени Земля.',
        'tags': [
            {
                'tag': f'Bay\'s operating systems',
                'id': 1,
            },
            {
                'tag': f'Real Optimus Prime',
                'id': 2,
            }
        ] 
    },
    {
        'id': 2,
        'userlink': f'#',
        'username': f'Megatron',
        'avatarlink': f'img/megatron.png',
        'title': f'Autobots must die',
        'rating': 15,
        'answers_num': 3,
        'text': f'Возглавив десептиконов, Мегатрон образовал возле себя «ближний круг» из наиболее сильных,\
            искусных и опытных воинов. В их число входили: Шоквейв (опытный стратег),\
            Старскрим (командующий военно-воздушными силами), Саундвейв (офицер связи).\
            Эти воины помогли Мегатрону провести десептиконов от бунтарей-подпольщиков до элитной военной касты Кибертрона.\
            Однако они выступали против планов Мегатрона по превращению Кибертрона в космическую крепость,\
            поэтому полного взаимопонимания междулидером и «ближним кругом» не было. Кроме того,\
            тщеславный и амбициозный Скандалист начал открыто претендовать на пост предводителя десептиконов,\
            считая Мегатрона неспособным справиться с автоботами.',
        'tags': [
            {
                'tag': f'Bay\'s operating systems',
                'id': 1,
            },
            {
                'tag': f'Megatron is back!',
                'id': 3,
            },
            {
                'tag': f'Hardcore rock',
                'id': 4,
            }   
        ] 
    },
    
    {
        'id': 2,
        'userlink': f'#',
        'username': f'Megatron',
        'avatarlink': f'img/megatron.png',
        'title': f'Autobots must die',
        'rating': 15,
        'answers_num': 3,
        'text': f'Что может быть прекраснее профессии врача? Она сложна и интересна. Она привлекает высокой социальной значимостью и уважением, каким пользуется в обществе. Игра во врача — одна из первых социальных детских игр, и сегодня она практически вытеснила игру в войну. Однако не все так просто, ведь эта профессия, наряду, к примеру, с профессией педагога, относится к «профессиям призвания», а это значит, что низкий уровень зарплат в этой индустрии компенсируется высоким профессиональным интересом и мотивацией ее представителей к работе. И, несмотря на трудности и критику отечественной медицины, работа врачей полна благородства и самоотдачи.',
        'tags': [
            {
                'tag': f'Bay\'s operating systems',
                'id': 1,
            },
            {
                'tag': f'Megatron is back!',
                'id': 3,
            },
            {
                'tag': f'Hardcore rock',
                'id': 4,
            }   
        ] 
    }
    # {
    #     'id': ,
    #     'userlink': f'#',
    #     'username': f'',
    #     'avatarlink': f'',
    #     'title': f'',
    #     'rating': 15,
    #     'answers_num': 3,
    #     'text': f'',
    #     'tags': [
    #     ]
    # }
]

answer_contents = [
    # [
        # {
        #     'id': ,
        #     'userlink': f'#',
        #     'username': f'',
        #     'avatarlink': f'',
        #     'correction_rating': ,
        #     'text': f''
        # }
    # ],
    [
        {
            'id': 1,
            'userlink': f'#',
            'username': f'Megatron',
            'avatarlink': f'img/megatron.png',
            'rating': 1,
            'text': f'Возглавив десептиконов, Мегатрон образовал возле себя «ближний круг» из наиболее сильных,\
                искусных и опытных воинов. В их число входили: Шоквейв (опытный стратег),\
                Старскрим (командующий военно-воздушными силами), Саундвейв (офицер связи).\
                Эти воины помогли Мегатрону провести десептиконов от бунтарей-подпольщиков до элитной военной касты Кибертрона.\
                Однако они выступали против планов Мегатрона по превращению Кибертрона в космическую крепость,\
                поэтому полного взаимопонимания междулидером и «ближним кругом» не было. Кроме того,\
                тщеславный и амбициозный Скандалист начал открыто претендовать на пост предводителя десептиконов,\
                считая Мегатрона неспособным справиться с автоботами.'
        },
        {
            'id': 2,
            'userlink': f'#',
            'username': f'Megatron',
            'avatarlink': f'img/megatron.png',
            'correction_rating': 0,
            'text': f'Извини что быканул'
        },
        {
            'id': 3,
            'userlink': f'#',
            'username': f'Megatron',
            'avatarlink': f'img/megatron.png',
            'correction_rating': 1,
            'text': f'я не то хотел сказать'
        },
        {
            'id': 4,
            'userlink': f'#',
            'username': f'Ratchet',
            'avatarlink': f'img/ratchet.png',
            'correction_rating': 3,
            'text': f'Ребята, давайте жить дружно'
        },
    ],

    [

    ],
]

# Create your views here.
from app.models import Question
from app.models import Tag
from app.models import User
from app.models import Answer

#def paginate(list_, per_page = 5, page = 1):
 #   paginator = Paginator(list_, per_page)
  #  return paginator.page(page)


def paginate(objects_list, request, per_page = 5):
    paginator = Paginator(objects_list, per_page)
    page = int(request.GET.get('page', 1))
    max_page = page + 2
    min_page = page - 2

    obList = paginator.get_page(page)
    return {'list': obList, "max_page": max_page, "min_page": min_page}


# не задействован
def index(request):
    question_contents_short_text = question_contents.copy()
    for i in range(len(question_contents_short_text)):
        question_contents_short_text[i]['text'] = question_contents_short_text[i]['text'][:197] + '...'
    # 3-й параметр - это контекст
    return render(request, 'index.html', {'questions': question_contents_short_text})



# def index_page(request, pk=1): # передавал страницу как часть урла
def index_page(request):
    contact_list = Question.objects.all()
    questions = paginate(contact_list, request, 1)
    return render(request, 'index.html', {'page': questions})
    # questions = paginate(questns, request, 3)
    #question_contents_short_text = pages.object_list
    #for i in range(len(question_contents_short_text)):
    #    question_contents_short_text[i].text = question_contents_short_text[i].text[:197] + '...'
    #return render(request, 'index.html', {'questions': question_contents_short_text, 'pages': pages})

def question(request, pk):
    question = Question.objects.get(pk=pk)
    # question.update_answers_num()
    answers = paginate(Answer.objects.get_by_question_id(pk), request, 1)
    return render(request, 'question.html', {'question': question, 'page': answers})

def ask(request):
    return render(request, 'ask.html')

def login(request):
    return render(request, 'login.html')

def reg(request):
    return render(request, 'registration.html')

def tag_search(request):
    return render(request, 'tag_search.html', {'questions': question_contents})

def user(request):
    return render(request, 'user.html')