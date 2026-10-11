from build import Sheet, Topic
from ws import (P, H, Box, Vocab, Fig, Cols, Row, Case, Links, Lines, Blanks, Match, TrueFalse, MCQ, Order, Table,
                Ans, Sort, Label, Draw, Graph, WordSearch, Q, Part, Bullets)
import art

learn = Sheet('learn', 'Solids, liquids and gases: changing state', level=1, goals=[
    'Explain evaporation, condensation, boiling, melting and freezing.',
    'Recall that water boils at 100 °C and ice melts at 0 °C.',
    'Explain that adding or removing heat causes changes of state.',
], blocks=[
    P('Wet clothes dry on the roof. A glass of cold water "sweats" on a hot day. Ice in a glass of lemon sherbet melts. A '
      'kettle whistles as water boils. All of these are **changes of state**, and every one is caused by **heating** or '
      '**cooling**.', 'lead'),
    Fig(art.states_particles(), 'The particles in a solid, a liquid and a gas.', width='90%'),
    Cols(
        H('Three states of matter', 3),
        P('In a **solid**, particles are packed tightly in rows and can only vibrate, so a solid keeps its shape. In a '
          '**liquid**, particles are close together but can move past each other, so a liquid flows and takes the shape of '
          'its container. In a **gas**, particles are far apart and move quickly in all directions, so a gas spreads out to '
          'fill any space.'),
        H('Evaporation', 3),
        P('**Evaporation** is when a liquid turns into a gas. It happens at the **surface** of a liquid, at any temperature. '
          'Water evaporates faster when it is **warmer**, when it is **windy**, and when it has a **larger surface area**. '
          'That is why clothes dry fastest when they are spread out on a hot, windy day.'),
        H('Condensation', 3),
        P('**Condensation** is the **reverse** of evaporation: a gas turns into a liquid when it **cools**. Air always contains '
          'some invisible **water vapour**. When it touches a cold surface, such as a cold glass, a window in winter or grass '
          'at night, it condenses into drops. This is how **dew** forms on winter mornings.'),
        H('Boiling', 3),
        P('When water is heated strongly it **boils** at **100 °C**. Bubbles of water vapour form all through the liquid, not '
          'just at the surface. While it is boiling, the temperature stays at 100 °C: the heat energy is being used to turn '
          'liquid into gas.'),
        H('Melting and freezing', 3),
        P('Ice **melts** at **0 °C**, and water **freezes** at 0 °C. Different materials melt at different temperatures: '
          'chocolate melts at about 30–35 °C (in your hand!), candle wax at about 60 °C, and iron at over 1500 °C.'),
        Fig(art.heating_setup(), 'Heating ice and recording the temperature.', width='70%'),
        H('Evaporating a solution', 3),
        P('If you dissolve salt in water and then let the water **evaporate**, the salt is left behind as crystals. The salt '
          'does not evaporate. This is how salt is made from sea water.'),
        Box('history', P('The **Celsius** scale was invented in 1742 by the Swedish astronomer Anders Celsius. Surprisingly, he '
                         'first set 0 for boiling water and 100 for freezing water! It was turned the other way round after he '
                         'died. In the USA people still often use the **Fahrenheit** scale, on which water freezes at 32 °F and boils at 212 °F.')),
        Box('fact', P('On top of Mount Everest water boils at only about 70 °C, because the air pressure is much lower. '
                      'It is hard to cook rice up there!')),
    ),
    Vocab([('evaporation', 'liquid → gas, at the surface, at any temperature'), ('condensation', 'gas → liquid when it cools'),
           ('boiling', 'liquid → gas all through the liquid, at the boiling point'), ('melting', 'solid → liquid'),
           ('freezing', 'liquid → solid'), ('water vapour', 'water as a gas (invisible)'), ('melting point', 'the temperature at which a solid melts'),
           ('boiling point', 'the temperature at which a liquid boils')]),
])

facts = Sheet('facts', 'Changes of state', level=1, goals=['Name the changes of state.', 'Recall key temperatures.'], blocks=[
    Q('Label the changes of state on the arrows.',
      Fig(art.states_particles(labels=True)),
      Table(['Change', 'Name'], [['solid → liquid', Ans('melting')], ['liquid → solid', Ans('freezing')],
                                 ['liquid → gas', Ans('evaporating / boiling')], ['gas → liquid', Ans('condensing')]], widths=['50%', '50%']), marks=4),
    Q('Fill in the gaps.',
      Blanks('Water boils at [100] °C. Ice melts at [0] °C. When water vapour touches a cold window it [condenses]. '
             'Puddles dry up because the water [evaporates]. When salty water evaporates, the [salt] is left behind.',
             extra=['50', 'melts']), marks=5),
    Q('Match each everyday event to the change of state.',
      Match([('wet clothes drying', 'evaporation'), ('dew on the grass in the morning', 'condensation'), ('ice cream dripping', 'melting'),
             ('a kettle making steam', 'boiling'), ('water turning into ice cubes in a freezer', 'freezing')]), marks=5),
    Q('True or false?', TrueFalse([
        ('Evaporation only happens at 100 °C.', False, 'Evaporation happens at any temperature.'),
        ('Condensation is the reverse of evaporation.', True),
        ('The temperature of boiling water keeps rising while it boils.', False, 'It stays at 100 °C while it boils.')]), marks=3),
])

think = Sheet('think', 'Explaining changes of state', level=2, goals=['Explain changes using heating and cooling.', 'Interpret a heating graph.'], blocks=[
    Q('Explain each observation.',
      Part('A cold bottle of water from the fridge becomes wet on the outside.', Lines(2, 'Water vapour in the air touches the cold bottle, cools and condenses into droplets.')),
      Part('Clothes dry faster when they are spread out than when they are folded.', Lines(2, 'A larger surface area means more water can evaporate at the same time.')),
      Part('In winter, people\'s breath looks like a little cloud.', Lines(2, 'Warm water vapour in the breath cools quickly in the cold air and condenses into tiny droplets.')), marks=6),
    Q('Class 5A heated ice and recorded the temperature every minute.',
      Table(['Time (min)', '0', '2', '4', '6', '8', '10', '12', '14'], [['Temp (°C)', '−10', '0', '0', '25', '58', '90', '100', '100']], center=True),
      Graph(['0', '2', '4', '6', '8', '10', '12', '14'], [-10, 0, 0, 25, 58, 90, 100, 100],
            'Temperature (°C)', 'Time (minutes)', ymin=-10, ymax=110, step=10, kind='line', width=150, height=66),
      Part('Plot the line graph.'),
      Part('Why did the temperature stay at 0 °C between 2 and 4 minutes?', Lines(2, 'The ice was melting: the heat was being used to change solid to liquid.')),
      Part('What was happening at 12–14 minutes?', Lines(2, 'The water was boiling; the temperature stayed at 100 °C.')), marks=6),
    Q('Why do people in Bangladesh store drinking water in clay pots (*kolshi*) to keep it cool?',
      Lines(3, 'Water seeps through the clay and evaporates from the outside; evaporation takes heat from the pot, cooling the water inside.'), marks=2),
])

investigate = Sheet('investigate', 'Does surface area affect evaporation?', level=2, goals=['Plan a fair test.', 'Plot two lines on one graph.', 'Draw a conclusion.'], blocks=[
    Fig(art.evaporation_dishes(), width='60%'),
    P('Arif and Mitu put 100 ml of water in a wide dish and 100 ml in a narrow cup. They left both in the same sunny place and '
      'measured the water left every hour.'),
    Q('Complete the plan.',
      Table(None, [['Question', Ans('Does surface area affect how fast water evaporates?')], ['Change', Ans('the container (wide dish or narrow cup) = surface area')],
                   ['Measure', Ans('volume of water left every hour (ml)')], ['Keep the same', Ans('starting volume, place, temperature, time, type of water')],
                   ['Prediction', Ans('The wide dish will lose water faster because more surface is open to the air.')]], widths=['24%', '76%']), marks=5),
    Q('Plot both sets of results on one line graph.',
      Table(['Time (hours)', '0', '1', '2', '3', '4'], [['Wide dish (ml)', '100', '82', '64', '46', '30'], ['Narrow cup (ml)', '100', '96', '92', '89', '85']], center=True),
      Graph(['0', '1', '2', '3', '4'], [[100, 82, 64, 46, 30], [100, 96, 92, 89, 85]], 'Water left (ml)', 'Time (hours)', ymax=100, step=10,
            kind='line', series_names=['wide dish', 'narrow cup'], width=150, height=70), marks=5),
    Q('How much water evaporated from each container in 4 hours?', Lines(1, 'Dish: 100 − 30 = 70 ml. Cup: 100 − 85 = 15 ml.'), marks=2),
    Q('Write a conclusion.', Lines(2, 'The larger the surface area, the faster water evaporates.'), marks=2),
])

case = Sheet('case', 'Salt from the sun: Cox\'s Bazar salt farmers', level=3, goals=['Apply evaporation to a real industry.', 'Use data and maths.', 'Consider how weather and climate affect people.'], blocks=[
    Links('Science', 'Geography', 'Maths', 'Economics', 'Health'),
    Fig(art.salt_pans(), 'Salt pans: sea water is let into shallow fields and the Sun evaporates the water.', width='92%'),
    Case('Almost all the salt eaten in Bangladesh is made on the coast of **Cox\'s Bazar** and Chattogram. From about '
         'November to May, the dry season, farmers let sea water into shallow, flat fields covered with plastic sheets. The '
         'Sun and the wind **evaporate** the water, and white **salt crystals** are left behind. Farmers rake up the salt and '
         'carry it away in baskets.',
         'In the monsoon, rain stops salt making: rain dissolves the salt and adds fresh water to the fields. Many salt farmers '
         'then grow shrimp or rice instead. Before it is sold, salt is cleaned and **iodine** is added, because our bodies '
         'need a small amount of iodine for healthy growth and brain development.',
         source='Based on descriptions of the Bangladesh salt industry (BSCIC and news reports). Numbers below are examples.'),
    Q('Explain how salt is made using the words *evaporate*, *dissolved* and *crystals*.',
      Lines(3, 'Salt is dissolved in sea water. The Sun and wind make the water evaporate, and the salt is left behind as crystals.'), marks=3),
    Q('Why can salt not be made during the monsoon?', Lines(2, 'Rain adds fresh water and dissolves the salt; there is less sunshine for evaporation.'), marks=2),
    Q('About 3.5 kg of salt is dissolved in every 100 litres of sea water.',
      Part('How much salt is in 1000 litres of sea water?', Lines(1, '3.5 × 10 = 35 kg')),
      Part('A farmer\'s field holds 20 000 litres. How much salt could it make?', Lines(1, '3.5 × 200 = 700 kg')), marks=3),
    Q('Why is iodine added to salt?', Lines(2, 'The body needs iodine for growth and brain development; everyone eats salt, so it is an easy way to get enough.'), marks=1),
    Q('Rising sea levels and stronger storms may affect salt farms. Suggest one problem and one solution.',
      Lines(3, 'Problem: storm surges and flooding destroy fields and stop production. Solution: higher earth walls (embankments), early warnings, insurance.'), marks=2),
])

review = Sheet('review', 'Show what you know', level=3, goals=['Use key vocabulary.', 'Answer test-style questions.'], blocks=[
    Q('Find the key words.', WordSearch(['SOLID', 'LIQUID', 'GAS', 'MELT', 'FREEZE', 'BOIL', 'VAPOUR', 'CONDENSE', 'STEAM'], size=10, seed=101)),
    Q('At what temperature does pure water boil?', MCQ(['0 °C', '37 °C', '100 °C', '212 °C'], 2), marks=1),
    Q('Which change happens when dew forms?', MCQ(['evaporation', 'condensation', 'melting', 'boiling'], 1), marks=1),
    Q('Draw the particles in a solid, a liquid and a gas.',
      Row([Draw('35mm', 'solid', 'Particles packed tightly in rows.')], [Draw('35mm', 'liquid', 'Particles close but jumbled, touching.')],
          [Draw('35mm', 'gas', 'Particles far apart, moving in all directions.')]), marks=3),
    Q('**Challenge.** Explain the difference between evaporation and boiling.',
      Lines(3, 'Evaporation happens only at the surface and at any temperature; boiling happens throughout the liquid, with bubbles, at the boiling point (100 °C for water).'), marks=2),
])

TOPIC = Topic(
    code='C1', strand='physical', title='States of Matter: Evaporation, Condensation, Boiling and Melting', short='States of matter',
    subtitle='Solids, liquids and gases, and how heating and cooling change them',
    outcomes=[
        'know that evaporation occurs when a liquid turns into a gas.',
        'know that condensation occurs when a gas turns into a liquid, and that it is the reverse of evaporation.',
        'know that air contains water vapour, and that when this meets a cold surface it may condense.',
        'know that the boiling point of water is 100°C and the melting point of ice is 0°C.',
        'know that when a liquid evaporates from a solution the solid is left behind.',
        'understand that a change of state between solid, liquid and gas can be caused by adding or removing heat.',
    ],
    cambridge=['Unit 3 States of matter (3.1–3.9)'],
    sheets=[learn, facts, think, investigate, case, review],
    selfcheck=['describe solids, liquids and gases using particles', 'explain evaporation and condensation', 'recall that water boils at 100 °C and ice melts at 0 °C',
               'explain why the temperature stays the same while ice melts', 'investigate what affects evaporation', 'explain how salt is made from sea water'],
    cover_art=art.states_particles(),
)
