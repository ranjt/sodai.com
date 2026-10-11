from build import Sheet, Topic
from ws import (P, H, Box, Vocab, Fig, Cols, Row, Case, Links, Lines, Blanks, Match, TrueFalse, MCQ, Order, Table,
                Ans, Sort, Label, Draw, Graph, WordSearch, Q, Part, Bullets, Pics, KeyFig)
import art
import art4

learn = Sheet('learn', 'Storms, cyclones and our changing climate', level=1, goals=[
    'Explain how tropical depressions, storms and cyclones form.',
    'Describe how cyclones affect people, animals and plants, and how warnings keep people safe.',
    'Explain how human actions are changing weather patterns and the climate.',
], blocks=[
    P('Bangladesh sits at the top of the **Bay of Bengal**, a warm sea shaped like a funnel. Several times a year, huge '
      'spinning storms called **cyclones** form over this warm water. Some of them travel north towards our coast. Learning '
      'how they form, and tracking where they go, saves thousands of lives.', 'lead'),
    Cols(
        H('How a cyclone is born', 3),
        Bullets(['The Sun heats the sea. When the water is warmer than about **27 °C**, lots of water **evaporates**.',
                 'Warm, damp air **rises** quickly. As it rises it cools and the water vapour **condenses** into huge clouds.',
                 'More air rushes in to take its place, and because the Earth is spinning, the air begins to **spin** too.',
                 'If the sea stays warm, the storm keeps growing: from a **low pressure area** to a **depression**, a **cyclonic storm**, '
                 'and finally a **severe cyclone**.']),
        Table(['Name', 'Wind speed (about)'], [['depression', 'up to 61 km/h'], ['cyclonic storm', '62 – 88 km/h'],
                                               ['severe cyclonic storm', '89 – 117 km/h'], ['very severe cyclone', '118 km/h or more']]),
        Box('world', P('The same kind of storm has different names: a **cyclone** in the Bay of Bengal and Indian Ocean, a **hurricane** '
                       'in the Atlantic, and a **typhoon** in the Pacific.')),
        Fig(art4.cyclone_diagram(labels=art4.CYCLONE_PARTS), 'A cyclone seen from above.', width='96%'),
        H('Why are cyclones so dangerous?', 3),
        Bullets(['**Strong winds** blow down houses, trees and power lines.',
                 '**Heavy rain** causes floods and landslides.',
                 'A **storm surge**, a wall of sea water pushed onto the land by the wind, floods villages and makes the soil salty.']),
        Table(['Who is affected', 'How'], [['people', 'homes and crops destroyed, injuries, no clean water or electricity'],
                                           ['animals', 'cattle drown, wild animals lose their homes, fish ponds flood with salt water'],
                                           ['plants', 'trees uprooted, crops flattened, salty water kills rice and vegetables']]),
        H('Tracking a cyclone', 3),
        P('Weather satellites take pictures of the clouds every few minutes. Scientists mark the centre of the cyclone on a map '
          'using **latitude** (how far north) and **longitude** (how far east). Joining the points shows the cyclone\'s **track** '
          'and helps predict where it will reach land.'),
        H('Warning signals', 3),
        P('Bangladesh uses **warning signals numbered 1 to 11** for the sea ports. The higher the number, the greater the danger. '
          'Signals 8, 9 and 10 mean **great danger**: people in the coastal areas must go to a **cyclone shelter**. Volunteers spread '
          'the warning with megaphones, flags and mobile phone messages.'),
        Fig(art.cyclone_shelter(), 'A cyclone shelter stands on tall pillars above the storm surge.', width='80%'),
        H('Our changing climate', 3),
        P('Burning **coal, oil and gas** in cars, factories and power stations, and **cutting down forests**, add more **carbon '
          'dioxide** to the air. It acts like a blanket and traps heat, so the Earth is slowly getting **warmer**. Warmer seas can '
          'make cyclones **stronger** and wetter, melting ice makes the **sea level rise**, and rainfall becomes harder to predict.'),
        Pics([('factory smoke', 'factories'), ('car exhaust', 'vehicles'), ('axe', 'cutting forests'), ('sea level rise', 'rising sea')], cols=4, size='14mm', small=True),
        Box('bd', P('Bangladesh produces only a tiny share of the world\'s carbon dioxide, but it is one of the countries most at risk '
                    'from climate change, because so much of the land is low and close to the sea.')),
    ),
    Vocab([('cyclone', 'a huge spinning storm that forms over warm sea'), ('depression', 'an area of low pressure; a weak tropical storm'),
           ('storm surge', 'sea water pushed onto land by a cyclone'), ('track', 'the path a cyclone follows'),
           ('latitude', 'how far north or south a place is'), ('longitude', 'how far east or west a place is'),
           ('cyclone shelter', 'a strong building on pillars where people stay safe'), ('climate change', 'long-term change in the Earth\'s weather patterns')]),
])

facts = Sheet('facts', 'Cyclone facts', level=1, goals=['Order the stages of a cyclone.', 'Label a cyclone.', 'Recall safety facts.'], blocks=[
    Q('Number the steps in the order a cyclone forms.',
      Order(['The Sun heats the sea above 27 °C.', 'Water evaporates and warm, damp air rises.', 'Huge clouds form as the vapour condenses.',
             'Air rushes in and starts to spin.', 'The storm grows into a cyclone.']), marks=4),
    Q('Label the cyclone.', Label(art4.cyclone_diagram(), art4.CYCLONE_PARTS, width='76%', cols=2), marks=4),
    Q('Match the danger to what it does.',
      Match([('strong wind', 'blows down trees and houses'), ('heavy rain', 'causes floods and landslides'), ('storm surge', 'pushes salty sea water onto the land')]), marks=3),
    Q('True or false?', TrueFalse([
        ('Cyclones form over cold water.', False, 'They form over warm sea water.'),
        ('Signal 10 means great danger.', True),
        ('A cyclone shelter is built on tall pillars.', True),
        ('Burning fuels adds carbon dioxide to the air.', True)]), marks=4),
])

think = Sheet('think', 'Cyclones and climate', level=2, goals=['Explain cyclone formation.', 'Link human actions to climate change.'], blocks=[
    Q('Why do most cyclones in the Bay of Bengal happen in April–May and October–November, and not in January?',
      Lines(3, 'The sea is warmest before and after the monsoon; in January the sea is cooler, so there is not enough warm, damp air to feed a cyclone.'), marks=2),
    Q('Why do cyclones get weaker after they move over land?', Lines(2, 'Over land there is no warm sea water to give them heat and moisture, so they lose energy.'), marks=2),
    Q('Explain how salty water from a storm surge can cause problems for farmers for many months.',
      Lines(3, 'Salt stays in the soil and ponds; rice and vegetables cannot grow in salty soil and fish ponds are spoiled until rain washes the salt away.'), marks=2),
    Q('Complete the chain to show how human actions can make cyclones more dangerous.',
      Order(['people burn coal, oil and gas', 'more carbon dioxide in the air', 'heat is trapped and the Earth warms', 'the sea gets warmer', 'cyclones can become stronger']), marks=3),
    Q('Suggest two ways people in Bangladesh can **adapt** to stronger cyclones.', Lines(2, 'build more cyclone shelters and strong houses; plant mangroves along the coast; better warnings; raise embankments.'), marks=2),
])

investigate = Sheet('investigate', 'Track a cyclone', level=2, goals=['Plot points using latitude and longitude.', 'Describe a track.', 'Use data to make predictions.'], blocks=[
    P('These are the positions of the centre of Cyclone **Sidr** in November 2007 (rounded). Plot each point on the map, '
      'join them in order, and write the date next to each point.'),
    Table(['Date', '11 Nov', '12 Nov', '13 Nov', '14 Nov', '15 Nov', '16 Nov'],
          [['Latitude (°N)', '11.5', '13', '15', '17.5', '21', '24'], ['Longitude (°E)', '92', '90', '89.5', '89.3', '89.6', '90.8']], center=True),
    Q('Plot the track.', KeyFig(art4.cyclone_map(), art4.cyclone_map(art4.SIDR_TRACK, plotted=True), width='76%'), marks=4),
    Q('In which direction did Sidr mostly travel?', Lines(1, 'north (first north-west, then north, then north-east)'), marks=1),
    Q('On which date did it reach the coast of Bangladesh?', Lines(1, '15 November (evening)'), marks=1),
    Q('About how far north did it move each day between 13 and 15 November?', Lines(1, 'about 3 degrees of latitude a day (15 → 17.5 → 21)'), marks=1),
    Q('Why is it important to track a cyclone several days before it reaches land?', Lines(2, 'So warnings can be given early and people have time to move to shelters with their animals and belongings.'), marks=2),
])

case = Sheet('case', 'Ready for the storm: a family cyclone plan', level=3, goals=['Use real warnings.', 'Plan to keep people and animals safe.', 'Think about helping others.'], blocks=[
    Links('Science', 'Citizenship', 'Health', 'Maths'),
    Case('Rahima lives with her family in a village near the coast in Khulna. One evening the radio says the signal has '
         'been raised from **4** to **7**, and a cyclone may reach the coast in two days. Volunteers from the **Cyclone '
         'Preparedness Programme** walk through the village with megaphones and raise warning flags.',
         'Rahima\'s family must decide what to take to the shelter, what to do with their goats and chickens, and how to help '
         'their grandmother, who cannot walk far. Thanks to warnings, shelters and volunteers, the number of people who lose '
         'their lives in cyclones in Bangladesh has fallen enormously since 1970.',
         source='Based on the Cyclone Preparedness Programme (Bangladesh Red Crescent Society and the Government of Bangladesh).'),
    Q('Sort the items: which should Rahima\'s family take to the shelter?',
      Sort(['Take', 'Leave or protect at home'], [('drinking water', 'Take'), ('dry food', 'Take'), ('medicines', 'Take'), ('important papers in a plastic bag', 'Take'),
                                                  ('television', 'Leave or protect at home'), ('heavy furniture', 'Leave or protect at home')]), marks=6),
    Q('The signal goes up to **9**. What does that mean, and what should the family do?', Lines(2, 'Great danger: the cyclone is close; go to the cyclone shelter now.'), marks=2),
    Q('How could the family keep their goats and chickens safe?', Lines(2, 'Take them to the raised ground near the shelter (many shelters have space for animals) or untie them so they can escape.'), marks=1),
    Q('How can the family help Grandmother? Who else in the village might need help?', Lines(2, 'Leave early and carry her or use a van; ask volunteers to help. Others: babies, pregnant women, people who are ill or disabled.'), marks=2),
    Q('Design a "cyclone ready" checklist poster for families.', Draw('40mm', 'Cyclone ready!', 'e.g. listen to the radio; know the way to the shelter; pack water, food, medicine, torch, papers; help neighbours.'), marks=2),
])

review = Sheet('review', 'Show what you know', level=3, goals=['Use key vocabulary.', 'Answer test-style questions.'], blocks=[
    Q('Find the key words.', WordSearch(['CYCLONE', 'STORM', 'SURGE', 'SIGNAL', 'SHELTER', 'WARM', 'TRACK', 'EYE', 'WIND'], size=10, seed=408)),
    Q('Where do cyclones form?', MCQ(['over cold mountains', 'over warm seas', 'in deserts', 'over ice'], 1), marks=1),
    Q('The calm centre of a cyclone is called the…', MCQ(['eye', 'tail', 'surge', 'track'], 0), marks=1),
    Q('Draw a simple diagram to show how warm, damp air rising from the sea forms storm clouds.', Draw('40mm', 'Storm clouds forming', 'Sea with arrows of vapour rising, a tall cloud above, arrows showing air rushing in at the bottom.'), marks=3),
    Q('**Challenge.** Bangladesh is planting mangrove forests along the coast. Explain how this can protect people from cyclones and how it helps the climate.',
      Lines(4, 'Mangroves slow down the wind and the storm surge, so less water and wind reach villages. Trees also take in carbon dioxide, which helps slow climate change.'), marks=3),
])

TOPIC = Topic(
    code='B2', strand='earth', title='Storms, Cyclones and Climate Change', short='Cyclones and climate',
    subtitle='How tropical storms and cyclones form, their effects, tracking and warnings, and how people are changing the climate',
    outcomes=[
        'explain how weather systems such as tropical depressions, tropical storms and hurricanes are generated, and how their impacts affect humans, animals and plants.',
        'track a hurricane over time and connect this to the hurricane warning system for Bangladesh.',
        'identify how various human actions contribute to changing weather patterns and climate.',
    ],
    sheets=[learn, facts, think, investigate, case, review],
    selfcheck=['explain how a cyclone forms', 'describe the dangers of wind, rain and storm surge', 'plot a cyclone track on a map',
               'explain the warning signals', 'plan how a family can stay safe', 'explain how human actions change the climate'],
    cover_art=art4.cyclone_diagram(),
)
