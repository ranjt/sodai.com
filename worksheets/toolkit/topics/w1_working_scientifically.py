from build import Sheet, Topic
from ws import (P, H, Box, Vocab, Fig, Cols, Row, Case, Links, Lines, Blanks, Match, TrueFalse, MCQ, Order, Table,
                Ans, Sort, Label, Draw, Graph, WordSearch, Q, Part, Bullets)
import art

learn = Sheet('learn', 'Thinking and working like a scientist', level=1, goals=[
    'Ask questions that can be tested and choose a type of enquiry.',
    'Plan a fair test, measure accurately and record results in tables and graphs.',
    'Spot patterns and anomalies, draw conclusions and use models.',
], blocks=[
    P('Scientists are curious people who ask questions about the world and then **collect evidence** to answer them. You '
      'already work like a scientist whenever you wonder "What will happen if…?" and then try it to find out. This toolkit '
      'is used in **every** science topic you study this year.', 'lead'),
    Cols(
        H('1. Ask a question', 3),
        P('A good scientific question can be **answered by collecting evidence**. "Does warm water dissolve sugar faster than cold '
          'water?" can be tested. "Is sugar nicer than salt?" is an opinion, so it cannot be tested scientifically.'),
        H('2. Choose a type of enquiry', 3),
        Table(['Type of enquiry', 'Example from Grade 5'], [
            ['**fair test**', 'Does the length of a ruler change the pitch of its twang?'],
            ['**observing over time**', 'How does a bean seed change as it germinates?'],
            ['**pattern seeking**', 'Do people with longer legs jump further?'],
            ['**identifying and classifying**', 'Which materials are transparent, translucent or opaque?'],
            ['**research (secondary sources)**', 'How did Ole Rømer find out that light takes time to travel?']]),
        H('3. Plan a fair test', 3),
        P('In a **fair test** you change **one** thing, measure **one** thing and keep **everything else the same**. These '
          'things are called **variables**. If you change two things at once, you cannot tell which one caused the result.'),
        Table(None, [['**Change** (independent variable)', 'the one thing you choose to change'],
                     ['**Measure** (dependent variable)', 'what you measure or observe to see the effect'],
                     ['**Keep the same** (control variables)', 'everything else that could affect the result']]),
        P('Write a **prediction** with a reason: "I think … will happen **because** …". Your reason should use science you know.'),
        H('4. Measure accurately', 3),
        Table(['Measuring…', 'Equipment', 'Unit'], [['length', 'ruler, tape measure', 'mm, cm, m'], ['mass', 'balance (scales)', 'g, kg'],
                                                  ['volume', 'measuring cylinder', 'ml, l'], ['time', 'stopwatch', 's, min'],
                                                  ['temperature', 'thermometer', '°C'], ['force', 'forcemeter', 'N (newtons)'],
                                                  ['light / sound', 'light meter, sound meter', 'lux, dB']]),
        Fig(art.instruments_to_read(), 'Read each scale carefully, with your eye level with the mark.', span=True, width='64%'),
        P('**Repeat** measurements (often three times) and work out the **mean** (average) to make results more **reliable**. A '
          'result that does not fit the pattern is called an **anomaly** (an odd result). Check it and measure again.'),
        Box('tip', P('To find the **mean**: add up the results, then divide by how many results there are. '
                     '(20 + 22 + 24) ÷ 3 = 66 ÷ 3 = **22**.')),
        H('5. Record and present', 3),
        Bullets(['A **table** has clear headings with **units**, e.g. Time (s).',
                 'Use a **bar chart** when the thing you changed is in **groups or words** (types of soil, kinds of fabric).',
                 'Use a **line graph** when the thing you changed is a **number that changes smoothly** (time, temperature, distance).']),
        H('6. Find patterns and conclude', 3),
        P('Look for a **pattern**: "The **longer** the ruler, the **lower** the pitch." Then write a **conclusion** that answers '
          'your question, using the data as evidence, and say whether it **supports your prediction**. Finally, **evaluate**: '
          'How could you improve the investigation?'),
        H('7. Use models', 3),
        P('Scientists use **models** to explain things that are too small, too big, too fast or too slow to see: the particle '
          'model of solids, liquids and gases; a globe and torch for day and night; a wave diagram for sound. Every model is '
          'useful, but every model has **limitations**: it is never exactly like the real thing.'),
    ),
    Vocab([('variable', 'something that can change in an investigation'), ('fair test', 'only one variable is changed'),
           ('prediction', 'what you think will happen, with a reason'), ('reliable', 'results you can trust because they are repeated'),
           ('mean', 'the average of a set of results'), ('anomaly', 'a result that does not fit the pattern'),
           ('conclusion', 'what the results show, answering the question'), ('model', 'a way of representing an idea or object')]),
])

facts = Sheet('facts', 'Tools of the scientist', level=1, goals=['Read scales accurately.', 'Match units to measurements.', 'Name types of enquiry.'], blocks=[
    Q('Read each instrument. Include the unit.', Fig(art.instruments_to_read(), width='90%'),
      Table(['Instrument', 'A measuring cylinder', 'B thermometer', 'C ruler', 'D stopwatch'], [['Reading', Ans('34 ml'), Ans('37 °C'), Ans('7 cm'), Ans('20 s')]], center=True), marks=4),
    Q('Match each measurement to its unit.',
      Match([('mass of an apple', 'grams (g)'), ('force of a push', 'newtons (N)'), ('loudness of a horn', 'decibels (dB)'),
             ('brightness of a room', 'lux'), ('volume of juice', 'millilitres (ml)'), ('time for a race', 'seconds (s)')]), marks=6),
    Q('Sort the questions.',
      Sort(['Can be tested scientifically', 'Cannot be tested (opinion)'], [
          ('Does salt make ice melt faster?', 'Can be tested scientifically'), ('Which fabric dries fastest in the sun?', 'Can be tested scientifically'),
          ('Do bigger seeds grow taller plants?', 'Can be tested scientifically'), ('Is red the best colour?', 'Cannot be tested (opinion)'),
          ('Are cats nicer than dogs?', 'Cannot be tested (opinion)'), ('Which song is the most beautiful?', 'Cannot be tested (opinion)')]), marks=6),
    Q('Write the type of enquiry: **fair test**, **observing over time**, **pattern seeking**, **identifying and classifying** or **research**.',
      Table(['Investigation', 'Type of enquiry'], [
          ['Recording the height of a sunflower every week', Ans('observing over time')],
          ['Sorting leaves by their shape', Ans('identifying and classifying')],
          ['Testing which paper towel soaks up most water', Ans('fair test')],
          ['Reading about how vaccines were discovered', Ans('research')],
          ['Do children who sleep more have faster reaction times?', Ans('pattern seeking')]], widths=['62%', '38%']), marks=5),
])

think = Sheet('think', 'Fair tests, graphs and results', level=2, goals=['Spot unfair tests.', 'Choose the right graph.', 'Calculate a mean and spot anomalies.'], blocks=[
    Q('Rima wants to find out whether ice melts faster in salt water. She puts one ice cube in a cup of salt water in the sun and '
      'a bigger ice cube in a cup of tap water in the shade.',
      Part('Why is this not a fair test?', Lines(2, 'She changed more than one thing: the size of the ice cube and the place (sun or shade) as well as the salt.')),
      Part('How should she change her plan?', Lines(2, 'Use same-sized ice cubes and the same amount of water, put both cups in the same place, and change only salt or no salt.')), marks=4),
    Q('Bar chart or line graph? Tick the best choice.',
      Table(['Results', 'Bar chart', 'Line graph'], [
          ['Height of a plant measured every day for two weeks', Ans(''), Ans('✓')],
          ['Number of learners who like each fruit', Ans('✓'), Ans('')],
          ['Temperature of cooling tea every 5 minutes', Ans(''), Ans('✓')],
          ['Water held by sand, soil and clay', Ans('✓'), Ans('')]], center=True, widths=['60%', '20%', '20%']), marks=4),
    Q('Tanvir timed how long a paper helicopter took to fall three times.',
      Table(['Try', '1', '2', '3', 'Mean'], [['Time (s)', '2.1', '2.3', '2.2', Ans('2.2')]], center=True),
      Part('Work out the mean. Show your working.', Lines(1, '(2.1 + 2.3 + 2.2) ÷ 3 = 6.6 ÷ 3 = 2.2 s')),
      Part('Why is it better to repeat the measurement?', Lines(2, 'Single measurements can have errors; repeating and taking a mean gives more reliable results and shows anomalies.')), marks=3),
    Q('Write a prediction with a reason for this question: "Will a wet towel dry faster on a windy day or a still day?"',
      Lines(2, 'I think it will dry faster on a windy day because wind carries the water vapour away, so evaporation is faster.'), marks=2),
])

investigate = Sheet('investigate', 'Which fabric soaks up the most water?', level=2, goals=['Plan a fair test with repeats.', 'Identify an anomaly and calculate means.', 'Present and evaluate results.'], blocks=[
    P('Class 5D wanted to find the best fabric for a cleaning cloth. They dipped a 10 cm × 10 cm square of each fabric in water '
      'for 30 seconds, let it drip for 10 seconds, then squeezed it into a measuring cylinder. They repeated each test three times.'),
    Q('Complete the plan.',
      Table(None, [['Question', Ans('Which fabric soaks up the most water?')], ['Change', Ans('type of fabric')],
                   ['Measure', Ans('volume of water squeezed out (ml)')],
                   ['Keep the same', Ans('size of square, dipping time, dripping time, squeezing, same water')]], widths=['24%', '76%']), marks=4),
    Q('Here are the results.',
      Table(['Fabric', 'Test 1 (ml)', 'Test 2 (ml)', 'Test 3 (ml)', 'Mean (ml)'], [
          ['cotton gamchha', '18', '19', '17', Ans('18')], ['jute (*pat*)', '12', '25', '13', Ans('12.5 (without the anomaly)')],
          ['polyester', '6', '5', '7', Ans('6')], ['newspaper', '9', '8', '10', Ans('9')]], center=True),
      Part('Circle the anomaly. Suggest a reason for it.', Lines(2, 'Jute test 2 (25 ml). Perhaps the square was bigger, left in the water longer or not allowed to drip.')),
      Part('Work out the mean for each fabric and write it in the table. Leave out the anomaly.'), marks=5),
    Q('Draw a bar chart of the means.',
      Graph(['gamchha', 'jute', 'polyester', 'newspaper'], [18, 12.5, 6, 9], 'Mean water held (ml)', 'Fabric', ymax=20, step=2, width=110, height=44), marks=3),
    Q('Write a conclusion and suggest one improvement.',
      Lines(2, 'The cotton gamchha soaked up the most water (18 ml) and polyester the least (6 ml), so cotton is best for a cleaning cloth. Improvement: repeat the anomalous test, or test more fabrics.'), marks=3),
])

case = Sheet('case', 'Two Boses: scientists from Bengal', level=3, goals=['Learn how real scientists work.', 'Link evidence, creativity and new instruments.', 'Reflect on sharing knowledge.'], blocks=[
    Links('Science', 'History', 'Maths', 'Language', 'Ethics'),
    Case('**Jagadish Chandra Bose** was born in **1858** in Mymensingh, in what is now Bangladesh. He studied in Kolkata, '
         'Cambridge and London, then became a professor in Kolkata. In **1895** he showed that invisible radio waves could ring a '
         'bell and set off a small explosion in another room, one of the earliest demonstrations of **wireless** signals.',
         'Later he asked a bold question: do **plants** respond to the world as animals do? Plant growth is far too slow to see, so '
         'he invented the **crescograph**, which magnified tiny movements about **10 000 times**. His careful measurements showed '
         'that plants react to light, heat, touch and chemicals. Bose believed knowledge should be **shared** with everyone and was '
         'reluctant to make money from patents. He also wrote one of the first science fiction stories in Bengali, about a '
         'cyclone stopped by a bottle of hair oil!',
         '**Satyendra Nath Bose** taught physics at **Dhaka University** from 1921. In **1924**, in Dhaka, he wrote a new way of '
         'explaining light and sent it to **Albert Einstein**, who was so impressed that he translated it into German himself. A '
         'whole family of tiny particles, **bosons**, is named after him.',
         source='Based on biographies of J. C. Bose (Bose Institute) and S. N. Bose (University of Dhaka).'),
    Q('Put these events in order.',
      Order(['J. C. Bose is born in Mymensingh (1858).', 'J. C. Bose demonstrates wireless signals (1895).',
             'S. N. Bose starts teaching at Dhaka University (1921).', 'S. N. Bose sends his paper to Einstein (1924).']), marks=2),
    Q('**Maths.** A plant grows 0.002 mm in one minute. The crescograph magnifies 10 000 times. How far does the pointer move in one minute?',
      Lines(1, '0.002 × 10 000 = 20 mm (2 cm)'), marks=2),
    Q('Why did J. C. Bose need to **invent** a new instrument? What does this tell you about how science moves forward?',
      Lines(3, 'Plant movements were too small and slow to see or measure with existing tools. New instruments let scientists collect new evidence and answer new questions.'), marks=2),
    Q('J. C. Bose shared his discoveries freely instead of keeping them secret to make money. What are the benefits and problems of sharing?',
      Table(['Benefits of sharing', 'Problems of sharing'], [[Ans('others can build on the ideas; science moves faster; everyone gains'), Ans('the scientist may earn no money to fund more research; others may take credit')]], widths=['50%', '50%']), marks=2),
    Q('**Design.** Invent an instrument to measure something too small, slow or fast to see. Draw it and explain what it measures.',
      Draw('36mm', 'My instrument', 'Any reasoned idea, e.g. a long pointer lever to magnify how much a seed swells; a sound-triggered timer for fast events.'), marks=2),
])

review = Sheet('review', 'Show what you know', level=3, goals=['Use key vocabulary.', 'Answer test-style questions.'], blocks=[
    Q('Find the key words.', WordSearch(['VARIABLE', 'FAIR', 'PREDICT', 'MEASURE', 'REPEAT', 'GRAPH', 'TABLE', 'MODEL', 'PATTERN'], size=11, seed=191)),
    Q('Which unit measures force?', MCQ(['grams', 'newtons', 'litres', 'degrees Celsius'], 1), marks=1),
    Q('A result that does not fit the pattern is called…', MCQ(['a conclusion', 'a variable', 'an anomaly', 'a prediction'], 2), marks=1),
    Q('Draw a results table for this investigation: "How does the temperature of water change the time sugar takes to dissolve?" '
      'Include headings with units and space for three repeats.',
      Draw('34mm', 'My table', 'Columns: Temperature (°C) | Time 1 (s) | Time 2 (s) | Time 3 (s) | Mean time (s), with rows for each temperature.'), marks=3),
    Q('**Challenge.** We often draw particles in a solid as circles in neat rows. Give **one** way this model is useful and **one** limitation.',
      Lines(3, 'Useful: it shows that particles are close together and in a pattern. Limitation: real particles are far too small to see, are always vibrating, and are not flat circles.'), marks=2),
])

TOPIC = Topic(
    code='W1', strand='skills', title='The Scientist\'s Toolkit', short='Working scientifically',
    subtitle='Questions, enquiry types, fair tests, measuring, tables and graphs, patterns, conclusions and models',
    outcomes=[
        'observe carefully in order to gather data — examining objects and living things, observing change over a period of time, distinguishing between significant and less significant observations, and recording observations systematically.',
        'use a variety of instruments and tools to measure data accurately, selecting appropriate tools and units, and measuring, comparing and recording mass, weight, time and temperature.',
        'decide when observations and measurements need to be checked by repeating them, to give more reliable data.',
        'use tables, bar charts and line graphs to present results.',
        'identify or generate a question or problem to be explored, posing questions and defining problems that will facilitate effective investigation.',
        'plan and carry out systematic investigations, manipulating variables as necessary, and recognize the way in which an experiment is unfair if the relevant variables are not controlled.',
        'make and test predictions, using scientific knowledge and understanding to justify them.',
        'identify patterns in results, and results that do not appear to fit the pattern.',
        'use results to draw conclusions and to make further predictions; say if and how the evidence supports any prediction made.',
        'consider scientific models and the applications of these models, including their limitations.',
        'consider how scientists have combined evidence from observation and measurement with creative thinking to suggest new ideas and explanations for phenomena.',
    ],
    sheets=[learn, facts, think, investigate, case, review],
    selfcheck=['ask a question that can be tested', 'name the five types of enquiry', 'plan a fair test with variables',
               'read scales and use the right units', 'calculate a mean and spot an anomaly', 'choose a bar chart or line graph',
               'explain how J. C. Bose combined measurement and creativity'],
    cover_art=art.instruments_to_read(),
)
