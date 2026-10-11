from build import Sheet, Topic
from ws import (P, H, Box, Vocab, Fig, Cols, Row, Case, Links, Lines, Blanks, Match, TrueFalse, MCQ, Order, Table,
                Ans, Sort, Label, Draw, Graph, WordSearch, Q, Part, Bullets, Pics)
import art
import art4

learn = Sheet('learn', 'Floating and flying', level=1, goals=[
    'Describe features of plants and animals that help them float or fly, and link them to human-made floaters and flyers.',
    'Label the four forces of flight and explain how they work together.',
    'Explain floating using weight, upthrust, displaced water and density, and describe the properties of air.',
], blocks=[
    P('In a country of rivers, boats are everywhere: wooden *nouka*, river launches, fishing trawlers and huge cargo ships. '
      'Above them, kites, birds and aeroplanes fill the sky. How does a heavy steel ship float? How does a bird stay up? '
      'The answers are all about **forces**.', 'lead'),
    Cols(
        H('Nature\'s floaters and flyers', 3),
        Table(['Living thing', 'Feature', 'Helps it to…'], [
            ['duck', 'oily, waterproof feathers trap air; webbed feet', 'float and paddle'],
            ['fish', 'an air bag inside (swim bladder)', 'float at the right depth'],
            ['water hyacinth', 'stalks full of air', 'float on rivers'],
            ['coconut', 'air-filled husk', 'float across the sea to new islands'],
            ['bird', 'light hollow bones, feathers, curved wings', 'fly'],
            ['silk-cotton (*shimul*) seed', 'fluffy fibres', 'drift on the wind']]),
        Pics([('duck', 'duck'), ('coconut', 'coconut'), ('eagle', 'eagle'), ('feather', 'feather')], cols=4, size='13mm', small=True),
        H('Copying nature', 3),
        P('People have copied these features. **Life jackets** trap air like a duck\'s feathers. **Boats** have wide hollow hulls. '
          '**Aeroplane wings** are curved like a bird\'s. A **parachute** catches the air like a fluffy seed. **Kites** and gliders '
          'use the wind like soaring eagles.'),
        Pics([('canoe', 'boat'), ('airplane', 'aeroplane'), ('parachute', 'parachute'), ('kite', 'kite')], cols=4, size='13mm', small=True),
        H('The four forces of flight', 3),
        Fig(art4.flight_forces(), 'The four forces on a plane.', width='96%'),
        Bullets(['**Lift** pushes the plane **up**. It is made by air flowing over and under the curved wings.',
                 '**Weight** (gravity) pulls the plane **down**.',
                 '**Thrust** pushes the plane **forward**. It comes from the engines (or a bird flapping its wings).',
                 '**Drag** (air resistance) pulls the plane **back**.']),
        P('To take off, **lift must be bigger than weight** and **thrust bigger than drag**. When the forces are balanced, the plane '
          'flies level at a steady speed.'),
        H('How things float', 3),
        Fig(art4.float_forces(), 'Forces on a floating boat.', width='92%'),
        P('When you put an object in water, it **pushes some water out of the way** (it **displaces** water). The water pushes back '
          'up on the object. This upward push is called **upthrust** (or buoyancy). Gravity pulls the object down (its **weight**).'),
        Bullets(['If the upthrust can become **as big as the weight**, the object **floats**.',
                 'If the weight is **bigger** than the biggest upthrust, the object **sinks**.']),
        H('Density', 3),
        P('**Density** tells us how heavy something is for its size. A stone is heavy for its size (dense), so it sinks. Wood is '
          'light for its size, so it floats. A steel ship floats because it is **hollow**: its shape is full of air, so the ship as a '
          'whole is light for its size and it displaces a lot of water.'),
        H('The properties of air', 3),
        Bullets(['Air **takes up space** and **has mass**.', 'Air can be **squashed** (compressed): we pump it into tyres and balls.',
                 'Air **pushes** on things (air pressure) and **moves** (wind).']),
        P('We use these properties in tyres, balloons, life jackets, kites, sails, windmills and parachutes.'),
        Box('bd', P('In winter, Old Dhaka celebrates **Shakrain** with hundreds of colourful kites flying from the rooftops. Kite fliers '
                    'use the wind to give their kites lift, and the string\'s tension to steer them.')),
    ),
    Vocab([('float', 'stay on the surface of a liquid'), ('upthrust (buoyancy)', 'the upward push of water or air'), ('displace', 'push out of the way'),
           ('density', 'how heavy something is for its size'), ('lift', 'the upward force on a wing'), ('thrust', 'the forward force from engines or flapping'),
           ('drag', 'air resistance that pulls a flyer back'), ('weight', 'the pull of gravity')]),
])

facts = Sheet('facts', 'Forces for floating and flying', level=1, goals=['Label the forces of flight.', 'Sort floaters and sinkers.'], blocks=[
    Q('Label the four forces of flight.', Fig(art4.flight_forces(labels=False), width='62%'),
      Table(['1', '2', '3', '4'], [[Ans('lift'), Ans('weight'), Ans('thrust'), Ans('drag')]], center=True), marks=4),
    Q('Predict: float or sink?', Sort(['Floats', 'Sinks'], [('a cork', 'Floats'), ('a plastic duck', 'Floats'), ('a dry leaf', 'Floats'), ('a wooden stick', 'Floats'),
                                                            ('a stone', 'Sinks'), ('a metal key', 'Sinks'), ('a glass marble', 'Sinks'), ('a coin', 'Sinks')]), marks=8),
    Q('Match the human invention to the living thing it copies.', Match([('life jacket', 'duck feathers trap air'), ('parachute', 'fluffy seeds drifting on the wind'),
                                                                      ('aeroplane wing', 'curved bird wing'), ('boat hull', 'floating coconut shell')]), marks=4),
    Q('Fill in the gaps.', Blanks('The upward push of water is called [upthrust]. A stone sinks because its weight is [bigger] than the upthrust. '
                                  'Air can be [squashed] into a tyre.', extra=['smaller', 'gravity']), marks=3),
])

think = Sheet('think', 'Why do things float and fly?', level=2, goals=['Explain floating with forces and density.', 'Explain flight forces.'], blocks=[
    Q('A steel nail sinks, but a steel ship floats. Explain why.', Lines(3, 'The ship is hollow and full of air, so it is light for its size and displaces a lot of water, giving enough upthrust to hold up its weight; the solid nail is too dense.'), marks=3),
    Q('Why do life jackets help you float?', Lines(2, 'They are full of air or light foam, which makes you less dense overall, so the water can push you up enough to float.'), marks=2),
    Q('A plane is taking off. Which forces must be bigger? Tick two.',
      Table(['', 'True?'], [['lift is bigger than weight', Ans('✓')], ['weight is bigger than lift', Ans('')], ['thrust is bigger than drag', Ans('✓')], ['drag is bigger than thrust', Ans('')]], center=True, widths=['70%', '30%']), marks=2),
    Q('Why does a parachute have such a big canopy?', Lines(2, 'A big canopy catches lots of air, making a big drag (air resistance) force, so the person falls slowly.'), marks=2),
    Q('Draw a boat with arrows for weight and upthrust. Show what happens when the boat is overloaded.', Draw('38mm', 'Boat forces', 'Normal: weight and upthrust arrows equal. Overloaded: weight arrow longer; the boat sits lower and water may come in.'), marks=2),
])

investigate = Sheet('investigate', 'Foil boats: which shape holds most?', level=2, goals=['Design and test model floaters.', 'Record results.', 'Improve a design.'], blocks=[
    P('Class 4A made boats from the same size of aluminium foil (20 cm × 20 cm) in four shapes. They added marbles one at a time until each boat sank.'),
    Q('Complete the plan.', Table(None, [['Change', Ans('the shape of the boat')], ['Measure', Ans('number of marbles before it sinks')],
                                         ['Keep the same', Ans('size and type of foil, the marbles, the bowl of water, how marbles are added')]], widths=['26%', '74%']), marks=3),
    Q('Draw a bar chart.',
      Table(['Boat shape', 'flat raft', 'tall narrow', 'wide low tray', 'canoe'], [['Marbles before sinking', '6', '9', '24', '15']], center=True),
      Graph(['raft', 'tall narrow', 'wide tray', 'canoe'], [6, 9, 24, 15], 'Marbles', 'Boat shape', ymax=26, step=2, width=110, height=50), marks=3),
    Q('Which shape held the most? Explain using the word **displace**.', Lines(2, 'The wide low tray: it pushes aside (displaces) the most water, so the upthrust is biggest.'), marks=2),
    Q('How could you improve the best boat?', Lines(2, 'Make the sides a little higher so water does not come in, or spread the marbles evenly so it stays balanced.'), marks=2),
])

case = Sheet('case', 'Safe on the water: boats and launches', level=3, goals=['Apply floating science to safety.', 'Use data about loads.', 'Suggest rules to save lives.'], blocks=[
    Links('Science', 'Citizenship', 'Maths', 'Geography'),
    Case('Millions of people in Bangladesh travel by water every day: small *nouka*, ferries and big **launches** that carry '
         'hundreds of passengers between Dhaka and the south. When a boat is loaded, it sinks lower in the water. Every launch '
         'is allowed to carry only a certain number of people.',
         'Sometimes, especially before holidays like Eid, launches are **overloaded**. The boat sits too low, waves can wash in, '
         'and it becomes unstable. In storms, overloaded boats can capsize. Safety rules say launches must not leave in bad '
         'weather, must carry life jackets and life buoys, and must not carry more people than allowed.',
         source='Based on river transport safety rules in Bangladesh. Data below are example values.'),
    Q('A launch is allowed to carry 300 passengers (example data).',
      Table(['Trip', 'A', 'B', 'C', 'D'], [['Passengers', '250', '300', '420', '280']], center=True),
      Part('Which trip was overloaded? By how many people?', Lines(1, 'Trip C, by 120 people (420 − 300)')),
      Part('Why is an overloaded boat more likely to sink?', Lines(2, 'Its weight is bigger, so it sits lower; waves come over the side and fill it with water.')), marks=3),
    Q('Many boats have a painted line on the side called a **load line**. What do you think it is for?', Lines(2, 'If the water reaches the line, the boat is carrying too much and must not leave.'), marks=2),
    Q('What might each person say about overloading?',
      Table(['Person', 'View'], [['a passenger going home for Eid', Ans('I need to get home; there are not enough boats.')], ['the launch owner', Ans('More passengers means more money, but it is dangerous and illegal.')],
                                 ['a river police officer', Ans('I must stop overloaded boats to save lives.')]], widths=['34%', '66%']), marks=3),
    Q('Design a safety poster for a launch terminal. Include two rules and a picture.', Draw('38mm', 'Safety poster', 'e.g. "Wear a life jacket", "Do not board a full launch", picture of a boat with the load line.'), marks=2),
])

review = Sheet('review', 'Show what you know', level=3, goals=['Use key vocabulary.', 'Answer test-style questions.'], blocks=[
    Q('Find the key words.', WordSearch(['FLOAT', 'SINK', 'LIFT', 'DRAG', 'THRUST', 'WEIGHT', 'UPTHRUST', 'AIR', 'BOAT'], size=10, seed=415)),
    Q('Which force pulls an aeroplane backwards?', MCQ(['lift', 'thrust', 'drag', 'weight'], 2), marks=1),
    Q('Why does a block of wood float?', MCQ(['it is heavy for its size', 'it is light for its size', 'it has no weight', 'water pulls it up'], 1, one_col=True), marks=1),
    Q('Design a paper glider. Draw it and explain one change you could test to make it fly further.', Draw('40mm', 'My glider', 'e.g. wider wings for more lift, or a paper clip on the nose to balance it; test by measuring the distance flown.'), marks=3),
    Q('**Challenge.** A ball of clay sinks, but the same clay shaped into a bowl floats. Explain.', Lines(3, 'As a bowl it pushes aside much more water, so the upthrust is bigger and can match its weight. The mass is the same but the shape is different.'), marks=2),
])

TOPIC = Topic(
    code='C5', strand='physical', title='Floating and Flying', short='Floating and flying',
    subtitle='Nature\'s floaters and flyers, the four forces of flight, upthrust, density and the properties of air',
    outcomes=[
        'recognize features of some plants and animals that enable them to float or fly.',
        'make connections between the features of plants and animals and the features of human-made floaters and flyers.',
        'identify and describe on a diagram the four forces that interact for flight — lift, weight, drag and thrust — and the relationships between them required for flight.',
        'plan, design and make model flyers, and investigate through altering the design how flight can be improved.',
        'identify and describe on a diagram the principles of floatation — buoyancy, downward force, upward force, displaced volume and density — and the relationships between them required for floatation.',
        'plan, design and make model floaters, and investigate through altering the design how to improve buoyancy.',
        'describe the properties of air and their practical applications.',
    ],
    sheets=[learn, facts, think, investigate, case, review],
    selfcheck=['link animal features to human floaters and flyers', 'label the four forces of flight', 'explain upthrust and weight',
               'explain floating using density and displacement', 'test and improve a model boat', 'explain why overloading boats is dangerous'],
    cover_art=art4.flight_forces(),
)
