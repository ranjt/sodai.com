from build import Sheet, Topic
from ws import (P, H, Box, Fig, Q, Lines, MCQ, Draw, Pics, Ans, Case, Choose, PicMatch, PicSort, Pictograph, Trace, Label)
import art
import art23

learn = Sheet('learn', 'My body and my senses', level=1, goals=['Name parts of my body.', 'Name my five senses.'], blocks=[
    Box('adult', P('Read aloud. Play "Simon says": touch your head, shoulders, knees and toes!')),
    P('This is my **body**. I use it to run, jump, hug and play.', 'lead'),
    Fig(art23.body_outline(labels=art23.BODY_PARTS), 'The parts of my body.', width='40%'),
    H('My five senses', 3),
    Pics([('eye', 'eyes: see'), ('ear', 'ears: hear'), ('nose', 'nose: smell'), ('tongue', 'tongue: taste'), ('hand', 'skin: touch')], cols=5, size='20mm'),
    H('I am growing!', 3),
    Pics([('baby', 'baby'), ('child', 'child'), ('adult', 'grown-up'), ('older person', 'grandparent')], cols=4, size='20mm'),
])

facts = Sheet('facts', 'Body and senses', level=1, goals=['Label my body.', 'Match senses.'], blocks=[
    Q('Circle the parts we use to **walk** and **run**.', Choose([('leg', 'legs'), ('ear', 'ears'), ('foot', 'feet'), ('eye', 'eyes')], right=[0, 2])),
    Q('Match the sense to what it finds.', PicMatch([(('ear', 'ears'), ('musical notes', 'music')), (('tongue', 'tongue'), ('lemon', 'sour lemon')),
                                                     (('nose', 'nose'), ('blossom', 'flower smell'))], size='15mm')),
])

think = Sheet('think', 'Same and different', level=2, goals=['Compare myself with a friend.', 'Order growing up.'], blocks=[
    Q('Draw yourself and a friend. How are you the same? How are you different?', Draw('42mm', 'Me and my friend', 'Same: two eyes, two hands. Different: hair, height, clothes.')),
    Q('Put in order from youngest to oldest. Write **1**, **2**, **3**.', Pics([('adult', Ans('3')), ('baby', Ans('1')), ('child', Ans('2'))], cols=3, size='24mm')),
])

investigate = Sheet('investigate', 'Taste test', level=2, goals=['Use taste to sort foods.', 'Make a picture graph.'], blocks=[
    Box('adult', P('Give children tiny tastes of sweet, sour and salty foods (check for allergies first; children only taste food a grown-up gives them). They hold their nose for the last try: is it harder to taste?')),
    Q('Sort the foods: **sweet** or **sour**?', PicSort(['Sweet', 'Sour'], [('banana', 'banana', 'Sweet'), ('honey pot', 'honey', 'Sweet'), ('mango', 'mango', 'Sweet'),
                                                                      ('lemon', 'lemon', 'Sour'), ('tangerine', 'green orange', 'Sour'), ('grapes', 'sour grapes', 'Sour')], height='28mm')),
    Q('Which taste did we like best? Colour one box for each child.', Pictograph([('candy', 'sweet', 8), ('lemon', 'sour', 3), ('salt', 'salty', 4)], top=9)),
])

case = Sheet('case', 'Tuli wears glasses', level=3, goals=['Listen to a story.', 'Talk about our senses.'], blocks=[
    Case('Tuli could not see the pictures on the board. They looked fuzzy. Her teacher told her mother.',
         'The eye doctor gave Tuli glasses. Now she can see clearly! "My eyes help me read, play and learn," says Tuli.'),
    Q('Which sense did the glasses help? Circle.', Choose([('ear', 'hearing'), ('eye', 'seeing'), ('nose', 'smelling')], right=[1], cols=3)),
    Q('How can we look after our eyes? Draw one way.', Draw('38mm', '', 'Do not look at the Sun; do not sit too close to the TV; wear glasses if you need them.')),
])

review = Sheet('review', 'I can do it!', level=3, goals=['Trace body words.'], blocks=[
    Q('Trace the words.', Trace([('hand', 'hand'), ('eye', 'eye')])),
    Q('Circle the part you **hear** with.', Choose([('eye', 'eye'), ('ear', 'ear'), ('foot', 'foot'), ('nose', 'nose')], right=[1])),
])

TOPIC = Topic(
    code='A4', strand='living', title='My Body and My Senses', short='Body and senses',
    subtitle='Parts of my body, my five senses, growing up, and how we are the same and different',
    outcomes=[
        'recognize and name the main external parts of the human body.',
        'identify the five major sense organs, give the function of each, and suggest why they are important.',
        'explore how the senses enable humans and animals to be aware of the world around them.',
        'identify similarities and differences between themselves and other children.',
        'identify the general physical changes they have undergone since birth, and link them to the idea of growth.',
    ],
    sheets=[learn, facts, think, investigate, case, review],
    selfcheck=['name parts of my body', 'name my five senses', 'say how I have grown'],
    cover_art=art.pic_row(['baby', 'child', 'adult', 'older person']),
)
