from build import Sheet, Topic
from ws import (P, H, Box, Vocab, Fig, Q, Lines, Blanks, Match, TrueFalse, MCQ, Table, Ans, Sort, Draw, Graph, WordSearch, Bullets, Pics,
                Choose, PicMatch, PicSort, Pictograph, Trace, Case)
import art

learn = Sheet('learn', 'Keeping our environment clean', level=1, goals=['Describe a healthy environment.', 'Plan ways to keep it clean.'], blocks=[
    P('A **healthy environment** has clean land, clean water, clean air and plenty of trees. People and animals stay well there.', 'lead'),
    Pics([('seedling', 'trees and plants'), ('water wave', 'clean rivers'), ('wind face', 'fresh air'), ('toilet', 'clean toilets'), ('wastebasket', 'rubbish in bins')], cols=5, size='18mm'),
    H('What harms our environment?', 3),
    Pics([('no littering', 'litter'), ('factory smoke', 'smoke'), ('axe', 'cutting trees'), ('oil spill', 'dirty water in rivers')], cols=4, size='18mm'),
    H('Sort your rubbish', 3),
    P('We can sort waste by what it is made of, so it can be **recycled**: paper, plastic, metal, glass, and food waste for compost.'),
    Pics([('newspaper', 'paper'), ('plastic bottle', 'plastic'), ('tin can', 'metal'), ('glass bottle', 'glass'), ('banana', 'food waste')], cols=5, size='18mm'),
    P('Remember the three Rs: **reduce** (use less), **reuse** (use again) and **recycle** (make into something new).'),
])

facts = Sheet('facts', 'Clean or harmful?', level=1, goals=['Sort helpful and harmful actions.', 'Sort waste.'], blocks=[
    Q('Sort the actions.', Sort(['Helps the environment', 'Harms the environment'], [('planting trees', 'Helps the environment'), ('using a bin', 'Helps the environment'),
                                                                                   ('reusing a bag', 'Helps the environment'), ('dropping litter', 'Harms the environment'),
                                                                                   ('burning rubbish', 'Harms the environment'), ('throwing bottles in the river', 'Harms the environment')])),
    Q('Which bin? Match the waste to its material.', Match([('a newspaper', 'paper bin'), ('a juice bottle', 'plastic bin'), ('a can', 'metal bin'), ('a mango peel', 'compost')])),
])

think = Sheet('think', 'Our school plan', level=2, goals=['Suggest ways to keep the school clean.'], blocks=[
    Q('Write two ways our school can stay clean and healthy.', Lines(3, 'Put bins in every class; sort recycling; plant trees; keep toilets clean; turn off taps.')),
    Q('Make a poster for your school.', Draw('48mm', 'Keep it clean!', 'e.g. "Use the bin!" with a picture of a child putting rubbish in a bin.')),
])

investigate = Sheet('investigate', 'Our class rubbish survey', level=2, goals=['Sort and count waste.', 'Read a bar chart.'], blocks=[
    Box('adult', P('Wearing gloves, empty the class bin onto a sheet. Sort the waste into groups and count them.')),
    Q('Our results. Draw the bars.', Table(['Waste', 'paper', 'plastic', 'food', 'metal'], [['Number', '12', '8', '5', '2']], center=True),
      Graph(['paper', 'plastic', 'food', 'metal'], [12, 8, 5, 2], 'Number', 'Waste', ymax=14, step=2, width=86, height=44)),
    Q('Which waste did we have the most of?', MCQ(['paper', 'plastic', 'metal'], 0)),
    Q('How could we make less of it?', Lines(1, 'use both sides of paper; reuse scrap paper')),
])

case = Sheet('case', 'The green school', level=3, goals=['Read about a school that cares.'], blocks=[
    Case('At a school in Dhaka, children noticed plastic bags blowing around the playground. They decided to act.',
         'They put labelled bins for paper, plastic and food waste in every class. They planted trees and made a small garden with compost from food waste. Now the school is cleaner and greener!'),
    Q('Write two things the children did.', Lines(2, 'put labelled bins in every class; planted trees; made compost')),
    Q('Why is food waste good for compost?', Lines(1, 'It rots and makes the soil rich.')),
])

review = Sheet('review', 'Show what you know', level=3, goals=['Use environment words.'], blocks=[
    Q('Find the words.', WordSearch(['BIN', 'TREE', 'CLEAN', 'REUSE', 'AIR'], size=7, seed=107)),
    Q('Which helps keep the river clean?', MCQ(['throwing bottles in it', 'putting rubbish in a bin'], 1)),
])

TOPIC = Topic(
    code='B3', strand='earth', title='Keeping Our Environment Clean', short='Clean environment',
    subtitle='A healthy environment, what harms it, sorting waste, and the three Rs',
    outcomes=[
        'identify a healthy environment — clean and controlled land use, a controlled system for disposing of human waste, natural forest and vegetation, clean waterways, and clean air rich in oxygen.',
        'identify different human activities that can degrade the quality of the environment.',
        'plan and carry out activities that can help improve the quality of the environment.',
        'suggest ways the school community can help keep the local environment healthy.',
        'segregate waste according to the material it is made from, and reuse, reduce and recycle materials.',
    ],
    sheets=[learn, facts, think, investigate, case, review],
    selfcheck=['describe a healthy environment', 'sort waste by material', 'plan a clean-up'],
    cover_art=art.pic_row(['seedling', 'wastebasket', 'recycling', 'water wave'], ['plant trees', 'use bins', 'recycle', 'clean rivers']),
)
