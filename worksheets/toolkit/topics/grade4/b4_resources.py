from build import Sheet, Topic
from ws import (P, H, Box, Vocab, Fig, Cols, Row, Case, Links, Lines, Blanks, Match, TrueFalse, MCQ, Order, Table,
                Ans, Sort, Label, Draw, Graph, WordSearch, Q, Part, Bullets, Pics)
import art
import art4

learn = Sheet('learn', 'Earth\'s resources: use them wisely', level=1, goals=[
    'Explain that some resources cycle through the environment while others will run out.',
    'Describe how technology can help and harm sustainability.',
    'Describe ways people conserve and protect resources, and how science helps.',
], blocks=[
    P('Everything we use comes from the Earth: the water we drink, the rice we eat, the wood in our furniture, the gas in '
      'our stoves and the metal in our phones. These are **natural resources**. Some will last for ever if we look after them. '
      'Others will one day run out.', 'lead'),
    Cols(
        H('Resources that cycle', 3),
        P('Some resources are used and then return to the environment to be used again. **Water** goes round and round in the '
          '**water cycle**: it evaporates from rivers and seas, forms clouds, falls as rain and flows back to the sea. **Soil** '
          'nutrients cycle when dead plants and animals rot. **Air** is cleaned by plants. Resources that are replaced naturally are '
          '**renewable**: sunlight, wind, water, trees and fish, if we do not use them faster than they are replaced.'),
        Fig(art.water_cycle(labels=art.WATER_CYCLE), 'Water is a resource that cycles.', width='96%'),
        H('Resources that run out', 3),
        P('Other resources took millions of years to form and cannot be replaced. They are **finite** or **non-renewable**: '
          '**natural gas**, **coal**, **oil** and **metals** such as iron and copper. When they are used up, they are gone.'),
        Pics([('sun', 'sunlight'), ('wind energy', 'wind'), ('droplet', 'water'), ('deciduous tree', 'trees'), ('fire', 'gas'), ('rock', 'coal'), ('oil spill', 'oil'), ('nut and bolt', 'metals')],
             cols=4, size='12mm', small=True),
        Box('bd', P('Most of Bangladesh\'s electricity has been made by burning **natural gas** from fields under the ground. These '
                    'gas fields are slowly running out, so the country is building more **solar** power and buying fuel from abroad.')),
        H('Technology: help or harm?', 3),
        Table(['Technology', 'How it helps', 'How it can harm'], [
            ['tube-wells', 'safe drinking water instead of dirty ponds', 'some water has arsenic; too much pumping lowers the water underground'],
            ['plastic', 'cheap, light and waterproof', 'lasts hundreds of years as litter'],
            ['motor boats and cars', 'fast travel and trade', 'burn fuel and pollute the air'],
            ['solar panels', 'clean electricity from sunlight', 'old panels and batteries must be recycled safely']]),
        H('Looking after resources', 3),
        Bullets(['**Saving water**: turn off taps, fix leaks, collect rainwater.',
                 '**Saving energy**: switch off lights and fans, use efficient LED bulbs and better cookstoves.',
                 '**Protecting fish**: stop fishing while fish lay eggs (like the ban on catching hilsa).',
                 '**Planting and protecting forests**: social forestry, where communities plant and care for trees.',
                 '**Reduce, reuse, recycle** materials such as paper, metal and plastic.']),
        H('Science helps solve problems', 3),
        P('Scientists invent **test kits** to find arsenic in tube-well water, breed **rice that grows in salty water**, design '
          '**cleaner cookstoves** that use less wood and make less smoke, and measure pollution so that we know where to act.'),
        H('Sudden and gradual changes', 3),
        P('A **sudden** change, such as a cyclone, can destroy forests and fields in a day. A **gradual** change, such as the water '
          'underground slowly getting lower each year, is harder to notice but just as important. Both can upset the balance '
          '(stability) of an environment, so scientists measure resources every year.'),
    ),
    Vocab([('natural resource', 'something from the Earth that people use'), ('renewable', 'replaced naturally; will not run out if used carefully'),
           ('finite (non-renewable)', 'will run out one day'), ('conserve', 'use carefully so it lasts'), ('sustainable', 'meeting our needs without spoiling things for the future'),
           ('fossil fuel', 'coal, oil or gas formed from ancient living things'), ('groundwater', 'water stored in the ground under our feet')]),
])

facts = Sheet('facts', 'Renewable or finite?', level=1, goals=['Sort resources.', 'Name ways to conserve resources.'], blocks=[
    Q('Sort the resources.',
      Sort(['Renewable (can be replaced)', 'Finite (will run out)'], [('sunlight', 'Renewable (can be replaced)'), ('wind', 'Renewable (can be replaced)'), ('trees', 'Renewable (can be replaced)'),
                                                                     ('fish', 'Renewable (can be replaced)'), ('natural gas', 'Finite (will run out)'), ('coal', 'Finite (will run out)'),
                                                                     ('oil', 'Finite (will run out)'), ('iron', 'Finite (will run out)')]), marks=8),
    Q('Match the action to the resource it saves.',
      Match([('fixing a dripping tap', 'water'), ('switching off the fan', 'electricity'), ('not catching young hilsa', 'fish'), ('using a cleaner cookstove', 'wood')]), marks=4),
    Q('Fill in the gaps.', Blanks('Water is a resource that [cycles] through the environment. Gas and coal are [finite]: they will run out. '
                                  'Using resources carefully so they last is called [conserving] them.', extra=['wasting', 'evaporating']), marks=3),
])

think = Sheet('think', 'Help or hindrance?', level=2, goals=['Evaluate technologies.', 'Explain sustainable choices.'], blocks=[
    Q('Tube-wells gave millions of people in Bangladesh safe water, but some wells have arsenic. Is the tube-well a help or a hindrance? Explain both sides.',
      Lines(4, 'Help: it stopped many diseases from dirty pond water. Hindrance: some water has arsenic, which is a poison, and pumping lowers the groundwater. With testing and safe wells it is mostly a help.'), marks=3),
    Q('Why is it a problem if people catch fish faster than the fish can breed?', Lines(2, 'There will be fewer and fewer fish until they run out, so there is no food or work later.'), marks=2),
    Q('Natural gas will run out. Suggest two other ways Bangladesh could make electricity. Are they renewable?',
      Lines(2, 'Solar panels and wind turbines (renewable); also water power (renewable).'), marks=2),
    Q('Give an example of a **sudden** change and a **gradual** change to a resource.', Lines(2, 'Sudden: a cyclone destroys a forest. Gradual: groundwater gets lower each year.'), marks=2),
])

investigate = Sheet('investigate', 'How much water does a dripping tap waste?', level=2, goals=['Measure volume and time.', 'Use multiplication to scale up.', 'Suggest action.'], blocks=[
    P('Class 4C put a measuring jug under a dripping tap for 10 minutes, three times.'),
    Q('Complete the table.',
      Table(['Test', '1', '2', '3', 'Mean'], [['Water collected in 10 minutes (ml)', '48', '52', '50', Ans('50')]], center=True),
      Lines(1, '(48 + 52 + 50) ÷ 3 = 50 ml'), marks=2),
    Q('Use the mean to work out the water wasted.',
      Table(['Time', 'Water wasted'], [['1 hour (6 × 10 minutes)', Ans('300 ml')], ['1 day (24 hours)', Ans('7200 ml = 7.2 litres')], ['1 week (7 days)', Ans('about 50 litres')]], widths=['50%', '50%']), marks=3),
    Q('Why did they repeat the test three times?', Lines(1, 'To get more reliable results and find a mean.'), marks=1),
    Q('A family needs about 3 litres of drinking water each day for each person. How many people could drink the water wasted in one day?', Lines(1, '7.2 ÷ 3 ≈ 2 people'), marks=2),
    Q('Write a message for your school about saving water.', Lines(2, 'e.g. "One dripping tap wastes 50 litres a week. Turn taps off tightly and report leaks!"'), marks=2),
])

case = Sheet('case', 'Catching the rain on the coast', level=3, goals=['Understand a real water problem.', 'Calculate rainwater from a roof.', 'Evaluate a sustainable solution.'], blocks=[
    Links('Science', 'Maths', 'Health', 'Design'),
    Case('In the south-west coast of Bangladesh, in places like Satkhira and Khulna, the water in ponds and under the ground '
         'has become **salty**. Sea water floods in during cyclones and moves into the ground. Drinking salty water is bad for '
         'health, so many women and girls walk long distances each day to fetch fresh water.',
         'One solution is **rainwater harvesting**. Rain falls on a roof, runs into a gutter and pipe, and is stored in a big '
         'clean tank. The monsoon brings plenty of rain, so a family can store water to drink during the dry season. Rain is a '
         '**renewable** resource that cycles through the environment.',
         source='Based on information about water salinity and rainwater harvesting in coastal Bangladesh.'),
    Q('**Maths.** 1 mm of rain falling on 1 square metre of roof gives 1 litre of water.',
      Table(['Roof area', 'Rain in one storm', 'Water collected'], [['20 square metres', '10 mm', Ans('200 litres')], ['20 square metres', '50 mm', Ans('1000 litres')], ['40 square metres', '50 mm', Ans('2000 litres')]], center=True), marks=3),
    Q('Why is rainwater safer to drink than the pond water on the coast?', Lines(2, 'Rain is fresh water (not salty); stored in a clean, covered tank it stays free of salt and germs.'), marks=2),
    Q('How does a rainwater tank help girls and women?', Lines(2, 'They do not need to walk far to fetch water, so they have more time for school, work and rest.'), marks=2),
    Q('Design a rainwater harvesting system for your school. Label the roof, gutter, pipe, filter and tank.',
      Draw('46mm', 'Rainwater system', 'Roof → gutter → pipe → simple filter (cloth/sand) → covered tank with a tap; first flush thrown away.'), marks=3),
])

review = Sheet('review', 'Show what you know', level=3, goals=['Use key vocabulary.', 'Answer test-style questions.'], blocks=[
    Q('Find the key words.', WordSearch(['RESOURCE', 'WATER', 'GAS', 'SOLAR', 'CONSERVE', 'RECYCLE', 'FOREST', 'FISH', 'RAIN'], size=10, seed=410)),
    Q('Which resource is finite?', MCQ(['sunlight', 'wind', 'natural gas', 'rain'], 2), marks=1),
    Q('Which is a **sustainable** way to fish?', MCQ(['use nets with tiny holes', 'catch fish all year', 'stop fishing while fish lay eggs', 'use poison'], 2, one_col=True), marks=1),
    Q('Draw the water cycle and label: evaporation, condensation, rain, rivers.', Draw('46mm', 'Water cycle', 'Sun heats sea → evaporation → clouds (condensation) → rain → rivers flow back to the sea.'), marks=4),
    Q('**Challenge.** "Trees are renewable, so we can cut down as many as we like." Do you agree? Explain.',
      Lines(3, 'No. Trees are only renewable if we plant new ones and let them grow; if we cut them faster than they grow, forests disappear.'), marks=2),
])

TOPIC = Topic(
    code='B4', strand='earth', title='Earth\'s Resources and Sustainability', short='Resources',
    subtitle='Resources that cycle and resources that run out, technology, conservation and how science helps',
    outcomes=[
        'understand that some of Earth\'s resources cycle through the environment, while others are finite.',
        'discuss how the development of technology is both a help and a hindrance for sustainability.',
        'describe the diverse practices people establish to conserve, protect, sustain and maintain the Earth\'s resources.',
        'explore how science has contributed to understanding and resolving issues related to the impact of human activities.',
        'understand that changes, whether sudden or gradual, have an effect on stability and sustainability.',
    ],
    cambridge=['Unit 2 Living things and environments (2.7 Wonderful water)'],
    sheets=[learn, facts, think, investigate, case, review],
    selfcheck=['sort renewable and finite resources', 'explain how water cycles', 'say how a technology helps and harms',
               'calculate water wasted by a dripping tap', 'describe ways to conserve resources', 'explain rainwater harvesting'],
    cover_art=art.pic_row(['droplet', 'sun', 'wind energy', 'deciduous tree', 'fish']),
)
