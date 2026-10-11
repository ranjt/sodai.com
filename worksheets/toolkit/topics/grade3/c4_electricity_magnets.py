from build import Sheet, Topic
from ws import (P, H, Box, Vocab, Fig, Cols, Row, Case, Links, Lines, Blanks, Match, TrueFalse, MCQ, Order, Table,
                Ans, Sort, Label, Draw, Graph, WordSearch, Q, Part, Bullets, Pics)
import art
import art4
import art23

learn = Sheet('learn', 'Circuits and magnets', level=1, goals=[
    'Build a complete circuit with a cell, wires, a lamp and a switch.',
    'Explain why a break in a circuit stops it working, using a model of the current.',
    'Describe how magnets attract and repel, and which metals they attract.',
], blocks=[
    P('Fans, lights, phones and televisions all use **electricity**. Electricity from the wall socket (mains) is very **dangerous**. In science lessons we use small **cells** (batteries), which are safe.', 'lead'),
    Box('safety', P('Never touch wall sockets, plugs or wires with wet hands. Never poke anything into a socket. Mains electricity can kill.')),
    H('Parts of a circuit', 3),
    Pics([('battery', 'cell (battery)'), ('light bulb', 'lamp (bulb)'), ('thread', 'wire'), ('bell', 'buzzer'), ('fan', 'motor')], cols=5, size='14mm'),
    P('A **circuit** is a loop. Electricity flows from one end of the cell, through the wires and the lamp, and back to the other end of the cell. If the loop is **complete**, the lamp lights.'),
    Fig(art4.circuit_symbols(), 'Scientists draw circuits with symbols.', width='80%'),
    H('Breaks in a circuit', 3),
    P('If there is a **gap** anywhere in the loop, the electricity cannot flow and the lamp goes out. A **switch** makes a gap on purpose: switch **on** closes the gap; switch **off** opens it.'),
    Row([Fig(art4.circuit(('cell', 'lamp', 'switch'), closed=True), 'Switch on: complete circuit, lamp lights.')],
        [Fig(art4.circuit(('cell', 'lamp', 'switch'), closed=False), 'Switch off: a break, lamp is off.')]),
    H('A model of electricity', 3),
    P('We cannot see electricity flowing. Scientists use a **model** to help: imagine tiny **particles** in the wires. The cell pushes them, and they flow **all the way round** the circuit, like children in a ring passing a ball. If the ring breaks, everything stops.'),
    Fig(art23.current_model(), 'A model of an electric current.', width='58%'),
    H('Magnets', 3),
    P('A **magnet** pulls (**attracts**) things made of **iron** and **steel**, and a few other metals such as nickel. It does **not** attract aluminium, copper, brass, gold or silver, or non-metals like wood and plastic.'),
    P('Each magnet has two ends called **poles**: **north (N)** and **south (S)**. Two different poles **attract**. Two poles that are the same **repel** (push apart).'),
    Fig(art4.bar_magnets(), 'Magnets attract and repel.', width='48%'),
    P('We use magnets in fridge doors, bag clasps, compasses, toys, and in big cranes that lift scrap iron.'),
    Vocab([('circuit', 'a complete loop that electricity flows around'), ('cell', 'stores electricity (often called a battery)'), ('switch', 'opens or closes a gap in a circuit'),
           ('attract', 'pull together'), ('repel', 'push apart'), ('pole', 'the end of a magnet, north or south')]),
])

facts = Sheet('facts', 'Will it work?', level=1, goals=['Spot complete circuits.', 'Sort magnetic metals.'], blocks=[
    Q('Will the lamp light? Write yes or no.',
      Row([Fig(art4.circuit(('cell', 'lamp', 'switch'), closed=True), 'A')], [Fig(art4.circuit(('cell', 'lamp', 'switch'), closed=False), 'B')], [Fig(art4.circuit(('cell', 'lamp', 'buzzer'), closed=True), 'C')]),
      Table(['A', 'B', 'C'], [[Ans('yes'), Ans('no: switch open'), Ans('yes, and the buzzer sounds')]], center=True), marks=3),
    Q('Sort the objects.', Sort(['Attracted by a magnet', 'Not attracted'], [('iron nail', 'Attracted by a magnet'), ('steel pin', 'Attracted by a magnet'), ('steel spoon', 'Attracted by a magnet'),
                                                                               ('aluminium foil', 'Not attracted'), ('copper wire', 'Not attracted'), ('plastic toy', 'Not attracted')]), marks=6),
    Q('Attract or repel?', Table(['Poles facing', 'Attract or repel?'], [['N and S', Ans('attract')], ['N and N', Ans('repel')], ['S and S', Ans('repel')]], center=True, widths=['50%', '50%']), marks=3),
])

think = Sheet('think', 'Problem solving', level=2, goals=['Find faults in circuits.', 'Explain with a model.'], blocks=[
    Q('Raju\'s torch does not work. Give three things that could be wrong.', Lines(3, 'the cell is flat; the bulb is broken; a wire is loose; the switch is broken'), marks=3),
    Q('Use the particle model to explain why the lamp goes out when you open the switch.', Lines(2, 'The gap stops the particles flowing round the loop, so no electricity reaches the lamp.'), marks=2),
    Q('Why are electric wires covered in plastic?', Lines(2, 'Plastic does not let electricity through, so it keeps us safe from shocks.'), marks=2),
])

investigate = Sheet('investigate', 'Which magnet is the strongest?', level=2, goals=['Do a fair test.', 'Draw a bar chart and conclude.'], blocks=[
    P('Class 3B hung paper clips in a chain from each magnet, one at a time, until no more would stick.'),
    Q('Draw a bar chart.', Table(['Magnet', 'bar', 'horseshoe', 'ring', 'fridge'], [['Paper clips', '8', '12', '5', '2']], center=True),
      Graph(['bar', 'horseshoe', 'ring', 'fridge'], [8, 12, 5, 2], 'Paper clips', 'Magnet', ymax=14, step=2, width=100, height=48), marks=3),
    Q('Which magnet was strongest?', Lines(1, 'the horseshoe magnet'), marks=1),
    Q('Why must they use the same kind of paper clip each time?', Lines(2, 'To make it a fair test: only the magnet should change.'), marks=2),
])

case = Sheet('case', 'Light for every home: solar power', level=3, goals=['See how a circuit changes lives.'], blocks=[
    Links('Science', 'Technology', 'Community'),
    Case('Some villages and islands in Bangladesh are far from the electricity lines. Millions of families there use **solar home systems**: a **solar panel** on the roof, a **battery**, wires, **switches** and a few **LED lamps**.',
         'In the day, the solar panel turns sunlight into electricity, which is stored in the battery. At night the battery lights the lamps, so children can study and families can charge their phones, without smoky kerosene lamps.',
         source='Based on solar home systems in rural Bangladesh.'),
    Q('Name the parts of a solar home circuit.', Lines(1, 'solar panel, battery, wires, switch, lamps'), marks=2),
    Q('Why is a solar lamp better than a kerosene lamp?', Lines(2, 'no smoke, no fire danger, uses free sunlight, brighter'), marks=2),
    Q('Draw the circuit: battery, switch and lamp.', Draw('34mm', 'Solar lamp circuit', 'a loop: battery → switch → lamp → back to the battery.'), marks=2),
])

review = Sheet('review', 'Show what you know', level=3, goals=['Use circuit and magnet words.'], blocks=[
    Q('Find the words.', WordSearch(['CELL', 'WIRE', 'LAMP', 'SWITCH', 'MAGNET', 'POLE', 'IRON'], size=9, seed=313)),
    Q('A lamp will light if the circuit is…', MCQ(['broken', 'complete', 'wet'], 1), marks=1),
    Q('Two north poles will…', MCQ(['attract', 'repel', 'melt'], 1), marks=1),
    Q('**Challenge.** How could you use a magnet to separate iron nails from sand?', Lines(2, 'Move the magnet over the mixture; the nails stick to it and the sand stays behind.'), marks=2),
])

TOPIC = Topic(
    code='C4', strand='physical', title='Electricity and Magnets', short='Circuits and magnets',
    subtitle='Complete circuits, switches and breaks, a particle model of current, and magnets that attract and repel',
    outcomes=[
        'construct complete circuits using a switch, a cell, wire and lamps.',
        'explore how an electrical device will not work if there is a break in the circuit.',
        'know that electrical current flows, and that models can describe this flow — for example particles travelling around a circuit.',
        'explore the forces between magnets, and know that magnets can attract or repel each other.',
        'know that magnets attract some metals but not others.',
    ],
    cambridge=['Stage 2 Unit 5 Electricity'],
    sheets=[learn, facts, think, investigate, case, review],
    selfcheck=['build a complete circuit', 'find a break in a circuit', 'explain current with a model', 'say when magnets attract or repel', 'name metals a magnet attracts'],
    cover_art=art4.circuit(('cell', 'lamp', 'switch')),
)
