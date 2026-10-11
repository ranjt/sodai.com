from build import Sheet, Topic
from ws import (P, H, Box, Vocab, Fig, Q, Lines, Blanks, Match, TrueFalse, MCQ, Table, Ans, Sort, Draw, Graph, WordSearch, Bullets, Pics,
                Choose, PicMatch, PicSort, Pictograph, Trace, Case)
import art

learn = Sheet('learn', 'Light, dark and sound', level=1, goals=['Name light sources and explain darkness.', 'Explain shadows and how sounds are made.'], blocks=[
    P('We need **light** to see. Things that give out light are **light sources**. The biggest is the **Sun**.', 'lead'),
    Pics([('sun', 'Sun'), ('light bulb', 'lamp'), ('flashlight', 'torch'), ('candle', 'candle'), ('fire', 'fire'), ('mobile phone', 'screen')], cols=6, size='17mm'),
    P('**Darkness** is when there is no light. In a dark room we cannot see anything. The Moon is not a light source: it reflects light from the Sun.'),
    H('Shadows', 3),
    P('When something blocks the light, a dark **shadow** forms behind it. Shadows have the same shape as the thing blocking the light.'),
    Fig(art.shadow_setup(), 'An object blocks the light and makes a shadow.', width='66%'),
    H('Sound', 3),
    P('Sounds are made when things **vibrate**: shake very fast. A drum skin vibrates when you hit it. A string vibrates when you pluck it. We hear sounds with our **ears**.'),
    Pics([('drum', 'drum'), ('guitar', 'guitar'), ('bell', 'bell'), ('loudspeaker', 'speaker'), ('dog', 'barking dog')], cols=5, size='17mm'),
    Vocab([('light source', 'something that gives out light'), ('shadow', 'a dark shape where light is blocked'), ('vibrate', 'shake very fast')]),
])

facts = Sheet('facts', 'Light and sound facts', level=1, goals=['Find light sources.', 'Sort sources.'], blocks=[
    Q('Circle the **light sources**.', Choose([('sun', 'Sun'), ('moon', 'Moon'), ('candle', 'candle'), ('mirror', 'mirror'), ('flashlight', 'torch'), ('glass bottle', 'bottle')],
                                             right=[0, 2, 4], cols=6, size='17mm')),
    Q('True or false?', TrueFalse([('The Moon is a light source.', False, 'It reflects the Sun\'s light.'), ('A shadow forms when light is blocked.', True),
                                   ('Sounds are made by vibrations.', True)])),
])

think = Sheet('think', 'Explain it', level=2, goals=['Explain shadows and sounds.'], blocks=[
    Q('Why can\'t we see in a dark room?', Lines(2, 'There is no light to show us things.')),
    Q('Why does a rubber band make a sound when you pluck it?', Lines(1, 'It vibrates.')),
    Q('Draw a shadow puppet and its shadow.', Draw('40mm', '', 'A hand or card shape in front of a torch with the same-shaped shadow on the wall.')),
])

investigate = Sheet('investigate', 'Shadow size', level=2, goals=['Change a shadow.', 'Read a bar chart.'], blocks=[
    P('Class 1 moved a toy closer to a torch and measured the size of its shadow on the wall.'),
    Q('Our results. Draw the bars.', Table(['Toy to torch', 'far', 'middle', 'near'], [['Shadow height (cm)', '8', '14', '25']], center=True),
      Graph(['far', 'middle', 'near'], [8, 14, 25], 'Height (cm)', 'Toy to torch', ymax=26, step=4, width=78, height=44)),
    Q('What happens to the shadow when the toy is near the torch?', Lines(1, 'It gets bigger.')),
])

case = Sheet('case', 'Shadow puppets', level=3, goals=['Read about shadow puppets.'], blocks=[
    Case('At the village fair, a man put on a **shadow puppet** show. He held cut-out puppets between a lamp and a white cloth.',
         'The audience saw dark shadows of a tiger, a king and a boat on the cloth. A drummer played music. Everyone cheered!'),
    Q('What was the light source?', Lines(1, 'the lamp')),
    Q('Why were the shadows on the cloth?', Lines(2, 'The puppets blocked the lamp\'s light.')),
    Q('How did the drummer make sound?', Lines(1, 'He hit the drum, so it vibrated.')),
])

review = Sheet('review', 'Show what you know', level=3, goals=['Use light and sound words.'], blocks=[
    Q('Find the words.', WordSearch(['LIGHT', 'DARK', 'SUN', 'DRUM', 'EAR'], size=7, seed=110)),
    Q('A shadow forms when…', MCQ(['light is blocked', 'it is very loud'], 0)),
])

TOPIC = Topic(
    code='C3', strand='physical', title='Light and Sound', short='Light and sound',
    subtitle='Light sources, darkness, shadows, and sounds made by vibrations',
    outcomes=[
        'identify different light sources, including the Sun, and know that darkness is the absence of light.',
        'be able to identify shadows.',
        'identify how light and sound are produced by a range of sources, and recognize different properties of light and sound through their senses.',
        'explore how different sounds may be made by making a variety of materials vibrate.',
    ],
    sheets=[learn, facts, think, investigate, case, review],
    selfcheck=['name light sources', 'explain how a shadow forms', 'say how sounds are made'],
    cover_art=art.pic_row(['sun', 'flashlight', 'candle', 'drum', 'bell'], ['Sun', 'torch', 'candle', 'drum', 'bell']),
)
