from build import Sheet, Topic
from ws import (P, H, Box, Vocab, Fig, Cols, Row, Case, Links, Lines, Blanks, Match, TrueFalse, MCQ, Order, Table,
                Ans, Sort, Label, Draw, Graph, WordSearch, Q, Part, Bullets)
import art

learn = Sheet('learn', 'Atoms: nothing is lost, everything changes', level=1, goals=[
    'Explain that matter is made of atoms and that atoms are conserved in physical and chemical changes.',
    'Explain why mass stays the same in a closed system.',
    'Describe simply how nuclear changes are different.',
], blocks=[
    P('Everything around you (air, water, your desk, your body, the stars) is made of **matter**, and all matter is made '
      'of unbelievably tiny particles called **atoms**. A single human hair is about half a million atoms wide!', 'lead'),
    Cols(
        H('Atoms and elements', 3),
        P('There are about 118 different kinds of atom. A material made of only one kind of atom is an **element**: oxygen, '
          'carbon, iron, gold and aluminium are elements. Atoms can join together to make **molecules**. A water molecule is '
          'two hydrogen atoms joined to one oxygen atom: **H₂O**.'),
        Row([Fig(art.water_molecule())], [Fig(art.atom_model(labels=art.ATOM_PARTS))], widths=[1, 1.6]),
        P('Each atom has a tiny centre called the **nucleus**, made of **protons** and **neutrons**, with even tinier '
          '**electrons** moving around it.'),
        H('Atoms are conserved', 3),
        P('In a **physical change** (melting, dissolving, evaporating) atoms just move around. In a **chemical change** '
          '(burning, rusting, cooking) atoms are **rearranged** to make new substances. But in both kinds of change, **no '
          'atoms are made and none are destroyed**. This is the **law of conservation of mass**: the total mass stays the '
          'same.'),
        Bullets(['100 g of ice melts into 100 g of water.', '250 g of water + 20 g of salt makes 270 g of salt solution.']),
        H('Open and closed systems', 3),
        P('Sometimes mass *seems* to disappear. When vinegar and baking soda react in an open cup, the mass goes down. That is '
          'because a **gas** (carbon dioxide) escapes into the air. If the reaction happens in a **sealed bag**, a **closed '
          'system**, nothing can escape and the mass stays exactly the same.'),
        Row([Fig(art.balance_bag(True))], [Fig(art.balance_bag(False))]),
        Box('history', P('In the 1780s the French scientist **Antoine Lavoisier** weighed substances very carefully before '
                         'and after reactions in sealed containers. He showed that mass is never lost, only changed. He is '
                         'often called the father of modern chemistry.')),
        H('Energy is conserved too', 3),
        P('Energy cannot be made or destroyed either: it only moves from one place to another or changes form. In a closed '
          'system, the total amount of **energy** and **matter** stays the same.'),
        H('Nuclear changes: atoms change', 3),
        P('In a **nuclear** change, the nucleus itself changes. In a nuclear power station, big uranium atoms are **split** '
          'into smaller atoms of different elements, giving out a huge amount of heat. In the Sun, small hydrogen atoms '
          '**join** to make helium. So here atoms are **not** conserved: one element turns into another. But if you count '
          'all the **protons and neutrons**, the total before and after is the **same**.'),
        Table(['Before', 'After'], [['1 uranium atom: 236 protons + neutrons', 'barium (141) + krypton (92) + 3 free neutrons']], center=True),
        P('141 + 92 + 3 = **236**. Nothing is lost!'),
    ),
    Vocab([('matter', 'anything that has mass and takes up space'), ('atom', 'the tiny building block of matter'),
           ('element', 'a substance made of only one kind of atom'), ('molecule', 'atoms joined together'),
           ('conservation of mass', 'mass stays the same in a change'), ('closed system', 'nothing can get in or out'),
           ('nucleus', 'the centre of an atom'), ('nuclear change', 'a change in the nucleus that turns one element into another')]),
])

facts = Sheet('facts', 'Atoms and mass', level=1, goals=['Label an atom.', 'Recall the law of conservation of mass.'], blocks=[
    Q('Label the atom.', Label(art.atom_model(), art.ATOM_PARTS, width='70%'), marks=4),
    Q('Fill in the gaps.',
      Blanks('All matter is made of tiny [atoms]. A substance made of only one kind of atom is an [element]. In physical and '
             'chemical changes, atoms are not made or [destroyed], so the total [mass] stays the same. A sealed bag is a '
             '[closed] system.', extra=['open', 'bigger']), marks=5),
    Q('Work out the missing masses.',
      Table(['Change', 'Mass before', 'Mass after'], [['ice melting', '100 g of ice', Ans('100 g of water')],
                                                      ['dissolving sugar', '200 g water + 15 g sugar', Ans('215 g of sugar solution')],
                                                      ['freezing juice', '330 g of juice', Ans('330 g of ice lolly')]], center=True), marks=3),
    Q('True or false?', TrueFalse([
        ('When sugar dissolves, its atoms are destroyed.', False, 'The atoms are still there, spread through the water.'),
        ('Water is made of hydrogen and oxygen atoms.', True), ('In a nuclear change, one element can turn into another.', True),
        ('Burning wood makes the atoms disappear.', False, 'The atoms are rearranged into gases, smoke and ash.')]), marks=4),
])

think = Sheet('think', 'Where did the mass go?', level=2, goals=['Explain changes in mass using open and closed systems.', 'Apply conservation to new examples.'], blocks=[
    Q('A candle has a mass of 50 g. After burning for an hour its mass is 42 g. Has mass been destroyed? Explain.',
      Lines(3, 'No: the wax reacted with oxygen and turned into carbon dioxide gas and water vapour, which escaped into the air (an open system).'), marks=2),
    Q('Describe an experiment to show that mass is conserved when a candle burns.',
      Lines(3, 'Burn it inside a sealed (closed) container on a balance; the total mass before and after would be the same (with an adult, safely).'), marks=2),
    Q('An iron nail gets heavier as it rusts. Where does the extra mass come from?',
      Lines(2, 'Iron atoms join with oxygen (and water) from the air; the added atoms add mass.'), marks=2),
    Q('Use the idea of conservation to check this nuclear change. Are the protons and neutrons conserved?',
      Table(['Before', 'After'], [['a nucleus with 235 protons + neutrons, hit by 1 neutron', '139 + 94 + 3 free neutrons']], center=True),
      Lines(2, 'Before: 235 + 1 = 236. After: 139 + 94 + 3 = 236. Yes, the total is the same.'), marks=2),
])

investigate = Sheet('investigate', 'Is mass conserved?', level=2, goals=['Measure mass accurately.', 'Compare open and closed systems.', 'Explain unexpected results.'], blocks=[
    Box('need', P('a digital balance, a zip-lock bag, a small cup, vinegar, baking soda, a teaspoon, an open plastic cup')),
    Box('safety', P('Wear goggles. Vinegar can sting your eyes. Point the bag away from faces.')),
    P('Class 5C carried out three tests and measured the mass before and after.'),
    Q('Complete the table.',
      Table(['Test', 'Mass before (g)', 'Mass after (g)', 'Change (g)'], [
          ['dissolving salt in water (open cup)', '270', '270', Ans('0')],
          ['vinegar + baking soda in a sealed bag', '312', '312', Ans('0')],
          ['vinegar + baking soda in an open cup', '312', '309', Ans('−3')]], center=True), marks=3),
    Q('Why did the mass go down in the open cup but not in the sealed bag?',
      Lines(3, 'The reaction made a gas (carbon dioxide). In the open cup the gas escaped into the air; in the sealed bag it was trapped, so all the atoms stayed.'), marks=2),
    Q('What evidence showed that a gas was made?', Lines(2, 'Bubbles and fizzing; the sealed bag puffed up.'), marks=1),
    Q('Write a conclusion about conservation of mass.', Lines(2, 'In a closed system mass is conserved: no atoms are gained or lost, even in a chemical change.'), marks=2),
    Q('The balance shows whole grams only. How could this affect the results?', Lines(2, 'Small changes of less than 1 g would not show; a more precise balance (0.1 g) would be better.'), marks=1),
])

case = Sheet('case', 'Energy from atoms: Rooppur', level=3, goals=['Explain nuclear power simply.', 'Weigh advantages and disadvantages.', 'Consider different perspectives.'], blocks=[
    Links('Science', 'Geography', 'Economics', 'Ethics', 'Environment'),
    Case('Bangladesh needs more and more electricity for homes, schools, hospitals and factories. Most of it comes from '
         'burning **natural gas**, which is running out and gives off carbon dioxide.',
         'At **Rooppur**, in Pabna district on the bank of the Padma, Bangladesh is building its **first nuclear power plant**, '
         'with help from Russia, and it is starting up in the mid-2020s. Inside its reactors, uranium atoms are split. The '
         'heat boils water into steam, which spins turbines to make electricity. A small amount of uranium can produce a '
         'very large amount of energy, and the plant gives off almost no carbon dioxide while working.',
         'But nuclear power also has challenges: it is very **expensive** to build; it must be run with great **safety** '
         'care; and the used fuel stays **radioactive** (dangerous) for thousands of years, so it must be stored very carefully.',
         source='Based on public information about the Rooppur Nuclear Power Plant.'),
    Q('Put the steps of making electricity at Rooppur in order.',
      Order(['Uranium atoms split in the reactor.', 'This releases a lot of heat.', 'The heat boils water into steam.',
             'Steam spins a turbine.', 'The turbine turns a generator, making electricity.'], seed=8), marks=3),
    Q('Complete the table.',
      Table(['Advantages of nuclear power', 'Disadvantages of nuclear power'], [
          [Ans('a lot of energy from a little fuel'), Ans('very expensive to build')],
          [Ans('almost no carbon dioxide while working'), Ans('used fuel is radioactive for thousands of years')],
          [Ans('steady power day and night'), Ans('accidents, though rare, can be very serious')]], center=True), marks=6),
    Q('What might each person think about the plant?',
      Table(['Person', 'View'], [['a factory owner in Dhaka', Ans('More reliable electricity will help my business grow.')],
                                 ['a farmer living near Rooppur', Ans('Will my land and the river stay safe? Will there be jobs for us?')],
                                 ['a climate scientist', Ans('It cuts carbon dioxide compared with gas, but solar and wind are also needed.')]], widths=['34%', '66%']), marks=3),
    Q('Your opinion: should Bangladesh get more electricity from nuclear power, solar power or both? Give reasons.',
      Lines(4, 'Accept balanced reasoning, e.g. both: nuclear for steady power, solar for clean cheap power in the day; solar needs land and storage.'), marks=2),
])

review = Sheet('review', 'Show what you know', level=3, goals=['Use key vocabulary.', 'Answer test-style questions.'], blocks=[
    Q('Find the key words.', WordSearch(['ATOM', 'ELEMENT', 'MOLECULE', 'MASS', 'NUCLEUS', 'PROTON', 'NEUTRON', 'ELECTRON', 'SEALED'], size=11, seed=121)),
    Q('Salt (20 g) is dissolved in water (180 g). What is the mass of the solution?', MCQ(['160 g', '180 g', '200 g', '220 g'], 2), marks=1),
    Q('Which is a closed system?', MCQ(['an open pan of boiling water', 'a sealed jar', 'a candle burning in a room', 'a puddle drying'], 1), marks=1),
    Q('Draw particle pictures to show that 10 atoms before a change are still 10 atoms after.',
      Row([Draw('35mm', 'before', '10 atoms drawn, some joined in pairs.')], [Draw('35mm', 'after', 'The same 10 atoms, rearranged into different groups.')]), marks=2),
    Q('**Challenge.** Explain why scientists say atoms are conserved in chemical changes but not in nuclear changes, and what is still conserved in a nuclear change.',
      Lines(4, 'In chemical changes atoms only rearrange, so the same atoms are there before and after. In nuclear changes the nucleus changes, so atoms of one element become another; but the total number of protons plus neutrons stays the same.'), marks=3),
])

TOPIC = Topic(
    code='C3', strand='physical', title='Matter, Atoms and Conservation', short='Atoms and conservation',
    subtitle='Atoms and elements, conservation of mass in open and closed systems, and nuclear changes',
    outcomes=[
        'understand that matter is conserved because atoms are conserved in physical and chemical processes.',
        'identify that in nuclear processes, atoms are not conserved, but the total number of protons plus neutrons is conserved.',
        'understand that the total amount of energy and matter in closed systems is conserved.',
    ],
    sheets=[learn, facts, think, investigate, case, review],
    selfcheck=['explain that matter is made of atoms', 'explain why mass is conserved in physical and chemical changes',
               'explain the difference between open and closed systems', 'measure mass before and after a change',
               'explain how nuclear changes are different', 'discuss the advantages and disadvantages of nuclear power'],
    cover_art=art.atom_model(labels=art.ATOM_PARTS, w='70%'),
)
