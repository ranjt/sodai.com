from build import Sheet, Topic
from ws import (P, H, Box, Vocab, Fig, Q, Lines, Blanks, Match, TrueFalse, MCQ, Table, Ans, Sort, Draw, Graph, WordSearch, Bullets, Pics,
                Choose, PicMatch, PicSort, Pictograph, Trace, Case)
import art

learn = Sheet('learn', 'Healthy bodies', level=1, goals=['Say what a balanced diet is.', 'Name ways to keep healthy.'], blocks=[
    P('To stay healthy we need **good food**, **exercise**, **clean hands** and **rest**.', 'lead'),
    H('A balanced diet', 3),
    P('A **balanced diet** has some of each kind of food every day, and plenty of water.'),
    Table(['Food', 'What it does', 'Examples'], [
        ['**energy foods** (carbohydrates)', 'give us energy', 'rice, roti, potato'],
        ['**body-building foods** (proteins)', 'help us grow', 'fish, egg, meat, dal, milk'],
        ['**protecting foods** (vitamins, minerals, fibre)', 'keep us healthy', 'fruit, green vegetables'],
        ['**fats and oils** (a little)', 'store energy', 'oil, butter, nuts']]),
    Pics([('cooked rice', 'rice'), ('fish', 'fish'), ('leafy green', 'vegetables'), ('banana', 'fruit'), ('milk', 'milk'), ('water glass', 'water')], cols=6, size='17mm'),
    H('Keep healthy every day', 3),
    Pics([('person running', 'play actively'), ('soap', 'wash hands'), ('toothbrush', 'brush teeth'), ('bed', 'sleep about 10 hours')], cols=4, size='18mm'),
    Vocab([('balanced diet', 'eating the right amounts of different foods'), ('exercise', 'moving your body to keep fit'), ('hygiene', 'keeping clean to stop germs')]),
])

facts = Sheet('facts', 'Food and health facts', level=1, goals=['Sort foods.', 'Match habits.'], blocks=[
    Q('Sort the foods.', Sort(['Energy foods', 'Body-building foods', 'Protecting foods'], [('rice', 'Energy foods'), ('roti', 'Energy foods'), ('fish', 'Body-building foods'),
                                                                                         ('egg', 'Body-building foods'), ('mango', 'Protecting foods'), ('spinach', 'Protecting foods')])),
    Q('Match the habit to why it helps.', Match([('washing hands', 'gets rid of germs'), ('sleeping', 'rests the body'), ('playing outside', 'makes muscles strong')])),
])

think = Sheet('think', 'Make it healthier', level=2, goals=['Improve a meal.'], blocks=[
    P('Rafi\'s lunch: chips, a sweet cake and a fizzy drink.'),
    Q('What is missing from Rafi\'s lunch?', Lines(2, 'body-building food (fish, egg, dal), vegetables or fruit, and water')),
    Q('Draw a better lunch for Rafi.', Draw('46mm', 'A healthy lunch', 'e.g. rice, dal, fish, vegetables, a banana and water.')),
])

investigate = Sheet('investigate', 'How clean are our hands?', level=2, goals=['Test handwashing.', 'Read a chart.'], blocks=[
    Box('adult', P('Rub a little oil and glitter on children\'s hands (pretend germs). Try washing: water only for 5 seconds, water only for 20 seconds, soap for 20 seconds. Count glitter spots left.')),
    Q('Glitter spots left.', Table(['How we washed', 'water, 5 s', 'water, 20 s', 'soap, 20 s'], [['Spots left', '30', '15', '2']], center=True),
      Graph(['water 5 s', 'water 20 s', 'soap 20 s'], [30, 15, 2], 'Spots left', '', ymax=35, step=5, width=86, height=46)),
    Q('Which way cleaned best?', MCQ(['water for 5 seconds', 'water for 20 seconds', 'soap for 20 seconds'], 2)),
])

case = Sheet('case', 'A day for Tumpa', level=3, goals=['Read a story.', 'Give healthy advice.'], blocks=[
    Case('Tumpa watches cartoons until late at night. In the morning she is sleepy and skips breakfast.',
         'At school she feels tired and cannot play. Her teacher says, "Your body needs sleep, good food and exercise to work well."'),
    Q('Give Tumpa two tips to feel better.', Lines(2, 'Go to bed early (sleep about 10 hours); eat breakfast; play outside.')),
    Q('Why does Tumpa feel tired?', MCQ(['She did not sleep or eat enough.', 'She ate too much fruit.'], 0)),
])

review = Sheet('review', 'Show what you know', level=3, goals=['Use health words.'], blocks=[
    Q('Find the words.', WordSearch(['FOOD', 'SOAP', 'SLEEP', 'PLAY', 'WATER'], size=7, seed=104)),
    Q('Which food helps you grow?', MCQ(['sweets', 'egg', 'fizzy drink'], 1)),
])

TOPIC = Topic(
    code='A3', strand='living', title='Healthy Bodies', short='Healthy bodies',
    subtitle='A balanced diet, exercise, clean hands and rest',
    outcomes=[
        'define a balanced diet — one with sufficient fibre and the various nutrients, carbohydrates, proteins, fats, vitamins, minerals and water, to maintain good health.',
        'use the dietary guidelines for Bangladesh to make suggestions for improving the composition of sample meals.',
        'discuss the importance of regular physical activity to maintaining good health, and give examples of ways to be active every day.',
        'discuss good hygiene practices and the importance of good hygiene in maintaining a healthy body.',
        'discuss the importance of rest and recreation for emotional wellness and the maintenance of good health.',
    ],
    sheets=[learn, facts, think, investigate, case, review],
    selfcheck=['say what a balanced diet is', 'wash my hands well', 'name ways to stay healthy'],
    cover_art=art.pic_row(['cooked rice', 'fish', 'leafy green', 'soap', 'person running'], ['rice', 'fish', 'vegetables', 'soap', 'play']),
)
