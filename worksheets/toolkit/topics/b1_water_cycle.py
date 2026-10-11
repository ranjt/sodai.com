from build import Sheet, Topic
from ws import (P, H, Box, Vocab, Fig, Cols, Row, Case, Links, Lines, Blanks, Match, TrueFalse, MCQ, Order, Table,
                Ans, Sort, Label, Draw, Graph, WordSearch, Q, Part, Bullets)
import art

learn = Sheet('learn', 'Water for life and the water cycle', level=1, goals=[
    'Describe the water cycle and the change of state at each step.',
    'Explain why the water cycle matters to plants, animals and people.',
    'Discuss how people affect fresh water, and how desalination works.',
], blocks=[
    P('Bangladesh is a land of water: three great rivers (the Padma, the Jamuna and the Meghna), hundreds of smaller '
      'rivers, haors, beels and ponds, and heavy monsoon rain. Yet clean, safe drinking water is still hard to find in '
      'many places. Where does water come from, and where does it go?', 'lead'),
    Fig(art.water_cycle(labels=art.WATER_CYCLE), 'The water cycle: the same water goes round and round.'),
    Cols(
        H('Water changes state', 3),
        P('Water can be a **solid** (ice), a **liquid** (water) or a **gas** (water vapour). Heating makes ice **melt** at '
          '0 °C and makes water **evaporate**, or **boil** at 100 °C. Cooling makes water vapour **condense** into droplets, '
          'and makes water **freeze** at 0 °C.'),
        H('The water cycle', 3),
        Bullets(['**Evaporation:** the Sun heats water in seas, rivers and ponds. Liquid water turns into water vapour (a gas) and rises.',
                 '**Transpiration:** plants take up water through their roots and lose water vapour from their leaves.',
                 '**Condensation:** high in the sky the air is cooler. Water vapour cools and condenses into tiny droplets that make **clouds**.',
                 '**Precipitation:** droplets join together and become heavy, then fall as rain (or hail or snow).',
                 '**Collection:** rain runs over the ground into rivers and the sea, or soaks into the ground as **groundwater**. Then the cycle starts again.']),
        P('The Sun\'s energy drives the cycle. The water on Earth today is the same water that dinosaurs drank!'),
        H('Why the water cycle matters', 3),
        P('The water cycle brings **fresh water** to the land. Plants need it to grow, animals need it to drink, and people '
          'need it for drinking, cooking, washing, farming and factories. Seas are salty, but evaporation leaves the salt '
          'behind, so rain is fresh. Ice in glaciers and snow on mountains store fresh water and release it slowly.'),
        Box('fact', P('About 97 out of every 100 litres of water on Earth is salty sea water. Most of the rest is frozen. Less '
                      'than 1 litre in every 100 is fresh water that we can easily use.')),
        H('Fresh water in Bangladesh', 3),
        P('Most of the year\'s rain falls in the **monsoon** (June to September). Many people drink **groundwater** from '
          'tube-wells. Human activities affect both the **quantity** and **quality** of water:'),
        Bullets(['Pumping too much groundwater in Dhaka makes the water level under the city fall every year.',
                 'Factories, tanneries and sewage have polluted rivers such as the Buriganga.',
                 'In some areas, tube-well water contains **arsenic**, a poison that comes naturally from rocks underground.',
                 'On the coast, rising seas and storm surges push **salt** into ponds, rivers and soil.']),
        H('Desalination: making salt water drinkable', 3),
        P('**Desalination** removes salt from sea water. One way copies the water cycle: heat the salt water so that water '
          'evaporates, then cool the vapour so that it condenses as pure water. The salt is left behind. Another way, '
          'called **reverse osmosis**, pushes water through a very fine filter that stops the salt.'),
        H('Protecting water', 3),
        P('We can collect rainwater from roofs, fix dripping taps, never throw rubbish into rivers, and use less water at home. '
          'Some coastal villages use **pond sand filters** and rainwater tanks.'),
    ),
    Vocab([('evaporation', 'liquid changing into a gas'), ('condensation', 'gas changing into a liquid'),
           ('precipitation', 'water falling from clouds as rain, hail or snow'), ('transpiration', 'plants losing water vapour from their leaves'),
           ('groundwater', 'water stored in soil and rocks underground'), ('desalination', 'removing salt from sea water'),
           ('water vapour', 'water in the form of a gas')]),
])

facts = Sheet('facts', 'The water cycle', level=1, goals=['Label the water cycle.', 'Name the changes of state.'], blocks=[
    Q('Label the water cycle.', Label(art.water_cycle(), art.WATER_CYCLE, width='96%', cols=3), marks=5),
    Q('Complete the table.',
      Table(['Change', 'From', 'To', 'Caused by'], [
          ['evaporation', Ans('liquid'), Ans('gas'), Ans('heating')], ['condensation', Ans('gas'), Ans('liquid'), Ans('cooling')],
          ['melting', Ans('solid'), Ans('liquid'), Ans('heating')], ['freezing', Ans('liquid'), Ans('solid'), Ans('cooling')]], center=True), marks=8),
    Q('Fill in the gaps.',
      Blanks('Water boils at [100] °C and ice melts at [0] °C. Water vapour cools and [condenses] to make clouds. '
             'The [Sun] gives the energy that drives the water cycle.', extra=['50', 'wind']), marks=4),
    Q('True or false?', TrueFalse([
        ('Rain water is salty because it comes from the sea.', False, 'Rain is fresh; the salt stays behind when sea water evaporates.'),
        ('Plants put water vapour into the air.', True), ('Most of Earth\'s water is fresh water.', False, 'About 97% is salty sea water.')]), marks=3),
])

think = Sheet('think', 'Explaining the cycle', level=2, goals=['Order and explain the water cycle.', 'Link the cycle to everyday events.'], blocks=[
    Q('Number the stages to follow one drop of water from the Bay of Bengal back to the sea.',
      Order(['The Sun heats the sea and the water evaporates.', 'Water vapour rises and cools.', 'It condenses into droplets and forms clouds.',
             'Droplets join and fall as monsoon rain.', 'Rain runs into a river.', 'The river flows back into the sea.'], seed=21), marks=3),
    Q('Explain each observation using the words in brackets.',
      Part('A cold glass of water gets wet on the outside. (*water vapour, condenses*)', Lines(2, 'Water vapour in the air touches the cold glass, cools and condenses into liquid droplets.')),
      Part('Puddles disappear on a sunny day. (*evaporates*)', Lines(2, 'The Sun heats the water and it evaporates into water vapour in the air.')),
      Part('Clothes dry faster on a windy day.', Lines(2, 'Wind carries away the water vapour, so more water can evaporate quickly.')), marks=6),
    Q('Why is the water cycle important for farmers in Bangladesh?',
      Lines(3, 'It brings fresh rain for crops like rice; it fills rivers and groundwater used for irrigation and drinking.'), marks=2),
    Q('How does pumping too much groundwater affect the water cycle in a city? Suggest one solution.',
      Lines(3, 'Water is taken out faster than rain can soak back in, so the water level falls. Solutions: rainwater harvesting, using river water, leaving green ground for rain to soak in.'), marks=2),
])

investigate = Sheet('investigate', 'Make a solar still', level=2, goals=['Build a model that uses evaporation and condensation.',
                                                                          'Test a variable fairly.', 'Use results to explain desalination.'], blocks=[
    Row([Fig(art.solar_still(labels=art.SOLAR_STILL))], [Box('need', P('a large bowl, a cup, salty water, clear plastic sheet, a small stone, sticky tape, a measuring cylinder')),
                                                         Box('safety', P('Do not taste anything in a science lab. Test for salt by letting one drop dry on a dark tile.'))],
        widths=[1.4, 1]),
    Q('How does the solar still work? Use the words *evaporates*, *condenses* and *salt*.',
      Lines(3, 'The Sun heats the salty water so water evaporates; the vapour touches the cool plastic and condenses into droplets; they run to the low point and drip into the cup. The salt is left behind in the bowl.'), marks=3),
    Q('Class 5B set up two identical stills, one in sunshine and one in shade, and measured the clean water every hour.',
      Table(['Time (hours)', '1', '2', '3', '4'], [['In the sun (ml)', '4', '9', '15', '20'], ['In the shade (ml)', '1', '2', '4', '5']], center=True),
      Graph(['1', '2', '3', '4'], [[4, 9, 15, 20], [1, 2, 4, 5]], 'Clean water collected (ml)', 'Time (hours)', ymax=24, step=4, kind='line',
            series_names=['in the sun', 'in the shade'], width=140, height=66), marks=4),
    Q('What is the variable they changed? Name two variables they kept the same.',
      Lines(2, 'Changed: sunshine or shade (amount of heat). Same: amount and saltiness of water, size of bowl and cup, type of plastic, time.'), marks=2),
    Q('Write a conclusion and explain it.',
      Lines(3, 'The still in the sun made much more clean water: more heat makes water evaporate faster, so more condenses on the plastic.'), marks=2),
    Q('Was the water in the cup salty? How could you check without tasting it?',
      Lines(2, 'No: the salt does not evaporate. Let a drop dry on a dark tile; no white salt crystals are left.'), marks=1),
])

case = Sheet('case', 'Too much water, not enough to drink', level=3, goals=['Explain a real water problem using science.',
                                                                              'Compare solutions using evidence.', 'Plan actions to protect water.'], blocks=[
    Links('Science', 'Geography', 'Maths', 'Health', 'Climate change'),
    Case('In Satkhira and Khulna, in south-west Bangladesh, people are surrounded by water: rivers, shrimp ponds and the sea. '
         'But most of it is **too salty to drink**. Storm surges from cyclones such as Aila (2009) flooded ponds with sea '
         'water, and rising sea levels push salt further inland each year.',
         'Many women and girls walk several kilometres every day to fetch drinking water. Some families collect '
         '**rainwater** from their roofs in big tanks during the monsoon. Villages also use **pond sand filters**, which '
         'clean water from a protected pond, and small **desalination plants** that use reverse osmosis.',
         'Drinking salty water for a long time is bad for health, especially for pregnant women, whose blood pressure can rise.',
         source='Based on reports about coastal salinity in Bangladesh (WHO, UNICEF, Bangladesh research studies).'),
    Q('Why is there a water problem in a place that has so much water?',
      Lines(2, 'Most of the water is salty (sea water, salty rivers and ponds); fresh drinking water is scarce.'), marks=2),
    Q('A family of 5 needs about 3 litres of drinking water per person each day.',
      Part('How much drinking water does the family need in one day?', Lines(1, '5 × 3 = 15 litres')),
      Part('How much in 30 days?', Lines(1, '15 × 30 = 450 litres')),
      Part('Their rainwater tank holds 2000 litres. For about how many days will a full tank last?', Lines(1, '2000 ÷ 15 ≈ 133 days (about 4 months)')), marks=3),
    Q('Compare three solutions.',
      Table(['Solution', 'One advantage', 'One disadvantage'], [
          ['rainwater tank', Ans('free, clean water; uses the monsoon rain'), Ans('runs out in the dry season; tank costs money')],
          ['pond sand filter', Ans('shares clean water with many families'), Ans('the pond must be protected from salt and dirt')],
          ['desalination plant', Ans('makes fresh water from salty water all year'), Ans('expensive; needs electricity and repair')]],
            widths=['26%', '37%', '37%']), marks=6),
    Q('Fetching water often stops girls from going to school. Why is safe water a fairness issue too?',
      Lines(3, 'Girls lose learning time and future chances; everyone has a right to safe water, so a nearby supply gives girls the same chance to learn.'), marks=2),
])

review = Sheet('review', 'Show what you know', level=3, goals=['Use key vocabulary.', 'Answer test-style questions.'], blocks=[
    Q('Find the key words.', WordSearch(['EVAPORATE', 'CONDENSE', 'CLOUD', 'RAIN', 'VAPOUR', 'RIVER', 'MONSOON', 'SALT', 'SUN'], size=11, seed=51)),
    Q('Which process forms clouds?', MCQ(['evaporation', 'condensation', 'melting', 'freezing'], 1), marks=1),
    Q('What drives the water cycle?', MCQ(['the Moon', 'the wind', 'energy from the Sun', 'the sea'], 2), marks=1),
    Q('Draw your own water cycle diagram. Label four processes and show the direction with arrows.',
      Draw('55mm', 'My water cycle', 'Sea → evaporation (arrows up) → condensation (clouds) → precipitation (rain) → collection (river to sea); transpiration from plants.'), marks=4),
    Q('**Challenge.** Explain why the water cycle is called a *cycle* and why the total amount of water on Earth stays the same.',
      Lines(3, 'The water goes round and round (evaporate → condense → fall → collect → evaporate); it only changes state and place, so none is made or destroyed.'), marks=2),
])

TOPIC = Topic(
    code='B1', strand='earth', title='Water for Life and the Water Cycle', short='Water cycle',
    subtitle='Changes of state, the water cycle, fresh water in Bangladesh and desalination',
    outcomes=[
        'demonstrate that water changes from one state to another, and explain how the change in state is brought about.',
        'describe the water cycle and explain the changes of state water undergoes at each step of the cycle.',
        'explain the importance of the water cycle to plant, animal and human life.',
        'give examples of how water in its different forms sustains life.',
        'discuss how different human activities impact the quantity and quality of fresh water in Bangladesh and other parts of the world.',
        'explain how desalination converts salt water into drinking water.',
        'plan and implement activities to help conserve or protect water sources in Bangladesh.',
    ],
    cambridge=['Unit 3 States of matter: 3.5 Condensation, 3.6 The water cycle'],
    sheets=[learn, facts, think, investigate, case, review],
    selfcheck=['describe each step of the water cycle and the change of state', 'explain dew, drying clothes and clouds',
               'explain why the water cycle matters for life', 'make a solar still and explain desalination',
               'explain how people affect fresh water in Bangladesh', 'compare ways to provide safe drinking water'],
    cover_art=art.water_cycle(labels=art.WATER_CYCLE),
)
