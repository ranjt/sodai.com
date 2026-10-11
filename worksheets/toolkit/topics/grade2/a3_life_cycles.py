from build import Sheet, Topic
from ws import (P, H, Box, Vocab, Fig, Cols, Row, Case, Links, Lines, Blanks, Match, TrueFalse, MCQ, Order, Table,
                Ans, Sort, Label, Draw, Graph, WordSearch, Q, Part, Bullets, Pics)
import art
import art4
import art23

learn = Sheet('learn', 'Growing up', level=1, goals=[
    'Name the stages as animals grow: egg or baby, young, adult.',
    'Compare how people and animals grow.',
    'Say which places animals need at each stage.',
], blocks=[
    P('Every animal starts small and grows. A chick hatches from an egg, a calf is born from a cow, and you were once a tiny baby! '
      'The stages of growing up make a **life cycle**.', 'lead'),
    H('A chicken grows up', 3),
    Fig(art4.cycle(art4.CHICKEN_CYCLE, r=80, size=44), 'egg → chick → hen → egg', width='58%'),
    H('A frog grows up', 3),
    P('A frog starts as an **egg** in a pond. A **tadpole** hatches. It lives in water and has a tail. It grows legs and becomes a **frog** that can live on land and in water.'),
    Fig(art4.cycle(art4.FROG_CYCLE, r=80, size=44), 'The frog life cycle.', width='58%'),
    H('People grow up too', 3),
    Fig(art23.human_growth(), 'baby → child → adult → older adult', width='74%'),
    P('Babies grow into children. Children grow **taller** and **heavier**. They learn to walk, talk and read. Adults can have babies of their own. '
      'People do not change shape like frogs: a baby looks like a small person.'),
    H('Measuring growth', 3),
    P('We can measure **height** with a tape measure, **weight** with scales, and count **age** in years. Most children grow about 5 to 6 cm taller every year.'),
    H('The right home at each stage', 3),
    P('Animals need different places as they grow. Frog eggs and tadpoles need **pond water**. Chicks need a warm **nest** and their mother. '
      'Butterfly eggs are laid on **leaves** so the caterpillars can eat. A **habitat** is the place where an animal finds food, water and shelter.'),
    Box('bd', P('Hilsa fish lay their eggs in rivers. The baby fish grow in the river, then swim to the sea.')),
    Vocab([('life cycle', 'the stages an animal goes through as it grows'), ('hatch', 'come out of an egg'), ('young', 'a baby animal'),
           ('adult', 'fully grown'), ('habitat', 'the place where an animal lives')]),
])

facts = Sheet('facts', 'Baby and adult', level=1, goals=['Match young animals to adults.', 'Order life cycle stages.'], blocks=[
    Q('Draw a line to match the baby to its parent.', Match([('chick', 'hen'), ('tadpole', 'frog'), ('caterpillar', 'butterfly'), ('calf', 'cow'), ('kitten', 'cat')]), marks=5),
    Q('Number the pictures in order, from youngest to oldest.', Pics([('adult', None), ('baby', None), ('older person', None), ('child', None)], cols=4, size='16mm', letters=True),
      Lines(1, 'B (baby), D (child), A (adult), C (older adult)'), marks=4),
    Q('Fill in the gaps.', Blanks('A chick [hatches] from an egg. A tadpole grows into a [frog]. As children grow they get [taller].', extra=['smaller']), marks=3),
])

think = Sheet('think', 'How do they change?', level=2, goals=['Describe changes as animals grow.', 'Compare life cycles.'], blocks=[
    Q('How does a tadpole change as it grows into a frog?', Lines(2, 'It grows legs, its tail gets shorter and it can live on land.'), marks=2),
    Q('How is a baby like a grown-up? How is it different?', Lines(2, 'Same: same body parts and shape. Different: smaller, cannot walk or talk yet.'), marks=2),
    Q('Why does a frog lay its eggs in a pond, not on dry land?', Lines(2, 'The tadpoles need water to live and swim.'), marks=2),
])

investigate = Sheet('investigate', 'How tall are we?', level=2, goals=['Measure height.', 'Compare and find a pattern.'], blocks=[
    P('Class 2A measured the height of a baby, a Grade 2 child, a Grade 5 child and a teacher.'),
    Q('Draw a bar chart.', Table(['Person', 'baby (1 year)', 'child (7 years)', 'child (10 years)', 'teacher'], [['Height (cm)', '75', '120', '140', '160']], center=True),
      Graph(['baby', '7 years', '10 years', 'teacher'], [75, 120, 140, 160], 'Height (cm)', 'Person', ymax=180, step=20, width=110, height=50), marks=3),
    Q('What is the pattern?', Lines(1, 'Older people are taller (until they are adults).'), marks=1),
    Q('Measure your own height. Write it here.', Lines(1, 'About 115–130 cm.'), marks=1),
])

case = Sheet('case', 'Baby turtles on the beach', level=3, goals=['Read about a real animal.', 'Think about caring for animals.'], blocks=[
    Links('Science', 'Geography', 'Caring for nature'),
    Case('On the beaches of Saint Martin\'s Island and Cox\'s Bazar, mother **sea turtles** come out of the sea at night. Each one '
         'digs a hole in the sand and lays about 100 eggs, then goes back to the sea.',
         'After about two months, tiny baby turtles **hatch** and race to the sea. Bright lights and rubbish on the beach can make '
         'them lose their way. Volunteers protect the nests and help keep the beach dark and clean.',
         source='Based on turtle conservation work on the coast of Bangladesh.'),
    Q('Put the turtle life cycle in order.', Order(['mother lays eggs in the sand', 'baby turtles hatch', 'babies swim in the sea', 'they grow into adults']), marks=3),
    Q('Where does a turtle need to be to lay eggs? Where does it grow up?', Lines(2, 'Eggs: in the sand on the beach. Grows up: in the sea.'), marks=2),
    Q('How can people help baby turtles?', Lines(2, 'Keep the beach clean and dark at night; do not touch the nests.'), marks=2),
])

review = Sheet('review', 'Show what you know', level=3, goals=['Use science words.'], blocks=[
    Q('Find the words.', WordSearch(['EGG', 'BABY', 'ADULT', 'GROW', 'FROG', 'CHICK'], size=8, seed=204)),
    Q('What hatches from a frog\'s egg?', MCQ(['a chick', 'a tadpole', 'a kitten'], 1), marks=1),
    Q('Draw the life cycle of a chicken. Use arrows.', Draw('46mm', 'Chicken life cycle', 'egg → chick → hen → egg, with arrows.'), marks=3),
])

TOPIC = Topic(
    code='A3', strand='living', title='Life Cycles and Growth', short='Life cycles',
    subtitle='How animals and people grow, life cycle stages, and the habitats they need',
    outcomes=[
        'observe the growth cycle of specific animals in order to identify the growth stages.',
        'describe the typical physical growth cycle of an animal — egg, immature form, mature organism — using labelled line drawings, and measure the height, weight and age of people and other animals.',
        'identify the habitats needed to support different stages in the growth cycle of a variety of local animals.',
        'compare the life cycle of human beings with that of a variety of local animal species.',
        'describe how different places meet the needs of living things.',
        'identify and describe the changes in living things as they grow.',
    ],
    cambridge=['Stage 3 Unit 3 Living things (3.3 Movement and reproduction)'],
    sheets=[learn, facts, think, investigate, case, review],
    selfcheck=['match baby animals to adults', 'draw a life cycle', 'compare people and frogs', 'measure height', 'say what home animals need'],
    cover_art=art4.cycle(art4.CHICKEN_CYCLE),
)
