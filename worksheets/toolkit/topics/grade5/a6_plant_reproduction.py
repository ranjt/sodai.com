from build import Sheet, Topic
from ws import (P, H, Box, Vocab, Fig, Cols, Row, Case, Links, Lines, Blanks, Match, TrueFalse, MCQ, Order, Table,
                Ans, Sort, Label, Draw, Graph, WordSearch, Q, Part, Bullets)
import art

learn = Sheet('learn', 'How flowering plants make new plants', level=1, goals=[
    'Name the male and female parts of a flower and say what they do.',
    'Explain pollination, fertilisation and seed dispersal.',
    'Describe the life cycle of a flowering plant.',
], blocks=[
    P('Every spring the mango trees of Rajshahi and Chapainawabganj are covered in tiny flowers called *mukul*. '
      'A few months later the same branches are heavy with mangoes. Where did the fruit come from? It came from the '
      'flowers. **Flowers are the parts of a plant that make seeds**, and seeds grow into new plants. Making new living '
      'things of the same kind is called **reproduction**.', 'lead'),
    Cols(
        H('Inside a flower', 3),
        P('A flower is like a small factory with different workers. The green **sepals** protect the flower while it is a '
          'bud. The **petals** are often brightly coloured and scented to attract insects.'),
        P('The **stamens** are the *male* parts. Each stamen has a thin stalk called a **filament** holding up an '
          '**anther**. The anther makes **pollen**, a fine powder that contains the male cells.'),
        P('The **carpel** is the *female* part, in the centre of the flower. At the top is the sticky **stigma**, which '
          'catches pollen. The **style** is a tube joining the stigma to the **ovary**. Inside the ovary are tiny '
          '**ovules**. Each ovule contains a female cell, the egg (ovum).'),
        Fig(art.flower_section(labels=art.FLOWER_PARTS), 'A flower cut in half to show its parts.'),
        H('Pollination: moving pollen', 3),
        P('Before a seed can form, pollen must travel from an anther to a stigma. This is called **pollination**. '
          'Plants cannot walk, so they need help.'),
        P('**Insect-pollinated** flowers have large, bright petals, a sweet scent and sugary **nectar**. When a bee '
          'visits to drink nectar, sticky pollen rubs onto its hairy body. At the next flower, some of that pollen '
          'brushes off onto the stigma.'),
        P('**Wind-pollinated** flowers, such as grasses and maize, are small and dull with no scent or nectar. Their '
          'anthers hang outside the flower and release huge amounts of light, dusty pollen. Their feathery stigmas '
          'catch pollen floating in the air.'),
        Row([Fig(art.insect_flower())], [Fig(art.wind_flower())]),
        H('Fertilisation: a seed begins', 3),
        P('When a pollen grain lands on the right kind of stigma, it grows a thin **pollen tube** down through the style '
          'into the ovary. The male cell travels down the tube and joins with the female cell inside an ovule. This '
          'joining is called **fertilisation**.'),
        Fig(art.pollen_tube(labels=art.POLLEN_TUBE_PARTS), 'The pollen tube carries the male cell to the ovule.', width='85%'),
        P('After fertilisation, the petals wither and fall. Each fertilised **ovule becomes a seed**, and the **ovary '
          'grows into a fruit** that protects the seeds. A mango has one large seed; a tomato or a guava has many.'),
        H('Seed dispersal: spreading out', 3),
        P('If all the seeds dropped under the parent plant, the young plants would compete with their parent and with '
          'each other for **light, water and space**. So plants spread their seeds away. This is called **seed dispersal**.'),
        Bullets([
            '**Wind:** light seeds with parachutes or wings, such as the fluffy seeds of the *shimul* (silk-cotton) tree, dandelions and sycamore.',
            '**Water:** seeds that float, such as coconuts and the seedlings of mangrove trees in the Sundarbans.',
            '**Animals (eaten):** juicy fruits such as guava and berries. Animals eat the fruit and drop the seeds in their droppings far away.',
            '**Animals (hooks):** burrs with tiny hooks, such as *chorkanta* grass, catch on fur and clothes.',
            '**Explosion:** pods that dry and burst open, flinging seeds out, such as peas and *dopati* (balsam).',
        ]),
        Fig(art.dispersal_strip(names=art.DISPERSAL_NAMES), 'Seeds are shaped for the way they travel.'),
        H('The life cycle', 3),
        P('A **life cycle** is the series of changes a living thing goes through in its life. For a flowering plant it '
          'goes round and round: a seed **germinates**, grows into a young plant, then an adult plant that **flowers**. '
          'Its flowers are **pollinated**, **fertilisation** happens, fruits and seeds form, the seeds are **dispersed**, '
          'and new seeds germinate.'),
        Fig(art.life_cycle(labels=art.LIFE_CYCLE_STAGES), 'The life cycle of a flowering plant.'),
        Box('fact', P('Honeybees tell each other where to find flowers by doing a "waggle dance" inside the hive. '
                      'The angle and length of the dance show the direction and distance of the food.')),
        Box('bd', P('In winter, the yellow mustard fields of Bangladesh buzz with bees. Many beekeepers move their hives '
                    'to these fields. The bees collect nectar to make honey and, at the same time, pollinate the mustard '
                    'so that the plants make more seeds for mustard oil.')),
        Box('think', P('Plants and animals depend on each other. Bees need flowers for food; many flowers need bees to '
                       'carry their pollen. If pollinators disappeared, what would happen to the fruits and vegetables we eat?')),
    ),
    Vocab([
        ('reproduction', 'making new living things of the same kind'),
        ('stamen', 'male part of a flower: anther + filament'),
        ('carpel', 'female part of a flower: stigma + style + ovary'),
        ('pollen', 'powder made by the anther; contains male cells'),
        ('ovule', 'part inside the ovary that contains the female cell and becomes a seed'),
        ('pollination', 'moving pollen from an anther to a stigma'),
        ('fertilisation', 'a male cell from pollen joins with a female cell in an ovule'),
        ('seed dispersal', 'spreading seeds away from the parent plant'),
        ('germination', 'when a seed starts to grow'),
        ('nectar', 'sugary liquid in flowers that attracts animals'),
    ]),
])

facts = Sheet('facts', 'Parts of a flower', level=1, goals=[
    'Label the parts of a flower.', 'Sort the parts into male and female.', 'Use the key words correctly.'], blocks=[
    Q('Label the parts of this flower. Use the words in the box.',
      Label(art.flower_section(), art.FLOWER_PARTS, width='92%'), marks=9),
    Q('Sort the flower parts into the table.',
      Sort(['Male parts', 'Female parts', 'Other parts'],
           [('anther', 'Male parts'), ('filament', 'Male parts'), ('stigma', 'Female parts'), ('style', 'Female parts'),
            ('ovary', 'Female parts'), ('ovule', 'Female parts'), ('petal', 'Other parts'), ('sepal', 'Other parts')]),
      marks=4),
    Q('Match each word to its meaning.',
      Match([('pollination', 'pollen moves from an anther to a stigma'),
             ('fertilisation', 'a male cell joins with a female cell in an ovule'),
             ('seed dispersal', 'seeds are carried away from the parent plant'),
             ('germination', 'a seed starts to grow'),
             ('nectar', 'a sweet liquid that attracts insects'),
             ('pollen', 'a powder made by the anther')]), marks=6),
    Q('True or false? Tick the box. If a sentence is false, write the correct version.',
      TrueFalse([
          ('The anther is a female part of the flower.', False, 'The anther is a male part.'),
          ('Pollen contains male cells.', True),
          ('After fertilisation, the ovary grows into a fruit.', True),
          ('Wind-pollinated flowers usually have big, bright petals.', False, 'They are usually small and dull.'),
          ('Each fertilised ovule becomes a seed.', True),
      ]), marks=5),
])

think = Sheet('think', 'From flower to new plant', level=2, goals=[
    'Put the stages of a life cycle in order.', 'Compare insect- and wind-pollinated flowers.',
    'Explain how seeds are shaped for dispersal.'], blocks=[
    Q('These sentences describe what happens after a bee visits a flower. Number them 1 to 6 in the right order.',
      Order(['A bee carries pollen from another flower.', 'Pollen lands on the sticky stigma.',
             'A pollen tube grows down the style to the ovary.', 'The male cell joins the female cell in the ovule.',
             'The ovule becomes a seed and the ovary becomes a fruit.', 'The fruit is eaten and the seed is dropped far away.']),
      marks=3),
    Q('Label the stages of the life cycle.',
      Label(art.life_cycle(numbered=True), art.LIFE_CYCLE_STAGES, width='80%'), marks=7),
    Q('Read the descriptions of flowers A and B.',
      Table(['Flower A', 'Flower B'], [['Tiny green flowers, no smell, anthers hanging outside, feathery stigmas, lots of light pollen.',
                                        'Large purple petals, sweet smell, nectar, sticky pollen.']]),
      Part('Which flower is pollinated by insects? Give two reasons.', Lines(2, 'Flower B: it has large bright petals, a sweet smell, nectar and sticky pollen.')),
      Part('Why does flower A make so much pollen?', Lines(2, 'Most pollen blown by the wind is lost, so it must make a lot for some to reach a stigma.')),
      marks=4),
    Q('Look at the seeds A to F. Complete the table.',
      Fig(art.dispersal_strip()),
      Table(['Seed', 'How is it dispersed?', 'Which feature helps?'], [
          ['A', Ans('wind'), Ans('parachute of hairs')],
          ['B', Ans('wind'), Ans('wings make it spin and fall slowly')],
          ['C', Ans('water'), Ans('it floats (air inside)')],
          ['D', Ans('animals (fur)'), Ans('hooks that catch on fur')],
          ['E', Ans('animals (eaten)'), Ans('juicy, tasty fruit')],
          ['F', Ans('explosion'), Ans('pod dries and bursts open')],
      ], widths=['12%', '38%', '50%']), marks=6),
    Q('Why is it important for seeds to be dispersed away from the parent plant?',
      Lines(3, 'So the young plants do not compete with the parent (and each other) for light, water, space and nutrients; it also helps the plant spread to new places.'), marks=2),
])

investigate = Sheet('investigate', 'Spinning seeds: a paper helicopter test', level=2, goals=[
    'Use a model to investigate wind dispersal.', 'Identify variables in a fair test.',
    'Calculate averages, spot a result that does not fit and draw a conclusion.'], blocks=[
    Row([
        P('Sycamore and other winged seeds spin as they fall. Spinning slows them down, so the wind has more time to '
          'carry them away. Class 5B made paper helicopters as **models** of winged seeds. They asked:'),
        P('**Does wing length change how long a paper helicopter takes to fall?**'),
        Box('need', P('paper, scissors, ruler, paper clip, stopwatch, a safe place to drop from 2 m')),
    ], [Fig(art.paper_helicopter(), 'Paper helicopter template', width='88%')], widths=[1.5, 1]),
    Q('Name the variables in this investigation.',
      Table(['Variable', 'In this investigation'], [
          ['The variable we change (independent)', Ans('the wing length')],
          ['The variable we measure (dependent)', Ans('the time taken to fall (seconds)')],
          ['Two variables we keep the same (controlled)', Ans('drop height, type and size of paper, body length, paper clip, how it is dropped')],
      ], widths=['45%', '55%']), marks=3),
    Q('Here are the class results. Each helicopter was dropped three times.',
      Table(['Wing length (cm)', 'Drop 1 (s)', 'Drop 2 (s)', 'Drop 3 (s)', 'Average (s)'], [
          ['4', '1.2', '1.3', '1.1', Ans('1.2')],
          ['6', '1.6', '1.5', '1.7', Ans('1.6')],
          ['8', '2.0', '2.1', '1.9', Ans('2.0')],
          ['10', '2.4', '1.5', '2.6', Ans('2.5 (leaving out 1.5)')],
      ], center=True),
      Part('Work out the average for each wing length and write it in the table.'),
      Part('Which result does not fit the pattern? Suggest why it happened.',
           Lines(2, '1.5 s for the 10 cm helicopter. It may have been dropped badly, hit something or the stopwatch was started late.')),
      marks=5),
    Q('Draw a bar chart of the average times.',
      Graph(['4 cm', '6 cm', '8 cm', '10 cm'], [1.2, 1.6, 2.0, 2.5], 'Average time to fall (s)', 'Wing length', ymax=3, step=0.5,
            width=150, height=70), marks=4),
    Q('Write a conclusion. Use the words *longer* and *slower*.',
      Lines(2, 'The longer the wings, the slower the helicopter falls (the longer it takes to reach the ground).'), marks=2),
    Q('How does this help a real sycamore tree?',
      Lines(2, 'Seeds that fall slowly stay in the air longer, so the wind can carry them further from the parent tree.'), marks=2),
])

case = Sheet('case', 'Bees, mustard and honey', level=3, goals=[
    'Explain how plants and animals depend on each other.', 'Use data to compare results.',
    'Consider different points of view and suggest action.'], blocks=[
    Links('Science', 'Maths', 'Geography', 'Economics', 'Ethics'),
    Fig(art.mustard_field(), width='88%'),
    Case('From November to January, much of northern and central Bangladesh turns bright yellow with mustard flowers. '
         'Farmers grow mustard for its seeds, which are pressed to make **mustard oil** for cooking.',
         'Ayesha is a beekeeper from Sirajganj. Every winter she moves 40 wooden bee boxes to the edge of the mustard '
         'fields. "My bees collect nectar from the flowers and turn it into honey," she says. "The farmers like it too, '
         'because their mustard plants make more seeds when bees visit."',
         'But there is a problem. Some farmers spray **pesticides** on their crops to kill pests. If the spray is used '
         'while the flowers are open and bees are flying, it can kill the bees too. Ayesha now talks to farmers so they '
         'spray in the late evening, when bees are back in their hives, or use other ways to control pests.',
         source='This story is based on real beekeeping in Bangladesh; the names and numbers are examples for learning.'),
    Q('Explain how the bees and the mustard plants **depend on each other**.',
      Lines(3, 'The mustard flowers give the bees nectar (food) to make honey. The bees carry pollen between flowers, pollinating them so the plants make more seeds.'), marks=2),
    Q('Farmer Karim grew mustard in two fields of the same size, with the same seeds, soil and water. Field A was next to '
      'Ayesha\'s bee boxes. Field B was far away from any bees.',
      Table(['', 'Field A (near bees)', 'Field B (no bees nearby)'],
            [['Mustard seed harvested (kg)', '180', '150']], center=True),
      Part('How many more kilograms of seed did Field A produce?', Lines(1, '180 − 150 = 30 kg more')),
      Part('Suggest a scientific reason for the difference.', Lines(2, 'More flowers were pollinated by bees in Field A, so more ovules were fertilised and became seeds.')),
      Part('Why was it important that the fields were the same size, with the same seeds, soil and water?', Lines(2, 'To make it a fair test: the only difference was the bees, so the bees caused the difference.')),
      marks=4),
    Q('Different people see the problem in different ways. What might each person say about spraying pesticides?',
      Table(['Person', 'What they might think'], [
          ['A farmer with pests on his crop', Ans('Pests eat my crop; I need to spray to protect my harvest.')],
          ['Ayesha, the beekeeper', Ans('Spraying in the day kills my bees and I lose honey and income.')],
          ['A family buying mustard oil and honey', Ans('We want enough oil and honey at a fair price, and food that is safe.')],
      ], widths=['35%', '65%']), marks=3),
    Q('Suggest **two** actions that could help both farmers and bees.',
      Lines(3, 'Spray only in the evening when bees are in their hives; use fewer or safer pesticides; plant flower strips for bees; farmers and beekeepers agree on spraying times.'), marks=2),
    Box('link', P('**Maths:** if Field A grew 180 kg and oil is about one third of the seed\'s mass, about how much oil '
                  'could be pressed? (180 ÷ 3 = 60 kg). **Geography:** find Sirajganj on a map of Bangladesh.'),
        title='Take it further'),
])

review = Sheet('review', 'Show what you know', level=3, goals=[
    'Use key vocabulary.', 'Design a model that copies how an animal disperses seeds.',
    'Answer test-style questions.'], blocks=[
    Q('Find these ten words in the grid.',
      WordSearch(['POLLEN', 'STIGMA', 'ANTHER', 'OVARY', 'OVULE', 'NECTAR', 'SEED', 'FRUIT', 'PETAL', 'SEPAL'], size=11, seed=4),
      marks=None),
    Q('**Design challenge.** Burrs stick to animal fur so their seeds travel. Design a model seed that will stick to a '
      'woollen sock and stay on while you walk 10 steps.',
      Row([Draw('52mm', 'Draw and label your design',
                'A good design: a small ball (seed) covered with hooks, e.g. bent pipe-cleaner or Velcro hooks; labels show the hooks and the seed.')],
          [Part('What materials will you use?', Lines(2, 'e.g. clay ball, toothpicks bent into hooks, Velcro, pipe cleaners')),
           Part('How will you test if it works?', Lines(3, 'Press it onto a sock, walk 10 steps, count how many models are still attached; repeat 3 times.'))]),
      marks=4),
    Q('Which part of a flower becomes the fruit?', MCQ(['petal', 'stigma', 'ovary', 'anther'], 2), marks=1),
    Q('A coconut can float across the sea. Which way is it dispersed?', MCQ(['wind', 'water', 'animals', 'explosion'], 1), marks=1),
    Q('Rashid says, "Seeds need light to make a flower." Explain why he is wrong and what flowers are really for.',
      Lines(3, 'Flowers do not grow from light alone; a flower is the part of the plant used for reproduction. It makes pollen and ovules so that seeds can form after pollination and fertilisation.'),
      marks=2),
])

TOPIC = Topic(
    code='A6', strand='living', title='Flowering Plants: Reproduction and Life Cycles', short='Flowering plants',
    subtitle='Flowers, pollination, fertilisation, seed dispersal and the life cycle of a flowering plant',
    outcomes=[
        'know that plants reproduce.',
        'observe that plants produce flowers which have male and female organs, and that seeds are formed when pollen from the male organ fertilises the ovum.',
        'know that insects pollinate some flowers.',
        'observe how seeds can be dispersed in a variety of ways.',
        'recognise that flowering plants have a life cycle including pollination, fertilisation, seed production, seed dispersal and germination.',
        'design a model that mimics the function of an animal in dispersing seeds or pollinating plants.',
        'identify how the reproduction of living things connects to the interdependency of species and their survival.',
    ],
    cambridge=['Unit 2 The life cycle of flowering plants (2.1–2.7)'],
    sheets=[learn, facts, think, investigate, case, review],
    selfcheck=[
        'name the male and female parts of a flower and say what they do',
        'explain how insects and the wind pollinate flowers',
        'describe what happens at fertilisation',
        'explain why seeds are dispersed and give five ways it happens',
        'put the stages of a flowering plant\'s life cycle in order',
        'plan a fair test and spot a result that does not fit',
        'explain how plants and animals depend on each other',
    ],
    cover_art=art.life_cycle(labels=art.LIFE_CYCLE_STAGES, w='100%'),
)
