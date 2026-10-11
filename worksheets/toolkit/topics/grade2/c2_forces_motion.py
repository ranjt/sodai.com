from build import Sheet, Topic
from ws import (P, H, Box, Vocab, Fig, Cols, Row, Case, Links, Lines, Blanks, Match, TrueFalse, MCQ, Order, Table,
                Ans, Sort, Label, Draw, Graph, WordSearch, Q, Part, Bullets, Pics)
import art
import art4

learn = Sheet('learn', 'Pushes and pulls', level=1, goals=[
    'Explain that pushes and pulls are forces, and that forces can be measured.',
    'Show how forces start, stop and change the shape of things.',
    'Describe gravity, friction and weight.',
], blocks=[
    P('Kick a ball, open a door, pull a rickshaw van, squash some clay. Every time, you use a **force**. A force is a **push** or a **pull**.', 'lead'),
    Pics([('football', 'kick: push'), ('shopping cart', 'push'), ('rowing boat', 'pull the oars'), ('kite', 'pull the string'), ('hammer', 'hit: push')], cols=5, size='15mm'),
    H('What forces do', 3),
    Bullets(['make things **start** moving (push a swing);', 'make things **stop** (catch a ball);', 'make things go **faster** or **slower**;',
             'change the **direction** things move (hit a ball with a bat);', 'change the **shape** of things (squash, stretch, bend or twist clay).']),
    H('Measuring forces', 3),
    P('We can measure how big a force is with a **forcemeter**. It has a spring inside. The harder you pull, the more the spring stretches. Forces are measured in **newtons** (N).'),
    Row([Fig(art4.forcemeter(5), 'A forcemeter.')], [P('A heavy bag needs a **bigger** force to lift or move than a light bag. The **heavier** something is, the more force you need to move it.')], widths=['28%', '72%']),
    H('Gravity', 3),
    P('**Gravity** is a force that pulls everything **down** towards the Earth. That is why a mango falls from the tree and a ball comes back down. Your **weight** is how hard gravity pulls on you.'),
    H('Friction', 3),
    P('**Friction** is a force that happens when two things rub together. It **slows things down**. A ball rolls far on a smooth floor, but stops quickly on grass or sand. '
      'Friction helps us: our shoes grip the ground so we do not slip, and bicycle brakes stop the wheels.'),
    Fig(art4.force_arrows(), 'Forces on a box being pulled.', width='72%'),
    H('Motion', 3),
    P('**Motion** means moving: changing position over time. A car that goes further in the same time is moving **faster**.'),
    Vocab([('force', 'a push or a pull'), ('gravity', 'pulls things down to the Earth'), ('friction', 'slows things when they rub'),
           ('weight', 'how hard gravity pulls on something'), ('forcemeter', 'measures forces in newtons')]),
])

facts = Sheet('facts', 'Push or pull?', level=1, goals=['Sort pushes and pulls.', 'Name forces.'], blocks=[
    Q('Push or pull?', Sort(['Push', 'Pull'], [('kicking a ball', 'Push'), ('pushing a pram', 'Push'), ('pressing a button', 'Push'),
                                             ('opening a drawer', 'Pull'), ('flying a kite', 'Pull'), ('pulling a rope', 'Pull')]), marks=6),
    Q('What does the force do? Draw a line.', Match([('squashing clay', 'changes its shape'), ('catching a ball', 'stops it'), ('pushing a swing', 'starts it moving'), ('hitting a ball with a bat', 'changes its direction')]), marks=4),
    Q('Fill in the gaps.', Blanks('A mango falls down because of [gravity]. A ball stops on grass because of [friction]. A force is a push or a [pull].', extra=['light']), marks=3),
])

think = Sheet('think', 'Forces all around', level=2, goals=['Explain friction and gravity.', 'Compare forces.'], blocks=[
    Q('Why is it easier to slide on a wet, smooth floor than on a rough mat?', Lines(2, 'The smooth floor has less friction, so you slide; the rough mat has more friction.'), marks=2),
    Q('Which needs a bigger force to push? Why?', Pics([('shopping cart', 'empty cart'), ('package', 'cart full of heavy boxes')], cols=2, size='18mm'),
      Lines(2, 'The full cart; heavier things need more force to move.'), marks=2),
    Q('Draw an arrow to show which way gravity pulls a falling mango.', Draw('34mm', 'Falling mango', 'An arrow pointing straight down.'), marks=1),
])

investigate = Sheet('investigate', 'How far does the car roll?', level=2, goals=['Do a fair test.', 'Measure distance.'], blocks=[
    P('Class 2B rolled a toy car down a ramp onto three surfaces and measured how far it went.'),
    Q('Draw a bar chart.', Table(['Surface', 'smooth floor', 'mat', 'sand'], [['Distance (cm)', '150', '80', '20']], center=True),
      Graph(['floor', 'mat', 'sand'], [150, 80, 20], 'Distance (cm)', 'Surface', ymax=160, step=20, width=100, height=50), marks=3),
    Q('On which surface did the car go furthest?', Lines(1, 'the smooth floor'), marks=1),
    Q('Which surface had the most friction?', Lines(1, 'sand'), marks=1),
    Q('Why did they use the same ramp and car each time?', Lines(1, 'To make it a fair test.'), marks=1),
])

case = Sheet('case', 'The rickshaw van', level=3, goals=['Find forces in real life.'], blocks=[
    Links('Science', 'Work', 'Maths'),
    Case('Kamal drives a **rickshaw van** that carries vegetables to the market. He **pushes** the pedals with his feet to make it go. '
         'When the van is full of potatoes it is very **heavy**, and he must push much harder.',
         'When he wants to stop, he squeezes the **brakes**. The brakes rub on the wheels and **friction** slows the van down. On a wet road the van slides more, so Kamal goes slowly.',
         source='A story about forces at work.'),
    Q('What force does Kamal use to make the van go?', Lines(1, 'a push on the pedals'), marks=1),
    Q('Why is it harder to pedal when the van is full?', Lines(2, 'The van is heavier, so it needs a bigger force to move.'), marks=2),
    Q('How do the brakes stop the van?', Lines(2, 'They rub on the wheels; friction slows them down.'), marks=2),
])

review = Sheet('review', 'Show what you know', level=3, goals=['Use force words.'], blocks=[
    Q('Find the words.', WordSearch(['PUSH', 'PULL', 'FORCE', 'GRAVITY', 'SLOW', 'FAST'], size=8, seed=211)),
    Q('Which force pulls things down?', MCQ(['friction', 'gravity', 'a push'], 1), marks=1),
    Q('Squashing clay changes its…', MCQ(['colour', 'shape', 'weight'], 1), marks=1),
    Q('**Challenge.** Draw yourself pushing something and pulling something. Label each.', Row([Draw('30mm', 'push', 'e.g. pushing a door')], [Draw('30mm', 'pull', 'e.g. pulling a rope')]), marks=2),
])

TOPIC = Topic(
    code='C2', strand='physical', title='Forces and Motion', short='Pushes and pulls',
    subtitle='Pushes and pulls, measuring forces, gravity, friction, weight and motion',
    outcomes=[
        'know that pushes and pulls are examples of forces, and that forces can be measured.',
        'demonstrate a basic understanding of the concepts of gravity, friction and weight.',
        'relate the effect of gravity on the movement of an object.',
        'explore how forces can make objects start or stop moving.',
        'explore how forces can change the shape of objects.',
        'explain how friction affects the movement of an object, and explore how forces including friction can make objects move faster or more slowly.',
        'correlate the weight of an object to the amount of force required to move it.',
        'understand that motion is a change in position over time.',
    ],
    cambridge=['Stage 3 Unit 6 Forces and movement (6.1–6.5)', 'Stage 2 Unit 3 Changing materials (3.1–3.3)'],
    sheets=[learn, facts, think, investigate, case, review],
    selfcheck=['sort pushes and pulls', 'say what forces can do', 'explain gravity', 'explain friction', 'test how far a car rolls'],
    cover_art=art4.force_arrows(),
)
