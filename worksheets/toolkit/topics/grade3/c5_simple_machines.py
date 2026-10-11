from build import Sheet, Topic
from ws import (P, H, Box, Vocab, Fig, Cols, Row, Case, Links, Lines, Blanks, Match, TrueFalse, MCQ, Order, Table,
                Ans, Sort, Label, Draw, Graph, WordSearch, Q, Part, Bullets, Pics)
import art
import art23

learn = Sheet('learn', 'Simple machines make work easier', level=1, goals=[
    'Explain what a simple machine is.',
    'Find levers in everyday life and explain how they make work easier.',
    'Explain how ramps, pulleys and gears help us.',
], blocks=[
    P('Try to lift the lid off a tin of powdered milk with your fingers. Hard! Now push the end of a spoon under the lid and press down. Easy! The spoon is a **simple machine**.', 'lead'),
    P('A **simple machine** is a tool with few or no moving parts that makes work **easier**. It may let us use **less force**, **change the direction** of a force, or move something **further or faster**.'),
    Fig(art.simple_machines(), 'Six simple machines.', width='92%'),
    H('Levers', 3),
    P('A **lever** is a bar that turns on a point called the **fulcrum** (pivot). You push on one part (the **effort**) to move a **load**. The **further** your effort is from the fulcrum, the **less force** you need.'),
    Fig(art.lever(labels=art.LEVER_PARTS), 'A see-saw lever.', width='62%'),
    Pics([('scissors', 'scissors'), ('playground slide', 'see-saw in a park'), ('spoon', 'spoon opening a lid'), ('wheelbarrow', 'wheelbarrow'), ('hammer', 'hammer pulling a nail')], cols=5, size='14mm'),
    Box('bd', P('A **dheki** is a long wooden lever used in villages to husk rice, and a **tubewell** handle is a lever that lifts water.')),
    Row([Fig(art.dheki(), 'A dheki.')], [Fig(art.tubewell(labels=art.TUBEWELL_PARTS), 'A tubewell.')]),
    H('Ramps (inclined planes)', 3),
    P('A **ramp** is a slope. It is easier to push a heavy load up a ramp than to lift it straight up: you move it **further**, but with **less force**. Ramps help wheelchair users, people loading trucks, and cars on hill roads that zig-zag up the slope.'),
    Fig(art23.ramp_lift(), 'A ramp means less force.', width='62%'),
    H('Pulleys and gears', 3),
    P('A **pulley** is a wheel with a rope over it. Pulling **down** on the rope lifts the load **up**. Pulleys lift buckets from wells, flags up poles and heavy loads on building sites. '
      '**Gears** are wheels with teeth that turn each other. Bicycles, clocks, egg beaters and rice mills use gears.'),
    Fig(art23.pulley_gears(), 'A pulley and two gears.', width='60%'),
    Vocab([('simple machine', 'a tool that makes work easier'), ('lever', 'a bar that turns on a fulcrum'), ('fulcrum', 'the point a lever turns on'),
           ('effort', 'the push or pull you give'), ('load', 'the thing being moved'), ('pulley', 'a wheel with a rope'), ('gear', 'a wheel with teeth')]),
])

facts = Sheet('facts', 'Name the machine', level=1, goals=['Label a lever.', 'Name simple machines.'], blocks=[
    Q('Label the lever.', Label(art.lever(), art.LEVER_PARTS, width='60%', cols=3), marks=3),
    Q('Name each simple machine.', Fig(art.simple_machines(names=False), width='90%'),
      Table(['A', 'B', 'C', 'D', 'E', 'F'], [[Ans(m) for m in art.MACHINE_NAMES]], center=True), marks=6),
    Q('Draw a line to match.', Match([('scissors', 'lever'), ('wheelchair slope', 'ramp (inclined plane)'), ('flag pole rope', 'pulley'), ('bicycle chain wheels', 'gears')]), marks=4),
])

think = Sheet('think', 'How do machines help?', level=2, goals=['Explain how machines make work easier.'], blocks=[
    Q('Why is it easier to open a tin lid with a long spoon than with a coin?', Lines(2, 'The spoon is a longer lever, so you need less force.'), marks=2),
    Q('Why do roads up steep hills zig-zag?', Lines(2, 'The zig-zag makes a longer, gentler ramp, so cars need less force to climb.'), marks=2),
    Q('How does a pulley help someone raise a flag?', Lines(2, 'They pull down on the rope and the flag goes up; pulling down is easier.'), marks=2),
    Q('Draw a lever you use at home. Mark the fulcrum, effort and load.', Draw('36mm', 'My lever', 'e.g. scissors, bottle opener or spoon, with fulcrum, effort and load marked.'), marks=3),
])

investigate = Sheet('investigate', 'Does a ramp make it easier?', level=2, goals=['Measure force in newtons.', 'Draw a bar chart and conclude.'], blocks=[
    P('Class 3C used a forcemeter to pull a toy truck up ramps of different heights. Lifting it straight up needed 10 N.'),
    Q('Draw a bar chart.', Table(['Ramp height', '10 cm', '20 cm', '30 cm', 'straight up'], [['Force (N)', '3', '5', '7', '10']], center=True),
      Graph(['10 cm', '20 cm', '30 cm', 'straight up'], [3, 5, 7, 10], 'Force (N)', 'Ramp height', ymax=12, step=2, width=100, height=48), marks=3),
    Q('Which ramp needed the least force?', Lines(1, 'the lowest one (10 cm)'), marks=1),
    Q('Complete: the lower (gentler) the ramp, the ___ force is needed.', Lines(1, 'less'), marks=1),
    Q('What did they keep the same?', Lines(1, 'the same truck, the same ramp length, the same forcemeter'), marks=1),
])

case = Sheet('case', 'From dheki to rice mill', level=3, goals=['See how machines change daily life.'], blocks=[
    Links('Science', 'History', 'Work'),
    Case('For hundreds of years, village women in Bangladesh husked rice with a **dheki**. One person stepped on the end of a long wooden beam. The beam turned on a pivot and the other end lifted, then thumped down onto the rice to knock off the husks. It was slow, hard work.',
         'Today most rice is husked in **rice mills**. A motor turns **gears** and **belts** that work the machines, and one mill can husk tonnes of rice in a day. Some families still use a dheki to make special rice flour for winter pitha.',
         source='Based on rice husking in Bangladesh.'),
    Q('What kind of simple machine is a dheki?', Lines(1, 'a lever'), marks=1),
    Q('How did the dheki make work easier?', Lines(2, 'Pressing the long end with your foot lifted the heavy beam; the lever made it easier.'), marks=2),
    Q('Write one good thing and one problem about rice mills.', Lines(2, 'Good: much faster, less hard work. Problem: needs electricity or fuel; some people lost their work.'), marks=2),
])

review = Sheet('review', 'Show what you know', level=3, goals=['Use machine words.'], blocks=[
    Q('Find the words.', WordSearch(['LEVER', 'RAMP', 'PULLEY', 'GEAR', 'LOAD', 'EFFORT', 'WHEEL'], size=9, seed=314)),
    Q('The point a lever turns on is the…', MCQ(['load', 'fulcrum', 'gear'], 1), marks=1),
    Q('A ramp lets you use…', MCQ(['more force', 'less force', 'no force'], 1), marks=1),
    Q('**Challenge.** Design a machine to lift a bucket of sand to a first-floor window. Label the simple machines you used.', Draw('40mm', 'My machine', 'e.g. a pulley fixed above the window with a rope, maybe with a winding handle (wheel and axle).'), marks=3),
])

TOPIC = Topic(
    code='C5', strand='physical', title='Simple Machines', short='Simple machines',
    subtitle='Levers, ramps, pulleys and gears, and how simple machines make work easier',
    outcomes=[
        'explain what a simple machine is, based on observations they have made.',
        'identify levers as simple machines, and identify examples of levers in everyday life.',
        'explore how simple levers can be used to make work easier.',
        'explore how simple inclined planes can be used to make work easier.',
        'identify pulley and gear systems, and discuss their impact on daily life.',
        'demonstrate how a pulley or gear system performs a specific task.',
    ],
    cambridge=['Stage 3 Unit 6 Forces and movement (6.3–6.4 Forcemeters)'],
    sheets=[learn, facts, think, investigate, case, review],
    selfcheck=['explain what a simple machine is', 'find the fulcrum, effort and load', 'explain how a ramp helps', 'explain how pulleys and gears help', 'measure force on a ramp'],
    cover_art=art23.pulley_gears(),
)
