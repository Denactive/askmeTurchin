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
            }      
        ] 
    },
    
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
def index(request):
    question_contents_short_text = question_contents.copy()
    for i in range(len(question_contents_short_text)):
        question_contents_short_text[i]['text'] = question_contents[i]['text'][:197] + '...'
    return render(request, 'index.html', {'questions': question_contents_short_text})

def question(request, pk):
    return render(request, 'question.html', {'iquestion': question_contents[pk - 1], 'answers': answer_contents[pk - 1]})

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