from build import Sheet, Topic
from ws import (P, H, Box, Vocab, Fig, Cols, Row, Case, Links, Lines, Blanks, Match, TrueFalse, MCQ, Order, Table,
                Ans, Sort, Label, Draw, Graph, WordSearch, Q, Part, Bullets, Pics)
import art
import art4

learn = Sheet('learn', 'How to be a science detective', level=1, goals=[
    'Ask questions that can be tested and make predictions.',
    'Plan a fair test and measure carefully with the right tools and units.',
    'Present results in tables and graphs, find patterns and draw conclusions.',
], blocks=[
    P('Detectives look for clues, collect evidence and use it to solve mysteries. Scientists do the same! They **observe** '
      'the world, ask **questions**, **test** their ideas and use **evidence** to find answers. You can work like a scientist too.', 'lead'),
    Pics([('magnifying glass', 'observe'), ('scientist', 'ask and predict'), ('test tube', 'test'), ('ruler', 'measure'), ('bar chart', 'record'), ('check mark', 'conclude')], cols=6, size='13mm', small=True),
    Cols(
        H('1. Observe and ask', 3),
        P('Use your **senses** (and tools such as a hand lens) to look closely. Then ask a question you can **test**, such as "Which '
          'paper towel soaks up the most water?" or "Does a ball bounce higher if it is dropped from higher up?"'),
        H('2. Predict', 3),
        P('A **prediction** says what you think will happen **and why**: "I think the ball will bounce higher from higher up, '
          '**because** it will be moving faster when it hits the ground."'),
        H('3. Plan a fair test', 3),
        P('In a **fair test**, you change only **one** thing and keep everything else the same. Otherwise you will not know what caused the result.'),
        Table(None, [['**I will change…**', 'one thing (for example, the height of the drop)'], ['**I will measure…**', 'the result (how high it bounces)'],
                     ['**I will keep the same…**', 'everything else (the same ball, the same floor, the same person measuring)']]),
        H('4. Measure carefully', 3),
        Table(['To measure…', 'Use a…', 'Unit'], [['length', 'ruler or tape measure', 'cm, m'], ['volume', 'measuring cylinder or jug', 'ml, l'], ['temperature', 'thermometer', '°C'],
                                                 ['time', 'stopwatch', 'seconds (s), minutes'], ['force', 'forcemeter', 'newtons (N)'], ['mass', 'balance (scales)', 'g, kg']]),
        Fig(art.instruments_to_read(), 'Read the scale with your eye level with the mark.', span=True, width='70%'),
        P('Do each test **more than once**. If the results are close, you can trust them more. If one result is very different, '
          'check it and measure again.'),
        H('5. Record and present', 3),
        P('Record results in a **table** with clear headings and units. Then show them in a **bar chart** (when you compare '
          'separate things, like different balls) or a **line graph** (when you measure something changing, like temperature over time).'),
        H('6. Find patterns and conclude', 3),
        P('Look for a **pattern**: "The higher the drop, the higher the bounce." Write a **conclusion** that answers your question, '
          'and say whether the results **support your prediction**. Do you have **enough** evidence, or should you test more?'),
        H('7. Models and explaining', 3),
        P('Scientists use **models** (drawings, globes, diagrams) to explain things that are too big, too small or too slow to see. '
          'They share their findings so others can check them, and they combine evidence with **creative ideas**.'),
        Box('bd', P('**Dr Firdausi Qadri** is a Bangladeshi scientist at icddr,b in Dhaka. Through careful tests with thousands of '
                    'people, she helped bring low-cost vaccines against cholera and typhoid to the children of Bangladesh.')),
    ),
    Vocab([('observe', 'look closely using your senses'), ('prediction', 'what you think will happen, and why'), ('fair test', 'change one thing; keep everything else the same'),
           ('evidence', 'facts and measurements that support an idea'), ('pattern', 'something that is repeated in the results'), ('conclusion', 'what the results show'),
           ('reliable', 'results you can trust because you repeated them'), ('model', 'a way of showing an idea we cannot easily see')]),
])

facts = Sheet('facts', 'Tools and steps', level=1, goals=['Choose equipment and units.', 'Order the steps of an investigation.'], blocks=[
    Q('Read each instrument. Include the unit.', Fig(art.instruments_to_read(), width='86%'),
      Table(['A', 'B', 'C', 'D'], [[Ans('34 ml'), Ans('37 °C'), Ans('7 cm'), Ans('20 s')]], center=True), marks=4),
    Q('Match the measurement to the tool.', Match([('how hot the water is', 'thermometer'), ('how long a race takes', 'stopwatch'), ('how long a leaf is', 'ruler'),
                                                  ('how much juice is in a glass', 'measuring jug'), ('how hard you pull a rope', 'forcemeter')]), marks=5),
    Q('Put the steps of an investigation in order.', Order(['ask a question', 'make a prediction', 'plan a fair test', 'do the test and measure', 'record the results', 'write a conclusion']), marks=4),
    Q('Bar chart or line graph?', Table(['Results', 'Best graph'], [['favourite fruits of our class', Ans('bar chart')], ['temperature of the classroom every hour', Ans('line graph')],
                                                                    ['how far four kinds of balls bounce', Ans('bar chart')]], widths=['65%', '35%']), marks=3),
])

think = Sheet('think', 'Is it fair?', level=2, goals=['Spot unfair tests.', 'Write predictions.', 'Find patterns.'], blocks=[
    Q('Sami wants to find out which paper towel soaks up the most water. He uses a big piece of towel A and a small piece of towel B, and dips them for different times. Is this fair? Explain how to make it fair.',
      Lines(4, 'No: he changed the size and the time as well as the type of towel. Use pieces of the same size, dip them for the same time in the same amount of water, and change only the type of towel.'), marks=3),
    Q('Write a prediction with a reason: "Will an ice cube melt faster in the sun or in the shade?"', Lines(2, 'I think it will melt faster in the sun because the sun gives it more heat.'), marks=2),
    Q('Look at the results. What is the pattern?',
      Table(['Amount of water each day (ml)', '0', '25', '50', '100'], [['Height of bean plant after 2 weeks (cm)', '2', '9', '15', '16']], center=True),
      Lines(2, 'The more water the plant gets, the taller it grows, but above 50 ml it hardly grows any taller.'), marks=2),
    Q('Three children timed the same race: 12 s, 13 s and 25 s. Which result is odd? What should they do?', Lines(2, '25 s is odd (maybe the stopwatch was started late); they should time the race again.'), marks=2),
])

investigate = Sheet('investigate', 'Does a higher drop make a higher bounce?', level=2, goals=['Plan, measure and repeat.', 'Draw a line graph.', 'Conclude and evaluate.'], blocks=[
    P('Class 4A dropped a tennis ball from different heights onto the same floor and measured how high it bounced. They did each drop three times.'),
    Q('Complete the plan.', Table(None, [['Question', Ans('Does a higher drop make a higher bounce?')], ['Change', Ans('height of the drop')], ['Measure', Ans('height of the bounce (cm)')],
                                         ['Keep the same', Ans('the same ball, floor, and way of dropping (no throwing)')], ['Prediction', Ans('the higher the drop, the higher the bounce')]], widths=['26%', '74%']), marks=4),
    Q('Complete the means.',
      Table(['Drop height (cm)', 'Bounce 1', 'Bounce 2', 'Bounce 3', 'Mean bounce (cm)'], [['50', '28', '30', '29', Ans('29')], ['100', '57', '60', '57', Ans('58')],
                                                                                          ['150', '86', '88', '90', Ans('88')], ['200', '115', '118', '115', Ans('116')]], center=True), marks=4),
    Q('Draw a line graph of the means.', Graph(['50', '100', '150', '200'], [29, 58, 88, 116], 'Mean bounce (cm)', 'Drop height (cm)', ymax=120, step=10, kind='line', width=110, height=50), marks=3),
    Q('Write a conclusion. Did the results support the prediction?', Lines(2, 'Yes: the higher the drop, the higher the bounce. The bounce was always a bit more than half the drop height.'), marks=2),
])

case = Sheet('case', 'Dr Firdausi Qadri: science that saves lives', level=3, goals=['Learn how a real scientist uses evidence.', 'Read data from a trial.', 'Think about how science helps people.'], blocks=[
    Links('Science', 'Health', 'Maths', 'Citizenship'),
    Case('**Cholera** and **typhoid** are diseases spread by dirty water. They can make children very ill. **Dr Firdausi Qadri**, '
         'a scientist at **icddr,b** in Dhaka, has spent her life finding ways to protect people from them.',
         'Scientists cannot just guess that a vaccine works; they need **evidence**. So Dr Qadri and her team ran large **trials** '
         'with thousands of volunteers in Dhaka. Some people got the vaccine and others did not, and the team counted how many in '
         'each group became ill. The evidence helped make cheap vaccines available to millions of children. In 2021 she won the '
         'Ramon Magsaysay Award, one of Asia\'s top prizes, for her work.',
         source='Based on information about Dr Firdausi Qadri and icddr,b. Numbers below are example data.'),
    Q('A vaccine trial (example data): 1000 people in each group.',
      Table(['Group', 'Got the vaccine', 'Did not get the vaccine'], [['People who became ill', '10', '50']], center=True),
      Graph(['vaccine', 'no vaccine'], [10, 50], 'People who became ill', 'Group', ymax=60, step=10, width=90, height=48),
      Part('Draw the bar chart.'),
      Part('How many times more people became ill without the vaccine?', Lines(1, '50 ÷ 10 = 5 times more')), marks=3),
    Q('Why did the trial need **two** groups?', Lines(2, 'To compare: the group without the vaccine shows what would happen anyway, so we can see if the vaccine makes a difference.'), marks=2),
    Q('Why was it important to test **thousands** of people, not just ten?', Lines(2, 'With many people, the results are more reliable and not just luck.'), marks=2),
    Q('Besides vaccines, how can people protect themselves from diseases spread by dirty water?', Lines(2, 'Drink boiled or treated water; wash hands with soap; use clean toilets.'), marks=2),
])

review = Sheet('review', 'Show what you know', level=3, goals=['Use key vocabulary.', 'Answer test-style questions.'], blocks=[
    Q('Find the key words.', WordSearch(['OBSERVE', 'PREDICT', 'FAIR', 'TEST', 'MEASURE', 'RESULT', 'GRAPH', 'PATTERN', 'EVIDENCE'], size=10, seed=420)),
    Q('In a fair test you change…', MCQ(['everything', 'only one thing', 'two things', 'nothing'], 1), marks=1),
    Q('Which tool measures temperature?', MCQ(['ruler', 'stopwatch', 'thermometer', 'forcemeter'], 2), marks=1),
    Q('Plan your own investigation: "Which ball bounces highest?" Write what you will change, measure and keep the same.',
      Table(None, [['Change', Ans('the type of ball')], ['Measure', Ans('the height of the bounce (cm)')], ['Keep the same', Ans('drop height, floor, how it is dropped, who measures')]], widths=['30%', '70%']), marks=3),
    Q('**Challenge.** Why do scientists share their results with other scientists?', Lines(3, 'So others can check the results by repeating the tests, find mistakes, and build on the ideas to make new discoveries.'), marks=2),
])

TOPIC = Topic(
    code='W1', strand='skills', title='Science Detectives: Working Scientifically', short='Working scientifically',
    subtitle='Observing, asking and predicting, fair tests, measuring, tables and graphs, patterns and conclusions',
    outcomes=[
        'observe carefully in order to gather data — examining objects and living things, observing change over a period of time, and recording observations in a systematic way.',
        'use a variety of instruments and tools to measure data accurately, selecting appropriate tools and units.',
        'make relevant observations, and measure volume, temperature, time, length and force.',
        'discuss the need for repeated observations and measurements.',
        'present results in bar charts and line graphs.',
        'identify or generate a question or problem to be explored, asking questions that may lead to investigation.',
        'use knowledge and understanding to plan how to carry out a fair test, recognizing that an experiment is unfair if the relevant variables are not controlled.',
        'make predictions of what will happen based on scientific knowledge and understanding, and suggest and communicate how to test them.',
        'recognise patterns in data, make predictions from them, and suggest explanations using scientific knowledge and understanding.',
        'decide whether results support the predictions made; interpret data and think about whether it is sufficient to draw a conclusion.',
        'consider scientific models and the applications of these models, including their limitations.',
        'know that scientists have combined evidence with creative thinking to suggest new ideas and explanations for phenomena.',
    ],
    sheets=[learn, facts, think, investigate, case, review],
    selfcheck=['ask a question I can test', 'write a prediction with a reason', 'plan a fair test', 'measure with the right tool and unit',
               'draw a bar chart or line graph', 'write a conclusion using evidence'],
    cover_art=art.pic_row(['magnifying glass', 'test tube', 'ruler', 'stopwatch', 'bar chart']),
)
