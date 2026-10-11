from build import Sheet, Topic
from ws import (P, H, Box, Vocab, Fig, Cols, Row, Case, Links, Lines, Blanks, Match, TrueFalse, MCQ, Order, Table,
                Ans, Sort, Label, Draw, Graph, WordSearch, Q, Part, Bullets, Pics)
import art
import art23

learn = Sheet('learn', 'Rocks, minerals and soils', level=1, goals=[
    'Name some types of rock and their uses.',
    'Explain how rocks break down to make soil.',
    'Describe what soil is made of and how people use rocks, minerals and soil.',
], blocks=[
    P('Rocks are everywhere: in hills, on beaches, under rivers and deep under your feet. Rocks are made of **minerals**. Over a very long time, rocks break into tiny pieces that become **soil**.', 'lead'),
    H('Types of rock', 3),
    Fig(art23.rock_types(), 'Five kinds of rock.', width='88%'),
    Table(['Rock', 'What it is like', 'We use it for…'], [
        ['**granite**', 'very hard, speckled', 'buildings, kitchen tops, statues'], ['**sandstone**', 'made of sand grains stuck together', 'walls and buildings'],
        ['**marble**', 'smooth, can be polished', 'floors, statues'], ['**slate**', 'splits into thin flat sheets', 'roofs, writing boards'],
        ['**chalk**', 'soft, white, crumbly', 'writing on boards']]),
    H('Minerals', 3),
    P('**Minerals** are the natural materials rocks are made of. Salt is a mineral. Gold, iron and copper come from minerals in rocks. Shiny **gems** are minerals too.'),
    H('From rock to soil', 3),
    Fig(art23.rock_to_soil(), 'How rock becomes soil.', width='92%'),
    P('**Rain**, **heat**, **cold** and **plant roots** crack rocks. Rivers roll stones and rub them smooth and small. Over thousands of years rocks become **sand** and **soil**.'),
    H('What is soil?', 3),
    P('Soil is a **mixture** of tiny bits of rock (sand and clay), **dead plants and animals** (humus), **water** and **air**. It lies in **layers**.'),
    Fig(art.soil_layers(labels=art.SOIL_LAYERS), 'Layers of soil.', width='60%'),
    H('How we use them', 3),
    Pics([('house', 'bricks from clay'), ('building construction', 'stone for roads'), ('salt', 'salt'), ('ring', 'metals and gems'), ('rice plant', 'soil to grow food')], cols=5, size='14mm'),
    Box('bd', P('Bangladesh has very few rocks on the surface, so builders make **bricks** by baking clay soil in brick kilns. '
                'Stones for roads come from rivers in the north, such as near Sylhet.')),
    Vocab([('rock', 'hard natural material from the Earth'), ('mineral', 'a natural material that rocks are made of'),
           ('soil', 'tiny bits of rock mixed with dead plants, water and air'), ('humus', 'rotted plants and animals in soil')]),
])

facts = Sheet('facts', 'Rocks and their uses', level=1, goals=['Name rocks.', 'Match rocks to uses.'], blocks=[
    Q('Write the name of each rock.', Fig(art23.rock_types(names=False), width='86%'),
      Table(['A', 'B', 'C', 'D', 'E'], [[Ans('granite'), Ans('sandstone'), Ans('marble'), Ans('slate'), Ans('chalk')]], center=True), marks=5),
    Q('Draw a line to match the rock to its use.', Match([('slate', 'roofs'), ('chalk', 'writing on boards'), ('marble', 'floors and statues'), ('clay', 'bricks')]), marks=4),
    Q('What is soil made of? Tick.', Table(['', 'In soil?'], [['tiny bits of rock', Ans('✓')], ['dead leaves (humus)', Ans('✓')], ['water and air', Ans('✓')], ['plastic', Ans('')]], center=True, widths=['70%', '30%']), marks=4),
])

think = Sheet('think', 'Rocks change', level=2, goals=['Explain how rocks break down.'], blocks=[
    Q('Put the pictures in order to show how rock becomes soil.', Order(['a big rock', 'cracks in the rock', 'small stones', 'sand', 'soil']), marks=3),
    Q('How can a tiny plant root break a rock?', Lines(2, 'The root grows into a crack and pushes, making the crack bigger until the rock breaks.'), marks=2),
    Q('Why are pebbles in a river smooth and round?', Lines(2, 'The water rolls them and they rub against each other, wearing off the sharp edges.'), marks=2),
])

investigate = Sheet('investigate', 'Which soil holds most water?', level=2, goals=['Do a fair test.', 'Measure water.'], blocks=[
    P('Class 2C put the same amount of sand, garden soil and clay into three funnels. They poured 100 ml of water on each and measured how much dripped through.'),
    Q('Draw a bar chart of the water that dripped through.', Table(['Soil', 'sand', 'garden soil', 'clay'], [['Water through (ml)', '80', '50', '20']], center=True),
      Graph(['sand', 'garden soil', 'clay'], [80, 50, 20], 'Water through (ml)', 'Soil', ymax=100, step=10, width=100, height=50), marks=3),
    Q('Which soil let most water through?', Lines(1, 'sand'), marks=1),
    Q('Which soil held most water?', Lines(1, 'clay'), marks=1),
    Q('What did they keep the same?', Lines(1, 'the amount of soil and water, the funnels'), marks=1),
])

case = Sheet('case', 'The brick kiln', level=3, goals=['Learn how soil is used to make bricks.', 'Think about good and bad effects.'], blocks=[
    Links('Science', 'Building', 'Environment'),
    Case('Near many towns in Bangladesh you can see tall chimneys. These are **brick kilns**. Workers dig up **clay soil**, mix it with water, '
         'shape it into blocks and bake them in a very hot fire. The soft clay becomes hard **bricks** for houses, schools and roads.',
         'But brick kilns can cause problems: they use up good farm soil, and the smoke makes the air dirty. New kilns use cleaner fires and some builders use blocks made without burning.',
         source='Based on brick making in Bangladesh.'),
    Q('Put the steps in order.', Order(['dig up clay', 'mix with water', 'shape into blocks', 'bake in a fire', 'hard bricks']), marks=4),
    Q('Give one good thing and one problem about brick kilns.', Lines(2, 'Good: bricks to build houses and schools. Problem: smoke pollutes the air; farm soil is used up.'), marks=2),
])

review = Sheet('review', 'Show what you know', level=3, goals=['Use rock words.'], blocks=[
    Q('Find the words.', WordSearch(['ROCK', 'SOIL', 'SAND', 'CLAY', 'CHALK', 'SLATE'], size=8, seed=209)),
    Q('Which rock is soft and used for writing on boards?', MCQ(['granite', 'chalk', 'marble'], 1), marks=1),
    Q('Soil is made from tiny bits of…', MCQ(['plastic', 'rock', 'glass'], 1), marks=1),
    Q('**Challenge.** Draw the layers of soil and label two layers.', Draw('44mm', 'Soil layers', 'humus/topsoil, subsoil, bedrock.'), marks=2),
])

TOPIC = Topic(
    code='B2', strand='earth', title='Rocks, Minerals and Soils', short='Rocks and soils',
    subtitle='Types of rock and their uses, minerals, how rocks break down into soil, and what soil is made of',
    outcomes=[
        'recognise some types of rock and the uses of different rocks.',
        'demonstrate one or more ways by which rocks break down to form the basis of soil.',
        'describe soils as a combination of different minerals, rocks and organic materials layered together in various ways.',
        'give examples of how minerals, rocks and soils are used by humans.',
        'understand that the Earth\'s resources are used in a variety of ways.',
    ],
    cambridge=['Stage 2 Unit 2 Looking at rocks (2.1–2.4)'],
    sheets=[learn, facts, think, investigate, case, review],
    selfcheck=['name five rocks', 'say how rocks are used', 'explain how rock becomes soil', 'say what soil is made of', 'test which soil holds most water'],
    cover_art=art23.rock_types(),
)
