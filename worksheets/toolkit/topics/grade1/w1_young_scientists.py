from build import Sheet, Topic
from ws import (P, H, Box, Vocab, Fig, Q, Lines, Blanks, Match, TrueFalse, MCQ, Table, Ans, Sort, Draw, Graph, WordSearch, Bullets, Pics,
                Choose, PicMatch, PicSort, Pictograph, Trace, Case)
import art

learn = Sheet('learn', 'I am a young scientist', level=1, goals=['Say how scientists find things out.', 'Know how to stay safe.'], blocks=[
    P('Scientists are curious. They **ask questions** and find the answers by **looking closely**, **measuring** and **testing**. You can do this too!', 'lead'),
    H('How scientists work', 3),
    Pics([('child', '1. Ask a question'), ('alarm clock', '2. Guess what will happen'), ('test tube', '3. Test it'),
          ('clipboard', '4. Record what happens'), ('loudspeaker', '5. Tell others')], cols=5, size='18mm'),
    H('Tools we use', 3),
    Pics([('magnifying glass', 'hand lens: look closely'), ('ruler', 'ruler: measure'), ('stopwatch', 'timer: how long'), ('thermometer', 'thermometer: how hot')], cols=4, size='19mm'),
    H('Is it fair?', 3),
    P('To find out which ball bounces highest, we drop every ball from the **same height**. If we threw one ball harder, the test would **not be fair**.'),
    Box('safety', P('Listen to your teacher. Never taste or smell things unless you are told it is safe. Wash your hands after a test.')),
])

facts = Sheet('facts', 'Science tools', level=1, goals=['Match tools to jobs.', 'Order the steps.'], blocks=[
    Q('Match the tool to its job.', PicMatch([(('ruler', 'ruler'), ('footprints', 'measure how long')), (('magnifying glass', 'hand lens'), ('ant', 'look closely')),
                                             (('thermometer', 'thermometer'), ('hot face', 'how hot'))], size='15mm')),
    Q('Put the steps in order. Write 1, 2, 3, 4.', Table(['Step', 'Order'], [['Test it', Ans('2')], ['Ask a question', Ans('1')], ['Tell others', Ans('4')], ['Record what happens', Ans('3')]], widths=['70%', '30%'])),
])

think = Sheet('think', 'Fair or not fair?', level=2, goals=['Spot an unfair test.'], blocks=[
    P('Mina and Raju race toy cars down a ramp. Mina pushes her car. Raju just lets his car go.'),
    Q('Is it a fair test?', MCQ(['yes', 'no'], 1)),
    Q('Why?', Lines(2, 'Mina pushed her car, so it was not the same for both cars.')),
    Q('Draw yourself being a scientist.', Draw('40mm', '', 'e.g. using a hand lens to look at a leaf.')),
])

investigate = Sheet('investigate', 'Which ball bounces highest?', level=2, goals=['Do a fair test.', 'Read a bar chart.'], blocks=[
    P('Class 1 dropped three balls from the same height and measured how high they bounced.'),
    Q('Draw the bars.', Table(['Ball', 'tennis ball', 'football', 'rubber ball'], [['Bounce (hand spans)', '4', '3', '6']], center=True),
      Graph(['tennis', 'football', 'rubber'], [4, 3, 6], 'Hand spans', 'Ball', ymax=7, step=1, width=80, height=46)),
    Q('Which ball bounced highest?', MCQ(['tennis ball', 'football', 'rubber ball'], 2)),
    Q('Why did they drop all the balls from the same height?', Lines(1, 'to make it a fair test')),
])

case = Sheet('case', 'Little scientist at the pond', level=3, goals=['Read a story.', 'Think like a scientist.'], blocks=[
    Case('Nadia saw tiny black wriggly things in the village pond. "What are they?" she asked. She looked closely with a hand lens and drew them in her notebook.',
         'Every week she went back and drew them again. The wriggly things grew legs. Then they lost their tails. They were baby frogs, called tadpoles!'),
    Q('What question did Nadia ask?', Lines(1, '"What are they?"')),
    Q('How did Nadia record what she saw?', MCQ(['She drew pictures.', 'She took them home.'], 0)),
    Q('What were the wriggly things?', Lines(1, 'tadpoles: baby frogs')),
])

review = Sheet('review', 'Show what you know', level=3, goals=['Use science words.'], blocks=[
    Q('Find the words.', WordSearch(['ASK', 'TEST', 'LOOK', 'FAIR', 'TOOL'], size=7, seed=101)),
    Q('A test is fair when…', MCQ(['we change many things', 'we keep things the same'], 1)),
])

TOPIC = Topic(
    code='W1', strand='skills', title='Young Scientists', short='Young scientists',
    subtitle='Asking questions, predicting, testing fairly, measuring and recording like a scientist',
    outcomes=[
        'collect evidence by making observations when trying to answer a science question, using first-hand experience.',
        'make and record observations, and take simple measurements.',
        'ask questions and suggest ways to answer them, and predict what will happen before deciding what to do.',
        'recognise that a test or a comparison may be unfair.',
        'make comparisons, identify simple patterns, and talk about predictions, the outcome, and why things happened.',
        'talk about risks and how to avoid danger, and communicate ideas using their own scientific experience and understanding.',
    ],
    sheets=[learn, facts, think, investigate, case, review],
    selfcheck=['ask a science question', 'use science tools', 'say if a test is fair'],
    cover_art=art.pic_row(['magnifying glass', 'ruler', 'stopwatch', 'thermometer'], ['look', 'measure', 'time', 'temperature']),
)
