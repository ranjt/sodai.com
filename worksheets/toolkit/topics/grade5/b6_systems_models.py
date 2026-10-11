from build import Sheet, Topic
from ws import (P, H, Box, Vocab, Fig, Cols, Row, Case, Links, Lines, Blanks, Match, TrueFalse, MCQ, Order, Table,
                Ans, Sort, Label, Draw, Graph, WordSearch, Q, Part, Bullets)
import art

learn = Sheet('learn', 'Systems, models and clever technologies from the past', level=1, goals=[
    'Explain what a system and a model are, and the limits of models.',
    'Describe technologies from different civilisations.',
    'Explain how past technologies still affect our lives today.',
], blocks=[
    P('A bicycle, a beehive, the water cycle and the human body are all **systems**: sets of parts that work together and '
      'affect each other. Scientists and engineers use **models** to understand systems and to predict what will happen.', 'lead'),
    Cols(
        H('Systems', 3),
        P('Every system has **parts**, **connections** between them, and often **inputs** and **outputs**. In a tube-well, the '
          'input is your push on the handle, the parts are the handle, rod and valve, and the output is water. If one part '
          'breaks, the whole system may stop working.'),
        H('Models', 3),
        P('A **model** is a simpler way of showing something real. A **globe** models the Earth; a **map** models a town; a '
          'diagram of the water cycle models how water moves; weather forecasters use **computer models** to predict cyclones.'),
        Box('think', P('**Every model has limits.** A globe shows the shape of the Earth but not its real size or the '
                       'clouds moving over it. Good scientists always ask: "What does this model show well? What does it leave out?"')),
        H('Technologies from past civilisations', 3),
        Bullets([
            '**Indus Valley (about 4500 years ago):** cities such as Mohenjo-daro had planned streets, baked-brick houses and covered **drains** to carry dirty water away.',
            '**Ancient Egypt:** the **shadoof**, a long pole on a pivot with a bucket on one end and a heavy weight on the other, lifted water from the Nile to the fields. It is a **lever**.',
            '**Persia (Iran):** tall **windcatchers** caught the breeze and sent it down into houses to cool them, without electricity. Underground channels called **qanats** carried water across deserts.',
            '**China:** paper, the magnetic **compass** and printing.',
            '**The Islamic world (around 1200):** the engineer **al-Jazari** designed water-raising machines and clocks using gears and cranks.',
            '**Bengal:** for centuries weavers made **muslin**, a cotton cloth so fine that a whole sari could pass through a ring. Ancient cities such as **Wari-Bateshwar** traded beads across Asia more than 2000 years ago.',
        ]),
        Fig(art.shadoof(), 'A shadoof: a lever for lifting water.'),
        Fig(art.windcatcher(), 'A windcatcher sends cool air through a house.'),
        H('From the past to the present', 3),
        P('Today\'s **sewers** follow the same idea as Indus drains. **Cranes** use the lever and pulley ideas of the shadoof. '
          'Architects design new buildings with windcatcher-style towers to save energy. Old ideas often inspire new solutions.'),
    ),
    Vocab([('system', 'parts that work together'), ('input', 'what goes into a system'), ('output', 'what comes out of a system'),
           ('model', 'a simpler representation of something real'), ('limitation', 'something a model cannot show'),
           ('technology', 'tools and inventions people make to solve problems'), ('civilisation', 'a large, organised society')]),
])

facts = Sheet('facts', 'Inventions and where they came from', level=1, goals=['Link technologies to civilisations.', 'Identify parts of a system.'], blocks=[
    Q('Match each technology to the civilisation it came from.',
      Match([('covered drains in planned cities', 'Indus Valley'), ('shadoof', 'Ancient Egypt'), ('windcatchers and qanats', 'Persia'),
             ('magnetic compass', 'China'), ('fine muslin cloth', 'Bengal')]), marks=5),
    Q('Complete the table for a hand tube-well system.',
      Table(['Inputs', 'Parts', 'Outputs'], [[Ans('a push on the handle (force)'), Ans('handle, rod, plunger, valves, pipe'), Ans('water from underground')]], center=True), marks=3),
    Q('True or false?', TrueFalse([
        ('A globe is a model of the Earth.', True),
        ('Models always show everything about the real thing.', False, 'All models have limitations; they leave some things out.'),
        ('A shadoof is a kind of lever.', True), ('Windcatchers need electricity to work.', False, 'They use the wind.')]), marks=4),
    Q('Name **three** models you have used in school.', Lines(2, 'e.g. a globe, a map, a skeleton model, a water cycle diagram, a solar system model, a paper helicopter'), marks=3),
])

think = Sheet('think', 'How did it work? Why does it matter?', level=2, goals=['Explain how old technologies work.', 'Evaluate models.'], blocks=[
    Q('Explain how a shadoof makes lifting water easier.',
      Lines(3, 'It is a lever on a pivot: the heavy counterweight on one end helps lift the full bucket, so the farmer needs less force.'), marks=2),
    Q('Why were covered drains important for the health of people in Mohenjo-daro?',
      Lines(2, 'They carried dirty water and waste away from homes, so fewer germs spread and fewer people got diseases.'), marks=2),
    Q('Choose one model and complete the table.',
      Table(['Model', 'What it shows well', 'What it does not show'], [
          [Ans('e.g. a globe'), Ans('the shape of the Earth, continents and oceans'), Ans('real size, mountains\' height, weather, the Earth\'s movement')]], center=True), marks=3),
    Q('A weather forecaster says, "Our computer model predicts the cyclone will reach the coast on Tuesday." Why do '
      'forecasts sometimes change as the storm gets closer?',
      Lines(3, 'The model is a prediction based on data; new measurements of the storm (from satellites) update the model, so the prediction gets more accurate.'), marks=2),
    Q('How could an old idea help solve a problem in Dhaka today? Give one example.',
      Lines(3, 'e.g. windcatcher towers to cool buildings without air conditioning; rainwater harvesting like old step-wells; drains like the Indus cities to stop waterlogging.'), marks=2),
])

investigate = Sheet('investigate', 'Does a windcatcher model cool a room?', level=2, goals=['Test a model fairly.', 'Interpret results.', 'Evaluate the model.'], blocks=[
    P('Class 5B made three model houses from shoe boxes. They put each one 50 cm from a desk fan and a lamp for 20 minutes '
      'and then measured the temperature inside. All boxes started at 26 °C.'),
    Table(['Model house', 'Temperature after 20 minutes (°C)'], [
        ['A: no tower, closed', '34'], ['B: windcatcher tower facing the fan', '30'], ['C: windcatcher tower with a wet cloth inside', '27']], center=True),
    Q('Draw a bar chart of the temperatures.',
      Graph(['A: no tower', 'B: tower', 'C: tower + wet cloth'], [34, 30, 27], 'Temperature (°C)', 'Model house', ymax=36, step=2, width=130, height=66), marks=4),
    Q('Which house stayed coolest? Explain why, using the words *wind* and *evaporation*.',
      Lines(3, 'House C: the tower brought in moving air (wind), and water evaporating from the wet cloth took heat away, cooling the air further.'), marks=3),
    Q('Name **two** things the class kept the same.', Lines(2, 'distance from the fan and lamp, time (20 minutes), size of box, starting temperature, thermometer'), marks=2),
    Q('Give **one** limitation of this model compared with a real house.',
      Lines(2, 'A shoe box is tiny; real wind changes direction and strength; a real house has people, sun on the roof and many rooms.'), marks=1),
])

case = Sheet('case', 'Bringing back Dhaka muslin', level=3, goals=['Explain how a past technology connects to today.', 'Consider history, science and economics together.', 'Form an opinion with reasons.'], blocks=[
    Links('Science', 'History', 'Design', 'Economics', 'Culture'),
    Case('For hundreds of years, weavers in the Dhaka region made **muslin**, one of the finest cloths in the world. It was '
         'woven from a special cotton plant called **phuti karpas**, which grew along the banks of the Meghna river. Spinners '
         'twisted its short fibres into threads so thin they were almost invisible, often working in the damp morning air so '
         'that the threads did not break.',
         'Muslin was traded to kings and queens across Asia and Europe. But in the 1800s, cheap machine-made cloth from '
         'factories, changes in trade and the loss of the skilled workers caused muslin making to die out. Even the phuti '
         'karpas plant was thought to be lost.',
         'Recently, Bangladeshi scientists and weavers searched for the plant, compared its DNA with old muslin samples in '
         'museums, grew it again and trained weavers. In 2021 they succeeded in weaving new Dhaka muslin.',
         source='Based on news reports about the Bangladesh muslin revival project.'),
    Q('Draw a timeline of the story of Dhaka muslin with at least four events.',
      Draw('32mm', 'Timeline', 'centuries of muslin making → famous across Asia and Europe → 1800s decline (factory cloth, trade changes) → plant thought lost → scientists find the plant and compare DNA → 2021 new muslin woven'), marks=3),
    Q('How did scientists use **evidence** to find the right cotton plant?',
      Lines(3, 'They compared the DNA of plants they found with DNA from old muslin samples in museums to find a match.'), marks=2),
    Q('Why did spinners work in damp air? Use what you know about materials.',
      Lines(2, 'Damp air kept the very fine cotton fibres slightly moist and flexible, so the threads were less likely to snap.'), marks=2),
    Q('Muslin is very expensive and slow to make. Should the government keep supporting the revival? Give your opinion and two reasons.',
      Lines(4, 'Accept reasoned views, e.g. Yes: it protects heritage, gives skilled jobs, attracts tourism and pride. Or: money could go to other needs, so it should become self-supporting.'), marks=3),
])

review = Sheet('review', 'Show what you know', level=3, goals=['Use key vocabulary.', 'Answer test-style questions.'], blocks=[
    Q('Find the key words.', WordSearch(['SYSTEM', 'MODEL', 'INPUT', 'OUTPUT', 'LEVER', 'DRAIN', 'MUSLIN', 'COMPASS', 'GLOBE'], size=11, seed=17)),
    Q('Which is a model of the Earth?', MCQ(['a compass', 'a globe', 'a shadoof', 'a drain'], 1), marks=1),
    Q('What does a windcatcher do?', MCQ(['lifts water', 'cools a building using the wind', 'tells the time', 'makes electricity'], 1), marks=1),
    Q('Design a model to show one system you have learned about this year (for example, the water cycle or the digestive system). List the materials and one limitation.',
      Draw('45mm', 'My model', 'Any sensible model with labelled parts, materials listed and a limitation (e.g. not to scale, does not move).'), marks=3),
    Q('**Challenge.** Explain why a city is a system. Name three parts and how they depend on each other.',
      Lines(3, 'It has many connected parts: e.g. roads, water supply, drains, electricity, people. If drains block, roads flood and transport stops.'), marks=2),
])

TOPIC = Topic(
    code='B6', strand='earth', title='Systems, Models and Technologies', short='Systems and models',
    subtitle='Systems and models, their limits, and technologies from past civilisations that shape our lives today',
    outcomes=[
        'design models to represent systems and their interactions.',
        'use models to simulate systems and the interactions between them, and to predict the behaviour of a system.',
        'explore different technologies found in different civilizations.',
        'describe the impact of systems and technologies from past civilizations in present times.',
    ],
    sheets=[learn, facts, think, investigate, case, review],
    selfcheck=['explain what a system is, with inputs and outputs', 'explain what a model is and its limits',
               'describe technologies from four civilisations', 'explain how a shadoof and a windcatcher work',
               'test a model fairly', 'explain how an old technology still matters today'],
    cover_art=f'<div class="row"><div>{art.shadoof()}</div><div>{art.windcatcher()}</div></div>',
)
