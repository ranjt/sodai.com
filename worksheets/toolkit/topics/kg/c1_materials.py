from build import Sheet, Topic
from ws import (P, H, Box, Fig, Q, Lines, MCQ, Draw, Pics, Ans, Case, Choose, PicMatch, PicSort, Pictograph, Trace)
import art

learn = Sheet('learn', 'Materials around us', level=1, goals=['Name materials.', 'Say what things are made of.'], blocks=[
    Box('adult', P('Read aloud. Pass around real things made of wood, plastic, metal, glass, paper and cloth to touch and talk about.')),
    P('Everything is made of a **material**. Let us look and touch!', 'lead'),
    Pics([('wood', 'wood'), ('plastic bottle', 'plastic'), ('key', 'metal'), ('glass bottle', 'glass'), ('newspaper', 'paper'), ('shirt', 'cloth')], cols=6, size='18mm'),
    H('Feel the materials', 3),
    Pics([('rock', 'hard'), ('sponge', 'soft'), ('glass bottle', 'smooth'), ('wood', 'rough')], cols=4, size='20mm'),
    H('What is it made of?', 3),
    Pics([('pencil', 'a pencil: wood'), ('spoon', 'a spoon: metal'), ('cup with straw', 'a cup: plastic'), ('teddy bear', 'a teddy: cloth')], cols=4, size='20mm'),
])

facts = Sheet('facts', 'What is it made of?', level=1, goals=['Match things to materials.', 'Sort hard and soft.'], blocks=[
    Q('Match each thing to its material.', PicMatch([(('chair', 'chair'), ('wood', 'wood')), (('key', 'key'), ('coin', 'metal')),
                                                     (('socks', 'socks'), ('yarn', 'cloth'))], size='15mm')),
    Q('Cut and sort: **hard** or **soft**?', PicSort(['Hard', 'Soft'], [('rock', 'stone', 'Hard'), ('key', 'key', 'Hard'), ('wood', 'block', 'Hard'),
                                                                      ('teddy bear', 'teddy', 'Soft'), ('sponge', 'sponge', 'Soft'), ('socks', 'socks', 'Soft')], height='32mm')),
])

think = Sheet('think', 'The right material', level=2, goals=['Choose a good material.'], blocks=[
    Q('Which is best for a raincoat? It must keep the rain out. Circle.', Choose([('newspaper', 'paper'), ('plastic bottle', 'plastic'), ('yarn', 'wool')], right=[1], cols=3)),
    Q('Which can you see through? Circle.', Choose([('window', 'glass window'), ('door', 'wooden door'), ('brick', 'brick')], right=[0], cols=3)),
    Q('Draw something made of wood.', Draw('40mm', '', 'e.g. a chair, a table, a pencil, a door.')),
])

investigate = Sheet('investigate', 'Material hunt', level=2, goals=['Find materials in the classroom.', 'Make a picture graph.'], blocks=[
    Box('adult', P('Hunt around the classroom. For each thing, ask "What is it made of?" and colour one box.')),
    Q('Things we found. Colour one box for each.', Pictograph([('wood', 'wood', 6), ('plastic bottle', 'plastic', 7), ('key', 'metal', 4), ('newspaper', 'paper', 5)], top=8)),
    Q('Which material did we find the most? Circle it.', Choose([('wood', 'wood'), ('plastic bottle', 'plastic'), ('key', 'metal'), ('newspaper', 'paper')], right=[1])),
])

case = Sheet('case', 'The three little houses', level=3, goals=['Listen to a story.', 'Think about strong materials.'], blocks=[
    Case('Three friends built play houses. Tia used paper. Raju used sticks. Mila used bricks.',
         'Then a strong wind came: whoosh! The paper house blew away. The stick house fell down. The brick house stayed up. "Bricks are strong!" said Mila.'),
    Q('Which house stayed up? Circle.', Choose([('newspaper', 'paper house'), ('wood', 'stick house'), ('brick', 'brick house')], right=[2], cols=3)),
])

review = Sheet('review', 'I can do it!', level=3, goals=['Trace material words.'], blocks=[
    Q('Trace the words.', Trace([('wood', 'wood'), ('glass', 'glass bottle')])),
    Q('Circle the thing made of **metal**.', Choose([('teddy bear', 'teddy'), ('key', 'key'), ('newspaper', 'paper')], right=[1], cols=3)),
])

TOPIC = Topic(
    code='C1', strand='physical', title='Materials Around Us', short='Materials',
    subtitle='Wood, plastic, metal, glass, paper and cloth: what things are made of and how materials feel',
    outcomes=[
        'use the senses to talk about and explore different materials, and recognize and name common materials.',
        'identify the materials that everyday objects are made from — a pencil, a toy, a cup — and their use in daily life.',
        'identify the characteristics of different materials, and sort objects into groups based on the properties of their materials.',
        'gather, compare, sort, classify, order, interpret and describe observable characteristics and properties.',
        'observe patterns and draw conclusions from what they notice.',
    ],
    sheets=[learn, facts, think, investigate, case, review],
    selfcheck=['name materials', 'say what things are made of', 'sort hard and soft things'],
    cover_art=art.pic_row(['wood', 'plastic bottle', 'key', 'glass bottle', 'shirt'], ['wood', 'plastic', 'metal', 'glass', 'cloth']),
)
