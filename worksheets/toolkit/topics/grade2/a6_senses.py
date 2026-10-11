from build import Sheet, Topic
from ws import (P, H, Box, Vocab, Fig, Cols, Row, Case, Links, Lines, Blanks, Match, TrueFalse, MCQ, Order, Table,
                Ans, Sort, Label, Draw, Graph, WordSearch, Q, Part, Bullets, Pics)
import art

learn = Sheet('learn', 'Our five senses', level=1, goals=[
    'Name the five senses and the body part for each.',
    'Explain how we use our senses to learn about the world.',
    'Describe light and sound using our senses: bright, dark, loud and quiet.',
], blocks=[
    P('How do you know a mango is ripe? You can **see** it is yellow, **smell** it, **touch** it to feel if it is soft, and **taste** it. '
      'Your senses send messages to your **brain**, which tells you what is happening around you.', 'lead'),
    Pics([('eye', 'sight: eyes'), ('ear', 'hearing: ears'), ('nose', 'smell: nose'), ('tongue', 'taste: tongue'), ('hand', 'touch: skin')], cols=5, size='16mm'),
    Table(['Sense', 'Body part', 'It tells us…'], [
        ['**sight**', 'eyes', 'colour, shape, size, how far away, bright or dark'],
        ['**hearing**', 'ears', 'loud or quiet sounds, high or low sounds'],
        ['**smell**', 'nose', 'nice smells like flowers, or bad smells like smoke'],
        ['**taste**', 'tongue', 'sweet, salty, sour and bitter'],
        ['**touch**', 'skin', 'hot or cold, rough or smooth, hard or soft']]),
    H('Senses keep us safe', 3),
    P('We **smell** smoke and know there may be a fire. We **hear** a car horn and stop. We **feel** a hot pan and pull our hand away. '
      'We **taste** milk that has gone sour and do not drink it.'),
    H('Light and our eyes', 3),
    P('We need **light** to see. Light comes from **light sources** such as the Sun, a lamp, a torch and a candle. In a dark room '
      'with no light we cannot see anything. Bright light can hurt our eyes: **never look straight at the Sun**.'),
    Pics([('sun', 'Sun'), ('light bulb', 'lamp'), ('flashlight', 'torch'), ('candle', 'candle'), ('moon', 'Moon: reflects sunlight')], cols=5, size='14mm'),
    P('When something blocks the light, it makes a **shadow**.'),
    H('Sound and our ears', 3),
    P('Sounds come from **sound sources**: a drum, a bell, a bird, your voice. Some sounds are **loud**, some are **quiet**, some are **high** (a whistle) and some are **low** (a big drum).'),
    Pics([('drum', 'drum'), ('bell', 'bell'), ('bird', 'bird'), ('loudspeaker', 'loudspeaker')], cols=4, size='14mm'),
    Box('safety', P('Never put anything in your ears or nose. Keep away from very loud sounds and very bright lights.')),
    Vocab([('senses', 'sight, hearing, smell, taste and touch'), ('light source', 'something that gives out light'),
           ('shadow', 'a dark shape made when light is blocked'), ('sound source', 'something that makes a sound')]),
])

facts = Sheet('facts', 'Which sense?', level=1, goals=['Match senses to body parts.', 'Name light and sound sources.'], blocks=[
    Q('Draw a line to match.', Match([('sight', 'eyes'), ('hearing', 'ears'), ('smell', 'nose'), ('taste', 'tongue'), ('touch', 'skin')]), marks=5),
    Q('Which sense do you use most? Write it under each picture.', Pics([('rose', Ans('smell')), ('bell', Ans('hearing')), ('lemon', Ans('taste')), ('rainbow', Ans('sight')), ('ice cube', Ans('touch'))], cols=5, size='14mm'), marks=5),
    Q('Sort them.', Sort(['Gives out light', 'Makes sound'], [('Sun', 'Gives out light'), ('torch', 'Gives out light'), ('candle', 'Gives out light'), ('drum', 'Makes sound'), ('bell', 'Makes sound'), ('bird singing', 'Makes sound')]), marks=6),
])

think = Sheet('think', 'Senses keep us safe', level=2, goals=['Explain how senses help us.'], blocks=[
    Q('Which sense warns you? Explain.', Table(['Danger', 'Sense', 'What you do'], [['smoke from a fire', Ans('smell'), Ans('get out and tell an adult')], ['a car horn', Ans('hearing'), Ans('stop and look')], ['a hot cup', Ans('touch'), Ans('pull my hand away')]],
                                                                                 widths=['34%', '24%', '42%']), marks=6),
    Q('Why can\'t you see anything in a dark room with no light?', Lines(2, 'We need light to see; with no light, no light enters our eyes.'), marks=2),
    Q('Draw a sound that is loud and a sound that is quiet.', Row([Draw('30mm', 'loud', 'e.g. a drum, thunder')], [Draw('30mm', 'quiet', 'e.g. a whisper, a ticking clock')]), marks=2),
])

investigate = Sheet('investigate', 'The touch test', level=2, goals=['Use a sense to sort.', 'Record in a table.'], blocks=[
    P('Put objects in a bag. Close your eyes, touch each one and say what it feels like.'),
    Q('Complete the table.', Table(['Object', 'Rough or smooth?', 'Hard or soft?'], [['stone', Ans('rough or smooth'), Ans('hard')], ['sponge', Ans('rough'), Ans('soft')],
                                                                                    ['spoon', Ans('smooth'), Ans('hard')], ['cotton wool', Ans('smooth'), Ans('soft')]], center=True), marks=4),
    Q('Which sense did you use?', MCQ(['sight', 'touch', 'taste'], 1), marks=1),
    Q('Why did you close your eyes?', Lines(1, 'So I used only touch, not sight; it is fair.'), marks=1),
])

case = Sheet('case', 'Raju uses his other senses', level=3, goals=['Learn how people with sight loss use other senses.'], blocks=[
    Links('Science', 'Caring for others'),
    Case('Raju cannot see, but he goes to school like everyone else. He reads books in **Braille**: little raised dots that he feels '
         'with his **fingers**. He uses a white cane to **feel** the path in front of him and **listens** carefully to the sounds around him.',
         'Raju knows his friends by their **voices** and can tell what is for lunch by the **smell**. His classmates help by keeping '
         'bags off the floor and telling him when something moves.',
         source='A story about a learner with sight loss.'),
    Q('Which senses does Raju use?', Table(['Sense', 'How Raju uses it'], [['touch', Ans('reads Braille, feels the path with a cane')], ['hearing', Ans('knows friends by their voices')], ['smell', Ans('knows what is for lunch')]], widths=['30%', '70%']), marks=3),
    Q('How can classmates help Raju?', Lines(2, 'Keep the floor clear, tell him when things move, guide him kindly.'), marks=2),
])

review = Sheet('review', 'Show what you know', level=3, goals=['Use sense words.'], blocks=[
    Q('Find the words.', WordSearch(['EYES', 'EARS', 'NOSE', 'TONGUE', 'SKIN', 'LIGHT'], size=8, seed=207)),
    Q('Which body part do we use to taste?', MCQ(['nose', 'tongue', 'ear'], 1), marks=1),
    Q('Which is a light source?', MCQ(['the Sun', 'a mirror', 'a book'], 0), marks=1),
    Q('**Challenge.** Draw your favourite food and write how it looks, smells and tastes.', Draw('40mm', 'My favourite food', 'e.g. mango: yellow, sweet smell, sweet taste.'), marks=3),
])

TOPIC = Topic(
    code='A6', strand='living', title='Our Senses', short='Senses',
    subtitle='Sight, hearing, smell, taste and touch, and how we notice light and sound',
    outcomes=[
        'explore the human senses and the ways we use them to learn about our world.',
        'recognize different properties of light and sound through the senses.',
    ],
    cambridge=['Stage 3 Unit 4 Our five senses', 'Stage 2 Unit 4 Light and dark (4.1–4.4)'],
    sheets=[learn, facts, think, investigate, case, review],
    selfcheck=['name the five senses', 'match senses to body parts', 'say how senses keep me safe', 'name light sources and sound sources', 'sort objects by touch'],
    cover_art=art.pic_row(['eye', 'ear', 'nose', 'tongue', 'hand']),
)
