from build import Sheet, Topic
from ws import (P, H, Box, Fig, Q, Lines, MCQ, Draw, Pics, Ans, Case, Choose, PicMatch, PicSort, Pictograph, Trace)
import art

learn = Sheet('learn', 'I am a little scientist', level=1, goals=['Use my senses to find things out.', 'Ask questions and guess.'], blocks=[
    Box('adult', P('Read aloud and act it out: point to your eyes, ears, nose, tongue and hands. Ask the children what each one helps us do.')),
    P('Scientists find out about the world. **You can be a scientist too!** We use our **five senses**.', 'lead'),
    Pics([('eye', 'I see'), ('ear', 'I hear'), ('nose', 'I smell'), ('tongue', 'I taste'), ('hand', 'I touch')], cols=5, size='22mm'),
    H('Scientists ask questions', 3),
    P('"What is it? Why? What will happen if…?" Asking questions helps us learn.'),
    H('Scientists guess, then try', 3),
    P('First we **guess** what will happen. Then we **try it** and **look closely**. Did it happen?'),
    Pics([('magnifying glass', 'look closely'), ('ruler', 'measure'), ('camera', 'take a picture'), ('pencil', 'draw what I see')], cols=4, size='22mm'),
])

facts = Sheet('facts', 'My five senses', level=1, goals=['Match senses to things.'], blocks=[
    Q('Match each sense to something it finds out.', PicMatch([(('eye', 'eyes'), ('rainbow', 'rainbow')), (('ear', 'ears'), ('bell', 'bell')),
                                                             (('nose', 'nose'), ('blossom', 'flower')), (('tongue', 'tongue'), ('lemon', 'lemon'))], size='16mm')),
    Q('Circle the tools a scientist uses.', Choose([('magnifying glass', 'magnifier'), ('lollipop', 'lollipop'), ('ruler', 'ruler'), ('teddy bear', 'teddy')], right=[0, 2])),
])

think = Sheet('think', 'Guess and try', level=2, goals=['Guess what will happen.', 'Try it and see.'], blocks=[
    Q('Guess first: which things will **float**? Circle them. Then try with a bowl of water!',
      Choose([('fallen leaf', 'leaf'), ('key', 'key'), ('football', 'ball'), ('rock', 'stone'), ('wood', 'wood'), ('coin', 'coin')], right=[0, 2, 4], cols=6, size='18mm')),
    Q('Draw what happened.', Draw('48mm', 'What I saw', 'The leaf, ball and wood floated. The key, stone and coin sank.')),
])

investigate = Sheet('investigate', 'Soft or hard?', level=2, goals=['Use touch to sort things.', 'Make a picture graph.'], blocks=[
    Box('adult', P('Put the things in a bag. Each child feels one thing without looking and says "soft" or "hard".')),
    Q('Sort the things: **soft** or **hard**?', PicSort(['Soft', 'Hard'], [('teddy bear', 'teddy', 'Soft'), ('sponge', 'sponge', 'Soft'), ('yarn', 'wool', 'Soft'),
                                                                      ('rock', 'stone', 'Hard'), ('spoon', 'spoon', 'Hard'), ('wood', 'block', 'Hard')], height='34mm')),
    Q('On our sound walk we heard… Colour one box for each.', Pictograph([('bird', 'birds', 4), ('car', 'cars', 3), ('bell', 'bell', 1), ('child', 'children', 6)], top=7)),
])

case = Sheet('case', "Rafi's magnifying glass", level=3, goals=['Listen to a story.', 'Answer questions about it.'], blocks=[
    Case('Rafi had a new magnifying glass. In the garden he looked closely at a tiny ant. "It has six legs!" he said.',
         'Rafi asked, "Where is the ant going?" He followed it to a little hole in the ground. Then he told his friends what he found.'),
    Q('What did Rafi use? Circle it.', Choose([('spoon', 'spoon'), ('magnifying glass', 'magnifier'), ('football', 'ball')], right=[1], cols=3)),
    Q('What did Rafi look at? Circle it.', Choose([('cat', 'cat'), ('car', 'car'), ('ant', 'ant')], right=[2], cols=3)),
])

review = Sheet('review', 'I can do it!', level=3, goals=['Trace sense words.'], blocks=[
    Q('Trace the words.', Trace([('see', 'eye'), ('hear', 'ear')])),
    Q('Circle the part you **smell** with.', Choose([('ear', 'ear'), ('nose', 'nose'), ('foot', 'foot'), ('hand', 'hand')], right=[1])),
])

TOPIC = Topic(
    code='W1', strand='skills', title='Little Explorers', short='Little explorers',
    subtitle='Using our senses, asking questions, guessing and trying things out like a scientist',
    outcomes=[
        'explore and observe using each of the senses in order to find things out.',
        'notice and talk about what they see, hear, touch, smell and taste.',
        'ask questions about the things around them, and make a guess about what might happen.',
        'make predictions about what will happen and compare what happened with what they predicted.',
        'make simple comparisons between things they have observed, and communicate their ideas in their own words.',
        'record the stages in their work in simple ways.',
    ],
    sheets=[learn, facts, think, investigate, case, review],
    selfcheck=['use my five senses', 'ask a question', 'guess, then try it'],
    cover_art=art.pic_row(['eye', 'ear', 'nose', 'tongue', 'hand'], ['see', 'hear', 'smell', 'taste', 'touch']),
)
