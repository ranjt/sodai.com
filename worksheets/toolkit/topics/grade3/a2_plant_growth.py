from build import Sheet, Topic
from ws import (P, H, Box, Vocab, Fig, Cols, Row, Case, Links, Lines, Blanks, Match, TrueFalse, MCQ, Order, Table,
                Ans, Sort, Label, Draw, Graph, WordSearch, Q, Part, Bullets, Pics)
import art
import art4

learn = Sheet('learn', 'How plants grow', level=1, goals=[
    'Tell flowering and non-flowering plants apart.',
    'Describe the life cycle of a flowering plant and its main parts.',
    'Measure plant growth and compare plant and animal life cycles.',
], blocks=[
    P('A tiny seed can grow into a giant mango tree. How does it happen? Let\'s follow a plant through its life.', 'lead'),
    H('Flowering and non-flowering plants', 3),
    P('**Flowering plants** grow flowers that make seeds: mango, rice, lotus, sunflower, grass. **Non-flowering plants** do not have flowers: **ferns** and **mosses** grow from tiny **spores**, and pine trees make seeds in **cones**.'),
    Row([Pics([('mango', 'mango'), ('rice plant', 'rice'), ('lotus', 'lotus')], cols=3, size='13mm')], [Fig(art4.fern_moss(), 'Ferns and mosses: no flowers.')]),
    H('The parts of a flowering plant', 3),
    Fig(art.plant_parts(labels=art.PLANT_PARTS), 'Root, stem, leaf, flower and fruit.', width='54%'),
    H('The life cycle of a flowering plant', 3),
    Fig(art.life_cycle(labels=art.LIFE_CYCLE_STAGES), 'From seed to seed.', width='70%'),
    Bullets(['A **seed** **germinates** (starts to grow) when it has water and warmth.', 'It becomes a **seedling** with its first leaves.',
             'The seedling grows into a **mature** (adult) plant.', 'The plant makes **flowers**. Insects or wind carry pollen, and **seeds** form inside **fruits**.',
             'The seeds are spread, and the cycle starts again.']),
    H('Measuring growth', 3),
    P('We can measure a plant\'s **height** with a ruler each week, count its **leaves**, or measure the width of its stem. A bar chart shows how it grows over time.'),
    H('Plants and animals', 3),
    Table(['', 'Flowering plant', 'Chicken'], [['starts as', 'seed', 'egg'], ['young', 'seedling', 'chick'], ['adult', 'plant with flowers', 'hen'], ['new life from', 'seeds', 'eggs']]),
    Box('bd', P('Rice is the most important crop in Bangladesh. Farmers plant rice seedlings in flooded fields and harvest the grains (seeds) a few months later.')),
    Vocab([('germinate', 'start to grow from a seed'), ('seedling', 'a young plant'), ('mature', 'fully grown'), ('spore', 'a tiny part that grows into a fern or moss'), ('life cycle', 'the stages of life, from seed to seed')]),
])

facts = Sheet('facts', 'Plant life cycle', level=1, goals=['Sort plants.', 'Order the life cycle.'], blocks=[
    Q('Sort the plants.', Sort(['Flowering', 'Non-flowering'], [('mango tree', 'Flowering'), ('rice', 'Flowering'), ('sunflower', 'Flowering'), ('fern', 'Non-flowering'), ('moss', 'Non-flowering'), ('pine tree', 'Non-flowering')]), marks=6),
    Q('Number the stages in order.', Order(['seed', 'seed germinates', 'seedling', 'adult plant with flowers', 'fruit with new seeds']), marks=4),
    Q('Label the plant.', Label(art.plant_parts(), art.PLANT_PARTS, width='50%', cols=3), marks=5),
])

think = Sheet('think', 'Growing and comparing', level=2, goals=['Compare life cycles.', 'Explain plant needs.'], blocks=[
    Q('How is a plant life cycle like a chicken\'s? How is it different?', Lines(3, 'Same: both start small (seed/egg), grow into adults and make new young. Different: plants make seeds in fruits; chickens lay eggs.'), marks=2),
    Q('A seed is kept dry in a packet. Will it germinate? Why?', Lines(2, 'No: it needs water (and warmth) to germinate.'), marks=2),
    Q('Draw the life cycle of a bean plant with four stages and arrows.', Draw('46mm', 'Bean life cycle', 'seed → seedling → adult plant with flowers → bean pods with seeds.'), marks=3),
])

investigate = Sheet('investigate', 'How fast does a bean plant grow?', level=2, goals=['Measure height each week.', 'Draw a bar chart.', 'Find a pattern.'], blocks=[
    P('Class 3C measured a bean plant every week.'),
    Q('Draw a bar chart.', Table(['Week', '1', '2', '3', '4', '5'], [['Height (cm)', '2', '6', '11', '17', '20']], center=True),
      Graph(['1', '2', '3', '4', '5'], [2, 6, 11, 17, 20], 'Height (cm)', 'Week', ymax=22, step=2, width=110, height=48), marks=3),
    Q('Describe the pattern.', Lines(2, 'The plant grew taller every week.'), marks=1),
    Q('In which week did it grow the most?', Lines(1, 'Week 4 (6 cm more than week 3)'), marks=1),
    Q('Predict the height in week 6.', Lines(1, 'about 22–23 cm'), marks=1),
])

case = Sheet('case', 'A rice farmer\'s year', level=3, goals=['Follow a real crop through its life cycle.'], blocks=[
    Links('Science', 'Farming', 'Maths'),
    Case('Abdul is a rice farmer in Mymensingh. First he soaks rice seeds in water until they **germinate**. He plants them close together in a small bed of mud. After about a month the **seedlings** are moved to the big flooded field.',
         'The rice plants grow tall and green. Tiny **flowers** appear, and the wind carries pollen. The grains (**seeds**) grow and turn golden. About four months after planting, Abdul **harvests** the rice. He keeps some seeds to plant next year.',
         source='Based on rice farming in Bangladesh.'),
    Q('Put Abdul\'s year in order.', Order(['soak seeds so they germinate', 'grow seedlings in a mud bed', 'move seedlings to the field', 'rice flowers', 'harvest the grains']), marks=4),
    Q('Why does Abdul keep some seeds?', Lines(1, 'To plant next year: the life cycle starts again.'), marks=1),
    Q('Rice takes about 4 months from planting to harvest. How many weeks is that?', Lines(1, 'about 16–17 weeks'), marks=1),
])

review = Sheet('review', 'Show what you know', level=3, goals=['Use plant words.'], blocks=[
    Q('Find the words.', WordSearch(['SEED', 'ROOT', 'STEM', 'LEAF', 'FLOWER', 'FRUIT', 'FERN'], size=9, seed=303)),
    Q('Which plant has no flowers?', MCQ(['mango', 'fern', 'rice'], 1), marks=1),
    Q('A seed starting to grow is called…', MCQ(['germinating', 'flowering', 'wilting'], 0), marks=1),
    Q('**Challenge.** Why do plants make so many seeds?', Lines(2, 'Many seeds are eaten or land in bad places, so making lots means some will grow.'), marks=2),
])

TOPIC = Topic(
    code='A2', strand='living', title='Plant Growth and Development', short='Plant growth',
    subtitle='Flowering and non-flowering plants, the life cycle of a flowering plant and measuring growth',
    outcomes=[
        'distinguish between flowering and non-flowering plant species found locally.',
        'describe the typical physical growth cycle of a flowering plant — seed, immature form, mature organism — using labelled line drawings.',
        'observe the growth cycle of specific plants in order to identify the growth stages and the main parts of a flowering plant: root, stem, leaf and flower.',
        'use appropriate measures for plant growth at different stages in the growth cycle of a variety of local flowering plants.',
        'compare key stages in the life cycle of a plant and an animal, and relate them to growth and survival.',
    ],
    cambridge=['Stage 3 Unit 1 Plants (1.1–1.4)'],
    sheets=[learn, facts, think, investigate, case, review],
    selfcheck=['sort flowering and non-flowering plants', 'name the parts of a plant', 'draw a plant life cycle', 'measure plant growth', 'compare plant and animal life cycles'],
    cover_art=art.life_cycle(labels=art.LIFE_CYCLE_STAGES),
)
