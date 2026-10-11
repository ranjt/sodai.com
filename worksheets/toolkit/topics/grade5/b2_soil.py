from build import Sheet, Topic
from ws import (P, H, Box, Vocab, Fig, Cols, Row, Case, Links, Lines, Blanks, Match, TrueFalse, MCQ, Order, Table,
                Ans, Sort, Label, Draw, Graph, WordSearch, Q, Part, Bullets)
import art

learn = Sheet('learn', 'Soil: the living skin of the Earth', level=1, goals=[
    'Describe what soil is made of and how it forms.',
    'Use a simple key to identify soil types.',
    'Explain what earthworms and plants need from soil.',
], blocks=[
    P('Almost all our food grows in a thin layer of **soil**. In many places this layer is only a few tens of centimetres '
      'deep, yet it can take hundreds of years to form just a few centimetres of new soil. Soil is not just "dirt": it is '
      'a mixture full of life.', 'lead'),
    Cols(
        H('What is soil made of?', 3),
        Bullets(['tiny pieces of **rock** (sand, silt and clay)', '**humus**: dark, rotted remains of dead plants and animals',
                 '**water** and **air** in the spaces between the particles', '**living things**: earthworms, insects, fungi and millions of bacteria']),
        H('How does soil form?', 3),
        P('Rain, ice, heat and plant roots slowly break rocks into small pieces. This is called **weathering**. Dead leaves and '
          'animals are broken down by **decomposers** into humus, which mixes with the rock pieces. Rivers also carry soil and '
          'drop it in new places.'),
        Fig(art.soil_layers(labels=art.SOIL_LAYERS), 'If you dig a deep hole you can see layers.'),
        H('Types of soil', 3),
        Table(['Soil type', 'What it is like'], [
            ['sandy', 'large, gritty particles; water drains through fast; dries out quickly; few nutrients'],
            ['clay', 'tiny particles; sticky when wet, cracks when dry; holds water; can be rich in nutrients'],
            ['chalky', 'pale and stony; contains chalk, so it fizzes with vinegar; drains well'],
            ['woodland', 'dark and crumbly; full of rotting leaves (humus); holds water well'],
            ['garden topsoil', 'a mixture of sand, clay and humus; dark and crumbly; good for most plants']]),
        Box('bd', P('Most of Bangladesh is a giant river **delta**. Every year the Ganges, Brahmaputra and Meghna rivers drop '
                    'fine soil called **silt** on the land. This makes the soil very fertile, which is why farmers can grow '
                    'two or three rice crops a year.')),
        H('Earthworms: soil engineers', 3),
        P('Earthworms need **moist, loosely packed** soil. They have no lungs and breathe through their damp skin, so dry soil '
          'kills them. As they tunnel they let air and water into the soil. They eat dead leaves and soil, and their droppings '
          '(**worm casts**) are full of nutrients. Charles Darwin studied earthworms for 40 years!'),
        Fig(art.svg(140, 50, art.earthworm(5, 5)), 'An earthworm. The thick band helps it make eggs.', width='55%'),
        H('Plants and soil', 3),
        P('Plants grow best in soil that is **moist** and has plenty of **nutrients** (minerals). Roots also need air. '
          'Very sandy soil dries out and loses its nutrients; heavy clay can become waterlogged. Adding **compost** improves '
          'both kinds.'),
    ),
    Vocab([('soil', 'mixture of rock particles, humus, water, air and living things'), ('humus', 'rotted remains of plants and animals in soil'),
           ('weathering', 'rocks breaking into smaller pieces'), ('silt', 'very fine soil carried by rivers'),
           ('drainage', 'how fast water flows through soil'), ('nutrients', 'minerals in soil that plants need'),
           ('compost', 'rotted plant waste added to soil to improve it'), ('key', 'a set of questions used to identify things')]),
])

facts = Sheet('facts', 'Soil layers and soil types', level=1, goals=['Label soil layers.', 'Use a key to identify soils.'], blocks=[
    Q('Label the layers of soil.', Label(art.soil_layers(), art.SOIL_LAYERS, width='72%'), marks=4),
    Q('Use the key to identify each soil sample.',
      Fig(art.soil_key(), width='96%'),
      Table(['Sample', 'What the class observed', 'Soil type'], [
          ['A', 'gritty, does not fizz', Ans('sandy soil')], ['B', 'not gritty, sticky and shiny when wet', Ans('clay soil')],
          ['C', 'not gritty, not sticky, dark with rotting leaves', Ans('woodland soil')], ['D', 'gritty, pale and stony, fizzes', Ans('chalky soil')],
          ['E', 'not gritty, not sticky, dark and crumbly, few leaves', Ans('garden topsoil')]], widths=['12%', '58%', '30%']), marks=5),
    Q('Fill in the gaps.',
      Blanks('Soil is a mixture of rock particles, [humus], water and [air]. Earthworms need [moist] soil because they breathe '
             'through their [skin]. Plants grow best in moist soil with plenty of [nutrients].', extra=['plastic', 'dry']), marks=5),
])

think = Sheet('think', 'Soil, worms and plants', level=2, goals=['Explain soil properties.', 'Link soil to plant growth and soil animals.'], blocks=[
    Q('Why does water drain quickly through sandy soil but slowly through clay?',
      Lines(3, 'Sand particles are large with big gaps between them, so water runs through; clay particles are tiny and packed tightly, so water moves slowly and is held.'), marks=2),
    Q('Rina wants to grow vegetables, but her soil is very sandy. Suggest what she could do and explain why.',
      Lines(3, 'Mix in compost or manure: it adds nutrients and humus that holds water, so the soil stays moist.'), marks=2),
    Q('Earthworms come up to the surface after heavy rain. Suggest why.',
      Lines(2, 'The soil spaces fill with water, so there is less air for them to breathe; they come up to get air.'), marks=2),
    Q('Explain **two** ways earthworms help plants.',
      Lines(3, 'Their tunnels let air and water reach the roots; their casts add nutrients; they mix humus into the soil.'), marks=2),
    Q('Why does the soil of the river delta make Bangladesh good for farming?',
      Lines(2, 'Rivers drop fertile silt every year, adding nutrients and new soil.'), marks=2),
])

investigate = Sheet('investigate', 'Which soil holds the most water?', level=2, goals=['Carry out a fair test.', 'Present results as a bar chart.', 'Use results to answer a real question.'], blocks=[
    Fig(art.funnel_test(), 'Equal amounts of soil in each funnel; water poured in at the same time.', width='80%'),
    P('Class 5C put 100 g of each soil in a funnel lined with filter paper. They poured 100 ml of water into each one and '
      'measured how much water dripped through in 5 minutes.'),
    Q('Complete the table to work out how much water each soil **held**.',
      Table(['Soil', 'Water poured in (ml)', 'Water that dripped through (ml)', 'Water held by soil (ml)'], [
          ['sand', '100', '80', Ans('20')], ['garden soil', '100', '55', Ans('45')], ['clay', '100', '20', Ans('80')]], center=True), marks=3),
    Q('Draw a bar chart of the water held by each soil.',
      Graph(['sand', 'garden soil', 'clay'], [20, 45, 80], 'Water held (ml)', 'Soil type', ymax=100, step=10, width=130, height=66), marks=4),
    Q('Name **three** things the class kept the same to make it a fair test.',
      Lines(2, 'mass of soil (100 g), volume of water (100 ml), time (5 minutes), same size funnel and filter paper'), marks=3),
    Q('Which soil would be best for a plant that needs a lot of water, and which would be best for a cactus? Explain.',
      Lines(3, 'Clay or garden soil holds water for a thirsty plant; sandy soil drains fast for a cactus, which does not like wet roots.'), marks=2),
])

case = Sheet('case', 'Worms that make money: vermicompost', level=3, goals=['Apply soil science to farming.', 'Use data to compare.', 'Consider benefits and costs.'], blocks=[
    Links('Science', 'Economics', 'Maths', 'Environment'),
    Case('In many villages of Bangladesh, farmers, many of them women, keep earthworms in concrete rings or large pots filled '
         'with cow dung, vegetable peel and straw. The worms eat the waste and turn it into rich, dark **vermicompost** '
         '(*kecho sar*) in about 6 to 8 weeks.',
         'Farmers use vermicompost on their own fields and sell the rest. Many say their vegetables grow better and they '
         'can use less **chemical fertiliser**. Chemical fertiliser gives quick nutrients, but using too much can harm soil '
         'life and wash into rivers and ponds.',
         source='Based on vermicompost projects in Bangladesh; numbers below are examples for learning.'),
    Q('Why does vermicompost help plants grow?', Lines(3, 'It is full of nutrients and humus; it holds water and lets air into the soil; it contains helpful soil life.'), marks=2),
    Q('Fatema sells vermicompost for 15 taka per kilogram. One worm ring makes 40 kg every 2 months.',
      Part('How much money does one ring earn in 2 months?', Lines(1, '40 × 15 = 600 taka')),
      Part('She has 5 rings. How much do they earn in 2 months?', Lines(1, '600 × 5 = 3000 taka')),
      Part('How much in one year (6 lots of 2 months)?', Lines(1, '3000 × 6 = 18 000 taka')), marks=3),
    Q('A farmer tested two plots of tomatoes (example results).',
      Table(['Plot', 'Fertiliser', 'Tomatoes harvested (kg)'], [['A', 'chemical fertiliser only', '120'], ['B', 'half chemical + vermicompost', '135']], center=True),
      Part('Which plot grew more tomatoes and by how much?', Lines(1, 'Plot B, by 15 kg')),
      Part('Is one test enough to be sure? Explain.', Lines(2, 'No: the plots might differ in other ways (water, sun, pests); it should be repeated over more plots and seasons.')), marks=3),
    Q('Give **two** benefits of vermicompost for the environment.',
      Lines(2, 'It recycles waste (dung, peel) instead of dumping it; less chemical fertiliser washes into rivers; healthier soil life.'), marks=2),
])

review = Sheet('review', 'Show what you know', level=3, goals=['Use key vocabulary.', 'Answer test-style questions.'], blocks=[
    Q('Find the key words.', WordSearch(['SOIL', 'HUMUS', 'CLAY', 'SAND', 'CHALK', 'SILT', 'WORM', 'COMPOST', 'ROCK'], size=10, seed=61)),
    Q('Which soil is sticky when wet and cracks when dry?', MCQ(['sandy', 'clay', 'chalky', 'woodland'], 1), marks=1),
    Q('Which soil would fizz with vinegar?', MCQ(['sandy', 'clay', 'chalky', 'garden topsoil'], 2), marks=1),
    Q('Design a "worm hotel" to keep earthworms healthy for one week in the classroom. Draw and label it.',
      Draw('50mm', 'My worm hotel', 'A clear container with moist, loose soil and some dead leaves; air holes; kept dark and cool; not too wet; worms returned afterwards.'), marks=3),
    Q('**Challenge.** Soil takes hundreds of years to form but can be washed away in one flood. Why should we protect it?',
      Lines(3, 'We need soil to grow almost all our food; it forms very slowly, so lost soil cannot quickly be replaced. Protect it with plants, trees and compost.'), marks=2),
])

TOPIC = Topic(
    code='B2', strand='earth', title='Soil and the Living Earth', short='Soil',
    subtitle='What soil is, soil types and a key to identify them, earthworms and plant growth',
    outcomes=[
        'use a simple key to identify soil types, including woodland, clay, chalky, sandy and general garden topsoil.',
        'understand that soil-living animals, such as earthworms, require moist, loosely packed soil.',
        'understand that plants will grow better in moist soil that has plenty of nutrients.',
    ],
    sheets=[learn, facts, think, investigate, case, review],
    selfcheck=['describe what soil is made of', 'use a key to identify five soil types', 'explain why earthworms need moist, loose soil',
               'explain why plants grow better in moist, nutrient-rich soil', 'carry out a fair test on soil drainage',
               'explain the benefits of compost'],
    cover_art=art.soil_layers(labels=art.SOIL_LAYERS, w='80%'),
)
