from build import Sheet, Topic
from ws import (P, H, Box, Vocab, Fig, Cols, Row, Case, Links, Lines, Blanks, Match, TrueFalse, MCQ, Order, Table,
                Ans, Sort, Label, Draw, Graph, WordSearch, Q, Part, Bullets, Pics)
import art
import art4

learn = Sheet('learn', 'Life cycles, growing up and family likeness', level=1, goals=[
    'Describe and compare the life cycles of a plant and some animals.',
    'Explain what living things need to grow and survive.',
    'Explain why young living things are like their parents, but not exactly like them.',
], blocks=[
    P('Every living thing is born, grows, becomes an adult, has young of its own and one day dies. Then its young do the same. '
      'This pattern goes round and round, so we call it a **life cycle**. Some life cycles are quick: a mosquito grows from '
      'egg to adult in about ten days. Others are slow: an elephant takes about 15 years to become an adult.', 'lead'),
    Cols(
        H('A chicken\'s life cycle', 3),
        P('A hen lays an **egg**. Inside, a chick grows for about 21 days, then **hatches**. The fluffy **chick** grows into a young '
          'bird, and after about five months it is an **adult** that can lay eggs. Chickens look like small adults from the '
          'moment they hatch.'),
        Fig(art4.cycle(art4.CHICKEN_CYCLE, r=80, size=40), 'The life cycle of a chicken.', width='88%'),
        H('A frog\'s life cycle', 3),
        P('Frogs lay soft **eggs** (frogspawn) in water. A **tadpole** hatches. It has a tail and breathes with **gills**, like a '
          'fish. Slowly it grows legs, its tail shrinks and it grows lungs. It becomes a **froglet**, then an **adult frog** that '
          'can live on land. This big change of body shape is called **metamorphosis**.'),
        Fig(art4.cycle(art4.FROG_CYCLE, r=80, size=40), 'The life cycle of a frog.', width='88%'),
        H('A butterfly\'s life cycle', 3),
        P('A butterfly lays tiny **eggs** on a leaf. A **caterpillar** (larva) hatches and eats and eats. It then makes a hard case '
          'called a **chrysalis** (pupa). Inside, its body changes completely. Finally an **adult butterfly** comes out. This is '
          'also metamorphosis.'),
        Fig(art4.cycle(art4.BUTTERFLY_CYCLE, r=80, size=40), 'The life cycle of a butterfly.', width='88%'),
        H('A flowering plant\'s life cycle', 3),
        P('A **seed** **germinates** (starts to grow) into a **seedling**. It grows into an adult plant that makes **flowers**. '
          'Pollen is carried from flower to flower (**pollination**), seeds form inside a **fruit**, and the seeds are '
          '**scattered** (dispersed). Each seed can grow into a new plant.'),
        Fig(art.life_cycle(labels=art.LIFE_CYCLE_STAGES), 'The life cycle of a flowering plant.', width='88%'),
        H('Compare the life cycles', 3),
        Table(['', 'Plant', 'Chicken', 'Frog'], [['starts as', 'seed', 'egg', 'egg'], ['young', 'seedling', 'chick', 'tadpole'],
                                                 ['big change of shape?', 'yes', 'no', 'yes'], ['makes new young by', 'seeds', 'eggs', 'eggs']]),
        H('What do living things need?', 3),
        Bullets(['**Plants** need light, water, air, warmth and minerals from the soil.',
                 '**Animals** need food, water, air (oxygen), shelter and the right temperature.',
                 'If something is missing, a living thing cannot grow well and may not survive.']),
        H('Like parents, but not exactly', 3),
        P('Young living things **inherit** features from their parents: kittens look like cats, mango seeds grow into mango '
          'trees, and you may have your mother\'s eyes or your father\'s smile. But young are never **exactly** the same as their '
          'parents or each other. Kittens in one litter can have different colours and patterns. These small differences are '
          'called **variation**.'),
        Pics([('chicken', 'parent'), ('baby chick', 'young'), ('cat', 'parent'), ('rabbit', 'parent')], cols=4, size='13mm', small=True),
        Box('tip', P('**Inherited** features come from parents (eye colour, the shape of your ears). Some features are not '
                     'inherited: a scar, short hair after a haircut, or speaking Bangla.')),
        Box('safety', P('**Medicines** help our bodies when we are ill. They are **drugs**: substances that change how the body '
                        'works. Only take medicine given by a trusted adult or a doctor, take the right amount at the right time, '
                        'and never share it. Keep medicines away from small children.')),
    ),
    Vocab([('life cycle', 'the stages in the life of a living thing, repeating again and again'), ('hatch', 'come out of an egg'),
           ('larva', 'the young stage of an insect, such as a caterpillar'), ('pupa', 'the resting stage when an insect changes shape'),
           ('metamorphosis', 'a big change of body shape as an animal grows'), ('germinate', 'when a seed starts to grow'),
           ('inherit', 'get features from your parents'), ('variation', 'differences between living things of the same kind')]),
])

facts = Sheet('facts', 'Life cycle stages', level=1, goals=['Order life cycle stages.', 'Use life cycle vocabulary.'], blocks=[
    Q('Number the stages of a frog\'s life cycle in order.',
      Order(['eggs (frogspawn) in the water', 'a tadpole with a tail and gills', 'a tadpole with back legs', 'a froglet with a short tail', 'an adult frog']), marks=4),
    Q('Label the butterfly life cycle.', Fig(art4.cycle(art4.BUTTERFLY_CYCLE, labels=False, numbered=True, r=80, size=40), width='52%'),
      Table(['Number', 'Stage'], [['1', Ans('eggs')], ['2', Ans('caterpillar (larva)')], ['3', Ans('chrysalis (pupa)')], ['4', Ans('adult butterfly')]], center=True), marks=4),
    Q('Fill in the gaps.',
      Blanks('A seed [germinates] into a seedling. A chick [hatches] from an egg. A big change of body shape is called '
             '[metamorphosis]. Young living things [inherit] features from their parents.', extra=['melts', 'migrates']), marks=4),
    Q('Sort the features.',
      Sort(['Inherited from parents', 'Not inherited'], [('eye colour', 'Inherited from parents'), ('shape of nose', 'Inherited from parents'),
                                                        ('a puppy\'s fur colour', 'Inherited from parents'), ('a scar on your knee', 'Not inherited'),
                                                        ('the language you speak', 'Not inherited'), ('a haircut', 'Not inherited')]), marks=6),
])

think = Sheet('think', 'Comparing life cycles', level=2, goals=['Compare life cycles.', 'Explain variation.'], blocks=[
    Q('Give one way the life cycle of a frog is **similar** to a chicken\'s and one way it is **different**.',
      Lines(3, 'Similar: both start as eggs and grow into adults that lay eggs. Different: the frog changes shape (tadpole to frog), but the chick already looks like a small adult.'), marks=2),
    Q('Why does a butterfly lay its eggs on a leaf and not on a stone?', Lines(2, 'When the caterpillars hatch they need leaves to eat straight away.'), marks=2),
    Q('Five kittens are born to the same mother. Two are black, two are striped and one is white. Explain why they are not all the same.',
      Lines(3, 'Kittens inherit features from both parents, but each kitten gets a different mix, so there is variation between them.'), marks=2),
    Q('Tanvir says, "If I grow big muscles at the gym, my children will be born with big muscles." Is he right? Explain.',
      Lines(2, 'No. Muscles built by exercise are not inherited; they are not passed on to children.'), marks=2),
    Q('Why must you never take medicine that belongs to someone else?', Lines(2, 'It may be the wrong medicine or the wrong amount for you and could make you ill.'), marks=1),
])

investigate = Sheet('investigate', 'What do seeds need to grow?', level=2, goals=['Plan a fair test.', 'Present results in a bar chart.', 'Draw conclusions.'], blocks=[
    P('Class 4C planted 10 cress seeds in each of four pots. They changed one thing for each pot and measured the height of the '
      'seedlings after 7 days.'),
    Q('Here is the plan. What did they change for each pot?',
      Table(['Pot', 'Water?', 'Light?', 'Warm?', 'Average height after 7 days (cm)'], [
          ['A', 'yes', 'yes', 'yes', '6'], ['B', 'no', 'yes', 'yes', '0'], ['C', 'yes', 'no (in a dark cupboard)', 'yes', '7 (yellow and thin)'],
          ['D', 'yes', 'yes', 'no (in a fridge)', '1']], center=True),
      Lines(1, 'Each pot was missing one thing: B no water, C no light, D no warmth. A had everything.'), marks=2),
    Q('Draw a bar chart of the heights.', Graph(['A', 'B', 'C', 'D'], [6, 0, 7, 1], 'Average height (cm)', 'Pot', ymax=8, step=1, width=110, height=50), marks=3),
    Q('Pot C was tallest. Does that mean seedlings grow best in the dark? Explain.',
      Lines(3, 'No. They grew tall and thin looking for light, but were yellow and weak. Without light they cannot make food and will die.'), marks=2),
    Q('Write a conclusion.', Lines(2, 'Seeds need water and warmth to germinate; seedlings need light to grow into healthy green plants.'), marks=2),
    Q('Name two things they kept the same.', Lines(1, 'number of seeds, type of seed, size of pot, type of soil, amount of water'), marks=1),
])

case = Sheet('case', 'Rajshahi silk: the life cycle of the silkworm', level=3, goals=['Apply life cycle knowledge to a real industry.', 'Use numbers from a real process.', 'Think about the ethics of using animals.'], blocks=[
    Links('Science', 'History', 'Economics', 'Ethics', 'Art'),
    Case('**Rajshahi** is famous for its beautiful **silk** saris. Silk is made by the **silkworm**, the caterpillar of a moth. '
         'Farmers grow **mulberry** trees, because silkworms eat only mulberry leaves.',
         'A silk moth lays 300 to 500 tiny **eggs**. The silkworms (larvae) hatch and eat leaves day and night for about a month, '
         'growing about 10 000 times heavier! Then each one spins a **cocoon** around itself from a single thread of silk, which '
         'can be **one kilometre long**. Inside the cocoon it becomes a **pupa**. After about two weeks an adult **moth** comes out, '
         'and the cycle starts again.',
         'To get long unbroken threads, most cocoons are put in hot water before the moth comes out, which kills the pupa. Some '
         'makers produce "peace silk" by waiting for the moths to leave first, but the thread is broken into shorter pieces.',
         source='Based on information about sericulture (silk farming) in Rajshahi, Bangladesh.'),
    Q('Complete the silkworm life cycle.',
      Order(['egg', 'silkworm (larva) eating mulberry leaves', 'spins a cocoon', 'pupa inside the cocoon', 'adult moth lays eggs']), marks=3),
    Q('Why must silk farmers also be good at growing trees?', Lines(2, 'Silkworms eat only mulberry leaves, so farmers must grow lots of healthy mulberry trees.'), marks=1),
    Q('**Maths.** Suppose one sari needs 3000 cocoons. A farmer\'s silkworms make 12 000 cocoons. How many saris can be made?',
      Lines(1, '12 000 ÷ 3000 = 4 saris'), marks=2),
    Q('What might each person think about killing the pupae to make silk?',
      Table(['Person', 'View'], [['a silk farmer', Ans('It is our living and a tradition; we need long threads to make good silk.')],
                                 ['an animal-welfare worker', Ans('Many insects die; peace silk is kinder to animals.')],
                                 ['a sari buyer', Ans('I want beautiful silk, but I could choose peace silk if it is labelled.')]], widths=['30%', '70%']), marks=3),
])

review = Sheet('review', 'Show what you know', level=3, goals=['Use key vocabulary.', 'Answer test-style questions.'], blocks=[
    Q('Find the key words.', WordSearch(['EGG', 'LARVA', 'PUPA', 'ADULT', 'TADPOLE', 'SEED', 'HATCH', 'INHERIT', 'CYCLE'], size=10, seed=403)),
    Q('Which animal goes through metamorphosis?', MCQ(['chicken', 'cow', 'butterfly', 'goat'], 2), marks=1),
    Q('What does a seed need to germinate?', MCQ(['water and warmth', 'light only', 'soil only', 'wind'], 0), marks=1),
    Q('Draw the life cycle of a plant you know, such as rice or mango. Label four stages.',
      Draw('48mm', 'My plant life cycle', 'seed → seedling → adult plant with flowers → fruit with seeds (back to seed).'), marks=4),
    Q('**Challenge.** Many frogs in Bangladesh are disappearing because ponds and wetlands are being filled in for building. '
      'Use the frog life cycle to explain why losing ponds is a problem for frogs.',
      Lines(3, 'Frogs lay eggs in water and tadpoles can only live in water, so without ponds they cannot complete their life cycle and no young frogs grow up.'), marks=2),
])

TOPIC = Topic(
    code='A3', strand='living', title='Life Cycles, Growth and Inheritance', short='Life cycles',
    subtitle='Life cycles of plants, chickens, frogs and butterflies, what living things need, inheritance and variation',
    outcomes=[
        'design an investigation to determine what a living thing needs in order to grow and survive.',
        'make observations to construct an evidence-based account showing that young plants and animals are like, but not exactly like, their parents.',
        'compare key stages in the life cycle of a plant and an animal, and relate them to growth and survival (IB Phase 3).',
    ],
    cambridge=['Unit 1 Humans and animals (1.5–1.6 Medicines)'],
    sheets=[learn, facts, think, investigate, case, review],
    selfcheck=['describe the life cycles of a chicken, a frog, a butterfly and a plant', 'explain metamorphosis',
               'investigate what seeds need to grow', 'explain inherited features and variation', 'use medicines safely',
               'explain how silk comes from the silkworm life cycle'],
    cover_art=art4.cycle(art4.FROG_CYCLE),
)
