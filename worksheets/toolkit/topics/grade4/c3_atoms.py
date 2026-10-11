from build import Sheet, Topic
from ws import (P, H, Box, Vocab, Fig, Cols, Row, Case, Links, Lines, Blanks, Match, TrueFalse, MCQ, Order, Table,
                Ans, Sort, Label, Draw, Graph, WordSearch, Q, Part, Bullets, Pics)
import art
import art4

learn = Sheet('learn', 'Atoms: the building blocks of everything', level=1, goals=[
    'Explain that all matter is made of atoms.',
    'Describe and model the parts of an atom: nucleus, protons, neutrons and electrons.',
    'Compare the mass and charge of protons, neutrons and electrons.',
], blocks=[
    P('Imagine cutting a piece of gold in half, then in half again, and again, and again. Could you go on for ever? About '
      '2400 years ago, a Greek thinker called **Democritus** said no: in the end you would reach a tiny piece that cannot be '
      'cut. He called it *atomos*, which means "uncuttable". Today we know he was nearly right.', 'lead'),
    Cols(
        H('Everything is made of atoms', 3),
        P('Your body, the air, the Sun, a mango, a mobile phone: all matter is made of **atoms**. Atoms are incredibly small. '
          'The full stop at the end of this sentence contains millions and millions of them. There are about **118 kinds** of '
          'atom, one for each **element**.'),
        H('Inside an atom', 3),
        P('Atoms are made of even smaller particles:'),
        Bullets(['The **nucleus** is the tiny centre of the atom. It holds **protons** and **neutrons**.',
                 '**Protons** have a **positive** (+) electric charge.',
                 '**Neutrons** have **no** charge (they are neutral).',
                 '**Electrons** have a **negative** (−) charge. They move very fast in the space around the nucleus.']),
        Fig(art.atom_model(labels=art.ATOM_PARTS), 'A model of an atom (not to scale).', width='92%'),
        H('Comparing the particles', 3),
        Table(['Particle', 'Where it is', 'Charge', 'Mass'], [
            ['proton', 'in the nucleus', 'positive (+)', 'heavy (1 unit)'],
            ['neutron', 'in the nucleus', 'none (0)', 'heavy (1 unit)'],
            ['electron', 'around the nucleus', 'negative (−)', 'very light (about 2000 times lighter than a proton)']]),
        P('An atom has the **same number** of protons and electrons, so the + and − charges balance and the atom has no overall charge.'),
        Box('fact', P('An atom is mostly **empty space**! If the nucleus were the size of a marble in the middle of a football '
                      'field, the electrons would be like tiny specks of dust flying around the edges of the stadium.')),
        H('Different atoms, different elements', 3),
        P('The **number of protons** decides which element an atom is. Every hydrogen atom has 1 proton; every carbon atom has 6; '
          'every oxygen atom has 8; every gold atom has 79.'),
        Table(['Element', 'Protons', 'Neutrons (usual)', 'Electrons'], [['hydrogen', '1', '0', '1'], ['helium', '2', '2', '2'], ['carbon', '6', '6', '6'], ['oxygen', '8', '8', '8']], center=True),
        H('Atoms join together', 3),
        P('Atoms can join to make **molecules**. Two hydrogen atoms and one oxygen atom join to make one molecule of **water** (H~2~O).'),
        H('Models help us think', 3),
        P('Nobody can see inside an atom with their eyes. Scientists use **models**: drawings, balls and sticks, or computer '
          'pictures. Models help us understand, but they are not exactly like the real thing. Real electrons do not move in neat '
          'circles, and the nucleus is far smaller than in our drawings.'),
        Box('try', P('Make a model atom of carbon with clay or paper: 6 protons and 6 neutrons stuck together in the middle, and 6 electrons around them.')),
    ),
    Vocab([('atom', 'the tiny building block of all matter'), ('nucleus', 'the centre of an atom'), ('proton', 'a particle in the nucleus with a positive charge'),
           ('neutron', 'a particle in the nucleus with no charge'), ('electron', 'a very light particle with a negative charge, around the nucleus'),
           ('charge', 'positive (+) or negative (−) electricity'), ('molecule', 'two or more atoms joined together'), ('model', 'a way of showing something we cannot see')]),
])

facts = Sheet('facts', 'Parts of an atom', level=1, goals=['Label an atom.', 'Recall charges.'], blocks=[
    Q('Label the atom.', Label(art.atom_model(), art.ATOM_PARTS, width='66%', cols=4), marks=4),
    Q('Complete the table.',
      Table(['Particle', 'Charge', 'Where?'], [['proton', Ans('positive (+)'), Ans('nucleus')], ['neutron', Ans('none'), Ans('nucleus')], ['electron', Ans('negative (−)'), Ans('around the nucleus')]], center=True), marks=6),
    Q('Fill in the gaps.', Blanks('All matter is made of [atoms]. The centre of an atom is the [nucleus]. The number of [protons] decides which '
                                  'element an atom is. The lightest particle is the [electron].', extra=['cells', 'neutron']), marks=4),
    Q('True or false?', TrueFalse([('Neutrons have no charge.', True), ('Electrons are heavier than protons.', False, 'Electrons are about 2000 times lighter.'),
                                   ('There are about 118 kinds of atom.', True), ('An atom is mostly empty space.', True)]), marks=4),
])

think = Sheet('think', 'Thinking about atoms', level=2, goals=['Use the atom model.', 'Compare particles.'], blocks=[
    Q('An atom of nitrogen has 7 protons. How many electrons does it have? Explain.', Lines(2, '7 electrons, because atoms have the same number of protons and electrons so the charges balance.'), marks=2),
    Q('Most of the mass of an atom is in the nucleus. Explain why.', Lines(2, 'Protons and neutrons are heavy and are in the nucleus; electrons are very light.'), marks=2),
    Q('Two atoms both have 6 protons. Are they the same element? Explain.', Lines(2, 'Yes: both are carbon, because the number of protons decides the element.'), marks=2),
    Q('Give one way the drawing of an atom on the Learn it page is **useful** and one way it is **not like** a real atom.',
      Lines(3, 'Useful: it shows the nucleus, protons, neutrons and electrons and where they are. Not like a real atom: the nucleus is drawn far too big and electrons do not move in neat circles.'), marks=2),
])

investigate = Sheet('investigate', 'Build and compare atom models', level=2, goals=['Make models from data.', 'Find patterns in data.', 'Evaluate models.'], blocks=[
    Box('need', P('modelling clay or paper circles in three colours (one for protons, one for neutrons, one for electrons), card, glue.')),
    P('Make models of these atoms. Use the data to count the particles.'),
    Q('Complete the table.',
      Table(['Element', 'Protons', 'Neutrons', 'Electrons', 'Total particles', 'Mass (units)'], [
          ['helium', '2', '2', Ans('2'), Ans('6'), Ans('4')], ['lithium', '3', '4', Ans('3'), Ans('10'), Ans('7')],
          ['carbon', '6', '6', Ans('6'), Ans('18'), Ans('12')], ['oxygen', '8', '8', Ans('8'), Ans('24'), Ans('16')]], center=True),
      Lines(1, 'Mass = protons + neutrons (electrons are so light we leave them out).'), marks=8),
    Q('What pattern do you notice between the number of protons and the number of electrons?', Lines(1, 'They are always the same.'), marks=1),
    Q('Why do we not count the electrons when we work out the mass?', Lines(2, 'Electrons are about 2000 times lighter than protons, so they add almost nothing to the mass.'), marks=1),
])

case = Sheet('case', 'How did we find out about atoms?', level=3, goals=['Learn how ideas change with new evidence.', 'Order events on a timeline.', 'Think about creativity in science.'], blocks=[
    Links('Science', 'History', 'Maths'),
    Case('Nobody has ever seen inside an atom with their eyes. So how do we know what atoms are like? Over hundreds of years, '
         'scientists did clever experiments and changed their models when they found new **evidence**.',
         'In **1803**, **John Dalton** in England said that each element is made of its own kind of atom, like tiny hard balls. In '
         '**1897**, **J. J. Thomson** discovered the **electron**, so atoms could not be solid balls. In **1911**, **Ernest '
         'Rutherford** fired tiny particles at a thin sheet of gold. Most went straight through, but a few bounced back! This '
         'showed that atoms are mostly empty space with a tiny, heavy **nucleus**. In **1932**, **James Chadwick** discovered the '
         '**neutron**.',
         source='Based on the history of atomic models.'),
    Q('Put the discoveries in order on the timeline.',
      Order(['Democritus names the atom (about 400 BCE)', 'Dalton: elements are made of atoms (1803)', 'Thomson discovers the electron (1897)',
             'Rutherford discovers the nucleus (1911)', 'Chadwick discovers the neutron (1932)']), marks=4),
    Q('**Maths.** How many years passed between Dalton\'s idea and Chadwick\'s discovery?', Lines(1, '1932 − 1803 = 129 years'), marks=1),
    Q('Rutherford was surprised when some particles bounced back. Why did this make him change the model?', Lines(3, 'If atoms were solid balls or spread-out charge, the particles would not bounce back; the bounce showed there must be a tiny, heavy centre (the nucleus).'), marks=2),
    Q('Scientists combine **evidence** with **creative thinking**. Explain what this means using the story of the atom.', Lines(3, 'They did experiments to get evidence (like Rutherford\'s gold sheet), then imagined new models (a nucleus with electrons around it) to explain what they saw.'), marks=2),
])

review = Sheet('review', 'Show what you know', level=3, goals=['Use key vocabulary.', 'Answer test-style questions.'], blocks=[
    Q('Find the key words.', WordSearch(['ATOM', 'PROTON', 'NEUTRON', 'ELECTRON', 'NUCLEUS', 'CHARGE', 'MODEL', 'ELEMENT', 'MASS'], size=10, seed=413)),
    Q('Which particle has a negative charge?', MCQ(['proton', 'neutron', 'electron', 'nucleus'], 2), marks=1),
    Q('Which two particles are found in the nucleus?', MCQ(['protons and electrons', 'protons and neutrons', 'neutrons and electrons', 'only electrons'], 1, one_col=True), marks=1),
    Q('Draw a model of a helium atom (2 protons, 2 neutrons, 2 electrons). Label each part.', Draw('40mm', 'Helium atom', 'Nucleus with 2 protons (+) and 2 neutrons; 2 electrons (−) around it; labels.'), marks=3),
    Q('**Challenge.** Explain why an atom has no overall charge even though it contains charged particles.', Lines(3, 'It has the same number of positive protons and negative electrons, so the charges cancel out.'), marks=2),
])

TOPIC = Topic(
    code='C3', strand='physical', title='Atoms and Their Structure', short='Atoms',
    subtitle='Everything is made of atoms: protons, neutrons, electrons, their mass and charge, and how we found out',
    outcomes=[
        'understand that all matter is made of atoms, which are composed of protons, neutrons and electrons.',
        'describe and model the structure of the atom: nucleus, protons, neutrons and electrons.',
        'compare the mass and charge of protons, neutrons and electrons.',
    ],
    sheets=[learn, facts, think, investigate, case, review],
    selfcheck=['explain that all matter is made of atoms', 'label the parts of an atom', 'compare the charge and mass of the particles',
               'make atom models from data', 'explain how models of the atom changed', 'say why models are useful but not perfect'],
    cover_art=art.atom_model(labels=art.ATOM_PARTS),
)
