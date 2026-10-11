from build import Sheet, Topic
from ws import (P, H, Box, Vocab, Fig, Cols, Row, Case, Links, Lines, Blanks, Match, TrueFalse, MCQ, Order, Table,
                Ans, Sort, Label, Draw, Graph, WordSearch, Q, Part, Bullets)
import art

learn = Sheet('learn', 'Seeds, germination and growing plants', level=1, goals=[
    'Describe the parts of a seed and what each part does.',
    'Explain what seeds need to germinate and what plants need to grow.',
    'Explain why plants need light energy.',
], blocks=[
    P('Rice, wheat, lentils, mustard, jackfruit and mango: almost every food we eat starts as a **seed**. A seed may '
      'look dry and dead, but it is alive. Inside it is a tiny plant waiting for the right moment to grow.', 'lead'),
    Cols(
        H('What is inside a seed?', 3),
        P('A seed has three main parts. The tough **seed coat** protects the inside from damage and from drying out. '
          'The **embryo** is the tiny baby plant, with a first root and a first shoot. The **food store** gives the '
          'embryo the energy it needs to start growing, before it has leaves to make its own food.'),
        Fig(art.bean_seed(labels=art.BEAN_PARTS), 'A bean seed, outside and opened up.'),
        H('Germination', 3),
        P('When a seed starts to grow we say it **germinates**. First the seed **absorbs** water and swells, and the seed '
          'coat splits. The first root grows **down** into the soil to take in water and hold the plant in place. Then the '
          'first shoot grows **up** towards the light. Soon the first leaves open. The seed uses up its food store and '
          'shrivels.'),
        Fig(art.germination_strip(numbered=True), 'Stages A to E of a bean seed germinating.'),
        H('What do seeds need to germinate?', 3),
        P('Seeds need **water**, **warmth** and **air** (oxygen) to germinate. They do **not** need light, because the '
          'food store gives them energy. That is why seeds can germinate deep in dark soil. Seeds can wait for years until '
          'the conditions are right: lotus seeds more than 1000 years old have germinated!'),
        H('What do plants need to grow?', 3),
        P('Once a plant has leaves, it needs **light, water, warmth and air** to grow well. These are called **factors**. '
          'Most plants also take **nutrients** (minerals) from the soil through their roots.'),
        Fig(art.plant_needs(), 'Each plant is missing one factor except the first.'),
        H('Plants and light', 3),
        P('Plants make their own food in their leaves, using **light energy** from the Sun. A green substance called '
          '**chlorophyll** traps the light. A plant kept in the dark cannot make food. It grows tall, thin and weak, its '
          'leaves turn pale yellow, and in the end it dies. Plants grow **towards** the light, which is why pot plants on a '
          'windowsill lean towards the window.'),
        H('Parts of a plant and their jobs', 3),
        Fig(art.plant_parts(labels=art.PLANT_PARTS), width='80%'),
        Bullets(['**Roots** take in water and nutrients and hold the plant in the ground.',
                 '**Stem** holds the plant up and carries water and food around it.',
                 '**Leaves** use light energy to make food.',
                 '**Flowers** make seeds so new plants can grow.']),
        Box('bd', P('Bangladesh is one of the world\'s biggest rice producers. Farmers first grow rice seeds in a small, wet '
                    '**seedbed**. After about a month the seedlings are planted out in the paddy fields.')),
        Box('fact', P('A coconut is one of the biggest seeds in the world. Its "water" and white flesh are the food store '
                      'for the embryo.')),
    ),
    Vocab([
        ('seed coat', 'tough outer layer that protects the seed'),
        ('embryo', 'the tiny plant inside a seed'),
        ('food store', 'part of the seed that gives the embryo energy to grow'),
        ('germination', 'when a seed starts to grow'),
        ('absorb', 'to take in, like a sponge takes in water'),
        ('factor', 'something that affects how well a living thing grows'),
        ('chlorophyll', 'green substance in leaves that traps light energy'),
        ('nutrients', 'minerals from the soil that help plants stay healthy'),
    ]),
])

facts = Sheet('facts', 'Seeds and plant needs', level=1, goals=[
    'Label the parts of a seed and a plant.', 'Recall the conditions for germination and growth.'], blocks=[
    Q('Label the parts of the bean seed.', Label(art.bean_seed(), art.BEAN_PARTS, width='88%', cols=3), marks=5),
    Q('Complete the sentences. Use the words in the box.',
      Blanks('When a seed [germinates], it first [absorbs] water and swells. The seed coat splits and the first '
             '[root] grows downwards. Next the [shoot] grows upwards. The seed gets the energy it needs from its '
             '[food store]. Seeds need water, [warmth] and air to germinate, but they do not need [light].',
             extra=['soil', 'flower']), marks=7),
    Q('Draw a line to match each plant part to its job.',
      Match([('roots', 'take in water and hold the plant in the soil'),
             ('stem', 'holds the plant up and carries water'),
             ('leaves', 'use light energy to make food'),
             ('flower', 'makes seeds for new plants')]), marks=4),
    Q('True or false?',
      TrueFalse([('Seeds need light to germinate.', False, 'Seeds do not need light to germinate.'),
                 ('A plant kept in the dark grows pale and weak.', True),
                 ('Chlorophyll is the green substance that traps light.', True),
                 ('The embryo grows into the new plant.', True),
                 ('Plants grow away from the light.', False, 'Plants grow towards the light.')]), marks=5),
])

think = Sheet('think', 'Explaining germination and growth', level=2, goals=[
    'Order the stages of germination.', 'Use results to decide what seeds need.', 'Explain the effect of missing factors.'], blocks=[
    Q('Write the letter of each stage (A to E) next to its description.',
      Fig(art.germination_strip(numbered=True)),
      Table(['Description', 'Stage'], [
          ['The seed has absorbed water and swollen.', Ans('A')], ['The first root grows down.', Ans('B')],
          ['The shoot pushes up through the soil.', Ans('C')], ['The first leaves open above the ground.', Ans('D')],
          ['The leaves are bigger; the seed has shrivelled.', Ans('E')]], widths=['80%', '20%']), marks=5),
    Q('Class 5A put 20 cress seeds in each of four dishes. After 5 days they counted how many had germinated.',
      Table(['Dish', 'Conditions', 'Seeds germinated (out of 20)'], [
          ['1', 'warm, wet cotton wool, in the light', '18'], ['2', 'warm, wet cotton wool, in a dark cupboard', '19'],
          ['3', 'cold (fridge), wet cotton wool, dark', '2'], ['4', 'warm, dry cotton wool, in the light', '0']], center=True),
      Part('Do seeds need light to germinate? Use dishes 1 and 2 to explain.', Lines(2, 'No. Dishes 1 (light) and 2 (dark) had almost the same number germinate (18 and 19).')),
      Part('Which dish shows that seeds need water?', Lines(1, 'Dish 4: with no water, no seeds germinated.')),
      Part('Which dish shows that seeds need warmth? Explain.', Lines(2, 'Dish 3: in the cold only 2 germinated compared with 19 in the warm dark dish 2.')),
      Part('Why did the class use 20 seeds in each dish, not just one?', Lines(2, 'One seed might be dead or damaged; more seeds give more reliable results.')),
      marks=6),
    Q('Look at the four plants. For each one, say which factor is missing and how you can tell.',
      Fig(art.plant_needs()),
      Table(['Plant', 'Missing factor', 'What you can see'], [
          ['2', Ans('water'), Ans('drooping (wilted) stem and leaves')],
          ['3', Ans('light'), Ans('tall, thin, pale, few leaves')],
          ['4', Ans('warmth'), Ans('very small, has hardly grown')]], widths=['12%', '30%', '58%']), marks=6),
    Q('Why does a seed need a food store, but a grown plant does not?',
      Lines(3, 'A seed has no leaves yet, so it cannot make food from light; the food store gives energy until the leaves grow. A grown plant makes its own food in its leaves using light.'), marks=2),
])

investigate = Sheet('investigate', 'Does light affect plant growth?', level=2, goals=[
    'Plan a fair test.', 'Present results in a line graph.', 'Use evidence to write a conclusion.'], blocks=[
    P('Nadia and Tanvir had two pots of the same kind of plant, each with 4 leaves. They put **Plant A** on a sunny '
      'windowsill and **Plant B** in a dark cupboard. Each week they gave both plants 50 ml of water and counted the leaves.'),
    Q('Complete the plan for their fair test.',
      Table(None, [
          ['Question', Ans('Does light affect how well a plant grows?')],
          ['What we change', Ans('light (windowsill or dark cupboard)')],
          ['What we measure', Ans('the number of leaves each week')],
          ['What we keep the same', Ans('type and size of plant, pot, soil, amount of water, temperature')],
          ['Prediction', Ans('Plant A will grow more leaves because it gets light to make food.')]], widths=['30%', '70%']),
      marks=5),
    Q('Here are their results. Draw a line graph with both plants on the same axes.',
      Table(['Week', '1', '2', '3', '4', '5'], [
          ['Plant A: leaves (light)', '4', '6', '9', '12', '15'], ['Plant B: leaves (dark)', '4', '5', '5', '5', '4']], center=True),
      Graph(['1', '2', '3', '4', '5'], [[4, 6, 9, 12, 15], [4, 5, 5, 5, 4]], 'Number of leaves', 'Week', ymax=16, step=2,
            kind='line', series_names=['Plant A (light)', 'Plant B (dark)'], width=150, height=72), marks=5),
    Q('Why is a line graph better than a bar chart for these results?',
      Lines(2, 'Line graphs show how something changes over time; here the number of leaves changes week by week.'), marks=1),
    Q('What happened to Plant B in week 5? Suggest why.',
      Lines(2, 'It lost a leaf (4 leaves). Without light it could not make food, so leaves turned yellow and fell off.'), marks=2),
    Q('Write a conclusion for the investigation.',
      Lines(2, 'Plants need light to grow well: the plant in the light grew many more leaves than the plant in the dark.'), marks=2),
    Box('tip', P('Measure from the same point each time, and repeat measurements to make your results more reliable.')),
])

case = Sheet('case', 'Floating gardens: farming on flood water', level=3, goals=[
    'Apply ideas about plant needs to a real farming method.', 'Consider how people adapt to their environment.',
    'Link science to climate, culture and history.'], blocks=[
    Links('Science', 'Geography', 'History', 'Climate change', 'Design'),
    Fig(art.floating_garden(), 'A floating garden made from water hyacinth, with vegetable seedlings growing on top.', width='92%'),
    Case('In the south of Bangladesh, in districts such as Gopalganj, Pirojpur and Barishal, low land stays under water '
         'for several months during the monsoon. Farmers cannot plant crops in the flooded fields. For hundreds of years, '
         'families here have solved this problem with **floating gardens**, called *dhap* or *baira*.',
         'Farmers pile up water hyacinth (a floating water plant), straw and rice stubble to make a thick raft, about one '
         'metre deep. As the plants slowly rot, they make a rich, soft compost full of **nutrients**. Farmers sow seeds of '
         'okra, gourds, red amaranth and other vegetables on top. The gardens rise and fall with the water, so the crops '
         'never drown. When the floods go down, the rotted rafts are spread on the fields as fertiliser.',
         'In 2015 the Food and Agriculture Organization of the United Nations named Bangladesh\'s floating gardens a '
         '**Globally Important Agricultural Heritage System**. As climate change brings more floods, more farmers are '
         'interested in this old idea.',
         source='Sources: FAO GIAHS programme; descriptions of floating agriculture in southern Bangladesh.'),
    Q('List the four factors that plants need to grow. Explain how a floating garden gives the plants each one.',
      Table(['Factor', 'How the floating garden provides it'], [
          [Ans('water'), Ans('the roots reach moisture from the raft and the water below')],
          [Ans('light'), Ans('the garden floats in the open sunlight')],
          [Ans('air'), Ans('the leaves and stems are above the water, not drowned')],
          [Ans('nutrients / warmth'), Ans('the rotting water hyacinth makes compost full of nutrients; it is warm in the monsoon')]],
            widths=['28%', '72%']), marks=4),
    Q('Why would seeds planted in a flooded field not germinate, even though there is plenty of water?',
      Lines(2, 'Seeds also need air (oxygen) to germinate; under flood water they cannot get enough air and they rot.'), marks=2),
    Q('Floating gardens use water hyacinth, a plant that grows so fast it blocks rivers. Why is this a clever idea?',
      Lines(2, 'It turns a problem weed into something useful (free material and compost) and clears waterways.'), marks=2),
    Q('**Think globally.** In Mexico, the Aztecs grew food on *chinampas*, gardens built in lakes. What do people in both '
      'places have in common?', Lines(2, 'Both used local materials and knowledge to grow food where land was covered by water: they adapted to their environment.'), marks=2),
    Q('**Design.** Draw a floating garden that could grow vegetables for a school. Label the materials and show how the '
      'plants get water, light, air and nutrients.',
      Draw('48mm', 'Your design', 'Accept any design with a floating base (e.g. hyacinth/straw raft or plastic bottles), soil or compost layer, plants on top, and labels for the four needs.'), marks=4),
])

review = Sheet('review', 'Show what you know', level=3, goals=['Use key vocabulary.', 'Answer test-style questions.'], blocks=[
    Q('Find the key words.',
      WordSearch(['SEED', 'EMBRYO', 'ROOT', 'SHOOT', 'WATER', 'WARMTH', 'LIGHT', 'FACTOR', 'LEAF', 'STEM'], size=11, seed=9)),
    Q('Label the parts of the plant.', Label(art.plant_parts(), art.PLANT_PARTS, width='62%'), marks=5),
    Q('Which part of a seed grows into the new plant?', MCQ(['seed coat', 'embryo', 'food store', 'scar'], 1), marks=1),
    Q('A seed is planted deep in dark soil. Will it germinate? Explain.',
      Lines(2, 'Yes, if it has water, warmth and air: seeds do not need light to germinate because they use their food store.'), marks=2),
    Q('**Challenge.** Shabnam says, "Plants get their food from the soil." Is she right? Explain.',
      Lines(3, 'Not quite. Plants take water and nutrients (minerals) from the soil, but they make their food in their leaves using light energy.'), marks=2),
])

TOPIC = Topic(
    code='A5', strand='living', title='Plants: Seeds, Germination and Growth', short='Plant growth',
    subtitle='What is inside a seed, how seeds germinate, and what plants need to grow',
    outcomes=[
        'know that plants need energy from light for growth.',
        'investigate how seeds need water and warmth for germination, but not light.',
    ],
    cambridge=['Unit 1 Investigating plant growth (1.1–1.5)'],
    sheets=[learn, facts, think, investigate, case, review],
    selfcheck=['name the parts of a seed and say what each part does',
               'describe the stages of germination',
               'explain that seeds need water, warmth and air, but not light, to germinate',
               'explain why plants need light energy to grow',
               'draw a line graph and write a conclusion',
               'explain how floating gardens help people grow food in floods'],
    cover_art=art.plant_needs(),
)
