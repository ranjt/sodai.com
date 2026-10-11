from build import Sheet, Topic
from ws import (P, H, Box, Vocab, Fig, Cols, Row, Case, Links, Lines, Blanks, Match, TrueFalse, MCQ, Order, Table,
                Ans, Sort, Label, Draw, Graph, WordSearch, Q, Part, Bullets, Pics, Wide)
import art
import art4

learn = Sheet('learn', 'Matter: solids, liquids, gases, elements and compounds', level=1, goals=[
    'Describe solids, liquids and gases and model their particles.',
    'Explain melting, freezing and boiling, and melting and boiling points.',
    'Tell the difference between pure substances and mixtures, and between elements and compounds.',
], blocks=[
    P('Your pencil, the water in your bottle, and the air you breathe are all made of **matter**. Matter is anything that '
      'has **mass** (it weighs something) and takes up **space**. Even air is matter: blow up a balloon and you can see it '
      'take up space!', 'lead'),
    Cols(
        H('Three states of matter', 3),
        P('Matter is made of particles far too small to see. How the particles are arranged gives each **state** its properties.'),
        Fig(art.states_particles(), 'Particles in a solid, a liquid and a gas.', span=True, width='82%'),
        Wide(Table(['State', 'Particles', 'Properties', 'Examples'], [
            ['**solid**', 'packed tightly in rows; only vibrate', 'keeps its shape; cannot be poured or squashed', 'ice, wood, stone, a spoon'],
            ['**liquid**', 'close together but can slide past each other', 'flows; takes the shape of its container; keeps its volume', 'water, milk, oil, juice'],
            ['**gas**', 'far apart, moving fast in all directions', 'spreads out to fill any space; can be squashed', 'air, steam, the gas in a cylinder']])),
        Box('tip', P('Some things are tricky. Sand pours, but each grain is a tiny **solid**. Toothpaste flows when squeezed, but it is a mixture.')),
        H('Changing state', 3),
        Bullets(['**Melting**: a solid becomes a liquid when it is heated (ice → water).',
                 '**Freezing**: a liquid becomes a solid when it is cooled (water → ice).',
                 '**Boiling** and **evaporating**: a liquid becomes a gas (water → water vapour).',
                 '**Condensing**: a gas becomes a liquid when it is cooled (steam → water drops on a lid).']),
        P('The temperature at which a solid melts is its **melting point**. The temperature at which a liquid boils is its '
          '**boiling point**. Different materials have different melting points:'),
        Table(['Material', 'Melting point (about)'], [['ice', '0 °C'], ['butter', '32 °C'], ['chocolate', '34 °C'], ['candle wax', '60 °C'], ['iron', '1538 °C']], center=True),
        P('Pure water **freezes at 0 °C** and **boils at 100 °C**. While ice is melting, its temperature stays at 0 °C until all the ice has melted.'),
        H('Pure substances and mixtures', 3),
        P('A **pure substance** contains only one kind of material: pure water, salt, sugar, pure gold. A **mixture** contains two '
          'or more substances mixed together: air (many gases), sea water (water and salt), soil, cha with milk and sugar.'),
        H('Elements and compounds', 3),
        P('Pure substances can be **elements** or **compounds**. An **element** is made of only **one kind of atom**: oxygen, iron, '
          'gold, carbon. There are about 118 elements. A **compound** is made of **two or more kinds of atom joined together**: '
          'water (hydrogen and oxygen), salt (sodium and chlorine), carbon dioxide.'),
        Fig(art4.element_compound(), 'An element, a compound and a mixture.', span=True, width='76%'),
        H('Using them every day', 3),
        Bullets(['Hospitals use pure **saline** (salt and pure water) in drips.',
                 'Gold jewellery is usually a **mixture** of gold with a little copper, which makes it harder.',
                 '**Oral rehydration salt (ORS)** is a carefully measured mixture that helps children with diarrhoea.',
                 'We breathe **air**, a mixture. Our bodies use the **oxygen** in it.']),
        Box('bd', P('**Oral rehydration solution** was developed and tested in Bangladesh and India in the 1960s and 70s, including at '
                    'icddr,b in Dhaka. It has saved millions of children\'s lives around the world.')),
    ),
    Vocab([('matter', 'anything that has mass and takes up space'), ('solid', 'keeps its shape'), ('liquid', 'flows and takes the shape of its container'),
           ('gas', 'spreads out to fill any space'), ('melting point', 'the temperature at which a solid melts'), ('boiling point', 'the temperature at which a liquid boils'),
           ('element', 'a substance made of only one kind of atom'), ('compound', 'two or more kinds of atom joined together'), ('mixture', 'substances mixed but not joined')]),
])

facts = Sheet('facts', 'States and substances', level=1, goals=['Sort solids, liquids and gases.', 'Name changes of state.', 'Sort elements, compounds and mixtures.'], blocks=[
    Q('Sort the materials.',
      Sort(['Solid', 'Liquid', 'Gas'], [('stone', 'Solid'), ('ice', 'Solid'), ('rice grain', 'Solid'), ('milk', 'Liquid'), ('mustard oil', 'Liquid'), ('rain water', 'Liquid'),
                                        ('steam', 'Gas'), ('air in a balloon', 'Gas'), ('cooking gas', 'Gas')]), marks=9),
    Q('Name the change of state.',
      Table(['What happens', 'Change of state'], [['ice cream drips on a hot day', Ans('melting')], ['water is put in a freezer and becomes ice', Ans('freezing')],
                                                  ['a puddle disappears in the sun', Ans('evaporating')], ['drops form on a cold glass of water', Ans('condensing')]], widths=['62%', '38%']), marks=4),
    Q('Draw the particles in each state.', Row([Draw('28mm', 'solid', 'neat rows, touching')], [Draw('28mm', 'liquid', 'touching but jumbled')], [Draw('28mm', 'gas', 'few, far apart')]), marks=3),
    Q('Sort the substances.',
      Sort(['Element', 'Compound', 'Mixture'], [('iron', 'Element'), ('oxygen', 'Element'), ('gold', 'Element'), ('water', 'Compound'), ('salt', 'Compound'),
                                                ('carbon dioxide', 'Compound'), ('air', 'Mixture'), ('sea water', 'Mixture'), ('soil', 'Mixture')]), marks=9),
])

think = Sheet('think', 'Explaining matter', level=2, goals=['Explain properties using particles.', 'Use melting points.'], blocks=[
    Q('Use the particle model to explain why:',
      Part('a liquid takes the shape of its container.', Lines(2, 'Its particles can slide past each other, so the liquid flows to fill the bottom of the container.')),
      Part('you can squash a gas but not a solid.', Lines(2, 'Gas particles are far apart with lots of space between them; solid particles are already packed tightly.')), marks=4),
    Q('Chocolate melts at 34 °C and candle wax melts at 60 °C. On a 38 °C summer day, which one melts in your bag? Why?',
      Lines(2, 'The chocolate, because 38 °C is above its melting point, but below the melting point of wax.'), marks=2),
    Q('Rumi says, "Salt is an element because it is pure." Is she right? Explain.', Lines(2, 'No. Salt is pure, but it is a compound: two kinds of atom (sodium and chlorine) joined together.'), marks=2),
    Q('Why is it useful that iron has a very high melting point?', Lines(2, 'Iron pots and stoves do not melt when they are heated on a fire.'), marks=2),
])

investigate = Sheet('investigate', 'The melting race', level=2, goals=['Plan a fair test.', 'Time and record results.', 'Link results to melting points.'], blocks=[
    P('Class 4B put a 1 cm cube of four solids on four identical metal lids in the same sunny place, and timed how long each took to melt completely.'),
    Q('Complete the plan.',
      Table(None, [['Change', Ans('the type of solid')], ['Measure', Ans('time to melt (minutes)')], ['Keep the same', Ans('size of the cube, type of lid, place in the sun, start time')],
                   ['Prediction', Ans('e.g. ice will melt first because it has the lowest melting point')]], widths=['26%', '74%']), marks=4),
    Q('Draw a bar chart of the results.',
      Table(['Solid', 'ice', 'butter', 'chocolate', 'candle wax'], [['Time to melt (minutes)', '6', '14', '18', 'did not melt']], center=True),
      Graph(['ice', 'butter', 'chocolate'], [6, 14, 18], 'Time to melt (minutes)', 'Solid', ymax=20, step=2, width=100, height=50), marks=3),
    Q('Why did the candle wax not melt?', Lines(2, 'The lid did not get as hot as 60 °C, the melting point of wax.'), marks=1),
    Q('Describe the pattern between melting point and time to melt.', Lines(2, 'The lower the melting point, the faster the solid melted.'), marks=2),
])

case = Sheet('case', 'Ice for the fishing boats', level=3, goals=['Apply changes of state to a real job.', 'Use numbers.', 'Think about energy and waste.'], blocks=[
    Links('Science', 'Economics', 'Maths', 'Health'),
    Case('Before a fishing trawler leaves Chattogram or Cox\'s Bazar for the Bay of Bengal, workers load it with tonnes of '
         '**crushed ice**. A trip can last a week or more. The fishers pack each catch of hilsa and other fish in ice so it stays '
         'fresh until they return.',
         'The ice is made in **ice factories** near the harbour. Machines cool water below **0 °C** until it **freezes** into big '
         'blocks, which are crushed before loading. As the ice slowly **melts**, it takes heat from the fish and keeps them cold. '
         'Without ice, fish start to go bad in a few hours in the heat.',
         source='Based on information about fish preservation in Bangladesh\'s fishing industry. Numbers below are examples.'),
    Q('Which changes of state happen in the story?',
      Table(['Where', 'Change of state'], [['in the ice factory', Ans('freezing (liquid → solid)')], ['in the boat\'s fish hold', Ans('melting (solid → liquid)')]], widths=['50%', '50%']), marks=2),
    Q('Why is **crushed** ice better than one big block for keeping fish cold?', Lines(2, 'Small pieces fit closely around every fish and touch more of its surface, so the fish cool faster.'), marks=2),
    Q('**Maths.** A boat needs 2 kg of ice for every 1 kg of fish. It hopes to catch 500 kg. How much ice does it need?', Lines(1, '500 × 2 = 1000 kg (1 tonne)'), marks=2),
    Q('Making ice uses a lot of electricity. Suggest one way to waste less ice.', Lines(2, 'Use insulated boxes in the boat (like a cool box), keep the hold closed and in the shade.'), marks=2),
    Q('Why is it important for people\'s health that fish are kept cold?', Lines(2, 'Germs grow fast in warm fish and can make people ill; cold slows them down.'), marks=1),
])

review = Sheet('review', 'Show what you know', level=3, goals=['Use key vocabulary.', 'Answer test-style questions.'], blocks=[
    Q('Find the key words.', WordSearch(['SOLID', 'LIQUID', 'GAS', 'MELT', 'FREEZE', 'BOIL', 'ELEMENT', 'MIXTURE', 'MATTER'], size=10, seed=411)),
    Q('At what temperature does pure water boil?', MCQ(['0 °C', '50 °C', '100 °C', '34 °C'], 2), marks=1),
    Q('Which is a compound?', MCQ(['oxygen', 'water', 'gold', 'air'], 1), marks=1),
    Q('Draw a diagram to show what happens to the particles when ice melts.', Draw('34mm', 'Ice melting', 'Particles in neat rows (solid) → particles touching but jumbled (liquid), with an arrow labelled "heat".'), marks=3),
    Q('**Challenge.** A glass of iced water gets wet on the **outside**. Where does the water come from? Explain using states of matter.',
      Lines(3, 'Water vapour (a gas) in the air touches the cold glass, cools and condenses into liquid water drops.'), marks=2),
])

TOPIC = Topic(
    code='C1', strand='physical', title='Matter: States, Elements and Compounds', short='Matter',
    subtitle='Solids, liquids and gases, changes of state, melting and boiling points, pure substances, elements and compounds',
    outcomes=[
        'define matter, and describe and model the differences in the arrangement of molecules of matter in its three states.',
        'understand that solids, liquids and gases behave in different ways and have observable properties that help to classify them.',
        'differentiate between pure substances and mixtures, and state examples of each.',
        'differentiate between elements and compounds, and state examples of each.',
        'give examples of, and explain, how pure substances and mixtures are used in everyday life by humans.',
    ],
    cambridge=['Unit 3 Solids, liquids and gases (3.1–3.6)'],
    sheets=[learn, facts, think, investigate, case, review],
    selfcheck=['describe solids, liquids and gases using particles', 'name changes of state', 'use melting and boiling points',
               'tell pure substances from mixtures', 'tell elements from compounds', 'explain how ice keeps fish fresh'],
    cover_art=art.states_particles(),
)
