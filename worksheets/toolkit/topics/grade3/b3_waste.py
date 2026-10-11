from build import Sheet, Topic
from ws import (P, H, Box, Vocab, Fig, Cols, Row, Case, Links, Lines, Blanks, Match, TrueFalse, MCQ, Order, Table,
                Ans, Sort, Label, Draw, Graph, WordSearch, Q, Part, Bullets, Pics)
import art

learn = Sheet('learn', 'Waste and our world', level=1, goals=[
    'Explain the differences between waste, compost, recyclable and reusable materials.',
    'Give examples of solid, liquid and gas waste from plants, animals and people.',
    'Explain how waste harms nature and plan ways to reduce it with the three Rs.',
], blocks=[
    P('Every day, people throw things away: food scraps, plastic bags, paper, bottles. This is **waste**. If we do not deal with it well, it pollutes our rivers, land and air.', 'lead'),
    H('Kinds of waste', 3),
    Table(['', 'Solid waste', 'Liquid waste', 'Gas waste'], [
        ['**plants**', 'fallen leaves', 'water released from leaves', 'oxygen (useful to us!)'],
        ['**animals**', 'dung (poo)', 'urine', 'carbon dioxide breathed out'],
        ['**people\'s homes**', 'food scraps, plastic, paper', 'dirty water from washing', 'smoke from cooking fires'],
        ['**factories and vehicles**', 'scrap metal, packaging', 'dirty water, chemicals', 'smoke and exhaust fumes']]),
    H('Sort your waste', 3),
    Table(['Type', 'What it means', 'Examples'], [
        ['**compostable**', 'rots and becomes rich soil (compost)', 'fruit and vegetable peels, leaves, egg shells'],
        ['**recyclable**', 'can be made into new things', 'paper, glass bottles, metal cans, some plastic'],
        ['**reusable**', 'can be used again', 'glass jars, cloth bags, old clothes'],
        ['**waste to throw away**', 'cannot be reused, recycled or composted', 'used tissues, some wrappers']]),
    Pics([('apple', 'compost'), ('newspaper', 'recycle'), ('glass bottle', 'reuse'), ('reusable bag', 'reuse'), ('wastebasket', 'bin')], cols=5, size='14mm'),
    H('How waste harms nature', 3),
    Bullets(['Plastic in rivers and drains causes **floods** and harms **fish** and **turtles**.', 'Dirty water from factories **pollutes rivers** like the Buriganga.',
             'Smoke from burning rubbish makes the **air** unhealthy.', 'Rubbish heaps attract **rats** and **flies** that spread disease.']),
    H('The three Rs', 3),
    Bullets(['**Reduce**: use less. Take a cloth bag to the market.', '**Reuse**: use things again. Use a jar as a pencil pot.', '**Recycle**: make old things into new things. Give paper, metal and plastic to the *bhangari* collector.']),
    P('And **compost** your food scraps to make rich soil for plants.'),
    Pics([('recycling', 'recycle'), ('reusable bag', 'reduce'), ('glass bottle', 'reuse'), ('seedling', 'compost helps plants')], cols=4, size='14mm'),
    Vocab([('waste', 'things we throw away'), ('compost', 'rotted plant waste that makes soil rich'), ('recycle', 'make into something new'),
           ('reuse', 'use again'), ('reduce', 'use less'), ('pollution', 'harmful things in air, water or land')]),
])

facts = Sheet('facts', 'Sort the waste', level=1, goals=['Sort waste.', 'Name the three Rs.'], blocks=[
    Q('Sort the waste.', Sort(['Compost', 'Recycle', 'Reuse'], [('banana peel', 'Compost'), ('dead leaves', 'Compost'), ('newspaper', 'Recycle'), ('metal can', 'Recycle'), ('glass jar', 'Reuse'), ('cloth bag', 'Reuse')]), marks=6),
    Q('Solid, liquid or gas waste?', Table(['Waste', 'Solid, liquid or gas?'], [['smoke from a fire', Ans('gas')], ['dirty washing water', Ans('liquid')], ['a plastic bottle', Ans('solid')], ['carbon dioxide we breathe out', Ans('gas')]], widths=['60%', '40%']), marks=4),
    Q('Draw a line to match.', Match([('reduce', 'use less'), ('reuse', 'use again'), ('recycle', 'make into something new')]), marks=3),
])

think = Sheet('think', 'Less waste, cleaner world', level=2, goals=['Explain harm from waste.', 'Plan to reduce it.'], blocks=[
    Q('How can plastic bags cause floods in a city?', Lines(2, 'They block drains, so rain water cannot flow away.'), marks=2),
    Q('Write three things your family can do to make less waste.', Lines(3, 'take cloth bags; compost food scraps; reuse jars; give paper to the recycler; buy less packaging.'), marks=3),
    Q('Why is compost good for a garden?', Lines(2, 'It adds goodness to the soil so plants grow well.'), marks=2),
])

investigate = Sheet('investigate', 'What rots in the soil?', level=2, goals=['Observe over time.', 'Record results.'], blocks=[
    P('Class 3B buried four things in soil in a pot and dug them up after four weeks.'),
    Q('Complete the table.', Table(['Item', 'After 4 weeks', 'Rots (compostable)?'], [['banana peel', 'mostly gone, soft and black', Ans('yes')], ['paper', 'soft, falling apart', Ans('yes')],
                                                                                   ['plastic bag', 'no change', Ans('no')], ['metal bottle cap', 'no change (a little rust)', Ans('no')]], center=True), marks=4),
    Q('What does this tell you about plastic?', Lines(2, 'Plastic does not rot, so it stays in the environment for a very long time.'), marks=2),
    Q('Which living things helped the banana peel rot?', Lines(1, 'decomposers: worms, mould and microbes'), marks=1),
])

case = Sheet('case', 'Turning rubbish into compost', level=3, goals=['See how a community reduces waste.'], blocks=[
    Links('Science', 'Citizenship', 'Maths'),
    Case('In Dhaka, a lot of household rubbish is food and vegetable waste. In some neighbourhoods, workers collect this waste from homes and take it to a **compost plant**.',
         'They pile it up in boxes. Worms and microbes break it down. After about two months it becomes dark, crumbly **compost**, which is sold to farmers and gardeners. Less rubbish goes to the dump, and farmers get good soil.',
         source='Based on community composting projects in Dhaka (example numbers below).'),
    Q('Why is food waste good for making compost?', Lines(2, 'It rots easily and becomes rich soil.'), marks=2),
    Q('A family makes 2 kg of food waste every day. How much in a week?', Lines(1, '2 × 7 = 14 kg'), marks=1),
    Q('Make a poster for your school about the three Rs.', Draw('40mm', 'Three Rs poster', 'Reduce, reuse, recycle with pictures.'), marks=3),
])

review = Sheet('review', 'Show what you know', level=3, goals=['Use waste words.'], blocks=[
    Q('Find the words.', WordSearch(['WASTE', 'REDUCE', 'REUSE', 'RECYCLE', 'COMPOST', 'PLASTIC'], size=9, seed=309)),
    Q('Which can be composted?', MCQ(['a plastic bag', 'a mango peel', 'a glass bottle'], 1), marks=1),
    Q('Taking a cloth bag to the shop is…', MCQ(['reducing', 'recycling', 'burning'], 0), marks=1),
    Q('**Challenge.** Design a bin system for your classroom.', Draw('40mm', 'Classroom bins', 'Three bins: compost, recycle, rubbish, with pictures on each.'), marks=3),
])

TOPIC = Topic(
    code='B3', strand='earth', title='Waste and Our World', short='Waste',
    subtitle='Kinds of waste, compost, recycling and reusing, how waste harms nature, and the three Rs',
    outcomes=[
        'recognise ways that human activity affects the environment, such as river pollution and recycling waste.',
        'explain the differences between waste, compost, recyclable and reusable materials.',
        'identify and classify different types of waste — compostable, recycled and reused materials.',
        'recognize that plants, animals and human-made systems produce waste of different types, and give examples of the solid, liquid and gaseous waste each produces.',
        'explore the negative impacts of waste on various natural systems, and suggest ways in which those effects can be reduced.',
        'plan and implement actions they can take to reduce waste, practising the three Rs — reduce, reuse and recycle — including composting.',
    ],
    sheets=[learn, facts, think, investigate, case, review],
    selfcheck=['sort compost, recycle and reuse', 'name solid, liquid and gas waste', 'explain how waste harms nature', 'use the three Rs', 'test what rots in soil'],
    cover_art=art.pic_row(['recycling', 'reusable bag', 'glass bottle', 'seedling']),
)
