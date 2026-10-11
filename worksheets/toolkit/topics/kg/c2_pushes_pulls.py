from build import Sheet, Topic
from ws import (P, H, Box, Fig, Q, Lines, MCQ, Draw, Pics, Ans, Case, Choose, PicMatch, PicSort, Pictograph, Trace)
import art

learn = Sheet('learn', 'Pushes and pulls', level=1, goals=['Tell a push from a pull.', 'Say what pushes and pulls can do.'], blocks=[
    Box('adult', P('Read aloud and act it out: push a toy car away from you, then pull it back on a string.')),
    P('A **push** moves something **away** from you. A **pull** moves something **towards** you. Pushes and pulls are **forces**.', 'lead'),
    H('Pushes', 3),
    Pics([('shopping cart', 'push a trolley'), ('playground slide', 'push on a swing'), ('door', 'push a door'), ('football', 'kick a ball')], cols=4, size='19mm'),
    H('Pulls', 3),
    Pics([('kite', 'pull a kite string'), ('wheelbarrow', 'pull a cart'), ('bucket', 'pull up a bucket'), ('dog', 'pull a lead')], cols=4, size='19mm'),
    H('A push or pull can…', 3),
    P('make things **start** moving, go **faster**, go **slower**, **stop** or **change direction**. When something starts, stops or turns, a push or pull made it happen!'),
])

facts = Sheet('facts', 'Push or pull?', level=1, goals=['Sort pushes and pulls.'], blocks=[
    Q('Cut and sort: **push** or **pull**?', PicSort(['Push', 'Pull'], [('shopping cart', 'trolley', 'Push'), ('football', 'kick a ball', 'Push'), ('door', 'shut a door', 'Push'),
                                                                    ('kite', 'kite string', 'Pull'), ('bucket', 'bucket rope', 'Pull'), ('wheelbarrow', 'cart', 'Pull')], height='32mm')),
    Q('Circle the things you **push**.', Choose([('shopping cart', 'trolley'), ('kite', 'kite'), ('playground slide', 'swing'), ('bucket', 'bucket rope')], right=[0, 2])),
])

think = Sheet('think', 'Make it move', level=2, goals=['Think about how things move.'], blocks=[
    Q('How can you make the ball go **faster**? Circle.', MCQ(['kick it harder', 'kick it softly'], 0)),
    Q('Which will roll down a slope? Circle.', Choose([('football', 'ball'), ('package', 'box'), ('coin', 'coin on its edge'), ('notebook', 'book')], right=[0, 2])),
    Q('Draw yourself pushing or pulling something.', Draw('42mm', '', 'e.g. pushing a swing, pulling a kite.')),
])

investigate = Sheet('investigate', 'Ramp race', level=2, goals=['Roll toy cars down a ramp.', 'Make a picture graph.'], blocks=[
    Box('adult', P('Make a ramp with a book and a board. Let each child roll a toy car down. Count how many floor tiles it rolls past.')),
    Q('How far did the cars roll? Colour one box for each tile.', Pictograph([('car', 'red car', 6), ('bus', 'bus', 4), ('auto rickshaw', 'rickshaw', 7)], top=8)),
    Q('Which went the farthest? Circle it.', Choose([('car', 'red car'), ('bus', 'bus'), ('auto rickshaw', 'rickshaw')], right=[2], cols=3)),
])

case = Sheet('case', 'Pulling the boat', level=3, goals=['Listen to a story.', 'Talk about pushes and pulls.'], blocks=[
    Case('The fishermen came back from the river. Their boat was heavy and full of fish.',
         'Some people pulled the rope. Some people pushed the back of the boat. Heave-ho! Together they moved the boat up onto the bank.'),
    Q('How did they move the boat? Circle.', Choose([('family', 'they pushed and pulled together'), ('sleeping face', 'they slept')], right=[0], cols=2)),
])

review = Sheet('review', 'I can do it!', level=3, goals=['Trace force words.'], blocks=[
    Q('Trace the words.', Trace([('push', 'shopping cart'), ('pull', 'kite')])),
    Q('Opening a drawer is a…', MCQ(['push', 'pull'], 1)),
])

TOPIC = Topic(
    code='C2', strand='physical', title='Pushes and Pulls', short='Pushes and pulls',
    subtitle='Pushes and pulls are forces that start, stop, speed up, slow down and turn things',
    outcomes=[
        'understand that pushes and pulls are forces, and distinguish between a push and a pull.',
        'look for ways they use pushes and pulls in daily life — opening a door, playing with cars.',
        'explore, talk about and describe the movement of familiar things.',
        'recognise that when things speed up, slow down or change direction there is a cause.',
    ],
    sheets=[learn, facts, think, investigate, case, review],
    selfcheck=['tell a push from a pull', 'find pushes and pulls in my day', 'make a car go faster'],
    cover_art=art.pic_row(['shopping cart', 'football', 'kite', 'wheelbarrow'], ['push', 'push', 'pull', 'pull']),
)
