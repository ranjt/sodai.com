from build import Sheet, Topic
from ws import (P, H, Box, Vocab, Fig, Cols, Row, Case, Links, Lines, Blanks, Match, TrueFalse, MCQ, Order, Table,
                Ans, Sort, Label, Draw, Graph, WordSearch, Q, Part, Bullets, Pics)
import art
import art4

learn = Sheet('learn', 'Electricity and circuits', level=1, goals=[
    'Build and draw series circuits using conventional symbols.',
    'Sort materials into conductors and insulators and explain how they are used in cables and plugs.',
    'Predict how changing a circuit changes it, and explain why switches and safety devices matter.',
], blocks=[
    P('Press a switch and the fan starts spinning. Plug in a phone and it charges. Electricity powers our homes, schools, '
      'hospitals and factories. But how does it get from the battery or the wall to the bulb? It needs a complete path called a '
      '**circuit**.', 'lead'),
    Cols(
        H('A complete circuit', 3),
        P('Electricity flows from one end of a **cell** (battery), through **wires** and **components** such as a bulb, and back to '
          'the other end of the cell. The path must be **complete**, with no gaps. If there is a gap, the electricity stops and the '
          'bulb goes out. A circuit where everything is joined in one loop is a **series circuit**.'),
        Fig(art4.circuit(), 'A series circuit with a cell, a lamp and a closed switch.', width='76%'),
        H('Circuit symbols', 3),
        P('Scientists all over the world draw circuits with the same simple **symbols**, so everyone can understand them.'),
        Fig(art4.circuit_symbols(), 'Circuit symbols.', span=True, width='86%'),
        H('Conductors and insulators', 3),
        P('**Conductors** let electricity flow through them easily. Most **metals** are good conductors: copper, aluminium, iron, '
          'steel, silver. Graphite (pencil "lead") conducts too. **Insulators** do not let electricity flow: plastic, rubber, wood, '
          'glass, dry paper and cloth.'),
        Pics([('paperclip', 'steel clip'), ('key', 'metal key'), ('coin', 'coin'), ('pencil', 'pencil'), ('glass bottle', 'glass'), ('sponge', 'rubber'), ('wood', 'wood'), ('plastic bottle', 'plastic')],
             cols=4, size='12mm', small=True),
        P('Electrical **cables** have **copper** wires inside, because copper is an excellent conductor. They are covered in '
          '**plastic** to stop electricity reaching our hands. Plugs and switches have plastic cases for the same reason.'),
        H('Changing a circuit', 3),
        Table(['Change', 'What happens to the bulb'], [
            ['add another cell', 'brighter'], ['add another bulb', 'each bulb is dimmer'], ['use a longer wire', 'a little dimmer'],
            ['use a thinner wire', 'a little dimmer'], ['open the switch', 'goes out'], ['swap the bulb for a buzzer or motor', 'it buzzes or spins']]),
        H('Switches and safety', 3),
        P('A **switch** makes a gap in the circuit (off) or closes it (on), so we can control devices. **Fuses** and **circuit '
          'breakers** are safety switches: if too much electricity flows, they cut it off before wires get hot and start a fire.'),
        Box('safety', P('**Mains electricity** from the wall socket (220 volts in Bangladesh) is about 150 times stronger than a 1.5 volt '
                        'cell and can kill. Never touch sockets or switches with wet hands, never push anything into a socket, do not '
                        'plug too many things into one socket, and never fly kites near power lines.')),
        H('Electricity all around us', 3),
        P('At **home**: lights, fans, fridges, pumps, phone chargers. At **school**: computers, projectors, bells. In the '
          '**community**: traffic lights, hospital machines, water pumps, street lights and mobile phone towers. Each is an '
          '**electrical system**: a source, wires, switches and components working together.'),
    ),
    Vocab([('circuit', 'a complete path for electricity'), ('cell (battery)', 'a store of energy that pushes electricity round a circuit'),
           ('component', 'a part of a circuit, such as a bulb or switch'), ('conductor', 'lets electricity flow'), ('insulator', 'does not let electricity flow'),
           ('switch', 'opens or closes a gap in a circuit'), ('series circuit', 'all components in one loop'), ('mains electricity', 'electricity from the wall socket')]),
])

facts = Sheet('facts', 'Circuits and symbols', level=1, goals=['Use circuit symbols.', 'Sort conductors and insulators.'], blocks=[
    Q('Name each symbol.', Fig(art4.circuit_symbols(names=False), width='86%'),
      Table(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'], [[Ans('cell'), Ans('battery'), Ans('lamp'), Ans('open switch'), Ans('closed switch'), Ans('buzzer'), Ans('motor'), Ans('wire')]], center=True), marks=8),
    Q('Sort the materials.', Sort(['Conductor', 'Insulator'], [('copper', 'Conductor'), ('steel spoon', 'Conductor'), ('aluminium foil', 'Conductor'), ('pencil lead (graphite)', 'Conductor'),
                                                              ('plastic ruler', 'Insulator'), ('rubber band', 'Insulator'), ('wooden stick', 'Insulator'), ('glass', 'Insulator')]), marks=8),
    Q('Will the bulb light? Write **yes** or **no** and explain.',
      Table(['Circuit', 'Lights?', 'Why?'], [['cell, bulb and wires in a complete loop', Ans('yes'), Ans('the circuit is complete')], ['one wire is not connected', Ans('no'), Ans('there is a gap')],
                                             ['a plastic straw joins the gap', Ans('no'), Ans('plastic is an insulator')], ['a metal key joins the gap', Ans('yes'), Ans('metal is a conductor')]], widths=['46%', '16%', '38%']), marks=4),
])

think = Sheet('think', 'Predict and explain', level=2, goals=['Predict changes to circuits.', 'Explain safety features.'], blocks=[
    Q('Draw a circuit diagram with two cells, one lamp and a switch. Use the correct symbols.', Draw('42mm', 'My circuit', 'A rectangle loop with two cell symbols (or a battery), a lamp (circle with a cross) and a switch.'), marks=3),
    Q('Predict and explain.',
      Table(['Change', 'Prediction', 'Reason'], [['add a second bulb', Ans('both bulbs dimmer'), Ans('the same cell shares its push between two bulbs')],
                                                 ['add a second cell', Ans('bulb brighter'), Ans('more push makes more electricity flow')],
                                                 ['make the wire much longer', Ans('a little dimmer'), Ans('a long wire lets less electricity through')]], widths=['30%', '30%', '40%']), marks=6),
    Q('Why is the inside of a cable made of copper and the outside made of plastic?', Lines(2, 'Copper conducts electricity well; plastic is an insulator that keeps the electricity in and protects us.'), marks=2),
    Q('Why is it dangerous to use a hair dryer with wet hands in the bathroom?', Lines(2, 'Water with dirt or salt can conduct electricity, so electricity could flow through your body and give a dangerous shock.'), marks=1),
])

investigate = Sheet('investigate', 'Does wire length change brightness?', level=2, goals=['Plan a fair test.', 'Measure with a light meter.', 'Draw and use a line graph.'], blocks=[
    P('Class 4C made a circuit with a cell, a bulb and a long piece of thin nichrome wire. They moved a crocodile clip along the wire to change the '
      'length in the circuit, and used a light meter app to measure the brightness of the bulb in lux.'),
    Q('Complete the plan.', Table(None, [['Change', Ans('length of the wire in the circuit')], ['Measure', Ans('brightness of the bulb (lux)')],
                                         ['Keep the same', Ans('the same cell, bulb and type of wire; the meter at the same distance; a dark room')]], widths=['26%', '74%']), marks=3),
    Q('Draw a line graph.',
      Table(['Wire length (cm)', '10', '20', '30', '40', '50'], [['Brightness (lux)', '200', '160', '130', '110', '95']], center=True),
      Graph(['10', '20', '30', '40', '50'], [200, 160, 130, 110, 95], 'Brightness (lux)', 'Wire length (cm)', ymax=220, step=20, kind='line', width=110, height=50), marks=3),
    Q('Describe the pattern.', Lines(2, 'The longer the wire, the dimmer the bulb.'), marks=2),
    Q('Predict the brightness for 60 cm.', Lines(1, 'about 80–85 lux'), marks=1),
    Q('A dimmer switch for a lamp works in a similar way. How do you think it works?', Lines(1, 'It changes how much wire (resistance) the electricity has to go through.'), marks=1),
])

case = Sheet('case', 'Lights for every home', level=3, goals=['Use data about electricity in Bangladesh.', 'Think about electrical safety.', 'Plan how to save electricity.'], blocks=[
    Links('Science', 'History', 'Maths', 'Citizenship'),
    Case('In the year 2000, only about **one in three** homes in Bangladesh had electricity. Children studied by the light of '
         'kerosene lamps, which were smoky and dangerous. Since then, new power stations, power lines and millions of **solar '
         'home systems** have brought electricity to almost **every home** in the country.',
         'Electricity has changed lives: children can study at night, farmers use electric pumps, shops stay open and people '
         'charge mobile phones. But more electricity also means more need for **safety** and for **saving energy**, because much '
         'of it is made by burning gas and oil.',
         source='Approximate figures from World Bank data on access to electricity in Bangladesh.'),
    Q('Homes with electricity in Bangladesh (approximate).',
      Table(['Year', '2000', '2005', '2010', '2015', '2020'], [['Homes with electricity (out of 100)', '32', '44', '55', '74', '96']], center=True),
      Graph(['2000', '2005', '2010', '2015', '2020'], [32, 44, 55, 74, 96], 'Homes (out of 100)', 'Year', ymax=100, step=10, kind='line', width=110, height=50),
      Part('Draw the line graph.'),
      Part('By how much did it rise from 2000 to 2020?', Lines(1, '96 − 32 = 64 more homes out of every 100')), marks=3),
    Q('Give two ways electricity has helped families.', Lines(2, 'Children can study at night with bright, safe light; fans and pumps; charging phones; shops and clinics can work.'), marks=2),
    Q('Spot the danger. What is wrong in each case and how should it be fixed?',
      Table(['Situation', 'Danger and fix'], [['six plugs in one socket with an adaptor', Ans('overloading can overheat and start a fire; use fewer plugs')],
                                              ['a cable with the plastic cover cracked', Ans('bare wire can give a shock; replace the cable')],
                                              ['a kite caught on a power line', Ans('never pull it down; electricity can travel down the string; tell an adult')]], widths=['40%', '60%']), marks=3),
    Q('Write three tips for saving electricity at home.', Lines(3, 'switch off lights and fans when leaving; use LED bulbs; unplug chargers; open windows for light and air.'), marks=2),
])

review = Sheet('review', 'Show what you know', level=3, goals=['Use key vocabulary.', 'Answer test-style questions.'], blocks=[
    Q('Find the key words.', WordSearch(['CIRCUIT', 'CELL', 'BULB', 'SWITCH', 'WIRE', 'COPPER', 'PLASTIC', 'MOTOR', 'BUZZER'], size=10, seed=416)),
    Q('Which material is a conductor?', MCQ(['rubber', 'plastic', 'copper', 'wood'], 2), marks=1),
    Q('What happens if you add a second bulb to a series circuit?', MCQ(['both bulbs are brighter', 'both bulbs are dimmer', 'nothing changes', 'the cell explodes'], 1, one_col=True), marks=1),
    Q('Design a burglar alarm for a box: when the lid opens, a buzzer sounds. Draw the circuit.', Draw('44mm', 'Box alarm', 'Cell, buzzer and a switch made of foil strips; opening the lid closes the switch and completes the circuit.'), marks=3),
    Q('**Challenge.** Why is it important to have a switch in a circuit for a motor that turns a fan?', Lines(3, 'So we can turn the fan on and off safely without touching wires; we can stop it quickly if fingers or clothes get caught.'), marks=2),
])

TOPIC = Topic(
    code='C6', strand='physical', title='Electricity and Circuits', short='Electricity',
    subtitle='Complete circuits, symbols, conductors and insulators, changing circuits, switches and safety',
    outcomes=[
        'investigate how some materials are better conductors of electricity than others.',
        'investigate how some metals are good conductors of electricity while most other materials are not.',
        'know why metals are used for cables and wires, and why plastics are used to cover wires and as covers for plugs and switches.',
        'predict and test the effects of making changes to circuits, including the length or thickness of wire and the number and type of components.',
        'represent series circuits with drawings and conventional symbols.',
        'conduct investigations with different electrical circuits that operate lights, a small motor or induced magnetism, to determine what happens when the components of the circuit are altered.',
        'explain the importance of switches and other safety control mechanisms to the design and operation of electrical circuits and devices.',
        'identify examples of applications of electrical systems in the school, the community and the home, and explain how they are used.',
    ],
    cambridge=['Unit 5 Electricity and magnetism (5.1–5.6)'],
    sheets=[learn, facts, think, investigate, case, review],
    selfcheck=['build and draw a series circuit', 'use circuit symbols', 'sort conductors and insulators', 'predict changes to a circuit',
               'investigate wire length and brightness', 'stay safe with electricity'],
    cover_art=art4.circuit(),
)
