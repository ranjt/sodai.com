from build import Sheet, Topic
from ws import (P, H, Box, Vocab, Fig, Cols, Row, Case, Links, Lines, Blanks, Match, TrueFalse, MCQ, Order, Table,
                Ans, Sort, Label, Draw, Graph, WordSearch, Q, Part, Bullets, Pics)
import art
import art4

learn = Sheet('learn', 'People and our environment', level=1, goals=[
    'Describe good and bad effects people have on the environment.',
    'Explain how human activities affect animals and plants in Bangladesh, and suggest solutions.',
    'List ways to care for the environment: reduce, reuse, recycle and more.',
], blocks=[
    P('People are part of many ecosystems. We take water from rivers, grow food in fields, cut wood from forests and catch '
      'fish from the sea. Long ago, there were far fewer people and they used simple tools. Today there are more than '
      '170 million people in Bangladesh, and our actions can help or harm the living things around us.', 'lead'),
    Cols(
        H('How we can harm the environment', 3),
        Bullets(['**Cutting down forests** (deforestation) destroys the homes of animals such as elephants and gibbons.',
                 '**Pollution**: rubbish, plastic, smoke and dirty water from factories harm living things. Rivers near cities, '
                 'such as the Buriganga, have become very polluted.',
                 '**Hunting and overfishing** can make animals rare. Catching too many young fish leaves none to grow up and breed.',
                 '**Filling in wetlands** to build houses and roads destroys the homes of fish, frogs and birds.']),
        Pics([('axe', 'cutting trees'), ('factory smoke', 'air pollution'), ('oil spill', 'water pollution'), ('plastic bottle', 'plastic litter')], cols=4, size='14mm', small=True),
        P('When a living thing loses its habitat it may die out from that place. If it dies out everywhere, it is **extinct** and '
          'can never come back. Many kinds of animals and plants are now **endangered** (in danger of becoming extinct).'),
        H('How we can help the environment', 3),
        Bullets(['**Protecting habitats**: national parks and wildlife sanctuaries, such as the Sundarbans and Lawachara.',
                 '**Planting trees**: in Bangladesh, people plant millions of trees every year during the monsoon.',
                 '**Laws** that stop hunting, protect fish while they breed, and ban harmful things such as thin plastic bags.',
                 '**Cleaning up** rivers, beaches and parks.']),
        H('Caring for the environment every day', 3),
        Table(['Action', 'What it means', 'Example'], [
            ['**Reduce**', 'use less', 'take a cloth bag to the market'],
            ['**Reuse**', 'use things again', 'use a jar to store rice; give old clothes to others'],
            ['**Recycle**', 'make used materials into new things', 'collect paper, glass, metal and plastic for recycling'],
            ['**Save energy**', 'use less electricity and fuel', 'switch off lights and fans when you leave a room'],
            ['**Don\'t litter**', 'put rubbish in a bin', 'never throw plastic into drains or rivers']]),
        Pics([('reusable bag', 'reduce'), ('glass bottle', 'reuse'), ('recycling', 'recycle'), ('light bulb', 'switch off')], cols=4, size='14mm', small=True),
        Box('fact', P('A plastic bottle can take **hundreds of years** to break down. Plastic in rivers flows to the sea, where '
                      'turtles and dolphins can mistake it for food.')),
        H('Encouraging others', 3),
        P('One person can make a difference, but many people together can make a big difference. You can talk to your family, '
          'make posters, start an eco-club at school or join a clean-up day.'),
        Box('bd', P('In **2002**, Bangladesh became one of the first countries in the world to **ban thin plastic shopping bags**, '
                    'after they blocked drains and made floods worse in Dhaka.')),
        Box('try', P('Do a "rubbish diary" at home for one day. Write down everything your family throws away. Which things could be reduced, reused or recycled?')),
    ),
    Vocab([('environment', 'everything around us: air, water, land and living things'), ('pollution', 'harmful things put into the environment'),
           ('deforestation', 'cutting down forests'), ('extinct', 'no longer living anywhere on Earth'), ('endangered', 'in danger of becoming extinct'),
           ('reduce', 'use less'), ('reuse', 'use again'), ('recycle', 'make used materials into new things')]),
])

facts = Sheet('facts', 'Helping or harming?', level=1, goals=['Sort human actions.', 'Use reduce, reuse and recycle.'], blocks=[
    Q('Sort the actions.',
      Sort(['Helps the environment', 'Harms the environment'], [
          ('planting trees', 'Helps the environment'), ('using a cloth bag', 'Helps the environment'), ('cleaning a beach', 'Helps the environment'),
          ('throwing plastic in a river', 'Harms the environment'), ('hunting wild birds', 'Harms the environment'), ('leaving lights on', 'Harms the environment')]), marks=6),
    Q('Write **reduce**, **reuse** or **recycle** for each action.',
      Table(['Action', 'Reduce, reuse or recycle?'], [['taking a water bottle from home instead of buying one', Ans('reduce')], ['using an old tin as a pencil pot', Ans('reuse')],
                                                     ['taking newspapers to the paper collector (*bhangari*)', Ans('recycle')], ['printing on both sides of the paper', Ans('reduce')]], widths=['70%', '30%']), marks=4),
    Q('Fill in the gaps.',
      Blanks('Cutting down forests is called [deforestation]. An animal that has died out everywhere is [extinct]. Harmful things '
             'in the air or water are called [pollution]. A protected forest for animals is a wildlife [sanctuary].', extra=['recycling', 'habitat']), marks=4),
])

think = Sheet('think', 'Problems and solutions', level=2, goals=['Explain human impacts on living things.', 'Suggest solutions.'], blocks=[
    Q('For each problem, explain how it harms animals or plants and suggest a solution.',
      Table(['Problem', 'How it harms', 'Solution'], [
          ['forests cut down for farms', Ans('animals lose food and homes'), Ans('protect forests; plant new trees; farm without cutting more forest')],
          ['factories pour dirty water into rivers', Ans('fish and plants die'), Ans('clean the water before it leaves the factory; check with laws')],
          ['too many young fish are caught', Ans('not enough fish grow up to breed'), Ans('use bigger net holes; stop fishing in the breeding season')]],
            widths=['30%', '32%', '38%']), marks=6),
    Q('Long ago, people in Bangladesh carried shopping in jute bags and baskets. Today many use plastic. How has this change affected the environment?',
      Lines(3, 'Plastic does not rot, so it blocks drains and rivers, causes floods and harms animals; jute bags rot away and can be reused many times.'), marks=2),
    Q('Why is it important to tell others about caring for the environment?', Lines(2, 'Many people acting together make a much bigger difference than one person.'), marks=2),
])

investigate = Sheet('investigate', 'Our school litter survey', level=2, goals=['Collect and tally data.', 'Draw a bar chart.', 'Plan action from evidence.'], blocks=[
    P('Class 4A wore gloves and collected litter from the school playground at the end of one day. They sorted it and counted each type.'),
    Q('Complete the tally chart.',
      Table(['Type of litter', 'Tally', 'Total'], [['sweet wrappers', 'IIII IIII IIII III', Ans('18')], ['plastic bottles', 'IIII II', Ans('7')],
                                                  ['paper', 'IIII IIII', Ans('10')], ['food waste', 'IIII', Ans('5')], ['cans', 'II', Ans('2')]], center=True), marks=2),
    Q('Draw a bar chart.', Graph(['wrappers', 'bottles', 'paper', 'food', 'cans'], [18, 7, 10, 5, 2], 'Number of pieces', 'Type of litter', ymax=20, step=2, width=120, height=52), marks=3),
    Q('Which type of litter was most common? Suggest why.', Lines(2, 'Sweet wrappers; children eat snacks at break time and drop the wrappers.'), marks=2),
    Q('Use the evidence to plan **two** actions for the school.', Lines(3, 'e.g. put bins next to the snack shop; sell snacks without wrappers; make a poster; have a weekly clean-up team.'), marks=2),
    Q('Why did they wear gloves?', Lines(1, 'Litter can be dirty or sharp and have germs.'), marks=1),
])

case = Sheet('case', 'The golden fibre: can jute beat plastic?', level=3, goals=['Compare materials for the environment.', 'Use numbers to compare.', 'Weigh up different views.'], blocks=[
    Links('Science', 'History', 'Economics', 'Design', 'Environment'),
    Case('**Jute** is a plant that grows well in the warm, wet fields of Bangladesh. Its long stems give a strong fibre that is '
         'made into bags, sacks, rope and mats. It was once so valuable that it was called the **golden fibre**, and Bangladesh '
         'is still one of the world\'s biggest growers.',
         'Plastic bags are cheap and light, but they can last for hundreds of years and block drains and rivers. Jute bags rot '
         'away naturally in a few months, and jute plants take in a lot of carbon dioxide as they grow. A Bangladeshi scientist, '
         'Dr Mubarak Ahmad Khan, has developed a bag made from jute that looks like plastic, called the **Sonali bag**.',
         source='Based on information about jute in Bangladesh and the Sonali bag. Numbers below are rounded examples.'),
    Q('Compare a plastic bag and a jute bag.',
      Table(['', 'Plastic bag', 'Jute bag'], [['made from', Ans('oil (fossil fuel)'), Ans('a plant that can be regrown')], ['time to break down', Ans('hundreds of years'), Ans('a few months')],
                                              ['can it be reused many times?', Ans('a few times'), Ans('yes, many times')], ['cost', Ans('very cheap'), Ans('costs more')]], widths=['30%', '35%', '35%']), marks=4),
    Q('**Maths.** A family uses 5 plastic bags a week. How many is that in a year (52 weeks)? How many could one jute bag replace?',
      Lines(2, '5 × 52 = 260 plastic bags a year; one strong jute bag used every week could replace all 260.'), marks=2),
    Q('What might each person think about using jute bags?',
      Table(['Person', 'View'], [['a jute farmer', Ans('More jute bags means more work and money for farmers.')], ['a shopkeeper', Ans('Jute bags cost more; I need cheap bags for customers.')],
                                 ['a fish in the river', Ans('Please, no more plastic in my home!')]], widths=['30%', '70%']), marks=3),
    Q('Design a campaign to get your school to use jute or cloth bags. Write a slogan and two ideas.',
      Lines(3, 'e.g. "Go golden with jute!"; give each learner a jute bag; a no-plastic snack day; a poster competition.'), marks=2),
])

review = Sheet('review', 'Show what you know', level=3, goals=['Use key vocabulary.', 'Answer test-style questions.'], blocks=[
    Q('Find the key words.', WordSearch(['REDUCE', 'REUSE', 'RECYCLE', 'LITTER', 'PLASTIC', 'FOREST', 'EXTINCT', 'JUTE', 'HABITAT'], size=11, seed=406)),
    Q('Which action **reduces** waste?', MCQ(['throwing old toys away', 'buying drinks in small plastic bottles', 'taking a cloth bag to the shop', 'burning rubbish'], 2, one_col=True), marks=1),
    Q('An animal that is in danger of dying out is…', MCQ(['extinct', 'endangered', 'migrating', 'a producer'], 1), marks=1),
    Q('Draw a poster to stop people throwing plastic into rivers.', Draw('44mm', 'My poster', 'A picture and message, e.g. "Rivers are not bins! Plastic kills fish."'), marks=3),
    Q('**Challenge.** Give one way people have **helped** an ecosystem in Bangladesh and one way people have **harmed** one. Explain both.',
      Lines(4, 'Helped: protecting the Sundarbans as a sanctuary lets tigers and deer survive. Harmed: polluting the Buriganga killed fish and made the water unsafe.'), marks=3),
])

TOPIC = Topic(
    code='A6', strand='living', title='Humans and the Environment', short='Humans and environment',
    subtitle='How people help and harm ecosystems, protecting animals and plants, and caring for the environment',
    outcomes=[
        'explore how humans have positive and negative effects on the environment, such as the loss of species and the protection of habitats.',
        'explore a number of ways of caring for the environment — recycling, reducing waste, reducing energy consumption, not littering, and encouraging others to care for the environment.',
        'discuss how various human activities can impact animal diversity in Bangladesh, and suggest possible solutions to mitigate the impact.',
        'discuss how various human activities can impact plant diversity in Bangladesh, and suggest possible solutions to mitigate the impact.',
        'observe and explain how humans are part of many different ecosystems, how our interactions with them have changed over time, and how our actions can positively or negatively affect how those ecosystems function.',
    ],
    cambridge=['Unit 2 Living things and environments (2.6 How we affect the environment, 2.8 Recycling)'],
    sheets=[learn, facts, think, investigate, case, review],
    selfcheck=['give examples of people harming and helping the environment', 'explain what extinct and endangered mean',
               'use reduce, reuse and recycle', 'carry out a litter survey', 'suggest solutions to environmental problems',
               'compare jute and plastic bags'],
    cover_art=art.pic_row(['recycling', 'reusable bag', 'deciduous tree', 'solar energy']),
)
