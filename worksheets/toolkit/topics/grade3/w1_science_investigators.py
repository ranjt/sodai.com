from build import Sheet, Topic
from ws import (P, H, Box, Vocab, Fig, Cols, Row, Case, Links, Lines, Blanks, Match, TrueFalse, MCQ, Order, Table,
                Ans, Sort, Label, Draw, Graph, WordSearch, Q, Part, Bullets, Pics)
import art

learn = Sheet('learn', 'Science investigators', level=1, goals=[
    'Ask questions that can be tested and make predictions.',
    'Plan a fair test, measure carefully and repeat measurements.',
    'Show results in tables and bar charts and say what they show.',
], blocks=[
    P('Investigators find out the truth by collecting **evidence**. Scientists are investigators of the natural world. They ask questions, plan tests, measure carefully and use evidence to explain what they find.', 'lead'),
    Pics([('scientist', 'question'), ('pencil', 'predict'), ('test tube', 'plan and test'), ('stopwatch', 'measure'), ('bar chart', 'present'), ('check mark', 'explain')], cols=6, size='14mm'),
    H('Questions you can test', 3),
    P('"Which paper makes the best paper plane?" can be **tested**. "Which colour is prettiest?" cannot, because it is just an opinion.'),
    H('Predict', 3),
    P('Use what you know: "I think the heavy paper plane will fly furthest **because** it will not be blown about so easily."'),
    H('Plan a fair test', 3),
    Table(None, [['**Change** one thing', 'the type of paper'], ['**Measure** one thing', 'how far the plane flies (in metres)'],
                 ['**Keep the same**', 'the plane shape, who throws it, how hard, where']]),
    H('Choose the right tool', 3),
    Table(['Measure', 'Tool', 'Unit'], [['length', 'ruler, tape measure', 'cm, m'], ['temperature', 'thermometer', '°C'], ['time', 'stopwatch', 'seconds'], ['force', 'forcemeter', 'newtons (N)']]),
    Fig(art.instruments_to_read(), 'Read scales carefully.', width='70%'),
    H('Repeat it!', 3),
    P('Do each test **three times**. If one result is very different, check it again. Repeating makes results more **reliable** (you can trust them more).'),
    H('Present and explain', 3),
    P('Put results in a **table**, then draw a **bar chart**. Look for a **pattern**. Then say what the evidence shows: was your prediction right?'),
    Box('tip', P('Tables need **headings** and **units**, for example "Distance (m)".')),
    Vocab([('evidence', 'facts and measurements that show what is true'), ('predict', 'say what you think will happen and why'), ('fair test', 'change one thing, keep everything else the same'),
           ('reliable', 'results you can trust because you repeated them'), ('pattern', 'something that happens again and again in the results')]),
])

facts = Sheet('facts', 'Tools, units and tests', level=1, goals=['Match tools and units.', 'Spot testable questions.'], blocks=[
    Q('Read each instrument. Include the unit.', Fig(art.instruments_to_read(), width='82%'),
      Table(['A', 'B', 'C', 'D'], [[Ans('34 ml'), Ans('37 °C'), Ans('7 cm'), Ans('20 s')]], center=True), marks=4),
    Q('Draw a line to match the tool to the unit.', Match([('thermometer', '°C'), ('stopwatch', 'seconds'), ('ruler', 'cm'), ('forcemeter', 'newtons')]), marks=4),
    Q('Can it be tested? Sort the questions.', Sort(['Can be tested', 'Cannot be tested'], [('Which ball bounces highest?', 'Can be tested'), ('Does salt melt ice faster?', 'Can be tested'),
                                                                                         ('Which song is the nicest?', 'Cannot be tested'), ('Is red better than blue?', 'Cannot be tested')]), marks=4),
])

think = Sheet('think', 'Making it fair', level=2, goals=['Plan a fair test.', 'Explain repeats.'], blocks=[
    Q('Lina wants to know which cup keeps cha hot longest. She puts hot cha in a clay cup and cold cha in a steel cup. Is it fair? How can she fix it?',
      Lines(3, 'No: the starting temperature is different. She must start both with the same amount of cha at the same temperature.'), marks=3),
    Q('Why should you repeat a measurement three times?', Lines(2, 'To check the results and make them more reliable.'), marks=2),
    Q('Write a prediction with a reason: "Will a plant grow taller in sunlight or in shade?"', Lines(2, 'I think it will grow taller in sunlight because plants need light to make food.'), marks=2),
])

investigate = Sheet('investigate', 'Which paper makes the best paper plane?', level=2, goals=['Repeat measurements.', 'Draw a bar chart.', 'Say what the evidence shows.'], blocks=[
    P('Class 3A made the same paper plane from three kinds of paper and threw each one three times.'),
    Q('Complete the table. Find the middle (median) result of each.',
      Table(['Paper', 'Try 1 (m)', 'Try 2 (m)', 'Try 3 (m)', 'Middle result (m)'], [['newspaper', '4', '5', '6', Ans('5')], ['writing paper', '6', '8', '7', Ans('7')], ['card', '3', '2', '4', Ans('3')]], center=True), marks=3),
    Q('Draw a bar chart of the middle results.', Graph(['newspaper', 'writing paper', 'card'], [5, 7, 3], 'Distance (m)', 'Paper', ymax=8, step=1, width=100, height=48), marks=3),
    Q('Which paper was best? What does the evidence show?', Lines(2, 'Writing paper flew furthest (7 m), so it makes the best plane.'), marks=2),
])

case = Sheet('case', 'Testing umbrellas for the monsoon', level=3, goals=['Plan a real test.', 'Use evidence to choose.'], blocks=[
    Links('Science', 'Design', 'Maths'),
    Case('The monsoon rains are coming. A shopkeeper in Rajshahi wants to sell the best umbrellas. He asks a Grade 3 class to test three kinds of cloth: cotton, plastic sheet and nylon.',
         'The class drips 50 drops of water onto each cloth stretched over a cup, then measures how much water gets through.',
         source='A story about a class investigation. Results are example data.'),
    Q('Complete the plan.', Table(None, [['Change', Ans('the type of cloth')], ['Measure', Ans('water that gets through (ml)')], ['Keep the same', Ans('number of drops, size of cloth, cup')]], widths=['30%', '70%']), marks=3),
    Q('Results: cotton 8 ml, plastic 0 ml, nylon 1 ml. Which cloth should the shopkeeper use? Why?', Lines(2, 'Plastic sheet (or nylon): almost no water gets through.'), marks=2),
    Q('What else should they test before choosing?', Lines(2, 'Strength, weight, cost, whether it tears in wind.'), marks=1),
])

review = Sheet('review', 'Show what you know', level=3, goals=['Use science words.'], blocks=[
    Q('Find the words.', WordSearch(['FAIR', 'TEST', 'MEASURE', 'REPEAT', 'TABLE', 'CHART', 'PREDICT'], size=9, seed=301)),
    Q('Which tool measures time?', MCQ(['thermometer', 'stopwatch', 'ruler'], 1), marks=1),
    Q('In a fair test you change…', MCQ(['one thing', 'two things', 'everything'], 0), marks=1),
    Q('**Challenge.** Plan a test: "Which ball rolls furthest?" Write what you change, measure and keep the same.',
      Table(None, [['Change', Ans('the type of ball')], ['Measure', Ans('distance rolled (cm)')], ['Keep the same', Ans('ramp, push (none), floor')]], widths=['30%', '70%']), marks=3),
])

TOPIC = Topic(
    code='W1', strand='skills', title='Science Investigators', short='Working scientifically',
    subtitle='Testable questions, predictions, fair tests, measuring, repeating, tables and bar charts',
    outcomes=[
        'observe carefully in order to gather data, examining objects and living things and recording what is observed.',
        'make relevant observations and comparisons in a variety of contexts.',
        'measure temperature, time, force and length.',
        'begin to think about the need for repeated measurements.',
        'present results in drawings, bar charts and tables.',
        'identify or generate a question or problem to be explored, and suggest questions that can be tested.',
        'design a fair test and plan how to collect sufficient evidence.',
        'choose apparatus and decide what to measure.',
        'make predictions based on scientific knowledge and understanding, and communicate them.',
        'identify simple trends and patterns in results, and suggest explanations for some of them.',
        'explain what the evidence shows and whether it supports the predictions made.',
        'consider scientific models and the applications of these models.',
    ],
    sheets=[learn, facts, think, investigate, case, review],
    selfcheck=['ask a question I can test', 'make a prediction with a reason', 'plan a fair test', 'measure with the right tool', 'repeat measurements', 'draw a bar chart'],
    cover_art=art.pic_row(['magnifying glass', 'test tube', 'stopwatch', 'bar chart']),
)
