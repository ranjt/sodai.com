from build import Sheet, Topic
from ws import (P, H, Box, Vocab, Fig, Cols, Row, Case, Links, Lines, Blanks, Match, TrueFalse, MCQ, Order, Table,
                Ans, Sort, Label, Draw, Graph, WordSearch, Q, Part, Bullets, Pics)
import art

learn = Sheet('learn', 'Keeping healthy', level=1, goals=[
    'Name the life processes of humans and animals.',
    'Explain how breathing, the heart, digestion and getting rid of waste work together.',
    'Describe a healthy diet and why exercise and sleep matter.',
], blocks=[
    P('People and animals all do the same important things to stay alive. We call them **life processes**. Taking care of our bodies helps us do them well.', 'lead'),
    Table(['Life process', 'What it means'], [['**nutrition**', 'eating food and drinking water'], ['**growth**', 'getting bigger'],
                                            ['**movement**', 'moving our bodies'], ['**reproduction**', 'having young (babies)']]),
    H('Our body works as a team', 3),
    Bullets(['**Digestion**: the stomach and intestines break food down into goodness the body can use.',
             '**Breathing**: the lungs take in air with oxygen.',
             '**Circulation**: the heart pumps blood, which carries food and oxygen all around the body.',
             '**Getting rid of waste**: kidneys make urine; the large intestine gets rid of food we cannot use.']),
    P('If one part does not work well, the others find it harder too. That is why we must look after our whole body.'),
    H('Eat a healthy, varied diet', 3),
    Fig(art.healthy_plate(), 'A healthy plate.', width='62%'),
    P('Eat lots of **vegetables and fruit**, some **rice, bread or roti** for energy, and **fish, eggs, dal or meat** to help you grow. Drink plenty of **clean water**.'),
    Pics([('broccoli', 'vegetables'), ('banana', 'fruit'), ('cooked rice', 'rice'), ('fish', 'fish'), ('egg', 'eggs'), ('droplet', 'water')], cols=6, size='13mm'),
    P('Some foods can **damage** our health if we eat too much of them: very **sweet** foods (sweets, fizzy drinks, cakes) and very **fatty** foods (fried snacks, chips). They are **treats**, not everyday food.'),
    Pics([('lollipop', 'sweets'), ('cake', 'cake'), ('french fries', 'chips'), ('burger', 'fast food')], cols=4, size='13mm'),
    H('Move, rest and stay clean', 3),
    Bullets(['**Exercise** every day: run, play, swim, cycle. It makes your heart, lungs and muscles strong.',
             '**Sleep** about 10 hours a night so your body can rest and grow.',
             '**Wash your hands** with soap before eating and after the toilet. **Brush your teeth** twice a day.']),
    Pics([('person running', 'exercise'), ('bed', 'sleep'), ('soap', 'wash hands'), ('toothbrush', 'brush teeth')], cols=4, size='14mm'),
    Box('tip', P('Your body is precious. Look after it: eat well, drink water, play, sleep and keep clean!')),
    Vocab([('nutrition', 'eating and drinking'), ('diet', 'the food you usually eat'), ('exercise', 'moving your body to keep fit'),
           ('healthy', 'well and strong')]),
])

facts = Sheet('facts', 'Healthy or treat?', level=1, goals=['Sort healthy food and treats.', 'Name healthy habits.'], blocks=[
    Q('Sort the food.', Sort(['Everyday food', 'Treat (only sometimes)'], [('rice', 'Everyday food'), ('vegetables', 'Everyday food'), ('fish', 'Everyday food'), ('fruit', 'Everyday food'),
                                                                     ('sweets', 'Treat (only sometimes)'), ('fizzy drink', 'Treat (only sometimes)'), ('fried chips', 'Treat (only sometimes)'), ('cake', 'Treat (only sometimes)')]), marks=8),
    Q('Draw a line to match.', Match([('exercise', 'makes heart and muscles strong'), ('sleep', 'helps the body rest and grow'), ('washing hands', 'gets rid of germs'), ('drinking water', 'keeps the body working')]), marks=4),
    Q('Name the life processes.', Blanks('Eating and drinking is [nutrition]. Getting bigger is [growth]. Having young is [reproduction].', extra=['breathing']), marks=3),
])

think = Sheet('think', 'Making healthy choices', level=2, goals=['Explain healthy choices.'], blocks=[
    Q('Draw a healthy lunch on the plate.', Draw('48mm', 'My healthy lunch', 'e.g. rice, dal, fish, vegetables, a fruit and water.'), marks=3),
    Q('Why is it bad to eat sweets every day?', Lines(2, 'Too much sugar can hurt your teeth and make you unhealthy.'), marks=2),
    Q('Why must you wash your hands before you eat?', Lines(2, 'To wash away germs so they do not go into your mouth and make you ill.'), marks=2),
])

investigate = Sheet('investigate', 'How long do we sleep?', level=2, goals=['Collect data.', 'Make a bar chart.'], blocks=[
    P('Class 2A asked 20 children how many hours they sleep each night.'),
    Q('Draw a bar chart.', Table(['Hours of sleep', '8', '9', '10', '11'], [['Number of children', '3', '6', '8', '3']], center=True),
      Graph(['8 hours', '9 hours', '10 hours', '11 hours'], [3, 6, 8, 3], 'Number of children', 'Hours of sleep', ymax=10, step=1, width=110, height=50), marks=3),
    Q('How many hours do most children sleep?', Lines(1, '10 hours'), marks=1),
    Q('How many hours do you sleep? Is it enough?', Lines(1, 'Children need about 10 hours.'), marks=1),
])

case = Sheet('case', 'Shopon\'s tiffin box', level=3, goals=['Use healthy eating in real life.'], blocks=[
    Links('Science', 'Health', 'Maths'),
    Case('Every day Shopon buys crisps and a fizzy drink from the shop near school for his tiffin. In the afternoon he feels '
         'tired and cannot play football well. His teeth also hurt.',
         'His grandmother says, "Let\'s make your tiffin at home!" Now Shopon takes a roti with egg, a banana and a bottle of water. '
         'He feels full of energy, and he saves money too.',
         source='A story about healthy tiffin.'),
    Q('Why did Shopon feel tired and have sore teeth?', Lines(2, 'Crisps and fizzy drinks do not give lasting energy, and sugar hurts teeth.'), marks=2),
    Q('Circle the healthy tiffin.', Pics([('bread', 'roti and egg'), ('lollipop', 'sweets'), ('banana', 'banana'), ('french fries', 'chips')], cols=4, size='14mm'), Lines(1, 'roti and egg, banana'), marks=2),
    Q('Crisps and a drink cost 40 Tk. Shopon buys them 5 days a week. How much does he spend?', Lines(1, '40 × 5 = 200 Tk'), marks=1),
])

review = Sheet('review', 'Show what you know', level=3, goals=['Use health words.'], blocks=[
    Q('Find the words.', WordSearch(['SLEEP', 'WATER', 'FRUIT', 'SOAP', 'RUN', 'GROW'], size=8, seed=206)),
    Q('Which is the healthiest snack?', MCQ(['sweets', 'an apple', 'chips'], 1), marks=1),
    Q('How many hours should children sleep?', MCQ(['about 5', 'about 10', 'about 20'], 1), marks=1),
    Q('**Challenge.** Write two things you will do this week to keep healthy.', Lines(2, 'e.g. drink more water; play outside every day; brush my teeth twice a day.'), marks=2),
])

TOPIC = Topic(
    code='A5', strand='living', title='Life Processes and Keeping Healthy', short='Keeping healthy',
    subtitle='Life processes, how the body works as a team, healthy food, exercise, sleep and keeping clean',
    outcomes=[
        'know the life processes common to humans and animals: nutrition, growth, movement and reproduction.',
        'investigate how basic life processes such as circulation, simple respiration, excretion and digestion interact with each other in order to maintain a healthy body.',
        'explore and research the exercise and the adequate, varied diet needed to keep healthy.',
        'know that some foods can be damaging to health, for example very sweet and fatty foods.',
        'explain how and why they need to appreciate and care for their own body.',
    ],
    cambridge=['Stage 3 Unit 2 Looking after ourselves (2.1–2.4)'],
    sheets=[learn, facts, think, investigate, case, review],
    selfcheck=['name the life processes', 'choose healthy food', 'say why exercise and sleep matter', 'keep clean to stop germs', 'make a chart about sleep'],
    cover_art=art.healthy_plate(),
)
