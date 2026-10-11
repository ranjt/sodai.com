from build import Sheet, Topic
from ws import (P, H, Box, Vocab, Fig, Cols, Row, Case, Links, Lines, Blanks, Match, TrueFalse, MCQ, Order, Table,
                Ans, Sort, Label, Draw, Graph, WordSearch, Q, Part, Bullets)
import art

learn = Sheet('learn', 'Cells: the building blocks of life', level=1, goals=[
    'Recall that all living things are made of cells.',
    'Describe specialised cells in the human body and their jobs.',
    'Explain the levels of organisation: cell, tissue, organ, organ system, organism.',
], blocks=[
    P('A house is built from thousands of bricks. Your body is built from about **30 trillion** tiny units called '
      '**cells**. Every living thing, from a mango tree to a tiger, is made of cells. Most cells are far too small to see '
      'without a **microscope**.', 'lead'),
    Cols(
        H('Who discovered cells?', 3),
        P('In 1665 the English scientist **Robert Hooke** looked at a thin slice of cork through a microscope he had built. '
          'He saw rows of tiny boxes that reminded him of small rooms, so he called them **cells**. A few years later, '
          'Antonie van Leeuwenhoek in the Netherlands made better lenses and saw living cells, such as blood cells and tiny '
          'creatures swimming in pond water.'),
        Fig(art.microscope(), 'A school microscope. The lenses make things look much bigger.'),
        H('What is inside a cell?', 3),
        P('Animal cells have three main parts. The **cell membrane** is a thin skin that holds the cell together and controls '
          'what goes in and out. The **cytoplasm** is a jelly where the cell\'s work happens. The **nucleus** is the control '
          'centre: it holds the instructions that tell the cell what to do. Plant cells also have a tough **cell wall** and '
          'green **chloroplasts** that trap light.'),
        Fig(art.animal_cell(labels=art.CELL_PARTS), 'An animal cell.'),
        H('Specialised cells', 3),
        P('Cells come in different shapes because they do different jobs. Their shape helps them do their job well.'),
        Bullets([
            '**Red blood cells** are round and dented in the middle, like a doughnut without a hole. This gives them a large surface to carry oxygen, and they can squeeze through tiny blood vessels.',
            '**Nerve cells** are long and thin, with branches, to carry messages quickly over long distances.',
            '**Muscle cells** are long and can get shorter (contract) to move the body.',
            '**Fat cells** store energy and help keep us warm.',
            '**Skin cells** fit tightly together like tiles to make a protective layer.',
        ]),
        Fig(art.specialised_cells(), 'Some specialised cells in the human body (not drawn to scale).'),
        H('From cells to a whole body', 3),
        P('Cells of the same kind group together to make a **tissue**, such as muscle tissue. Different tissues work together '
          'to make an **organ**, such as the heart. Organs work together in an **organ system**, such as the circulatory '
          'system. All the organ systems together make an **organism**: a living thing, like you!'),
        Fig(art.organisation_levels(), 'Levels of organisation in the human body.'),
        Box('think', P('Think of a school: one **learner** (cell) belongs to a **class** (tissue), classes make a '
                       '**year group** (organ), year groups make the **school** (organ system)… What would the organism be?')),
        Box('fact', P('Your body makes about 2 million new red blood cells **every second**. Each one lives for about '
                      '120 days.')),
    ),
    Vocab([('cell', 'the smallest building block of a living thing'), ('nucleus', 'control centre of a cell'),
           ('cell membrane', 'thin layer around a cell that controls what goes in and out'),
           ('cytoplasm', 'jelly inside a cell where its work happens'), ('specialised cell', 'a cell with a special shape for a special job'),
           ('tissue', 'a group of similar cells doing the same job'), ('organ', 'different tissues working together'),
           ('organism', 'a whole living thing'), ('microscope', 'instrument that makes small things look bigger')]),
])

facts = Sheet('facts', 'Cells and specialised cells', level=1, goals=['Label a cell.', 'Match cells to their jobs.',
                                                                   'Order the levels of organisation.'], blocks=[
    Q('Label the parts of the animal cell.', Label(art.animal_cell(), art.CELL_PARTS, width='70%', cols=3), marks=3),
    Q('Write the letter of each cell next to its name.', Fig(art.specialised_cells(names=False)),
      Table(['Cell', 'Letter', 'Its job'], [['red blood cell', Ans('A'), Ans('carries oxygen')],
                                            ['nerve cell', Ans('B'), Ans('carries messages')],
                                            ['muscle cell', Ans('C'), Ans('contracts to move the body')],
                                            ['fat cell', Ans('D'), Ans('stores energy, keeps us warm')],
                                            ['skin cell', Ans('E'), Ans('makes a protective layer')]], widths=['28%', '14%', '58%']), marks=10),
    Q('Number the levels of organisation from smallest (1) to largest (5).',
      Order(['cell', 'tissue', 'organ', 'organ system', 'organism'], seed=3), marks=2),
    Q('True or false?', TrueFalse([
        ('All living things are made of cells.', True),
        ('The nucleus controls what the cell does.', True),
        ('A tissue is made of many different organs.', False, 'A tissue is made of many similar cells.'),
        ('Robert Hooke named cells after looking at cork.', True)]), marks=4),
])

think = Sheet('think', 'Shape and job', level=2, goals=['Explain how a cell\'s shape suits its job.',
                                                       'Use the levels of organisation to explain how the body is built.'], blocks=[
    Q('Explain how the shape of each cell helps it do its job.',
      Part('nerve cell', Lines(2, 'It is long and thin with branches, so it can carry messages a long way and connect to many other cells.')),
      Part('red blood cell', Lines(2, 'Its dented disc shape gives a large surface to carry oxygen, and it can bend to squeeze through narrow vessels.')),
      Part('skin cells', Lines(2, 'They are flat and fit tightly together, making a barrier that keeps germs out.')), marks=6),
    Q('Complete the table for the digestive system.',
      Table(['Level', 'Example'], [['cell', Ans('a stomach muscle cell')], ['tissue', Ans('muscle tissue in the stomach wall')],
                                    ['organ', Ans('stomach')], ['organ system', Ans('digestive system')],
                                    ['organism', Ans('a human')]], widths=['30%', '70%']), marks=5),
    Q('Rumana says, "If one organ stops working, the whole organism is in danger." Use the idea of organ systems to explain '
      'whether she is right.',
      Lines(3, 'Yes: organs depend on each other. For example, if the heart stops, oxygen from the lungs cannot reach the cells, so all the systems fail.'), marks=2),
    Q('A plant cell has a cell wall and chloroplasts. An animal cell does not. Suggest why plant cells need these.',
      Lines(3, 'The cell wall makes plant cells strong so the plant can stand up without bones; chloroplasts trap light to make food.'), marks=2),
])

investigate = Sheet('investigate', 'Looking at cells with a microscope', level=2, goals=[
    'Use a microscope safely.', 'Calculate magnification.', 'Observe, draw and compare cells.'], blocks=[
    Box('need', P('microscope, a thin piece of onion skin, a glass slide, a cover slip, a drop of iodine (stain), a pencil')),
    Box('safety', P('Handle glass slides carefully. Iodine stains skin and clothes. Never point a microscope mirror at the Sun.')),
    Q('Magnification tells us how many times bigger something looks. Multiply the eyepiece by the objective lens.',
      Table(['Eyepiece lens', 'Objective lens', 'Total magnification'], [['×10', '×4', Ans('×40')], ['×10', '×10', Ans('×100')],
                                                                         ['×10', '×40', Ans('×400')]], center=True), marks=3),
    Q('Follow the steps to look at onion cells. Then draw what you see.',
      Bullets(['Peel a thin, see-through layer from the inside of an onion piece.', 'Lay it flat on the slide and add one drop of iodine.',
               'Lower a cover slip gently on top.', 'Start with the smallest objective lens, focus, then try a bigger one.'], ordered=True),
      Row([Draw('55mm', 'My drawing of onion cells (×100)', 'Brick-shaped cells in rows; a cell wall around each; a dark round nucleus in many cells.')],
          [Part('Describe the shape of the cells.', Lines(2, 'Like long bricks or boxes, arranged in rows, touching each other.')),
           Part('Which part of the cell did the iodine make easier to see?', Lines(2, 'The nucleus (it stains darker).'))]),
      marks=5),
    Q('Compare onion cells with cheek cells (animal cells). Fill in the table.',
      Table(['Feature', 'Onion cell (plant)', 'Cheek cell (animal)'], [
          ['shape', Ans('regular, brick-like'), Ans('irregular, rounded')], ['cell wall?', Ans('yes'), Ans('no')],
          ['nucleus?', Ans('yes'), Ans('yes')]], center=True), marks=3),
    Q('Why do scientists add a stain such as iodine?',
      Lines(2, 'Cells are almost see-through; a stain colours parts of the cell so they are easier to see.'), marks=1),
])

case = Sheet('case', 'Giving blood: cells that save lives', level=3, goals=[
    'Explain the jobs of the parts of blood.', 'Use data and reasoning about a real health issue.',
    'Discuss why people choose to help others.'], blocks=[
    Links('Science', 'Health', 'Maths', 'Ethics', 'Community'),
    Case('Blood looks like a red liquid, but it is really a mixture of cells floating in a yellow liquid called **plasma**. '
         '**Red blood cells** carry oxygen. **White blood cells** fight germs. Tiny **platelets** help blood clot to stop '
         'bleeding.',
         'In Bangladesh, hospitals need blood every day for accident victims, mothers giving birth and people having '
         'operations. Many children have **thalassaemia**, an inherited condition in which the body cannot make enough '
         'healthy red blood cells. Many of these children need a blood transfusion every few weeks.',
         'Healthy adults can give (donate) blood safely. In 1977, students at Dhaka Medical College started **Sandhani**, a '
         'volunteer group that encourages young people to give blood. Today there are many blood donor groups across the '
         'country. The body replaces the donated blood: the liquid within a day or two, and the red blood cells within a few weeks.',
         source='Information from general medical sources; donors must meet age and health rules set by their blood bank.'),
    Q('Match each part of blood to its job.',
      Match([('red blood cells', 'carry oxygen'), ('white blood cells', 'fight germs'), ('platelets', 'help blood clot'),
             ('plasma', 'liquid that carries the cells and nutrients')]), marks=4),
    Q('A person usually gives about 450 ml of blood. An adult has about 5 litres (5000 ml) of blood.',
      Part('How much blood is left in the donor\'s body straight after giving?', Lines(1, '5000 − 450 = 4550 ml')),
      Part('About what fraction of their blood did they give? Circle: one half · one tenth · one hundredth', Lines(1, 'about one tenth (450 is about 1/10 of 5000)')),
      marks=2),
    Q('Why might a child with thalassaemia feel tired and weak? Use the word *oxygen*.',
      Lines(2, 'They do not have enough healthy red blood cells, so less oxygen reaches their cells to release energy.'), marks=2),
    Q('Only healthy adults can give blood. Suggest **two** reasons for this rule.',
      Lines(2, 'To protect the donor (children have less blood and are still growing); to make sure the blood is safe and free of infections for the patient.'), marks=2),
    Q('Why do you think thousands of students volunteer to give blood to people they will never meet? Give your opinion.',
      Lines(3, 'Accept thoughtful answers, e.g. kindness, it saves lives, community spirit, they may need help one day.'), marks=2),
])

review = Sheet('review', 'Show what you know', level=3, goals=['Use key vocabulary.', 'Answer test-style questions.'], blocks=[
    Q('Find the key words.', WordSearch(['CELL', 'NUCLEUS', 'TISSUE', 'ORGAN', 'SYSTEM', 'NERVE', 'MUSCLE', 'BLOOD', 'SKIN', 'FAT'], size=11, seed=13)),
    Q('Label the levels of organisation.', Label(art.organisation_levels(labels=False), art.ORGANISATION, bank=True, cols=3), marks=5),
    Q('Which cell carries messages around the body?', MCQ(['red blood cell', 'nerve cell', 'fat cell', 'skin cell'], 1), marks=1),
    Q('The heart is made of muscle tissue, nerve tissue and other tissues. This makes the heart:',
      MCQ(['a cell', 'a tissue', 'an organ', 'an organism'], 2), marks=1),
    Q('**Challenge.** Why can we not see cells with our eyes alone, but we can see an organ like the heart?',
      Lines(3, 'Cells are microscopic (too small for our eyes); an organ contains millions of cells grouped together, so it is big enough to see.'), marks=2),
])

TOPIC = Topic(
    code='A2', strand='living', title='Cells, Tissues and Organs', short='Cells',
    subtitle='Cells as building blocks, specialised cells and the levels of organisation in the human body',
    outcomes=[
        'recall that cells are the building blocks of all living things, and give examples of specialized cells that make up the human body — skin, blood, nerve, muscle and fat cells.',
        'discuss the relationship between cells, tissues, organs and organ systems: cells organise to form tissues, tissues organise to form organs, and groups of organs form organ systems.',
        'use the levels of biological organization — cell, tissue, organ, organ system, organism — to explain how the human body is structured and how its parts depend on one another.',
    ],
    sheets=[learn, facts, think, investigate, case, review],
    selfcheck=['explain that all living things are made of cells', 'label the parts of an animal cell',
               'describe five specialised cells and their jobs', 'order cell, tissue, organ, organ system, organism',
               'use a microscope and calculate magnification', 'explain the jobs of the parts of blood'],
    cover_art=art.organisation_levels(),
)
