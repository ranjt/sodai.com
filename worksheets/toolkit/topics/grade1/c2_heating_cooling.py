from build import Sheet, Topic
from ws import (P, H, Box, Vocab, Fig, Q, Lines, Blanks, Match, TrueFalse, MCQ, Table, Ans, Sort, Draw, Graph, WordSearch, Bullets, Pics,
                Choose, PicMatch, PicSort, Pictograph, Trace, Case)
import art

learn = Sheet('learn', 'Heating, cooling and dissolving', level=1, goals=['Describe how heating and cooling change things.', 'Find things that dissolve.'], blocks=[
    P('Some materials **change** when we heat them or cool them.', 'lead'),
    Table(['When we heat it…', 'When we cool it…'], [['ice **melts** into water', 'water **freezes** into ice'], ['chocolate and butter **melt**', 'melted chocolate goes **hard** again'],
                                                   ['an egg **cooks** and goes hard', 'a cooked egg stays cooked'], ['water **boils** and turns to steam', 'steam turns back into water drops']]),
    Pics([('ice cube', 'ice'), ('chocolate', 'chocolate'), ('frying egg', 'egg'), ('cup of tea', 'hot water')], cols=4, size='19mm'),
    P('Some changes can go **back** (ice ↔ water). Some changes **cannot** go back (a cooked egg).'),
    H('Dissolving', 3),
    P('When we stir **sugar** or **salt** into water, it seems to disappear. It has **dissolved**. Sand and rice do not dissolve.'),
    Pics([('salt', 'salt dissolves'), ('cookie', 'sugar dissolves'), ('rock', 'sand does not'), ('cooked rice', 'rice does not')], cols=4, size='19mm'),
    Box('safety', P('Only grown-ups use the stove and hot water.')),
    Vocab([('melt', 'change from solid to liquid when heated'), ('freeze', 'change from liquid to solid when cooled'), ('dissolve', 'mix into water and seem to disappear')]),
])

facts = Sheet('facts', 'Change facts', level=1, goals=['Sort changes.', 'Find what dissolves.'], blocks=[
    Q('Heating or cooling?', Sort(['Heating', 'Cooling'], [('ice melts', 'Heating'), ('an egg cooks', 'Heating'), ('water boils', 'Heating'),
                                                         ('water freezes', 'Cooling'), ('jelly sets', 'Cooling'), ('melted chocolate goes hard', 'Cooling')])),
    Q('Circle the things that **dissolve** in water.', Choose([('salt', 'salt'), ('rock', 'sand'), ('cookie', 'sugar'), ('coin', 'coin')], right=[0, 2])),
])

think = Sheet('think', 'Can it change back?', level=2, goals=['Explain reversible changes.'], blocks=[
    Q('Can an ice lolly that melted be frozen again?', MCQ(['yes', 'no'], 0)),
    Q('Can a cooked egg become raw again?', MCQ(['yes', 'no'], 1)),
    Q('Why does ice cream melt on a hot day?', Lines(2, 'The heat from the air warms it, so it melts.')),
])

investigate = Sheet('investigate', 'Where does ice melt fastest?', level=2, goals=['Do a fair test.', 'Read a bar chart.'], blocks=[
    P('Class 1 put the same size ice cubes in three places and timed how long they took to melt.'),
    Q('Our results. Draw the bars.', Table(['Place', 'in the sun', 'in the classroom', 'in the fridge'], [['Minutes to melt', '10', '25', '60']], center=True),
      Graph(['sun', 'classroom', 'fridge'], [10, 25, 60], 'Minutes', 'Place', ymax=60, step=10, width=80, height=44)),
    Q('Where did the ice melt fastest? Why?', Lines(2, 'In the sun, because it was the warmest place.')),
])

case = Sheet('case', 'Making pitha in winter', level=3, goals=['Read about heating food.'], blocks=[
    Case('In winter, Grandma makes **pitha**. She mixes rice flour with water to make a soft dough. She melts **date palm gur** (jaggery) in a pan.',
         'She steams the pitha over hot water until it is cooked. The soft dough changes into a firm cake. Yum! The changes from heating cannot go back.'),
    Q('What does heating do to the gur?', Lines(1, 'It melts it.')),
    Q('Can the cooked pitha turn back into dough?', MCQ(['yes', 'no'], 1)),
])

review = Sheet('review', 'Show what you know', level=3, goals=['Use change words.'], blocks=[
    Q('Find the words.', WordSearch(['MELT', 'ICE', 'HEAT', 'COOL', 'SALT'], size=7, seed=109)),
    Q('Water turns into ice when it is…', MCQ(['heated', 'cooled'], 1)),
])

TOPIC = Topic(
    code='C2', strand='physical', title='Heating, Cooling and Dissolving', short='Heating and cooling',
    subtitle='Melting, freezing, cooking and boiling, changes that can and cannot go back, and dissolving',
    outcomes=[
        'explore and describe the way some everyday materials change when they are heated or cooled.',
        'investigate how liquids and solids respond to changes in temperature, for example, water changing to ice, or melting chocolate.',
        'recognise that some materials can dissolve in water.',
        'describe matter as everything that has mass and occupies volume.',
    ],
    sheets=[learn, facts, think, investigate, case, review],
    selfcheck=['say what heating and cooling do', 'tell if a change can go back', 'find things that dissolve'],
    cover_art=art.pic_row(['ice cube', 'water glass', 'cup of tea', 'chocolate'], ['ice', 'water', 'hot water', 'chocolate']),
)
