from build import Sheet, Topic
from ws import (P, H, Box, Vocab, Fig, Cols, Row, Case, Links, Lines, Blanks, Match, TrueFalse, MCQ, Order, Table,
                Ans, Sort, Label, Draw, Graph, WordSearch, Q, Part, Bullets, Pics)
import art

learn = Sheet('learn', 'Solids, liquids and gases', level=1, goals=[
    'Sort materials into solids, liquids and gases.',
    'Explain that matter has mass and takes up space.',
    'Describe melting, freezing and how water turns to steam and back.',
], blocks=[
    P('Everything around you is made of **matter**: your desk, the water in your bottle and even the air. Matter has **mass** (it has weight) '
      'and takes up **space**. Matter can be a **solid**, a **liquid** or a **gas**.', 'lead'),
    Fig(art.states_particles(), 'Solid, liquid and gas.', width='76%'),
    Table(['', 'Solid', 'Liquid', 'Gas'], [['shape', 'keeps its shape', 'takes the shape of its container', 'spreads out to fill the space'],
                                           ['can you pour it?', 'no', 'yes', 'it floats and spreads'], ['examples', 'stone, ice, wood, spoon', 'water, milk, oil, juice', 'air, steam']]),
    Pics([('rock', 'solid'), ('ice cube', 'solid'), ('droplet', 'liquid'), ('milk', 'liquid'), ('balloon', 'gas inside'), ('wind face', 'air: a gas')], cols=6, size='13mm'),
    H('Heating and cooling change things', 3),
    Bullets(['**Melting**: when a solid is heated it can turn into a liquid. Ice melts into water; chocolate melts in your hand.',
             '**Freezing**: when a liquid is cooled it can turn into a solid. Water in the freezer becomes ice.',
             'Melting is the **reverse** (opposite) of freezing.',
             'When water is heated in a kettle it **boils** and turns into **steam** (a gas). When steam touches a cold lid, it turns back into **water drops**.']),
    Pics([('ice cube', 'ice'), ('fire', 'heat'), ('droplet', 'water'), ('hot drink', 'steam')], cols=4, size='14mm'),
    Box('safety', P('Steam and boiling water can burn you. Always ask an adult to help with heating.')),
    Box('bd', P('In winter in the north of Bangladesh it can be very cold, but water does not freeze outside. It only freezes in a fridge freezer, where it is below 0 °C.')),
    Vocab([('solid', 'keeps its shape'), ('liquid', 'can be poured'), ('gas', 'spreads out to fill a space'), ('melt', 'a solid turns into a liquid'),
           ('freeze', 'a liquid turns into a solid'), ('steam', 'water as a gas')]),
])

facts = Sheet('facts', 'Solid, liquid or gas?', level=1, goals=['Sort materials.', 'Name changes.'], blocks=[
    Q('Write **solid**, **liquid** or **gas**.', Pics([('rock', Ans('solid')), ('milk', Ans('liquid')), ('balloon', Ans('gas inside')), ('spoon', Ans('solid')), ('droplet', Ans('liquid'))], cols=5, size='14mm'), marks=5),
    Q('Sort them.', Sort(['Solid', 'Liquid', 'Gas'], [('ice', 'Solid'), ('brick', 'Solid'), ('juice', 'Liquid'), ('oil', 'Liquid'), ('steam', 'Gas'), ('air', 'Gas')]), marks=6),
    Q('Fill in the gaps.', Blanks('Ice [melts] into water when it is warm. Water [freezes] into ice in a freezer. Boiling water turns into [steam].', extra=['sand']), marks=3),
])

think = Sheet('think', 'What will happen?', level=2, goals=['Predict changes when heating and cooling.'], blocks=[
    Q('What happens to chocolate on a hot day? Can you change it back?', Lines(2, 'It melts. Yes: put it in the fridge and it becomes solid again.'), marks=2),
    Q('Rina puts a lid on a pot of boiling water. Later the lid is wet inside. Why?', Lines(2, 'Steam from the water touched the cold lid and turned back into water drops.'), marks=2),
    Q('Draw what happens to an ice cube left in the sun.', Row([Draw('28mm', 'start', 'an ice cube')], [Draw('28mm', 'after 1 hour', 'a puddle of water')]), marks=2),
])

investigate = Sheet('investigate', 'Where does ice melt fastest?', level=2, goals=['Do a fair test.', 'Time and record.'], blocks=[
    P('Class 2A put the same size ice cube in four places and timed how long each took to melt.'),
    Q('Draw a bar chart.', Table(['Place', 'in the sun', 'on a table', 'in the shade', 'in a cool box'], [['Minutes to melt', '10', '25', '30', '90']], center=True),
      Graph(['sun', 'table', 'shade', 'cool box'], [10, 25, 30, 90], 'Minutes to melt', 'Place', ymax=100, step=10, width=110, height=50), marks=3),
    Q('Where did the ice melt fastest? Why?', Lines(2, 'In the sun, because it was the warmest place.'), marks=2),
    Q('Why did they use the same size ice cubes?', Lines(1, 'To make the test fair.'), marks=1),
])

case = Sheet('case', 'The ice cream seller', level=3, goals=['Use melting and freezing in real life.'], blocks=[
    Links('Science', 'Food', 'Maths'),
    Case('On hot afternoons, an ice cream seller pushes his cart near the school. Inside the cart is a box with thick walls '
         'and lots of **ice**. The ice keeps the ice cream cold so it does not **melt**.',
         'In the morning he buys ice from the ice factory, where water is **frozen** in big machines. By evening most of the ice has melted into water.',
         source='A story about an ice cream cart.'),
    Q('Why does the seller need ice in his cart?', Lines(2, 'To keep the ice cream cold so it stays solid and does not melt.'), marks=2),
    Q('What happens to the ice by evening? Is it a solid or a liquid now?', Lines(1, 'It melts into water, a liquid.'), marks=2),
    Q('The seller sells 6 ice creams every hour for 4 hours. How many does he sell?', Lines(1, '6 × 4 = 24'), marks=1),
])

review = Sheet('review', 'Show what you know', level=3, goals=['Use matter words.'], blocks=[
    Q('Find the words.', WordSearch(['SOLID', 'LIQUID', 'GAS', 'MELT', 'ICE', 'STEAM'], size=8, seed=210)),
    Q('Which is a liquid?', MCQ(['a stone', 'milk', 'air'], 1), marks=1),
    Q('Water turns into ice when it…', MCQ(['melts', 'freezes', 'boils'], 1), marks=1),
    Q('**Challenge.** Is air matter? How do you know?', Lines(2, 'Yes. It takes up space: when you blow up a balloon, the air fills it.'), marks=2),
])

TOPIC = Topic(
    code='C1', strand='physical', title='States of Matter', short='Solids, liquids, gases',
    subtitle='Solids, liquids and gases, melting and freezing, and water turning to steam and back',
    outcomes=[
        'know that matter can be solid, liquid or gas.',
        'describe matter as everything that has mass and occupies volume.',
        'investigate how materials change when they are heated and cooled.',
        'know that melting is when a solid turns into a liquid, and that it is the reverse of freezing.',
        'observe how water turns into steam when it is heated, but on cooling the steam turns back into water.',
        'investigate how liquids and solids respond to changes in temperature — for example water changing to ice, or melting chocolate.',
    ],
    cambridge=['Stage 2 Unit 3 Changing materials (3.4–3.5 Heating and cooling)'],
    sheets=[learn, facts, think, investigate, case, review],
    selfcheck=['sort solids, liquids and gases', 'say that matter takes up space', 'explain melting and freezing', 'explain steam turning back to water', 'test where ice melts fastest'],
    cover_art=art.states_particles(),
)
