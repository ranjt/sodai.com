from build import Sheet, Topic
from ws import (P, H, Box, Vocab, Fig, Cols, Row, Case, Links, Lines, Blanks, Match, TrueFalse, MCQ, Order, Table,
                Ans, Sort, Label, Draw, Graph, WordSearch, Q, Part, Bullets)
import art

learn = Sheet('learn', 'Using the Earth\'s resources wisely', level=1, goals=[
    'Explain what "renewable" and "non-renewable" mean.',
    'Compare how long different resources take to regenerate.',
    'Explain how human actions such as recycling, conservation and over-use affect the Earth.',
], blocks=[
    P('Everything we use comes from the Earth: the air we breathe, the water we drink, the rice we eat, the gas that cooks '
      'it, the bricks of our homes and the phone in our pocket. These useful things are **natural resources**. Some will '
      'run out; others can last for ever if we use them with care.', 'lead'),
    Cols(
        H('Renewable and non-renewable', 3),
        P('A **renewable** resource is replaced by nature in a short time, or never runs out: sunlight, wind, flowing water, '
          'and living things such as trees, fish and crops, as long as we do not take too many. A **non-renewable** resource '
          'takes so long to form that, once used, it is gone for us: **coal, oil, natural gas** and metals in rocks.'),
        H('How long does it take to come back?', 3),
        Table(['Resource', 'Time to regenerate (approximate)'], [
            ['sunlight, wind', 'never runs out'], ['hilsa fish population', '1–2 years if young fish are protected'],
            ['bamboo', '3–5 years'], ['a teak or mahogany tree', '20–50 years'], ['groundwater', 'years to thousands of years'],
            ['a few centimetres of soil', 'hundreds of years'], ['coal, oil, natural gas', 'millions of years']]),
        P('Even renewable resources can run out if we use them faster than they regenerate. Cutting a forest in one year that '
          'took 50 years to grow is not sustainable.'),
        H('Sustainability', 3),
        P('**Sustainable** use means meeting our needs **today** without stopping people in the **future** from meeting '
          'theirs. It means using renewable resources no faster than they come back, and using non-renewable ones carefully.'),
        Box('bd', P('Bangladesh makes most of its electricity from **natural gas**, but its gas fields are slowly running out. '
                    'Millions of homes in villages now use **solar panels**, and the country is building more solar parks.')),
        H('The 5 Rs', 3),
        Bullets(['**Refuse** what you do not need (say no to a plastic bag).', '**Reduce** how much you use.',
                 '**Reuse** things again and again.', '**Recycle** materials into new products.',
                 '**Rot**: compost food and plant waste.']),
        H('People can help or harm', 3),
        Bullets(['**Harm:** over-fishing, cutting forests, wasting water, dumping plastic, burning too much fuel.',
                 '**Help:** recycling, tree planting, protecting young fish, national parks and saving endangered animals.']),
        Box('history', P('In **2002** Bangladesh became one of the first countries in the world to **ban thin plastic shopping '
                         'bags**, after they blocked drains and made floods in Dhaka worse.'), title='Bangladesh first'),
        Box('fact', P('Vultures clean up dead animals and stop diseases spreading. Bangladesh lost most of its vultures because '
                      'of a cattle medicine (diclofenac) that poisoned them. The medicine was banned in 2010 and "vulture safe '
                      'zones" were created to help them recover.')),
    ),
    Vocab([('natural resource', 'something useful we get from nature'), ('renewable', 'replaced naturally in a short time'),
           ('non-renewable', 'will run out because it takes millions of years to form'), ('sustainable', 'meeting today\'s needs without harming the future'),
           ('regenerate', 'grow back or be replaced'), ('fossil fuel', 'coal, oil or gas formed from ancient living things'),
           ('conservation', 'protecting nature and resources')]),
])

facts = Sheet('facts', 'Renewable or not?', level=1, goals=['Classify resources.', 'Use the key vocabulary.'], blocks=[
    Q('Sort the resources.',
      Sort(['Renewable', 'Non-renewable'], [('sunlight', 'Renewable'), ('wind', 'Renewable'), ('bamboo', 'Renewable'), ('fish', 'Renewable'),
                                           ('coal', 'Non-renewable'), ('natural gas', 'Non-renewable'), ('oil', 'Non-renewable'), ('iron ore', 'Non-renewable')]), marks=8),
    Q('Put these in order from fastest to slowest to regenerate (1 = fastest).',
      Order(['hilsa population (1–2 years)', 'bamboo (3–5 years)', 'a mahogany tree (20–50 years)', 'soil (hundreds of years)', 'natural gas (millions of years)'], seed=3), marks=3),
    Q('Match each "R" to an example.',
      Match([('refuse', 'say no to a plastic straw'), ('reduce', 'turn off the tap while brushing teeth'),
             ('reuse', 'refill a water bottle'), ('recycle', 'turn old paper into new paper'), ('rot', 'compost vegetable peel')]), marks=5),
    Q('Fill in the gaps.',
      Blanks('Using resources in a way that does not harm future generations is called [sustainable] use. Coal, oil and gas '
             'are [fossil] fuels. Bangladesh banned thin plastic bags in [2002].', extra=['1971', 'renewable']), marks=3),
])

think = Sheet('think', 'Is it sustainable?', level=2, goals=['Evaluate whether uses of resources are sustainable.', 'Explain the impact of human activities.'], blocks=[
    Q('For each example, decide if it is sustainable and explain why.',
      Table(['Example', 'Sustainable?', 'Why?'], [
          ['Planting a new tree for every tree cut down', Ans('yes'), Ans('the forest regrows as fast as it is used')],
          ['Catching every hilsa, even the young jatka', Ans('no'), Ans('fish are taken before they can breed, so numbers fall')],
          ['Using solar panels for electricity', Ans('yes'), Ans('sunlight is renewable and never runs out')],
          ['Pumping more groundwater than the rain replaces', Ans('no'), Ans('the water level keeps falling')]], widths=['44%', '16%', '40%']), marks=8),
    Q('Why is natural gas called non-renewable, even though it was made by nature?',
      Lines(2, 'It took millions of years to form from ancient living things; we use it far faster than it can form again.'), marks=2),
    Q('Explain how banning plastic bags helps both the environment and people in cities.',
      Lines(3, 'Fewer bags blocking drains means less flooding; less plastic in rivers and soil harms fewer animals; saves oil used to make plastic.'), marks=2),
    Q('Why does saving vultures matter to people too?',
      Lines(2, 'Vultures eat dead animals, removing a source of disease and keeping the environment clean.'), marks=2),
])

investigate = Sheet('investigate', 'Our class rubbish audit', level=2, goals=['Collect, sort and record data.', 'Present data in a bar chart.', 'Use evidence to plan action.'], blocks=[
    P('Class 5A collected all the rubbish from their classroom for one week, sorted it and weighed each type.'),
    Q('Complete the table.',
      Table(['Type of rubbish', 'Mass (g)', 'Can it be recycled, reused or composted?'], [
          ['paper and card', '1800', Ans('yes: recycle')], ['plastic wrappers and bottles', '950', Ans('some bottles recycle; wrappers mostly no')],
          ['food waste', '1200', Ans('yes: compost')], ['pencil shavings', '150', Ans('yes: compost')], ['other', '300', Ans('mostly no')]], widths=['36%', '16%', '48%']), marks=5),
    Q('Draw a bar chart of the results.',
      Graph(['paper', 'plastic', 'food', 'shavings', 'other'], [1800, 950, 1200, 150, 300], 'Mass (g)', 'Type of rubbish', ymax=2000, step=200,
            width=150, height=66), marks=4),
    Q('What was the total mass of rubbish? What fraction was paper and card?',
      Lines(2, 'Total = 1800 + 950 + 1200 + 150 + 300 = 4400 g. Paper: 1800 out of 4400, a bit less than half.'), marks=2),
    Q('Use the data to suggest **two** actions the class could take. Say which "R" each one is.',
      Lines(3, 'e.g. use both sides of paper (reduce) and put a paper recycling box in class (recycle); start a compost bin for food (rot); bring tiffin in reusable boxes (reuse/refuse).'), marks=2),
])

case = Sheet('case', 'Saving the hilsa', level=3, goals=['Explain how rules help a renewable resource regenerate.', 'Interpret data over time.', 'Consider different points of view.'], blocks=[
    Links('Science', 'Economics', 'Maths', 'Ethics', 'Culture'),
    Case('The **hilsa** (*ilish*) is the national fish of Bangladesh. Millions of people depend on catching, selling and '
         'eating it. Adult hilsa swim from the sea up rivers such as the Meghna and Padma to lay their eggs. The young fish, '
         'called **jatka**, then swim back to the sea to grow.',
         'In the past, so many jatka and breeding adults were caught that the hilsa catch fell. So the government made rules: '
         'catching jatka is banned for several months of the year, fishing is banned for **22 days** during the main breeding '
         'season in October, and some rivers are **sanctuaries**. During the bans, poor fishing families receive free rice.',
         source='Information from the Department of Fisheries, Bangladesh. Catch figures are approximate.'),
    Q('Use the data (approximate hilsa catch in lakh tonnes; 1 lakh = 100 000).',
      Table(['Year', '2008–09', '2012–13', '2016–17', '2020–21'], [['Hilsa catch (lakh tonnes)', '3.0', '3.5', '5.0', '5.7']], center=True),
      Graph(['2008–09', '2012–13', '2016–17', '2020–21'], [3.0, 3.5, 5.0, 5.7], 'Catch (lakh tonnes)', 'Year', ymax=6, step=1, kind='line',
            width=130, height=62),
      Part('Plot the graph and describe the trend.', Lines(2, 'The catch increased steadily, almost doubling from 3.0 to 5.7 lakh tonnes.')),
      Part('Suggest how the fishing bans helped.', Lines(2, 'More adults could breed and more jatka could grow up, so the population increased.')), marks=5),
    Q('Why are the bans an example of using a **renewable** resource sustainably?',
      Lines(2, 'Fish can regenerate if enough are left to breed; the bans give them time to grow back, so people can keep fishing in future.'), marks=2),
    Q('Complete the table to show different points of view.',
      Table(['Person', 'View'], [['a fisher during the 22-day ban', Ans('I cannot earn money; the rice helps but is not enough.')],
                                 ['a fisheries scientist', Ans('The ban lets hilsa breed, so there are more fish for everyone later.')],
                                 ['a family buying fish in Dhaka', Ans('We cannot buy fresh hilsa for a few weeks, but prices stay lower later.')]], widths=['36%', '64%']), marks=3),
    Q('Suggest **one** more way to help fishing families during the ban.',
      Lines(2, 'e.g. training for other jobs, small loans, cash support, help to farm fish in ponds or make nets.'), marks=1),
])

review = Sheet('review', 'Show what you know', level=3, goals=['Use key vocabulary.', 'Answer test-style questions.'], blocks=[
    Q('Find the key words.', WordSearch(['RENEWABLE', 'RECYCLE', 'REUSE', 'REDUCE', 'SOLAR', 'GAS', 'COAL', 'HILSA', 'FOREST'], size=11, seed=91)),
    Q('Which of these is a renewable source of energy?', MCQ(['coal', 'natural gas', 'wind', 'oil'], 2), marks=1),
    Q('What does "sustainable" mean?', MCQ(['using everything now', 'meeting our needs without harming future generations', 'never using any resources', 'only using metals'], 1, one_col=True), marks=1),
    Q('Make a poster plan to persuade your school to save one resource (water, paper or electricity). Include a fact, a picture idea and an action.',
      Draw('50mm', 'My poster plan', 'Any clear poster with a correct fact, an image idea and a practical action (e.g. "Turn off fans when you leave").'), marks=3),
    Q('**Challenge.** Trees are renewable, yet forests can disappear. Explain how.',
      Lines(3, 'If trees are cut faster than they can grow back (20–50 years), the forest shrinks; renewable resources can still run out if over-used.'), marks=2),
])

TOPIC = Topic(
    code='B5', strand='earth', title='Resources and Sustainability', short='Resources',
    subtitle='Renewable and non-renewable resources, regeneration time, the 5 Rs and how people affect the Earth',
    outcomes=[
        'consider what is meant by the term "renewable" in relation to the Earth\'s resources.',
        'identify timescales for the regeneration of resources.',
        'understand that resources must be used sustainably for the benefit of present generations without compromising the needs of future generations.',
        'explain how human activities in the environment — such as recycling and animal conservation, or the exploitation of natural resources — have an impact on Earth.',
    ],
    sheets=[learn, facts, think, investigate, case, review],
    selfcheck=['explain renewable and non-renewable', 'order resources by how long they take to regenerate', 'explain what sustainable means',
               'give examples of the 5 Rs', 'collect and present data about waste', 'explain how fishing rules help the hilsa'],
    cover_art=art.svg(300, 120, art.sun_icon(60, 60, 30) + art.wind_lines(130, 50) + art.wind_lines(130, 76) + art.cloud(240, 60, 0.9, art.LIGHT)),
)
