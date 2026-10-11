from build import Sheet, Topic
from ws import (P, H, Box, Vocab, Fig, Cols, Row, Case, Links, Lines, Blanks, Match, TrueFalse, MCQ, Order, Table,
                Ans, Sort, Label, Draw, Graph, WordSearch, Q, Part, Bullets, Pics)
import art
import art4

learn = Sheet('learn', 'Forces: pushes, pulls and motion', level=1, goals=[
    'Name types of force, show their direction with arrows and measure them in newtons.',
    'Explain the difference between mass (kg) and weight (N).',
    'Describe the laws of motion and how friction and air resistance affect movement.',
], blocks=[
    P('A rickshaw puller pushes the pedals. A goalkeeper stops a football. A coconut falls from a tree. A boat glides across a '
      'pond. In every case, a **force** is at work. A force is a **push** or a **pull**. You cannot see forces, but you can see '
      'what they do.', 'lead'),
    Cols(
        H('What forces can do', 3),
        Bullets(['make something **start** moving, or **stop**;', 'make it go **faster** or **slower**;', 'change its **direction**;',
                 'change its **shape**: squash, stretch, bend or twist (a lump of clay, a spring, a football when kicked).']),
        H('Measuring forces', 3),
        P('Forces are measured in **newtons** (N), named after the scientist Isaac Newton. We measure them with a **forcemeter** '
          '(newton meter), which has a spring inside. The bigger the pull, the more the spring stretches.'),
        Row([Fig(art4.forcemeter(4), 'A forcemeter reading 4 N.')], [P('On a diagram we show a force with an **arrow**. The arrow points in the **direction** of the force. A longer arrow means a bigger force.')], widths=['30%', '70%']),
        H('Mass and weight', 3),
        P('**Mass** is how much matter (stuff) is in an object. It is measured in **kilograms** (kg) with a balance. **Weight** is '
          'the **force of gravity** pulling the object down, so it is measured in **newtons** (N). On Earth, a mass of 1 kg has a '
          'weight of about 10 N. In everyday life we say "I weigh 30 kg", but scientists would say "my mass is 30 kg".'),
        Table(['', 'Mass', 'Weight'], [['what it is', 'amount of matter', 'pull of gravity'], ['unit', 'kilogram (kg)', 'newton (N)'],
                                       ['on the Moon', 'stays the same', 'about 6 times smaller']]),
        H('Kinds of force', 3),
        Fig(art4.force_arrows(), 'Forces on a box being pulled.', width='92%'),
        Table(['Force', 'What it does', 'Contact or not?'], [
            ['**gravity**', 'pulls everything down towards the Earth', 'non-contact'],
            ['**friction**', 'slows things when surfaces rub together', 'contact'],
            ['**air resistance**', 'friction from the air; slows moving things', 'contact'],
            ['**tension**', 'the pull in a stretched rope, string or spring', 'contact'],
            ['**upthrust**', 'water or air pushing up on an object', 'contact'],
            ['**magnetic force**', 'pulls or pushes magnets and iron', 'non-contact']]),
        P('**Contact forces** need the objects to touch. **Non-contact forces** act at a **distance**: gravity pulls a mango down '
          'from a tree without touching it.'),
        H('Friction: friend and enemy', 3),
        P('Friction helps us walk without slipping, lets brakes stop a bicycle and stops a rickshaw\'s tyres sliding. But '
          'friction also wastes energy as heat and wears out shoes and tyres. **Air resistance** slows a parachute so it lands '
          'gently, but it slows down cyclists and buses too, so racing bicycles are shaped to cut through the air.'),
        H('The laws of motion', 3),
        Bullets(['**1. Things keep doing what they are doing.** A still ball stays still, and a moving ball keeps moving in a straight '
                 'line, unless a force acts on it. (A ball rolling on grass stops because of friction.)',
                 '**2. Bigger force, bigger change.** Kick a ball harder and it speeds up more. A heavy cart needs a bigger push than a light one.',
                 '**3. Every push has a push back.** When you push the water backwards with an oar, the water pushes the boat forwards. '
                 'A rocket pushes gas down and the gas pushes the rocket up.']),
        H('Movement passes from object to object', 3),
        P('In carrom, the moving **striker** hits a coin. The striker slows down and the coin moves off: movement energy passes '
          'from one object to the other. The faster the striker, the further the coin goes. Moving things have **movement '
          '(kinetic) energy**; the faster they go, the more energy they have.'),
    ),
    Vocab([('force', 'a push or a pull'), ('newton (N)', 'the unit of force'), ('mass', 'how much matter is in something (kg)'), ('weight', 'the pull of gravity on something (N)'),
           ('gravity', 'the force that pulls things towards the Earth'), ('friction', 'a force that slows things when surfaces rub'),
           ('air resistance', 'friction from air'), ('tension', 'the pulling force in a stretched rope or string')]),
])

facts = Sheet('facts', 'Forces around us', level=1, goals=['Name forces.', 'Use units.', 'Show forces with arrows.'], blocks=[
    Q('Read the forcemeters.', Row([Fig(art4.forcemeter(3), 'A', width='70%')], [Fig(art4.forcemeter(7), 'B', width='70%')], [Fig(art4.forcemeter(9), 'C', width='70%')]),
      Table(['A', 'B', 'C'], [[Ans('3 N'), Ans('7 N'), Ans('9 N')]], center=True), marks=3),
    Q('Name the force.',
      Table(['What happens', 'Force'], [['a mango falls from a tree', Ans('gravity')], ['a bicycle slows down when you brake', Ans('friction')],
                                        ['a rope in tug-of-war is pulled tight', Ans('tension')], ['a parachute falls slowly', Ans('air resistance')], ['a boat floats', Ans('upthrust')]], widths=['62%', '38%']), marks=5),
    Q('Sort the forces.', Sort(['Contact force', 'Non-contact force'], [('friction', 'Contact force'), ('a kick', 'Contact force'), ('tension', 'Contact force'),
                                                                       ('gravity', 'Non-contact force'), ('magnetic force', 'Non-contact force')]), marks=5),
    Q('Fill in the gaps.', Blanks('Mass is measured in [kilograms]. Weight is a force, so it is measured in [newtons]. On the Moon your mass stays the [same] but your weight is [smaller].',
                                  extra=['bigger', 'metres']), marks=4),
])

think = Sheet('think', 'Forces in action', level=2, goals=['Draw force arrows.', 'Explain motion using the laws of motion.'], blocks=[
    Q('Draw arrows to show the forces on a boy on a slide: gravity pulling him down and friction slowing him.', Draw('38mm', 'Slide', 'Arrow pointing down (weight/gravity); arrow pointing up the slide, opposite to the movement (friction).'), marks=2),
    Q('Explain each one using a law of motion.',
      Table(['What happens', 'Explanation'], [['a football rolling on grass slowly stops', Ans('law 1: friction (a force) acts on it and stops it')],
                                              ['it is harder to push a full rickshaw van than an empty one', Ans('law 2: more mass needs a bigger force to change its speed')],
                                              ['a swimmer pushes water back and moves forward', Ans('law 3: the water pushes the swimmer forward')]], widths=['44%', '56%']), marks=6),
    Q('Why do people put sand or gravel on a slippery muddy path in the monsoon?', Lines(2, 'Sand increases friction so feet and tyres grip and do not slip.'), marks=2),
    Q('In carrom, what happens to the striker\'s movement when it hits a coin?', Lines(2, 'The striker slows down and passes some of its movement (kinetic) energy to the coin, which starts to move.'), marks=2),
])

investigate = Sheet('investigate', 'Which surface has the most friction?', level=2, goals=['Plan a fair test.', 'Measure distance.', 'Explain results using friction.'], blocks=[
    P('Class 4D let a toy car roll down the same ramp onto four different surfaces and measured how far it travelled before stopping.'),
    Q('Complete the plan.', Table(None, [['Change', Ans('the surface')], ['Measure', Ans('distance the car travels (cm)')],
                                         ['Keep the same', Ans('the car, the ramp height and slope, where the car starts, no push')]], widths=['26%', '74%']), marks=3),
    Q('Here are the results (mean of three tries). Draw a bar chart.',
      Table(['Surface', 'tiles', 'wood', 'jute mat', 'sand paper'], [['Distance (cm)', '180', '140', '70', '35']], center=True),
      Graph(['tiles', 'wood', 'jute mat', 'sandpaper'], [180, 140, 70, 35], 'Distance (cm)', 'Surface', ymax=200, step=20, width=110, height=50), marks=3),
    Q('Which surface had the most friction? How do you know?', Lines(2, 'Sandpaper: the car travelled the shortest distance, so friction slowed it most.'), marks=2),
    Q('Why did they do each test three times and find the mean?', Lines(1, 'To make the results more reliable.'), marks=1),
    Q('Which surface would be best for a playground slide landing area? Why?', Lines(1, 'A rough surface with lots of friction (like a jute mat) so children stop safely.'), marks=1),
])

case = Sheet('case', 'Kabaddi and tug-of-war: the forces in our games', level=3, goals=['Find forces in real games.', 'Use data from a tug-of-war.', 'Think about fairness and safety.'], blocks=[
    Links('Science', 'Physical education', 'Maths', 'Culture'),
    Case('**Kabaddi** is the national game of Bangladesh. A raider runs into the other team\'s half, tries to tag players and get '
         'back, while defenders try to hold them. Players **push**, **pull**, twist and change direction quickly. They play '
         'barefoot on soil or a mat, which gives good **friction** for gripping the ground.',
         'In **tug-of-war** (*dori tana*), two teams pull a rope in opposite directions. The rope is in **tension**. If both teams '
         'pull with the same force, the forces are **balanced** and the rope does not move. If one team pulls harder, the forces '
         'are **unbalanced** and the rope moves towards the stronger team.',
         source='Example game data below.'),
    Q('Two teams pull a rope (example data).',
      Table(['Round', 'Team Shapla (N)', 'Team Doel (N)', 'Which way does the rope move?'], [['1', '800', '800', Ans('it does not move (balanced)')], ['2', '900', '750', Ans('towards Shapla')], ['3', '700', '850', Ans('towards Doel')]], center=True),
      Part('What is the difference in force in round 2?', Lines(1, '900 − 750 = 150 N towards Shapla')), marks=4),
    Q('Why do kabaddi players play barefoot on soil or a mat, not on smooth tiles?', Lines(2, 'Soil and mats have more friction, so their feet grip and they can push off, stop and turn without slipping.'), marks=2),
    Q('When a raider pushes off the ground to run, which law of motion is at work? Explain.', Lines(2, 'Law 3: the feet push back on the ground and the ground pushes the raider forward.'), marks=2),
    Q('Suggest two rules that make kabaddi or tug-of-war safe and fair.', Lines(2, 'e.g. teams of the same total mass; no pulling hair or clothes; a soft surface; gloves for the rope; a referee.'), marks=2),
])

review = Sheet('review', 'Show what you know', level=3, goals=['Use key vocabulary.', 'Answer test-style questions.'], blocks=[
    Q('Find the key words.', WordSearch(['FORCE', 'PUSH', 'PULL', 'GRAVITY', 'FRICTION', 'NEWTON', 'MASS', 'WEIGHT', 'MOTION'], size=10, seed=414)),
    Q('Which is a non-contact force?', MCQ(['friction', 'tension', 'gravity', 'a push'], 2), marks=1),
    Q('What unit is used for weight?', MCQ(['kilograms', 'newtons', 'metres', 'litres'], 1), marks=1),
    Q('Draw a ball being kicked. Use arrows to show the kick, gravity and air resistance.', Draw('38mm', 'Kicked ball', 'Kick arrow in the direction of movement; gravity arrow down; air resistance arrow opposite to the movement.'), marks=3),
    Q('**Challenge.** An astronaut has a mass of 60 kg. What is her mass on the Moon? Is her weight bigger or smaller there? Explain.',
      Lines(3, 'Her mass is still 60 kg (the amount of matter does not change). Her weight is smaller (about 6 times less) because the Moon\'s gravity is weaker.'), marks=2),
])

TOPIC = Topic(
    code='C4', strand='physical', title='Forces and Motion', short='Forces and motion',
    subtitle='Pushes and pulls, newtons, mass and weight, friction, gravity and tension, and the laws of motion',
    outcomes=[
        'distinguish between mass measured in kilograms and weight measured in newtons, noting that kilograms are used in everyday life.',
        'recognise and use the units of force, mass and weight, and identify the direction in which forces act.',
        'identify and describe the different types of force, including friction, gravity and tension.',
        'describe the laws of motion and give everyday examples of each.',
        'recognise friction, including air resistance, as a force which can affect the speed at which objects move and which sometimes stops things moving.',
        'explain how forces can be exerted by one object on another through direct contact or from a distance.',
        'identify patterns of movement from one object to another.',
        'understand the notion of energy in movement.',
        'understand that forces can affect how an object moves or changes shape.',
        'describe the connections between motion and the behaviour of objects and systems.',
    ],
    sheets=[learn, facts, think, investigate, case, review],
    selfcheck=['measure forces in newtons', 'explain mass and weight', 'name contact and non-contact forces',
               'explain the three laws of motion with examples', 'investigate friction on different surfaces', 'explain balanced and unbalanced forces in tug-of-war'],
    cover_art=art4.force_arrows(),
)
