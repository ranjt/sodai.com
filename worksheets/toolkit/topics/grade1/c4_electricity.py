from build import Sheet, Topic
from ws import (P, H, Box, Vocab, Fig, Q, Lines, Blanks, Match, TrueFalse, MCQ, Table, Ans, Sort, Draw, Graph, WordSearch, Bullets, Pics, Row,
                Choose, PicMatch, PicSort, Pictograph, Trace, Case)
import art
import art4

learn = Sheet('learn', 'Electricity and circuits', level=1, goals=['Name the parts of a circuit.', 'Explain what a switch does.'], blocks=[
    P('Lights, fans, phones and televisions use **electricity**. Some things get electricity from the **wall socket**. Some use **batteries** (cells).', 'lead'),
    Pics([('light bulb', 'lamp'), ('fan', 'fan'), ('television', 'TV'), ('mobile phone', 'phone'), ('flashlight', 'torch')], cols=5, size='17mm'),
    Box('safety', P('Electricity from the wall is **dangerous**. Never touch sockets or wires, and keep water away from them.')),
    H('A simple circuit', 3),
    P('A **circuit** is a loop. It has a **cell**, **wires** and a **lamp**. Electricity flows round the loop from the cell, through the lamp and back. The loop must be **complete**, with no gaps.'),
    Row([Fig(art4.circuit(('cell', 'lamp', 'switch'), closed=True), 'Switch on: the lamp lights.')], [Fig(art4.circuit(('cell', 'lamp', 'switch'), closed=False), 'Switch off: a gap, no light.')]),
    P('A **switch** makes a gap in the circuit (off) or closes the gap (on).'),
    H('Where does electricity come from?', 3),
    Pics([('solar energy', 'sunlight (solar panels)'), ('wind energy', 'wind'), ('water wave', 'moving water'), ('factory smoke', 'burning gas or coal')], cols=4, size='18mm'),
    Vocab([('circuit', 'a complete loop for electricity'), ('cell', 'a battery that stores electricity'), ('switch', 'turns a circuit on and off')]),
])

facts = Sheet('facts', 'Circuit facts', level=1, goals=['Name circuit parts.', 'Spot complete circuits.'], blocks=[
    Q('Will the lamp light? Write yes or no.', Row([Fig(art4.circuit(('cell', 'lamp', 'switch'), closed=True), 'A')], [Fig(art4.circuit(('cell', 'lamp', 'switch'), closed=False), 'B')]),
      Table(['A', 'B'], [[Ans('yes'), Ans('no')]], center=True)),
    Q('Match the part to its job.', Match([('cell', 'pushes electricity round'), ('wire', 'carries electricity'), ('switch', 'turns it on and off'), ('lamp', 'gives light')])),
])

think = Sheet('think', 'Safe or not safe?', level=2, goals=['Think about electrical safety.'], blocks=[
    Q('Sort these.', Sort(['Safe', 'Not safe'], [('using a torch with batteries', 'Safe'), ('asking an adult to plug in', 'Safe'),
                                                 ('poking a socket', 'Not safe'), ('touching a switch with wet hands', 'Not safe')])),
    Q('Why does the lamp go out when you open the switch?', Lines(2, 'There is a gap, so electricity cannot flow round the loop.')),
])

investigate = Sheet('investigate', 'Make a circuit', level=2, goals=['Build a circuit.', 'Find out what makes it work.'], blocks=[
    Box('need', P('a cell (battery), two wires with clips, a small bulb in a holder, a switch.')),
    P('Join the cell, wires and bulb in a loop. Then add the switch.'),
    Q('Draw your circuit.', Draw('42mm', 'My circuit', 'A loop: cell → wire → switch → wire → bulb → back to the cell.')),
    Q('What happened when you took one wire off?', Lines(1, 'The bulb went out: the circuit was not complete.')),
])

case = Sheet('case', 'Light from the sun', level=3, goals=['Read about solar electricity.'], blocks=[
    Case('Shuvo lives on a char, an island in a big river. There are no electricity wires there.',
         'His family has a **solar panel** on the roof. In the day it turns sunlight into electricity and stores it in a battery. At night the battery lights two lamps, so Shuvo can do his homework.'),
    Q('Where does Shuvo\'s electricity come from?', MCQ(['the Sun', 'a wall socket far away'], 0)),
    Q('Why is a solar panel useful on the char?', Lines(2, 'There are no electricity wires, but there is sunshine.')),
])

review = Sheet('review', 'Show what you know', level=3, goals=['Use electricity words.'], blocks=[
    Q('Find the words.', WordSearch(['CELL', 'WIRE', 'LAMP', 'LOOP', 'SUN'], size=7, seed=111)),
    Q('A lamp lights when the circuit is…', MCQ(['complete', 'broken'], 0)),
])

TOPIC = Topic(
    code='C4', strand='physical', title='Electricity', short='Electricity',
    subtitle='Things that use electricity, safety, simple circuits and switches, and where electricity comes from',
    outcomes=[
        'recognise the components of simple circuits involving cells.',
        'know how a switch can be used to break a circuit.',
        'recognize how a complete circuit allows for the flow of electricity.',
        'investigate how different energy sources generate electricity.',
        'investigate different electrical conductors and insulators.',
    ],
    sheets=[learn, facts, think, investigate, case, review],
    selfcheck=['name the parts of a circuit', 'make a lamp light', 'stay safe with electricity'],
    cover_art=art4.circuit(('cell', 'lamp', 'switch')),
)
