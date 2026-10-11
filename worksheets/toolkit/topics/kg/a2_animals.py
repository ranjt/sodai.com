from build import Sheet, Topic
from ws import (P, H, Box, Fig, Q, Lines, MCQ, Draw, Pics, Ans, Case, Choose, PicMatch, PicSort, Pictograph, Trace)
import art

learn = Sheet('learn', 'Animals around us', level=1, goals=['Name animals.', 'Say how animals move and grow.'], blocks=[
    Box('adult', P('Read aloud. Ask the children to move like each animal: hop like a rabbit, swim like a fish, fly like a bird.')),
    P('There are many **animals** around us: in our homes, in the fields, in the water and in the sky.', 'lead'),
    H('Animals move in different ways', 3),
    Pics([('rabbit', 'hops'), ('fish', 'swims'), ('bird', 'flies'), ('snake', 'slides'), ('horse', 'runs'), ('elephant', 'uses its trunk')], cols=6, size='19mm'),
    H('Animal babies grow up', 3),
    P('Animals have **babies**. The babies grow into grown-ups, just like you!'),
    Pics([('baby chick', 'chick'), ('chicken', 'hen'), ('sheep', 'lamb grows into sheep'), ('cow', 'calf grows into cow')], cols=4, size='20mm'),
    H('Animals help us', 3),
    Pics([('milk', 'milk from cows'), ('egg', 'eggs from hens'), ('honey pot', 'honey from bees'), ('yarn', 'wool from sheep')], cols=4, size='20mm'),
])

facts = Sheet('facts', 'Find the animals', level=1, goals=['Find animals that live in water.', 'Match animals to how they move.'], blocks=[
    Q('Circle the animals that live in **water**.', Choose([('fish', 'fish'), ('cat', 'cat'), ('crab', 'crab'), ('cow', 'cow'), ('dolphin', 'dolphin'), ('dog', 'dog')], right=[0, 2, 4], cols=6, size='18mm')),
    Q('Match the animal to how it moves.', PicMatch([(('rabbit', 'rabbit'), ('footprints', 'hop')), (('bird', 'bird'), ('feather', 'fly')),
                                                     (('fish', 'fish'), ('water wave', 'swim'))], size='16mm')),
])

think = Sheet('think', 'Animals help us', level=2, goals=['Say what animals give us.', 'Draw a favourite animal.'], blocks=[
    Q('Match the animal to what it gives us.', PicMatch([(('cow', 'cow'), ('milk', 'milk')), (('chicken', 'hen'), ('egg', 'egg')),
                                                         (('honeybee', 'bee'), ('honey pot', 'honey'))], size='16mm')),
    Q('Draw your favourite animal. Show how it moves.', Draw('48mm', 'My animal', 'Any animal, e.g. a rabbit hopping or a fish swimming.')),
])

investigate = Sheet('investigate', 'Animal movement game', level=2, goals=['Move like animals.', 'Make a picture graph.'], blocks=[
    Box('adult', P('Play "move like an animal". Then ask each child which animal they liked best and colour one box for each vote.')),
    Q('Our favourite animal moves. Colour one box for each child.', Pictograph([('rabbit', 'hop', 6), ('fish', 'swim', 4), ('bird', 'fly', 7), ('snake', 'slide', 3)], top=8)),
    Q('Which did most children like? Circle it.', Choose([('rabbit', 'hop'), ('fish', 'swim'), ('bird', 'fly'), ('snake', 'slide')], right=[2])),
])

case = Sheet('case', "Nana's hen", level=3, goals=['Listen to a story.', 'Order the pictures.'], blocks=[
    Case('Nana has a hen in her village home. One day the hen sat on her eggs to keep them warm.',
         'After three weeks, crack! Little chicks came out of the eggs. The chicks ate and grew bigger every day. Soon they were hens too!'),
    Q('Put the pictures in order. Write **1**, **2**, **3**.', Pics([('chicken', Ans('3')), ('egg', Ans('1')), ('hatching chick', Ans('2'))], cols=3, size='28mm')),
    Q('What did the chicks do every day?', MCQ(['grew bigger', 'got smaller'], 0)),
])

review = Sheet('review', 'I can do it!', level=3, goals=['Trace animal words.'], blocks=[
    Q('Trace the words.', Trace([('fish', 'fish'), ('bird', 'bird')])),
    Q('Circle the animal that can **fly**.', Choose([('cow', 'cow'), ('bird', 'bird'), ('fish', 'fish'), ('cat', 'cat')], right=[1])),
])

TOPIC = Topic(
    code='A2', strand='living', title='Animals Around Us', short='Animals',
    subtitle='Common animals, how they move, how they grow, and how animals help us',
    outcomes=[
        'recognize and identify a range of common animals and plants.',
        'model the differing movements of living things — for example how rabbits hop, how elephants use their trunks, how dolphins swim.',
        'know that humans and animals produce offspring which grow into adults.',
        'describe how animals are a life-sustaining resource for us and other living beings.',
        'explore ways that different animals and plants inhabit local environments.',
    ],
    sheets=[learn, facts, think, investigate, case, review],
    selfcheck=['name animals', 'show how animals move', 'say what animals give us'],
    cover_art=art.pic_row(['rabbit', 'fish', 'bird', 'elephant', 'cow']),
)
