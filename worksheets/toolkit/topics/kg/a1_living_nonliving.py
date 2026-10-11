from build import Sheet, Topic
from ws import (P, H, Box, Fig, Q, Lines, MCQ, Draw, Pics, Ans, Case, Links, Choose, PicMatch, PicSort, Pictograph, Trace)
import art

learn = Sheet('learn', 'Living and non-living things', level=1, goals=['Tell living things from non-living things.', 'Say what living things need.'], blocks=[
    Box('adult', P('Read the page aloud. Point to each picture and talk about it together: "Does it grow? Does it eat? Does it move by itself?"')),
    P('Some things are **living**. Living things **grow**, **eat**, **move** and have **babies**.', 'lead'),
    Pics([('child', 'child'), ('dog', 'dog'), ('deciduous tree', 'tree'), ('bird', 'bird')], cols=4, size='26mm'),
    P('Some things are **non-living**. They do not grow, eat or breathe.', 'lead'),
    Pics([('football', 'ball'), ('chair', 'chair'), ('car', 'car'), ('rock', 'rock')], cols=4, size='26mm'),
    H('Plants are living too!', 3),
    P('A plant grows from a tiny seed. It drinks water and needs sunlight.'),
    Pics([('chestnut', 'seed'), ('seedling', 'little plant'), ('sunflower', 'big plant')], cols=3, size='24mm'),
    H('Living things need…', 3),
    Pics([('cooked rice', 'food'), ('droplet', 'water'), ('wind face', 'air'), ('house', 'a home'), ('family', 'care')], cols=5, size='20mm'),
    P('Living things are made of tiny **cells**. They are so small that we need a microscope to see them.'),
])

facts = Sheet('facts', 'Find the living things', level=1, goals=['Find and sort living things.'], blocks=[
    Q('Circle the **living** things.', Choose([('cat', 'cat'), ('teddy bear', 'teddy'), ('fish', 'fish'), ('car', 'car'),
                                              ('sunflower', 'flower'), ('rock', 'rock'), ('ant', 'ant'), ('chair', 'chair')], right=[0, 2, 4, 6])),
    Q('Cut and sort: **living** or **non-living**?', PicSort(['Living', 'Non-living'], [
        ('cow', 'cow', 'Living'), ('deciduous tree', 'tree', 'Living'), ('butterfly', 'butterfly', 'Living'),
        ('football', 'ball', 'Non-living'), ('pencil', 'pencil', 'Non-living'), ('glass bottle', 'bottle', 'Non-living')])),
])

think = Sheet('think', 'What do living things need?', level=2, goals=['Choose what a plant needs.', 'Draw a living thing.'], blocks=[
    Q('A plant needs these to grow. Circle them.', Choose([('sun', 'sunlight'), ('ice cream', 'ice cream'), ('droplet', 'water'), ('teddy bear', 'toy')], right=[0, 2])),
    Q('Match the baby to its grown-up.', PicMatch([(('baby chick', 'chick'), ('chicken', 'hen')), (('seedling', 'little plant'), ('deciduous tree', 'tree')),
                                                    (('baby', 'baby'), ('adult', 'adult'))], size='16mm')),
    Q('Draw a living thing you saw today.', Draw('44mm', 'My living thing', 'Any living thing: a cat, a tree, a bird, a person.')),
])

investigate = Sheet('investigate', 'Living things hunt', level=2, goals=['Look for living things outside.', 'Make a picture graph.'], blocks=[
    Box('adult', P('Take the children into the school garden or a park. Count the living things together. Then colour one box for each one.')),
    Q('What did we find? Colour one box for each.', Pictograph([('bird', 'birds', 3), ('ant', 'ants', 7), ('deciduous tree', 'trees', 4), ('blossom', 'flowers', 5)], top=8)),
    Q('Which did we find the **most**? Circle it.', Choose([('bird', 'birds'), ('ant', 'ants'), ('deciduous tree', 'trees'), ('blossom', 'flowers')], right=[1])),
    Box('safety', P('Look with your eyes. Do not touch insects or plants you do not know. Wash your hands after.')),
])

case = Sheet('case', "Mina's seed", level=3, goals=['Listen to a story.', 'Put pictures in order.'], blocks=[
    Case('Mina put a little seed in a pot of soil. Every day she gave it water and put it in the sunshine.',
         'After one week, a tiny green shoot came up! After many weeks it grew into a tall sunflower. "My seed is a living thing," said Mina. "It grows!"'),
    Q('Put the pictures in order. Write **1**, **2**, **3**.', Pics([('sunflower', Ans('3')), ('chestnut', Ans('1')), ('seedling', Ans('2'))], cols=3, size='28mm')),
    Q('Is Mina\'s plant living?', MCQ(['yes', 'no'], 0)),
])

review = Sheet('review', 'I can do it!', level=3, goals=['Trace science words.', 'Find the one that is not living.'], blocks=[
    Q('Trace the words.', Trace([('living', 'seedling'), ('grow', 'sunflower')])),
    Q('Circle the one that is **not** living.', Choose([('cat', 'cat'), ('dog', 'dog'), ('rock', 'rock'), ('bird', 'bird')], right=[2])),
])

TOPIC = Topic(
    code='A1', strand='living', title='Living and Non-living Things', short='Living things',
    subtitle='What living things do, what they need, and sorting living and non-living things',
    outcomes=[
        'identify, sort and classify living things and non-living things.',
        'know that plants are living things, and that there are living things and things that have never been alive.',
        'differentiate between living and non-living things, identifying the visible characteristics of each — growth, feeding, movement and reproduction.',
        'make observations and identify the basic needs of people, plants and animals — food, water, air, protection and care.',
        'name cells as the building blocks that make up all living things.',
        'plan and carry out, or take part in, an investigation into how living things survive.',
    ],
    sheets=[learn, facts, think, investigate, case, review],
    selfcheck=['find living things', 'say what living things need', 'sort living and non-living things'],
    cover_art=art.pic_row(['child', 'dog', 'deciduous tree', 'football', 'rock'], ['child', 'dog', 'tree', 'ball', 'rock']),
)
