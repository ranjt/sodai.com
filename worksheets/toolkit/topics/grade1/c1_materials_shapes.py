from build import Sheet, Topic
from ws import (P, H, Box, Vocab, Fig, Q, Lines, Blanks, Match, TrueFalse, MCQ, Table, Ans, Sort, Draw, Graph, WordSearch, Bullets, Pics,
                Choose, PicMatch, PicSort, Pictograph, Trace, Case)
import art

learn = Sheet('learn', 'Materials and their shapes', level=1, goals=['Tell natural materials from made materials.', 'Change the shape of materials.'], blocks=[
    P('Everything is made of **materials**. Some materials come from **nature**. Others are **made by people**.', 'lead'),
    Table(['Natural materials', 'Made by people'], [['wood (from trees)', 'plastic'], ['cotton and wool', 'glass'], ['stone and clay', 'paper'], ['jute', 'metal objects like spoons']]),
    Pics([('wood', 'wood'), ('rock', 'stone'), ('yarn', 'wool'), ('plastic bottle', 'plastic'), ('glass bottle', 'glass'), ('newspaper', 'paper')], cols=6, size='17mm'),
    H('Changing shape', 3),
    P('We can change the shape of some materials by **squashing**, **bending**, **twisting** and **stretching**.'),
    Table(['Action', 'Try it with'], [['**squash**', 'a sponge, clay, play dough'], ['**bend**', 'a pipe cleaner, a straw'], ['**twist**', 'a towel, a rope'], ['**stretch**', 'a rubber band, a balloon']]),
    P('Some materials go back to their shape (a sponge). Some stay in the new shape (clay).'),
    Vocab([('natural', 'comes from nature'), ('made by people', 'made in factories or by hand'), ('squash', 'press hard'), ('stretch', 'pull to make longer')]),
])

facts = Sheet('facts', 'Sort the materials', level=1, goals=['Sort natural and made materials.'], blocks=[
    Q('Sort the materials.', Sort(['Natural', 'Made by people'], [('wood', 'Natural'), ('cotton', 'Natural'), ('stone', 'Natural'),
                                                                 ('plastic', 'Made by people'), ('glass', 'Made by people'), ('paper', 'Made by people')])),
    Q('Match the action to the object.', Match([('squash', 'a sponge'), ('stretch', 'a rubber band'), ('twist', 'a wet towel'), ('bend', 'a pipe cleaner')])),
])

think = Sheet('think', 'Which material?', level=2, goals=['Explain choices of materials.'], blocks=[
    Q('Why is a ball made of rubber, not stone?', Lines(2, 'Rubber bends and bounces; stone is hard and heavy.')),
    Q('Which material goes back to its shape after squashing?', MCQ(['clay', 'a sponge'], 1)),
    Q('Draw something you can stretch.', Draw('36mm', '', 'e.g. a rubber band, a balloon, a hair band.')),
])

investigate = Sheet('investigate', 'Which band stretches most?', level=2, goals=['Do a fair test.', 'Read a bar chart.'], blocks=[
    P('Class 1 hung the same toy from three rubber bands and measured how long each band became.'),
    Q('Our results. Draw the bars.', Table(['Band', 'thin', 'medium', 'thick'], [['Length (cm)', '14', '11', '8']], center=True),
      Graph(['thin', 'medium', 'thick'], [14, 11, 8], 'Length (cm)', 'Band', ymax=16, step=2, width=78, height=44)),
    Q('Which band stretched the most?', MCQ(['thin', 'medium', 'thick'], 0)),
    Q('What did they keep the same?', Lines(1, 'the same toy (the same weight)')),
])

case = Sheet('case', 'The potter of Rajshahi', level=3, goals=['Read about a natural material.'], blocks=[
    Case('Mr Paul is a potter. He digs **clay** from the river bank. He squashes and shapes the soft wet clay on his spinning wheel to make pots.',
         'Then he dries the pots in the sun and heats them in a hot fire called a **kiln**. Now the clay is hard and will never go soft again.'),
    Q('Is clay a natural material or made by people?', MCQ(['natural', 'made by people'], 0)),
    Q('How does Mr Paul change the shape of the clay?', Lines(1, 'He squashes and shapes it on a spinning wheel.')),
])

review = Sheet('review', 'Show what you know', level=3, goals=['Use material words.'], blocks=[
    Q('Find the words.', WordSearch(['WOOD', 'GLASS', 'BEND', 'TWIST', 'CLAY'], size=7, seed=108)),
    Q('Which is made by people?', MCQ(['stone', 'plastic', 'wool'], 1)),
])

TOPIC = Topic(
    code='C1', strand='physical', title='Materials and Their Shapes', short='Materials',
    subtitle='Natural and made materials, and changing shape by squashing, bending, twisting and stretching',
    outcomes=[
        'know that some materials occur naturally and others are made by people.',
        'recognise different materials, such as plastics and wood.',
        'know how the shapes of some materials can be changed by squashing, bending, twisting and stretching.',
    ],
    sheets=[learn, facts, think, investigate, case, review],
    selfcheck=['tell natural from made materials', 'change the shape of materials', 'test which band stretches most'],
    cover_art=art.pic_row(['wood', 'yarn', 'plastic bottle', 'glass bottle', 'balloon'], ['wood', 'wool', 'plastic', 'glass', 'stretch']),
)
