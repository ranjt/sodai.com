from build import Sheet, Topic
from ws import (P, H, Box, Vocab, Fig, Cols, Row, Case, Links, Lines, Blanks, Match, TrueFalse, MCQ, Order, Table,
                Ans, Sort, Label, Draw, Graph, WordSearch, Q, Part, Bullets, Pics)
import art

learn = Sheet('learn', 'I am a scientist!', level=1, goals=[
    'Use my senses to look closely and ask questions.',
    'Make a prediction and test it.',
    'Measure, record and tell others what I found.',
], blocks=[
    P('Scientists are people who are curious about the world. They look closely, ask questions and try things out to find '
      'answers. You can be a scientist too!', 'lead'),
    Pics([('magnifying glass', 'look closely'), ('scientist', 'ask a question'), ('test tube', 'try it out'), ('ruler', 'measure'), ('clipboard', 'record'), ('check mark', 'tell others')],
         cols=6, size='15mm'),
    H('1. Look closely', 3),
    P('Use your **senses**: look, listen, touch and smell (but never taste in science!). A **hand lens** makes small things look bigger.'),
    H('2. Ask a question', 3),
    P('Good questions start with **What**, **Why**, **How** or **Which**. "Which ball bounces highest?" "Does a plant need water to grow?"'),
    H('3. Predict', 3),
    P('A **prediction** is what you think will happen. "I think the big ball will bounce highest."'),
    H('4. Try it out fairly', 3),
    P('Change only **one** thing. Keep everything else the **same**. If you test balls, drop them from the same height on the same floor.'),
    H('5. Measure and record', 3),
    P('Use simple tools: a **ruler** for length, a **thermometer** for how hot or cold, a **timer** for time and **scales** for how heavy. '
      'Write or draw what you find in a **table** or a **chart**.'),
    Pics([('ruler', 'ruler'), ('thermometer', 'thermometer'), ('stopwatch', 'timer'), ('balance scale', 'scales')], cols=4, size='15mm'),
    H('6. Tell others', 3),
    P('Share what you found with drawings, charts and words. Did your prediction come true?'),
    Box('safety', P('Never taste or smell things in science unless your teacher says it is safe. Wash your hands after touching soil or animals.')),
    Vocab([('observe', 'look closely'), ('predict', 'say what you think will happen'), ('measure', 'find out how long, heavy, hot or how much'),
           ('record', 'write or draw what you found'), ('fair test', 'change only one thing')]),
])

facts = Sheet('facts', 'Science tools', level=1, goals=['Name science tools.', 'Match tools to jobs.'], blocks=[
    Q('Name the tool.', Pics([('magnifying glass', Ans('hand lens')), ('ruler', Ans('ruler')), ('thermometer', Ans('thermometer')), ('stopwatch', Ans('timer')), ('balance scale', Ans('scales'))], cols=5, size='15mm'), marks=5),
    Q('Draw a line to match the tool to its job.', Match([('ruler', 'how long'), ('thermometer', 'how hot or cold'), ('timer', 'how much time'), ('scales', 'how heavy'), ('hand lens', 'see small things')]), marks=5),
    Q('Which sense do you use? Write **see**, **hear**, **touch** or **smell**.',
      Table(['I want to find out…', 'Sense'], [['the colour of a flower', Ans('see')], ['if a stone is rough', Ans('touch')], ['which bird is singing', Ans('hear')], ['if the mango is ripe', Ans('smell (or touch)')]], widths=['65%', '35%']), marks=4),
])

think = Sheet('think', 'Is it fair?', level=2, goals=['Spot a fair test.', 'Make predictions.'], blocks=[
    Q('Rina and Sami race toy cars down a slope. Rina pushes her car. Sami lets his car go. Is it fair? Why?', Lines(2, 'No. Rina pushed her car, so it is not fair. Both cars should just be let go.'), marks=2),
    Q('Predict: Which will dry faster, a wet towel in the sun or a wet towel in the shade?', Pics([('sun', 'in the sun'), ('deciduous tree', 'in the shade')], cols=2, size='16mm'),
      Lines(1, 'The towel in the sun.'), marks=1),
    Q('Draw what you would see if you looked at your thumb through a hand lens.', Draw('40mm', 'My thumb', 'The lines and swirls of the fingerprint look big.'), marks=2),
    Q('Write one question you want to find out about animals.', Lines(1, 'e.g. Which animals live in our school garden?'), marks=1),
])

investigate = Sheet('investigate', 'Which ball bounces highest?', level=2, goals=['Do a fair test.', 'Make a bar chart.'], blocks=[
    P('Class 2A dropped four balls from the same height onto the floor and measured the bounce with a metre ruler.'),
    Q('Here are the results. Draw the bar chart.',
      Table(['Ball', 'football', 'tennis ball', 'plastic ball', 'cloth ball'], [['Bounce (cm)', '60', '50', '30', '10']], center=True),
      Graph(['football', 'tennis', 'plastic', 'cloth'], [60, 50, 30, 10], 'Bounce (cm)', 'Ball', ymax=70, step=10, width=110, height=50), marks=3),
    Q('Which ball bounced the highest?', Lines(1, 'the football'), marks=1),
    Q('Which ball bounced the lowest?', Lines(1, 'the cloth ball'), marks=1),
    Q('What did they keep the same?', MCQ(['the height they dropped the balls from', 'the type of ball', 'the colour of the balls'], 0, one_col=True), marks=1),
])

case = Sheet('case', 'Rumi the bird watcher', level=3, goals=['Read a true-to-life story.', 'Count and record.', 'Ask questions.'], blocks=[
    Links('Science', 'Maths', 'Nature'),
    Case('Rumi lives in a village near a big lake. Every morning before school she sits quietly by the window with her '
         'grandfather\'s old notebook. She looks at the birds in the mango tree and counts them.',
         'Rumi draws each bird and writes the date. She sees that in winter there are many ducks on the lake, but in summer they '
         'are gone. "Where do they go?" she asks. Her teacher says, "You are thinking like a scientist!"',
         source='A story about observing nature. Numbers below are example data.'),
    Q('Rumi counted birds for five mornings. Make a tally and write the totals.',
      Table(['Bird', 'Tally', 'Total'], [['crow', 'IIII I', Ans('6')], ['myna', 'IIII', Ans('4')], ['magpie robin (doyel)', 'II', Ans('2')], ['kingfisher', 'I', Ans('1')]], center=True), marks=4),
    Q('Which bird did Rumi see most?', Lines(1, 'the crow'), marks=1),
    Q('Which science skills did Rumi use? Tick them.', Table(['Skill', 'Tick'], [['looking closely', Ans('✓')], ['counting', Ans('✓')], ['asking a question', Ans('✓')], ['tasting', Ans('')]], center=True, widths=['70%', '30%']), marks=3),
])

review = Sheet('review', 'Show what you know', level=3, goals=['Use science words.', 'Answer questions.'], blocks=[
    Q('Find the words.', WordSearch(['LOOK', 'TEST', 'RULER', 'TIMER', 'GUESS', 'SENSE'], size=8, seed=201)),
    Q('Which tool measures how hot something is?', MCQ(['ruler', 'thermometer', 'scales'], 1), marks=1),
    Q('A fair test changes…', MCQ(['one thing', 'everything', 'nothing'], 0), marks=1),
    Q('**Challenge.** Draw a table to record how many legs these animals have: spider, bird, cow, ant.',
      Draw('36mm', 'My table', 'Two columns: animal | number of legs. spider 8, bird 2, cow 4, ant 6.'), marks=2),
])

TOPIC = Topic(
    code='W1', strand='skills', title='I Am a Scientist', short='Working scientifically',
    subtitle='Looking closely, asking questions, predicting, fair tests, measuring and recording',
    outcomes=[
        'observe carefully in order to gather data, using the senses to examine objects and living things.',
        'observe and compare objects, living things and events.',
        'measure using simple equipment, and record observations in a variety of ways.',
        'select different tools and explore ways of using them for an investigation.',
        'identify a question or problem to be explored.',
        'suggest ideas, make predictions, and communicate them.',
        'with help, think about collecting evidence and planning a fair test.',
        'interpret the data gathered in order to draw conclusions, sorting and classifying by observable features.',
        'make generalisations and begin to identify simple patterns in results.',
        'use scientific vocabulary to explain observations and experiences, and present findings using drawings, charts and tables.',
    ],
    sheets=[learn, facts, think, investigate, case, review],
    selfcheck=['use my senses to look closely', 'ask a science question', 'make a prediction', 'do a fair test', 'measure with a tool', 'make a bar chart'],
    cover_art=art.pic_row(['magnifying glass', 'test tube', 'ruler', 'thermometer']),
)
