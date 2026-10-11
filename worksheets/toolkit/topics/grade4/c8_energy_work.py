from build import Sheet, Topic
from ws import (P, H, Box, Vocab, Fig, Cols, Row, Case, Links, Lines, Blanks, Match, TrueFalse, MCQ, Order, Table,
                Ans, Sort, Label, Draw, Graph, WordSearch, Q, Part, Bullets, Pics)
import art
import art4

learn = Sheet('learn', 'Energy makes things happen', level=1, goals=[
    'Explain that energy is needed to make things work or move.',
    'Name forms of energy and describe how energy is converted and transferred.',
    'Track energy through a system and explain how people can save energy.',
], blocks=[
    P('You need energy to run, to think and to grow. A bus needs energy to move, a fan needs energy to spin, and a lamp needs '
      'energy to shine. **Energy** is what makes things **work**, **move**, **change** or **happen**. Energy cannot be seen, but '
      'we can see what it does.', 'lead'),
    Cols(
        H('Forms of energy', 3),
        Table(['Form', 'Examples'], [
            ['**kinetic** (movement)', 'a moving rickshaw, wind, a flowing river'],
            ['**stored (potential)**', 'a book on a high shelf, a stretched rubber band, water behind a dam'],
            ['**chemical** (stored)', 'food, wood, gas, petrol, batteries'],
            ['**heat** (thermal)', 'a hot cup of cha, the Sun, a cooking stove'],
            ['**light**', 'the Sun, a lamp, a firefly'],
            ['**sound**', 'a dhol, a car horn, your voice'],
            ['**electrical**', 'electricity flowing in wires']]),
        Pics([('person running', 'kinetic'), ('battery', 'chemical'), ('fire', 'heat'), ('light bulb', 'light'), ('drum', 'sound'), ('high voltage', 'electrical')], cols=6, size='11mm', small=True),
        H('Energy changes form', 3),
        P('Energy can be **converted** (changed) from one form to another. We show this with an **energy chain**:'),
        Fig(art.energy_chain([('chemical', 'in the battery'), ('electrical', 'in the wires'), ('light + heat', 'from the bulb')]), 'A torch.', span=True, width='70%'),
        Bullets(['**Electric fan**: electrical → kinetic (and a little sound and heat).', '**Solar panel**: light → electrical.',
                 '**Your body**: chemical (food) → kinetic (movement) + heat.', '**Gas stove**: chemical → heat + light.']),
        H('Energy moves from object to object', 3),
        P('Energy can be **transferred** (passed on): a hot spoon passes heat to your hand; your foot passes kinetic energy to a '
          'football; a drum passes sound energy through the air to your ears.'),
        H('Tracking energy through a system', 3),
        P('Almost all our energy starts in the **Sun**. Follow it through a system: the Sun\'s light helps rice grow (stored as '
          'chemical energy). You eat the rice. Your muscles use the energy to pedal a bicycle (kinetic energy). Some energy is '
          'always lost as **heat**, so no machine turns all its energy into useful work.'),
        Fig(art.energy_chain([('light', 'from the Sun'), ('chemical', 'in rice'), ('chemical', 'in your body'), ('kinetic', 'pedalling')]), 'Tracking energy from the Sun to a bicycle ride.', span=True, width='88%'),
        H('Energy that can run out', 3),
        P('**Coal, oil and natural gas** are energy stores that took millions of years to form. Burning them gives us electricity and '
          'fuel, but they will **run out**, and they pollute the air. **Renewable** sources such as **sunlight**, **wind**, '
          '**flowing water** and **biogas** will not run out.'),
        H('You can save energy', 3),
        Bullets(['Switch off lights, fans and TVs when no one is using them.', 'Use LED bulbs: they give the same light with much less electricity.',
                 'Walk, cycle or share transport for short trips.', 'Cook with lids on pots so less heat escapes.']),
        Box('bd', P('Bangladesh has one of the largest **solar home system** programmes in the world. Millions of families in villages use '
                    'small solar panels on their roofs to light their homes and charge phones.')),
    ),
    Vocab([('energy', 'what makes things work, move or change'), ('kinetic energy', 'energy of movement'), ('stored energy', 'energy waiting to be used, such as in food or a stretched band'),
           ('convert', 'change from one form to another'), ('transfer', 'pass from one object to another'), ('energy chain', 'a diagram showing how energy changes'),
           ('renewable', 'will not run out'), ('conserve energy', 'use less and waste less energy')]),
])

facts = Sheet('facts', 'Forms of energy', level=1, goals=['Name forms of energy.', 'Complete energy chains.'], blocks=[
    Q('Which form of energy?', Table(['Example', 'Form of energy'], [['a flowing river', Ans('kinetic')], ['a plate of rice', Ans('chemical')], ['a ringing bell', Ans('sound')],
                                                                    ['a stretched catapult', Ans('stored (potential)')], ['sunshine', Ans('light (and heat)')], ['a phone battery', Ans('chemical')]], widths=['55%', '45%']), marks=6),
    Q('Complete the energy chains.', Table(['Device', 'Energy in', 'Useful energy out'], [['electric fan', Ans('electrical'), Ans('kinetic')], ['solar panel', Ans('light'), Ans('electrical')],
                                                                                        ['radio', Ans('electrical'), Ans('sound')], ['candle', Ans('chemical'), Ans('light and heat')]], center=True), marks=8),
    Q('Sort the energy sources.', Sort(['Renewable', 'Will run out'], [('sunlight', 'Renewable'), ('wind', 'Renewable'), ('biogas', 'Renewable'), ('river water', 'Renewable'),
                                                                     ('coal', 'Will run out'), ('natural gas', 'Will run out'), ('oil', 'Will run out')]), marks=7),
])

think = Sheet('think', 'Following the energy', level=2, goals=['Track energy through systems.', 'Explain energy losses.'], blocks=[
    Q('Draw an energy chain for a rickshaw puller, starting with the Sun.', Draw('34mm', 'Rickshaw energy chain', 'Sun (light) → rice plant (chemical) → puller\'s body (chemical) → moving rickshaw (kinetic) + heat.'), marks=3),
    Q('An old filament bulb gets very hot. An LED bulb stays cool. Which one wastes more energy? Explain.', Lines(2, 'The filament bulb: much of its electrical energy becomes heat instead of light.'), marks=2),
    Q('Rubbing your hands together makes them warm. What energy change is happening?', Lines(1, 'kinetic (movement) → heat'), marks=1),
    Q('Why do we say almost all our energy comes from the Sun? Give two examples.', Lines(3, 'Plants store the Sun\'s energy in food we eat; coal, oil and gas came from ancient plants; wind and rain are driven by the Sun\'s heat.'), marks=2),
    Q('Suggest two ways your school could save energy.', Lines(2, 'switch off fans and lights at break; use LED bulbs; open windows for daylight; solar panels on the roof.'), marks=2),
])

investigate = Sheet('investigate', 'Rubber band launcher', level=2, goals=['Plan a fair test.', 'Plot a line graph.', 'Explain using stored and kinetic energy.'], blocks=[
    P('Class 4A used a rubber band stretched between two chair legs to launch a toy car. They pulled the band back by different amounts and measured how far the car travelled.'),
    Q('Complete the plan.', Table(None, [['Change', Ans('how far the band is pulled back (cm)')], ['Measure', Ans('distance the car travels (cm)')],
                                         ['Keep the same', Ans('the same band, car and floor; release without pushing')]], widths=['26%', '74%']), marks=3),
    Q('Draw a line graph.',
      Table(['Pull back (cm)', '2', '4', '6', '8', '10'], [['Distance travelled (cm)', '40', '85', '130', '170', '210']], center=True),
      Graph(['2', '4', '6', '8', '10'], [40, 85, 130, 170, 210], 'Distance (cm)', 'Pull back (cm)', ymax=220, step=20, kind='line', width=110, height=50), marks=3),
    Q('Describe the pattern and explain it using energy.', Lines(3, 'The further the band is pulled back, the further the car goes, because a more stretched band stores more energy, which becomes more kinetic energy in the car.'), marks=3),
    Q('Predict the distance for a pull of 12 cm.', Lines(1, 'about 250 cm'), marks=1),
])

case = Sheet('case', 'Cooking with cow dung: biogas', level=3, goals=['Track energy through a real system.', 'Use numbers.', 'Weigh up benefits.'], blocks=[
    Links('Science', 'Farming', 'Health', 'Environment', 'Economics'),
    Case('In many villages in Bangladesh, families cook on clay stoves that burn wood, leaves or dried cow dung. The smoke fills '
         'the kitchen and harms people\'s lungs, especially women and children.',
         'A **biogas plant** offers another way. Cow dung and water are fed into a closed underground tank. Tiny **microbes** break '
         'down the dung and make a gas called **methane**. The gas flows through a pipe to a stove in the kitchen, where it burns '
         'with a clean blue flame. The leftover **slurry** is an excellent fertiliser for the fields. A family with a few cows can '
         'make enough gas to cook their meals.',
         source='Based on information about household biogas in Bangladesh (e.g. IDCOL\'s biogas programme). Numbers below are examples.'),
    Q('Complete the energy chain for biogas cooking.',
      Order(['light from the Sun', 'grass grows (chemical energy)', 'cows eat grass; dung holds chemical energy', 'microbes make biogas', 'gas burns: heat for cooking']), marks=3),
    Q('Why is biogas called a **renewable** energy source?', Lines(2, 'As long as cows eat grass and make dung, more gas can be made; it will not run out.'), marks=2),
    Q('**Maths.** A family uses 15 kg of firewood a week. A biogas plant replaces all of it. How much wood is saved in a year (52 weeks)?', Lines(1, '15 × 52 = 780 kg of wood'), marks=2),
    Q('Give one benefit of biogas for each.', Table(['For…', 'Benefit'], [['health', Ans('no smoke in the kitchen, so healthier lungs')], ['the environment', Ans('fewer trees cut for firewood')],
                                                                         ['farming', Ans('slurry is free fertiliser')]], widths=['30%', '70%']), marks=3),
])

review = Sheet('review', 'Show what you know', level=3, goals=['Use key vocabulary.', 'Answer test-style questions.'], blocks=[
    Q('Find the key words.', WordSearch(['ENERGY', 'KINETIC', 'HEAT', 'LIGHT', 'SOUND', 'SOLAR', 'BIOGAS', 'STORED', 'CHAIN'], size=10, seed=418)),
    Q('What energy change happens in a solar panel?', MCQ(['heat → sound', 'light → electrical', 'electrical → light', 'kinetic → chemical'], 1), marks=1),
    Q('Which energy source will run out?', MCQ(['wind', 'sunlight', 'natural gas', 'biogas'], 2), marks=1),
    Q('Draw an energy chain for a mobile phone playing music, starting from the charged battery.', Draw('30mm', 'Phone energy chain', 'chemical (battery) → electrical → sound (+ light from the screen, + heat).'), marks=3),
    Q('**Challenge.** "Energy is never used up, it only changes form." Explain this using a bicycle that slows down and stops when you stop pedalling.',
      Lines(3, 'The kinetic energy of the bicycle is not destroyed; friction and air resistance change it into heat (and a little sound) in the tyres, brakes and air.'), marks=2),
])

TOPIC = Topic(
    code='C8', strand='physical', title='Energy and Work', short='Energy',
    subtitle='Forms of energy, energy changes and transfers, tracking energy through systems, and saving energy',
    outcomes=[
        'understand that energy is required to enable things to work or move.',
        'identify the different forms of energy, and describe how energy can be converted from one form to another.',
        'understand that energy can be transferred in various ways and between objects.',
        'describe how the transfer of energy can be tracked as energy flows through a system.',
        'understand that some sources of energy can be depleted, and explain the part people play in energy conservation.',
        'recognize how heat can be produced in many ways (IB Phase 3).',
    ],
    sheets=[learn, facts, think, investigate, case, review],
    selfcheck=['name forms of energy', 'draw energy chains', 'explain energy transfer between objects', 'track energy from the Sun through a system',
               'investigate stored energy in a rubber band', 'explain how biogas works and why it is renewable'],
    cover_art=art.energy_chain([('light', 'from the Sun'), ('chemical', 'in food'), ('kinetic', 'movement')]),
)
