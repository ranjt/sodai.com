from build import Sheet, Topic
from ws import (P, H, Box, Vocab, Fig, Cols, Row, Case, Links, Lines, Blanks, Match, TrueFalse, MCQ, Order, Table,
                Ans, Sort, Label, Draw, Graph, WordSearch, Q, Part, Bullets)
import art

learn = Sheet('learn', 'A balanced diet for a healthy life', level=1, goals=[
    'Name the food groups and what each does for the body.',
    'Plan a balanced meal with foods in the right proportions.',
    'Discuss what affects the food choices people make.',
], blocks=[
    P('A plate of rice, dal, fish curry and vegetables. A packet of chips and a fizzy drink. Both fill your stomach, '
      'but only one gives your body what it needs. A **balanced diet** means eating a **variety** of foods, in the '
      '**right amounts**, so the body gets all the nutrients it needs.', 'lead'),
    Cols(
        H('The nutrients in food', 3),
        Table(['Nutrient', 'What it does', 'Foods'], [
            ['carbohydrates', 'give energy', 'rice, roti, bread, potato, chira'],
            ['proteins', 'growth and repair', 'fish, eggs, meat, dal (lentils), milk, beans'],
            ['fats and oils', 'store energy, keep us warm', 'oil, ghee, butter, nuts (small amounts)'],
            ['vitamins and minerals', 'keep the body healthy', 'fruit, vegetables, milk, small fish'],
            ['fibre', 'helps food move through the gut', 'vegetables, fruit, whole grains, dal'],
            ['water', 'needed by every cell', 'safe drinking water']]),
        P('Some minerals have special jobs: **calcium** (milk, small fish such as *mola*) builds strong bones and teeth; '
          '**iron** (leafy greens such as *lal shak*, meat, eggs) helps blood carry oxygen; **iodine** (iodised salt) '
          'helps the brain develop.'),
        H('A healthy plate', 3),
        Fig(art.healthy_plate(), 'A balanced meal: half vegetables and fruit, a quarter grains, a quarter protein.', width='90%'),
        P('Dietary guidelines for Bangladesh give similar advice: eat a **variety** of foods every day; do not fill the plate '
          'with rice alone; eat plenty of **vegetables and fruit**; include **fish, eggs, meat or dal**; drink **safe '
          'water**; use **iodised salt**; and limit salt, sugar, oil and fried snacks.'),
        H('Moderation: not too much, not too little', 3),
        P('Even healthy food can be eaten in the wrong amounts. Too little food can stop children growing properly. Too much '
          'food, especially sugary and fatty food, can lead to **obesity**, tooth decay and, later, diseases such as '
          '**diabetes** and heart disease.'),
        H('What affects our food choices?', 3),
        Bullets(['**Cost:** fresh food can cost more than cheap snacks.', '**Availability and season:** mangoes in summer, winter vegetables in winter.',
                 '**Culture and family:** *panta-ilish* at Pohela Boishakh, sweets and semai at Eid, pitha in winter.',
                 '**Media and technology:** adverts, cartoons and food-delivery apps make fast food look exciting.']),
        H('Things to avoid', 3),
        P('**Caffeine** (in tea, coffee, cola and energy drinks) can stop children sleeping well. **Tobacco**, in cigarettes '
          'and in chewed forms such as *jorda* and *gul*, harms the mouth, lungs and heart and is very hard to stop using. '
          '**Alcohol and drugs** damage the brain and body and are especially harmful to children.'),
        Box('fact', P('About 4 grams of sugar make one teaspoon. A 250 ml can of cola can contain more than 6 teaspoons of sugar.')),
    ),
    Vocab([('balanced diet', 'a variety of foods in the right amounts'), ('nutrient', 'a useful substance in food'),
           ('carbohydrate', 'nutrient that gives energy'), ('protein', 'nutrient for growth and repair'),
           ('moderation', 'not too much and not too little'), ('obesity', 'having too much body fat, which harms health'),
           ('caffeine', 'a substance in tea, coffee and some drinks that keeps people awake')]),
])

facts = Sheet('facts', 'Food groups and nutrients', level=1, goals=['Sort foods into groups.', 'Match nutrients to their jobs.'], blocks=[
    Q('Sort the foods into the main nutrient they give.',
      Sort(['Carbohydrates', 'Proteins', 'Vitamins and minerals'],
           [('rice', 'Carbohydrates'), ('roti', 'Carbohydrates'), ('potato', 'Carbohydrates'), ('fish', 'Proteins'),
            ('egg', 'Proteins'), ('dal', 'Proteins'), ('guava', 'Vitamins and minerals'), ('spinach (palong shak)', 'Vitamins and minerals'),
            ('carrot', 'Vitamins and minerals')]), marks=9),
    Q('Match each nutrient to its job.',
      Match([('carbohydrates', 'give us energy'), ('proteins', 'help us grow and repair'), ('calcium', 'builds strong bones and teeth'),
             ('iron', 'helps blood carry oxygen'), ('fibre', 'helps food move through the gut')]), marks=5),
    Q('Fill in the gaps.',
      Blanks('A balanced diet has a [variety] of foods in the right amounts. Half of a healthy plate should be '
             '[vegetables] and fruit. Eating too much sugar can cause tooth [decay]. We should use [iodised] salt.',
             extra=['chips', 'cola']), marks=4),
])

think = Sheet('think', 'Is this meal balanced?', level=2, goals=['Evaluate meals.', 'Plan a balanced day of meals.',
                                                                'Explain factors that affect food choices.'], blocks=[
    Q('Look at these two lunches. Which is more balanced? Explain your answer.',
      Table(['Lunch A', 'Lunch B'], [['a big plate of white rice, a little dal, a fried egg, a glass of cola',
                                       'rice (one quarter of plate), mixed vegetables, fish curry, a banana, water']]),
      Lines(3, 'Lunch B: it has carbohydrate, protein, vegetables and fruit in better proportions and water instead of a sugary drink. Lunch A is mostly rice and has a sugary drink and few vegetables.'), marks=3),
    Q('Plan a balanced day of meals for a 10-year-old. Include a drink each time.',
      Table(['Meal', 'Foods and drink'], [['Breakfast', Ans('e.g. roti, egg, vegetable bhaji, water/milk')],
                                          ['School tiffin', Ans('e.g. fruit, chira with yoghurt or a sandwich, water')],
                                          ['Lunch', Ans('e.g. rice, dal, fish, shak, salad, water')],
                                          ['Dinner', Ans('e.g. rice or roti, chicken or egg curry, vegetables, water')]],
            widths=['25%', '75%']), marks=4),
    Q('Why do some families buy more instant noodles and fewer vegetables? Give **two** reasons.',
      Lines(2, 'e.g. noodles are cheap, quick and easy; advertising; children like the taste; vegetables can be expensive or not available.'), marks=2),
    Q('Why should children not drink tea, coffee or energy drinks in the evening?',
      Lines(2, 'They contain caffeine, which keeps the brain awake and stops children getting enough sleep.'), marks=2),
    Q('Tobacco advertising is banned in Bangladesh. Why do you think the law does this?',
      Lines(2, 'Tobacco seriously harms health and is addictive; banning adverts helps stop young people starting.'), marks=2),
])

investigate = Sheet('investigate', 'How much sugar is in our drinks?', level=2, goals=[
    'Read information from food labels.', 'Convert grams to teaspoons.', 'Present and compare data.'], blocks=[
    P('Class 5D collected the nutrition labels from five drinks. They recorded the sugar in one 250 ml serving. '
      '(These are example values similar to real labels.)'),
    Q('Convert the grams of sugar into teaspoons (4 g = 1 teaspoon). Round to the nearest whole teaspoon.',
      Table(['Drink (250 ml)', 'Sugar (g)', 'Teaspoons of sugar'], [
          ['cola', '27', Ans('7')], ['mango juice drink', '32', Ans('8')], ['energy drink', '28', Ans('7')],
          ['plain milk', '12', Ans('3')], ['water', '0', Ans('0')]], center=True), marks=5),
    Q('Draw a bar chart of the grams of sugar in each drink.',
      Graph(['cola', 'mango drink', 'energy', 'milk', 'water'], [27, 32, 28, 12, 0], 'Sugar (g) in 250 ml', 'Drink',
            ymax=35, step=5, width=150, height=66), marks=4),
    Q('Health experts advise that children should have no more than about 6 teaspoons (24 g) of added sugar a day.',
      Part('Which drinks contain more than this in one serving?', Lines(1, 'cola, mango juice drink, energy drink')),
      Part('Milk contains natural sugar but is still a good choice. Why?', Lines(2, 'It also gives protein and calcium for growth and strong bones.')), marks=3),
    Q('Write a conclusion and one piece of advice for your school.',
      Lines(3, 'Many packaged drinks contain a lot of sugar, more than a child\'s daily limit in one serving. Advice: sell or bring water or plain milk instead of sugary drinks.'), marks=2),
])

case = Sheet('case', 'From panta bhat to pizza: changing plates', level=3, goals=[
    'Use evidence about how diets are changing.', 'Weigh up cost, culture and health.', 'Plan a healthy meal on a budget.'], blocks=[
    Links('Science', 'Health', 'Maths', 'Culture', 'Economics'),
    Case('Fifty years ago most families in Bangladesh ate home-cooked food: rice, dal, fish and vegetables, with seasonal '
         'fruit. Many children in poor families did not get enough to eat, and many were too short for their age because of '
         '**undernutrition**.',
         'Today the country grows much more food and fewer children are undernourished. But in towns and cities, more '
         'people buy **fast food**, fried snacks, sweets and sugary drinks, and many children spend hours on screens instead '
         'of playing outside. Doctors are seeing more children who are **overweight**, and more adults with **diabetes**.',
         'Nutritionists say we can keep the best of both: traditional dishes such as shak, dal, small fish and seasonal '
         'fruit are cheap and very healthy, while fast food is fine as an occasional treat.',
         source='Based on reports on nutrition in Bangladesh (FAO, UNICEF, national nutrition surveys).'),
    Q('What are the **two** different nutrition problems described in the text?',
      Lines(2, 'Undernutrition (not enough food / nutrients, children too short) and overnutrition (too much fatty/sugary food, overweight, diabetes).'), marks=2),
    Q('Plan a healthy school tiffin that costs **no more than 60 taka**. Use the price list.',
      Table(['Food', 'Price (Tk)'], [['banana', '10'], ['boiled egg', '15'], ['roti (2 pieces)', '10'], ['vegetable bhaji (small box)', '20'],
                                     ['guava', '15'], ['packet of chips', '20'], ['cola (250 ml)', '35'], ['bottle of water', '15']], center=True),
      Table(['My tiffin items', 'Cost (Tk)'], [[Ans('roti (2), vegetable bhaji, boiled egg'), Ans('10 + 20 + 15 = 45')],
                                               [Ans('+ banana'), Ans('45 + 10 = 55 (bring water from home)')]], widths=['70%', '30%']),
      marks=4),
    Q('Explain why your tiffin is balanced.', Lines(2, 'It has carbohydrate (roti), protein (egg), vegetables and fruit, with water to drink and little sugar or fat.'), marks=2),
    Q('Different people have different views. What might each say?',
      Table(['Person', 'View on fast food'], [['a fast-food shop owner', Ans('People enjoy it; it gives jobs; we could offer healthier options.')],
                                              ['a doctor', Ans('Too much fast food and sugar causes obesity and diabetes; eat it only sometimes.')],
                                              ['a busy working parent', Ans('It is quick and easy; healthy cooking needs time and planning.')]],
            widths=['32%', '68%']), marks=3),
    Q('Suggest **one** change your school could make to help learners eat better.',
      Lines(2, 'e.g. sell fruit and water instead of chips and cola; a "healthy tiffin day"; a school vegetable garden.'), marks=1),
])

review = Sheet('review', 'Show what you know', level=3, goals=['Use key vocabulary.', 'Answer test-style questions.'], blocks=[
    Q('Find the key words.', WordSearch(['PROTEIN', 'FIBRE', 'VITAMIN', 'CALCIUM', 'IRON', 'ENERGY', 'BALANCED', 'WATER', 'SUGAR'], size=11, seed=41)),
    Q('Which food is the best source of protein?', MCQ(['rice', 'dal', 'cola', 'butter'], 1), marks=1),
    Q('Which nutrient helps blood carry oxygen?', MCQ(['iron', 'fibre', 'fat', 'iodine'], 0), marks=1),
    Q('Label each part of the healthy plate with a food group.',
      Fig(art.healthy_plate(labels=False), width='70%'),
      Table(['Part of the plate', 'Food group'], [['the half on the left', Ans('vegetables and fruit')], ['top right quarter', Ans('grains (rice, roti)')],
                                                  ['bottom right quarter', Ans('protein (fish, egg, dal, meat)')]], widths=['45%', '55%']), marks=3),
    Q('**Challenge.** "Fat is bad for you, so we should never eat it." Do you agree? Explain.',
      Lines(3, 'No: the body needs some fat for energy, warmth and some vitamins; we should eat small amounts and avoid too much fried food.'), marks=2),
])

TOPIC = Topic(
    code='A4', strand='living', title='Eating for Health', short='Eating for health',
    subtitle='Nutrients, food groups, a balanced diet for Bangladesh and the choices we make',
    outcomes=[
        'identify and communicate the need for a variety of foods, and for moderation in the amount of food consumed, in a balanced diet for good health.',
        'plan a healthy daily diet, selecting healthy foods in the right proportions to make a balanced meal, with reference to the Dietary Guidelines for Bangladesh.',
        'identify and evaluate factors that affect choices for healthy eating — the impact of technology and media, the cost of food, the variety available, and cultural preferences.',
        'discuss the impact of caffeine, alcohol, tobacco and drugs on personal food choices.',
    ],
    sheets=[learn, facts, think, investigate, case, review],
    selfcheck=['name the nutrients and what they do', 'sort foods into food groups', 'plan a balanced meal using a healthy plate',
               'explain how cost, culture and media affect food choices', 'read a food label and compare sugar',
               'explain why caffeine, tobacco, alcohol and drugs are harmful'],
    cover_art=art.healthy_plate(w='75%'),
)
