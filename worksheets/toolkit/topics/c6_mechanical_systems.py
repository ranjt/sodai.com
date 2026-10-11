from build import Sheet, Topic
from ws import (P, H, Box, Vocab, Fig, Cols, Row, Case, Links, Lines, Blanks, Match, TrueFalse, MCQ, Order, Table,
                Ans, Sort, Label, Draw, Graph, WordSearch, Q, Part, Bullets)
import art

learn = Sheet('learn', 'Simple machines and mechanical systems', level=1, goals=[
    'Name the six simple machines and explain how they make work easier.',
    'Identify simple machines inside mechanical systems.',
    'Explain how forces start and stop moving devices.',
], blocks=[
    P('How does a small person lift a heavy bucket of water from a well, crack a hard nut, or carry three passengers '
      'through Dhaka on a rickshaw? They use **machines**. Machines help us by changing the **size** or **direction** of a '
      '**force** (a push or a pull).', 'lead'),
    Fig(art.simple_machines(), 'The six simple machines.', width='92%'),
    Cols(
        H('1. Lever', 3),
        P('A **lever** is a bar that turns on a **pivot** (also called a **fulcrum**). You push on one part (the **effort**) to '
          'move a **load**. The further the effort is from the pivot, the **less force** you need. Examples: a see-saw, '
          'scissors, a bottle opener, a nutcracker, the handle of a tube-well, and the *dheki*.'),
        Fig(art.lever(labels=art.LEVER_PARTS)),
        Box('bd', P('The **dheki** is a traditional Bengali rice-husker. A long wooden beam rests on a pivot. A person presses '
                    'one end with their foot, and the heavy head at the other end lifts and then drops onto the rice, '
                    'removing the husks.')),
        Fig(art.dheki(), 'A dheki is a lever.'),
        H('2. Pulley', 3),
        P('A **pulley** is a wheel with a rope around it. It changes the **direction** of a force: you pull **down** to lift a '
          'load **up**. Using several pulleys together means less force is needed. Examples: a flagpole, a well bucket, a crane.'),
        H('3. Wheel and axle', 3),
        P('A large **wheel** fixed to a thin rod (the **axle**) turns together with it. A small force on the big wheel makes a '
          'bigger turning force on the axle. Examples: rickshaw wheels, a door knob, a screwdriver, a steering wheel.'),
        H('4. Inclined plane (ramp)', 3),
        P('A **ramp** lets you raise a heavy load by pushing it a **longer** distance with **less** force. Examples: a wheelchair '
          'ramp, a sloping road up a bridge, a plank for loading a truck.'),
        H('5. Wedge', 3),
        P('A **wedge** is two ramps back to back. It turns a push into a sideways force that **splits** or **cuts**. Examples: '
          'an axe, a knife, a nail point and the Bengali **boti**.'),
        H('6. Screw', 3),
        P('A **screw** is a ramp wrapped around a rod. Turning it moves it in or out with great force. Examples: jar lids, '
          'bolts, a bottle cap, a car jack.'),
        H('Mechanical systems', 3),
        P('A **mechanical system** is a device in which several simple machines work together. A bicycle or rickshaw uses '
          'pedals and cranks (levers and wheel and axle), a chain and gears, wheels and axles, and brake levers. Forces '
          '**start** it (the rider pushing the pedals), and forces **stop** it (**friction** from the brakes).'),
        Fig(art.tubewell(labels=art.TUBEWELL_PARTS), 'A hand tube-well is a mechanical system with a lever handle.'),
    ),
    Vocab([('force', 'a push or a pull'), ('lever', 'a bar that turns on a pivot'), ('fulcrum (pivot)', 'the point a lever turns on'),
           ('effort', 'the force you put in'), ('load', 'the object being moved'), ('pulley', 'a wheel with a rope that changes the direction of a force'),
           ('friction', 'a force that slows moving things'), ('mechanical system', 'simple machines working together')]),
])

facts = Sheet('facts', 'Six simple machines', level=1, goals=['Name and identify simple machines.', 'Label a lever.'], blocks=[
    Q('Write the letter of each simple machine.', Fig(art.simple_machines(names=False), width='92%'),
      Table(['Machine', 'Letter'], [[n, Ans(l)] for n, l in (('wedge', 'E'), ('lever', 'A'), ('screw', 'F'), ('pulley', 'B'), ('inclined plane', 'D'), ('wheel and axle', 'C'))], center=True), marks=6),
    Q('Label the lever.', Label(art.lever(), art.LEVER_PARTS, width='75%', cols=3), marks=3),
    Q('Sort the examples into the simple machine they use.',
      Sort(['Lever', 'Wedge', 'Wheel and axle'], [('scissors', 'Lever'), ('bottle opener', 'Lever'), ('dheki', 'Lever'),
                                                  ('axe', 'Wedge'), ('boti', 'Wedge'), ('knife', 'Wedge'),
                                                  ('rickshaw wheel', 'Wheel and axle'), ('screwdriver', 'Wheel and axle'), ('door knob', 'Wheel and axle')]), marks=9),
    Q('Fill in the gaps.',
      Blanks('A lever turns on a [pivot]. A pulley can change the [direction] of a force. A ramp lets you lift a load with '
             '[less] force. Brakes stop a bicycle using [friction].', extra=['more', 'gravity']), marks=4),
])

think = Sheet('think', 'Machines at work', level=2, goals=['Explain how simple machines help.', 'Analyse a mechanical system.'], blocks=[
    Q('Rahim pushes a heavy box up a ramp instead of lifting it straight up. What does he gain, and what does he give up?',
      Lines(2, 'He needs a smaller force, but he must push the box a longer distance.'), marks=2),
    Q('Why is it easier to open a door by pushing near the handle than near the hinges?',
      Lines(2, 'The door is a lever with the hinge as the pivot; pushing further from the pivot needs less force.'), marks=2),
    Q('Analyse the hand tube-well.',
      Fig(art.tubewell(), width='40%'),
      Part('Which simple machine is the handle?', Lines(1, 'a lever (the pivot is near the pump body)')),
      Part('Why is the handle long?', Lines(2, 'A long handle means the effort is far from the pivot, so less force is needed to lift the water.')),
      Part('What force starts the pump, and what is the output?', Lines(1, 'a person pushing down on the handle; water flows out of the spout')), marks=4),
    Q('Name **three** simple machines on a bicycle or rickshaw and what each does.',
      Table(['Part', 'Simple machine', 'What it does'], [[Ans('pedal and crank'), Ans('lever / wheel and axle'), Ans('turns the push of the feet into turning')],
                                                        [Ans('wheels'), Ans('wheel and axle'), Ans('help it roll with less friction')],
                                                        [Ans('brake handles'), Ans('lever'), Ans('make a big squeezing force on the wheel')]], center=True), marks=6),
])

investigate = Sheet('investigate', 'How does distance from the pivot change the effort?', level=2, goals=['Measure force with a forcemeter.', 'Find a pattern.', 'Make a prediction.'], blocks=[
    P('Class 5A put a 10 N load on a ruler lever, 10 cm from the pivot. They used a **forcemeter** to measure the effort needed '
      'to lift it, pulling at different distances from the pivot on the other side. (N = newton, the unit of force.)'),
    Q('Here are the results. Plot them as a line graph.',
      Table(['Distance of effort from pivot (cm)', '10', '20', '30', '40', '50'], [['Effort needed (N)', '10', '5', '3.3', '2.5', '2']], center=True),
      Graph(['10', '20', '30', '40', '50'], [10, 5, 3.3, 2.5, 2], 'Effort needed (N)', 'Distance from pivot (cm)', ymax=11, step=1, kind='line',
            width=140, height=56), marks=4),
    Q('Describe the pattern.', Lines(2, 'The further the effort is from the pivot, the less force is needed.'), marks=2),
    Q('Predict the effort needed at 60 cm.', Lines(1, 'about 1.7 N (a little less than 2 N)'), marks=1),
    Q('Name **two** things the class kept the same.', Lines(2, 'the load (10 N), the load\'s distance from the pivot, the same ruler and pivot'), marks=2),
    Q('Use the results to explain why a long crowbar helps to lift a heavy stone.',
      Lines(2, 'A long crowbar lets you push far from the pivot, so you need much less force to lift the heavy stone.'), marks=1),
])

case = Sheet('case', 'The rickshaw: a city on three wheels', level=3, goals=['Analyse a real mechanical system.', 'Explain how forces power and stop it.', 'Consider people, jobs and technology change.'], blocks=[
    Links('Science', 'Design', 'Economics', 'Ethics', 'Art'),
    Case('Dhaka has hundreds of thousands of **cycle rickshaws**, famous for their colourful hand-painted art. A rickshaw is '
         'a **mechanical system**: the puller pushes the **pedals** (levers), which turn a **crank** and **gear wheel**. A '
         '**chain** carries the turning to a small gear on the back axle, turning the big **wheels**. **Brake levers** press '
         'pads against the wheels, and **friction** slows them down.',
         'Pulling a rickshaw is hard work, especially with three passengers or on a bridge. In recent years many rickshaws '
         'have been fitted with **batteries and electric motors**. They are faster and easier for the puller, but they can '
         'be dangerous at high speed, the batteries must be charged with electricity, and old batteries can pollute if not '
         'recycled.',
         source='Based on reports about rickshaws and battery rickshaws in Bangladesh.'),
    Q('Complete the table to show how the rickshaw works as a system.',
      Table(['Part', 'Simple machine', 'Job in the system'], [
          ['pedals and crank', Ans('lever / wheel and axle'), Ans('turn the puller\'s push into turning')],
          ['chain and gears', Ans('wheel and axle (gears)'), Ans('carry the turning to the back wheels')],
          ['wheels and axles', Ans('wheel and axle'), Ans('let the rickshaw roll')],
          ['brake levers', Ans('lever'), Ans('press the brakes hard on the wheel to stop it with friction')]], widths=['24%', '30%', '46%']), marks=6),
    Q('Which force **starts** the rickshaw moving and which force **stops** it?',
      Lines(2, 'Starts: the puller\'s push on the pedals (muscle force). Stops: friction from the brakes (and air resistance).'), marks=2),
    Q('What might each person think about battery rickshaws?',
      Table(['Person', 'View'], [['a rickshaw puller', Ans('Less tiring and I can earn more, but the battery costs money.')],
                                 ['a traffic police officer', Ans('They go too fast in traffic and can cause accidents.')],
                                 ['an environmental scientist', Ans('No smoke, but the batteries need electricity and safe recycling.')]], widths=['32%', '68%']), marks=3),
    Q('**Design.** Suggest one improvement to make the cycle rickshaw easier to pull or safer. Explain how it uses forces or simple machines.',
      Lines(3, 'e.g. lower gears for bridges (smaller force needed); better brakes with longer levers; lighter frame; reflectors and lights for safety.'), marks=2),
])

review = Sheet('review', 'Show what you know', level=3, goals=['Use key vocabulary.', 'Answer test-style questions.'], blocks=[
    Q('Find the key words.', WordSearch(['LEVER', 'PULLEY', 'WHEEL', 'AXLE', 'WEDGE', 'SCREW', 'RAMP', 'FORCE', 'PIVOT'], size=10, seed=151)),
    Q('Which simple machine is a knife?', MCQ(['pulley', 'wedge', 'screw', 'wheel and axle'], 1), marks=1),
    Q('What does a single fixed pulley do?', MCQ(['makes the load lighter', 'changes the direction of the force', 'stops friction', 'makes the rope longer'], 1, one_col=True), marks=1),
    Q('Design a machine to lift a bucket of sand to the top of a wall. Draw and label which simple machines it uses.',
      Draw('50mm', 'My machine', 'e.g. a pulley at the top with a rope; or a lever like a shadoof; labels showing effort, load and pivot or pulley.'), marks=3),
    Q('**Challenge.** A see-saw has a heavy child on one side and a light child on the other. How can they balance? Explain using the pivot.',
      Lines(3, 'The heavy child sits closer to the pivot and the light child sits further away; the light child\'s smaller force acts further from the pivot.'), marks=2),
])

TOPIC = Topic(
    code='C6', strand='physical', title='Mechanical Systems', short='Mechanical systems',
    subtitle='Forces, the six simple machines and how they combine in mechanical systems',
    outcomes=[
        'explain what a mechanical system is and give examples — combinations of inclined planes, levers, pulleys, wheel and axle, wedges and screws designed to interact and perform a given function.',
        'analyze a variety of simple mechanical systems, identifying the components that act as simple machines and determining the contribution of each to the overall function of the device.',
        'identify and demonstrate how simple forces can be used to power or stop a moving mechanical device.',
    ],
    sheets=[learn, facts, think, investigate, case, review],
    selfcheck=['name the six simple machines with examples', 'label the effort, load and pivot of a lever', 'explain how simple machines make work easier',
               'find simple machines in a mechanical system', 'investigate how distance from the pivot changes the effort', 'explain how forces start and stop a rickshaw'],
    cover_art=art.simple_machines(),
)
