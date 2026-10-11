from build import Sheet, Topic
from ws import (P, H, Box, Vocab, Fig, Cols, Row, Case, Links, Lines, Blanks, Match, TrueFalse, MCQ, Order, Table,
                Ans, Sort, Label, Draw, Graph, WordSearch, Q, Part, Bullets, Pics)
import art
import art23

learn = Sheet('learn', 'Plants and their parts', level=1, goals=[
    'Name the parts of a plant and say what each part does.',
    'Explain that plants need water, light and the right temperature to grow.',
    'Explain how water travels from the roots up the stem.',
], blocks=[
    P('Plants are living things. They grow all around us: rice in the fields, mango trees in the garden, and the shapla '
      'flower in the pond. Most plants have the same parts.', 'lead'),
    Fig(art.plant_parts(labels=art.PLANT_PARTS), 'The parts of a plant.', width='62%'),
    Table(['Part', 'What it does'], [
        ['**roots**', 'hold the plant in the soil and take in **water** from the soil'],
        ['**stem**', 'holds the plant up and carries water from the roots to the leaves'],
        ['**leaves**', 'use **sunlight** to make food for the plant'],
        ['**flower**', 'makes seeds, so new plants can grow'],
        ['**fruit**', 'holds and protects the seeds']]),
    H('How water travels', 3),
    P('Water goes **in** through the **roots**. Then it travels **up** the **stem**, like water up a straw, to the leaves and flowers.'),
    Fig(art23.celery_stem(), 'Put a white flower in coloured water. What happens?', width='62%'),
    H('What plants need', 3),
    Pics([('droplet', 'water'), ('sun', 'light'), ('thermometer', 'warmth'), ('rock', 'soil and minerals'), ('wind face', 'air')], cols=5, size='14mm'),
    P('Plants need **water**, **light**, **air**, the right **temperature** (not too hot, not too cold) and **minerals** from the soil. '
      'Without water, a plant **wilts** (droops). Without light, it turns **yellow** and weak. Plants need **healthy** roots, stems and leaves to grow well.'),
    Pics([('potted plant', 'healthy plant'), ('wilted flower', 'no water: it wilts')], cols=2, size='18mm'),
    Box('bd', P('Bangladesh is warm and wet, so plants grow very well here. Farmers plant rice when the monsoon rains come.')),
    Box('try', P('Plant two bean seeds in cups. Water one every day and do not water the other. What happens after a week?')),
    Vocab([('roots', 'take in water from the soil'), ('stem', 'carries water up the plant'), ('leaves', 'make food using sunlight'),
           ('flower', 'makes seeds'), ('wilt', 'droop because there is not enough water')]),
])

facts = Sheet('facts', 'Parts of a plant', level=1, goals=['Label a plant.', 'Say what plants need.'], blocks=[
    Q('Label the plant.', Label(art.plant_parts(), art.PLANT_PARTS, width='56%', cols=3), marks=5),
    Q('Draw a line to match.', Match([('roots', 'take in water'), ('stem', 'carries water up'), ('leaves', 'make food'), ('flower', 'makes seeds')]), marks=4),
    Q('Circle what a plant needs to grow.', Pics([('droplet', 'water'), ('sun', 'light'), ('chocolate', 'chocolate'), ('thermometer', 'warmth'), ('football', 'a ball')], cols=5, size='14mm'),
      Lines(1, 'water, light, warmth'), marks=3),
    Q('Fill in the gaps.', Blanks('Water goes into the plant through the [roots]. It travels up the [stem]. Leaves need [light] to make food.', extra=['flower']), marks=3),
])

think = Sheet('think', 'Why did it happen?', level=2, goals=['Explain what happens when plants do not get what they need.'], blocks=[
    Q('Look at the two plants. What happened to plant B? Why?', Pics([('potted plant', 'A'), ('wilted flower', 'B')], cols=2, size='20mm'),
      Lines(2, 'Plant B wilted (drooped). It did not get enough water.'), marks=2),
    Q('A plant was kept in a dark cupboard for a week. What colour will its leaves be?', MCQ(['dark green', 'yellow', 'red'], 1), marks=1),
    Q('Why does a plant need healthy roots?', Lines(2, 'To hold it in the soil and to take in water.'), marks=2),
    Q('A plant was left outside on a very cold night. Predict what might happen.', Lines(2, 'It may stop growing or be damaged, because plants need the right temperature.'), marks=1),
])

investigate = Sheet('investigate', 'Does a plant need light to grow?', level=2, goals=['Do a simple fair test.', 'Measure and compare.'], blocks=[
    P('Class 2B grew two bean plants. Plant A was by the window. Plant B was in a dark cupboard. They both got the same water. After 10 days they measured them.'),
    Q('Complete the table.', Table(['', 'Plant A (light)', 'Plant B (dark)'], [['Height (cm)', '12', '15'], ['Colour of leaves', 'green', 'yellow'], ['Healthy?', Ans('yes'), Ans('no, weak and thin')]], center=True), marks=2),
    Q('Plant B is taller, but is it healthier? Why?', Lines(2, 'No. It grew tall and thin looking for light, but it is yellow and weak.'), marks=2),
    Q('What did they keep the same?', Lines(1, 'the same amount of water, the same kind of plant and pot'), marks=1),
    Q('Draw the two plants.', Row([Draw('34mm', 'A: in the light', 'short, green, strong')], [Draw('34mm', 'B: in the dark', 'tall, thin, yellow')]), marks=2),
])

case = Sheet('case', 'Mina\'s rooftop garden', level=3, goals=['Use plant science in real life.', 'Solve a problem.'], blocks=[
    Links('Science', 'Food', 'Maths'),
    Case('Mina lives in a flat in Dhaka. There is no garden, so her family grows vegetables in pots on the **roof**: tomatoes, '
         'chillies and spinach (*palong shak*). Mina waters the pots every evening.',
         'In April the weather is very hot. Some plants start to wilt in the middle of the day. Mina\'s mother puts up an old '
         'cloth to give some shade, and Mina gives them water early in the morning too. Soon the plants are green and strong again.',
         source='A story about a rooftop garden in Dhaka.'),
    Q('Why did the plants wilt?', Lines(2, 'It was very hot and they lost water; they did not have enough water.'), marks=2),
    Q('What did Mina and her mother do to help the plants?', Lines(2, 'They gave shade with a cloth and watered the plants in the morning too.'), marks=2),
    Q('What do the plants on the roof need? Circle them.', Pics([('sun', 'light'), ('droplet', 'water'), ('wind face', 'air'), ('television', 'TV')], cols=4, size='14mm'), Lines(1, 'light, water, air'), marks=3),
])

review = Sheet('review', 'Show what you know', level=3, goals=['Use plant words.', 'Answer questions.'], blocks=[
    Q('Find the words.', WordSearch(['ROOT', 'STEM', 'LEAF', 'FLOWER', 'SEED', 'WATER'], size=8, seed=202)),
    Q('Which part takes in water?', MCQ(['flower', 'roots', 'leaf'], 1), marks=1),
    Q('Which part makes seeds?', MCQ(['stem', 'flower', 'roots'], 1), marks=1),
    Q('**Challenge.** Draw a plant and label four parts.', Draw('50mm', 'My plant', 'Plant with roots, stem, leaves, flower labelled.'), marks=4),
])

TOPIC = Topic(
    code='A1', strand='living', title='Plants and Their Parts', short='Plants',
    subtitle='Roots, stems, leaves and flowers, and what plants need to grow',
    outcomes=[
        'know that plants have roots, leaves, stems and flowers.',
        'explain observations that plants need water and light to grow.',
        'know that water is taken in through the roots and transported through the stem.',
        'know that plants need healthy roots, leaves and stems to grow well.',
        'know that plant growth is affected by temperature.',
        'identify and describe examples of the external features and basic needs of living things.',
        'analyse how investigations can help us understand how living things survive.',
    ],
    cambridge=['Stage 3 Unit 1 Plants (1.1–1.4)'],
    sheets=[learn, facts, think, investigate, case, review],
    selfcheck=['name the parts of a plant', 'say what each part does', 'say what plants need', 'explain how water moves up a stem', 'test if plants need light'],
    cover_art=art.plant_parts(labels=art.PLANT_PARTS),
)
