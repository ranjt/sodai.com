from build import Sheet, Topic
from ws import (P, H, Box, Vocab, Fig, Cols, Row, Case, Links, Lines, Blanks, Match, TrueFalse, MCQ, Order, Table,
                Ans, Sort, Label, Draw, Graph, WordSearch, Q, Part, Bullets)
import art

learn = Sheet('learn', 'How the Earth\'s surface changes', level=1, goals=[
    'Explain weathering, erosion and deposition, and how water shapes the land.',
    'Use evidence to find patterns in natural processes.',
    'Describe how sudden events and extreme weather change the Earth\'s surface.',
], blocks=[
    P('Mountains look as if they will last for ever, and rivers seem to stay in the same place. But the Earth\'s surface is '
      'always changing. Some changes are so **slow** that we cannot see them in a lifetime; others happen **suddenly**, '
      'in minutes.', 'lead'),
    Fig(art.river_landscape(labels=art.RIVER_PARTS), 'From mountain to sea: weathering, erosion and deposition.'),
    Cols(
        H('Weathering: rocks break up', 3),
        P('Rain, ice, heat and cold, and plant roots slowly crack and break rocks into smaller pieces. Water that freezes in a '
          'crack expands and splits the rock. This breaking-up is called **weathering**.'),
        H('Erosion: rocks and soil move', 3),
        P('Moving water, wind and ice carry the broken pieces away. This is **erosion**. Rivers are the strongest force of '
          'erosion in Bangladesh. A fast river in flood can carry huge amounts of sand and silt and can wash away its banks.'),
        H('Deposition: new land forms', 3),
        P('When a river slows down, especially where it meets the sea, it drops the sand and silt it was carrying. This is '
          '**deposition**. Over thousands of years the deposits build up into flat, fertile land called a **delta**.'),
        Box('bd', P('Bangladesh sits on the **Bengal delta**, the largest river delta in the world, built by the Ganges, '
                    'Brahmaputra and Meghna rivers. New islands called **chars** appear in rivers, and old riverbanks are '
                    'eaten away. Every year riverbank erosion destroys homes and farmland, especially along the Jamuna and Padma.')),
        H('Patterns in nature', 3),
        P('Scientists look for **patterns**. In Bangladesh, rivers flood most in the **monsoon** (June to September). '
          'Cyclones in the Bay of Bengal are most common in **April–May** and **October–November**. Knowing these patterns '
          'helps people prepare.'),
        H('Sudden changes', 3),
        Bullets(['**Earthquakes:** the Earth\'s outer layer is broken into giant **tectonic plates** that move a few centimetres a year. When they suddenly slip, the ground shakes. Bangladesh lies close to where three plates meet.',
                 '**Landslides:** heavy rain soaks hillsides until soil and rock slide down, as has happened in the Chattogram hill districts.',
                 '**Cyclones:** powerful storms with very strong winds and a **storm surge**, a wall of sea water pushed onto the coast.',
                 '**Floods:** can drop new silt (good for farming) but also destroy crops, roads and homes.']),
        H('People change the land too', 3),
        P('Cutting down forests on hills makes landslides more likely because roots no longer hold the soil. Taking sand from '
          'rivers can make banks collapse. Planting trees and grass protects soil from erosion.'),
    ),
    Vocab([('weathering', 'rocks breaking into smaller pieces'), ('erosion', 'rock and soil being carried away by water, wind or ice'),
           ('deposition', 'dropping of sand and silt in a new place'), ('delta', 'flat land built up where a river meets the sea'),
           ('tectonic plate', 'a giant piece of the Earth\'s outer layer'), ('storm surge', 'sea water pushed onto land by a cyclone'),
           ('char', 'a new island formed from river deposits')]),
])

facts = Sheet('facts', 'Shaping the land', level=1, goals=['Label the processes.', 'Sort fast and slow changes.'], blocks=[
    Q('Label the diagram.', Label(art.river_landscape(), art.RIVER_PARTS, width='92%'), marks=4),
    Q('Match each word to its meaning.',
      Match([('weathering', 'rocks breaking into pieces'), ('erosion', 'rock and soil being carried away'),
             ('deposition', 'sand and silt being dropped'), ('delta', 'land built where a river meets the sea'),
             ('storm surge', 'sea water pushed onto the land by a cyclone')]), marks=5),
    Q('Sort the changes into slow and sudden.',
      Sort(['Slow changes', 'Sudden changes'],
           [('a delta growing', 'Slow changes'), ('rock weathering in a cliff', 'Slow changes'), ('a river valley getting deeper', 'Slow changes'),
            ('an earthquake', 'Sudden changes'), ('a landslide', 'Sudden changes'), ('a cyclone storm surge', 'Sudden changes')]), marks=6),
    Q('Fill in the gaps.',
      Blanks('Bangladesh is built on the world\'s largest [delta]. Rivers flood most during the [monsoon]. The Earth\'s '
             'outer layer is made of [tectonic] plates.', extra=['desert', 'winter']), marks=3),
])

think = Sheet('think', 'Causes and patterns', level=2, goals=['Explain causes of change.', 'Use a pattern to make predictions.'], blocks=[
    Q('Explain how a river can both **destroy** land and **make** new land.',
      Lines(3, 'Fast water erodes banks and carries soil away; where the river slows, it deposits the soil and builds chars and the delta.'), marks=2),
    Q('This table shows (example) the number of cyclones that formed in the Bay of Bengal in each season over 20 years.',
      Table(['Months', 'Jan–Mar', 'Apr–May', 'Jun–Sep', 'Oct–Dec'], [['Cyclones', '1', '12', '4', '19']], center=True),
      Graph(['Jan–Mar', 'Apr–May', 'Jun–Sep', 'Oct–Dec'], [1, 12, 4, 19], 'Number of cyclones', 'Months', ymax=20, step=2, width=130, height=62),
      Part('Draw the bar chart.'),
      Part('Describe the pattern.', Lines(2, 'Most cyclones form in April–May and October–December; very few form in January–March.')),
      Part('In which months should coastal people be most prepared?', Lines(1, 'April–May and October–November/December')), marks=5),
    Q('Why are landslides more likely on hills where the trees have been cut down?',
      Lines(3, 'Tree roots hold soil in place and leaves slow the rain; without them, heavy rain soaks and loosens the soil so it slides.'), marks=2),
    Q('Floods are dangerous, but farmers in Bangladesh also say "the flood brings gold". What do they mean?',
      Lines(2, 'Floods deposit fertile silt on the fields, which helps crops grow well afterwards.'), marks=2),
])

investigate = Sheet('investigate', 'Do plants stop soil erosion?', level=2, goals=['Use a model to investigate erosion.', 'Control variables.', 'Draw conclusions and evaluate the model.'], blocks=[
    Fig(art.erosion_trays(), 'Two trays at the same slope. The same amount of water is poured on each.', width='90%'),
    P('Class 5D tested two trays: one of bare soil and one where grass had grown for three weeks. They poured 500 ml of water '
      'from the same height onto each tray and weighed the soil washed into the cup. They repeated it three times.'),
    Q('Complete the table and find the averages.',
      Table(['Tray', 'Test 1 (g)', 'Test 2 (g)', 'Test 3 (g)', 'Average (g)'], [['bare soil', '62', '58', '60', Ans('60')],
                                                                             ['soil with grass', '9', '12', '9', Ans('10')]], center=True), marks=2),
    Q('List three things they kept the same.', Lines(2, 'slope (angle) of tray, amount of water, height it was poured from, type and amount of soil, size of tray'), marks=3),
    Q('Write a conclusion.', Lines(2, 'Grass greatly reduces erosion: about 6 times less soil washed away (10 g compared with 60 g).'), marks=2),
    Q('Explain your conclusion using what roots and leaves do.', Lines(2, 'Roots hold the soil together; leaves and stems slow down the water so it carries less soil.'), marks=2),
    Q('How is this model **like** a real hillside in the Chattogram hills, and how is it **different**?',
      Lines(3, 'Like: soil on a slope, rain washing it down, plants holding it. Different: much smaller, the real hill has rock, trees and much more rain over a long time.'), marks=2),
])

case = Sheet('case', 'Ready for the storm: saving lives from cyclones', level=3, goals=['Use data to show change over time.', 'Explain how science and people reduce risk.', 'Suggest further actions.'], blocks=[
    Links('Science', 'Geography', 'History', 'Maths', 'Citizenship'),
    Fig(art.cyclone_shelter(), 'A cyclone shelter on raised pillars, used as a school in normal times.', width='60%'),
    Case('In November **1970** the Bhola cyclone struck the coast of what is now Bangladesh. With almost no warning and few '
         'safe buildings, an estimated **300 000 to 500 000** people died, mostly drowned by the storm surge.',
         'After this disaster, the **Cyclone Preparedness Programme** began in 1972. Today tens of thousands of trained '
         'volunteers warn villages using radios, megaphones and flags, and help people reach thousands of raised **cyclone '
         'shelters**. Weather scientists use satellites to track storms days before they arrive.',
         'When Cyclone **Sidr** hit in 2007, about **3400** people died: still a terrible loss, but far fewer than in 1970. '
         'When Cyclone **Amphan** hit in 2020, more than 2 million people were moved to shelters and fewer than 30 people '
         'died in Bangladesh. The mangroves of the Sundarbans also helped to slow the wind and waves.',
         source='Sources: Bangladesh Cyclone Preparedness Programme; UN and Red Cross reports. Death tolls are estimates.'),
    Q('Complete the table.',
      Table(['Cyclone', 'Year', 'Approximate deaths in Bangladesh'], [['Bhola', '1970', Ans('300 000 – 500 000')], ['Sidr', '2007', Ans('about 3400')],
                                                                      ['Amphan', '2020', Ans('fewer than 30')]], center=True), marks=3),
    Q('Describe the pattern in the deaths over time and give **three** reasons for it.',
      Lines(4, 'Deaths fell hugely. Reasons: early warnings from satellites and forecasts; volunteers spreading warnings; cyclone shelters; evacuation of millions; mangrove protection; better roads and awareness.'), marks=4),
    Q('Why are cyclone shelters built on tall pillars with an open ground floor?',
      Lines(2, 'So the storm surge and flood water can flow underneath while people stay safe above the water.'), marks=2),
    Q('Some families do not want to leave their homes, animals and belongings. Suggest how volunteers could persuade them, '
      'and how shelters could be improved.',
      Lines(3, 'Explain the danger clearly; leave early; allow animals near shelters; separate safe spaces for women and girls; water, toilets and food in shelters; protect property.'), marks=2),
])

review = Sheet('review', 'Show what you know', level=3, goals=['Use key vocabulary.', 'Answer test-style questions.'], blocks=[
    Q('Find the key words.', WordSearch(['EROSION', 'DELTA', 'RIVER', 'FLOOD', 'CYCLONE', 'PLATE', 'SILT', 'CHAR', 'ROCK'], size=11, seed=71)),
    Q('Which process drops sand and silt to form a delta?', MCQ(['weathering', 'erosion', 'deposition', 'evaporation'], 2), marks=1),
    Q('What causes earthquakes?', MCQ(['heavy rain', 'tectonic plates suddenly moving', 'strong wind', 'the Moon'], 1), marks=1),
    Q('Sort these into helpful and harmful effects of a flood.',
      Sort(['Helpful', 'Harmful'], [('new silt for fields', 'Helpful'), ('fills ponds with fish', 'Helpful'), ('crops destroyed', 'Harmful'),
                                     ('homes washed away', 'Harmful'), ('dirty water spreads disease', 'Harmful')]), marks=5),
    Q('**Challenge.** Why do you think Bangladesh has more new land (chars) in some places and loses land in others, even in the same year?',
      Lines(3, 'Rivers erode banks where the water is fast (outside of bends) and deposit silt where it slows (inside of bends, near the sea).'), marks=2),
])

TOPIC = Topic(
    code='B3', strand='earth', title='Earth\'s Changing Surface', short='Changing surface',
    subtitle='Weathering, erosion and deposition, patterns in nature, and sudden changes such as floods, cyclones and earthquakes',
    outcomes=[
        'model how the Earth is shaped by water, erosion and other factors.',
        'use evidence to analyse and conclude that the Earth\'s natural processes have patterns.',
        'understand that sudden geological changes and extreme weather conditions affect the Earth\'s surface.',
    ],
    sheets=[learn, facts, think, investigate, case, review],
    selfcheck=['explain weathering, erosion and deposition', 'explain how rivers build the Bengal delta',
               'find a pattern in data about natural events', 'describe earthquakes, landslides, cyclones and floods',
               'use a model to show how plants reduce erosion', 'explain how Bangladesh prepares for cyclones'],
    cover_art=art.river_landscape(labels=art.RIVER_PARTS),
)
