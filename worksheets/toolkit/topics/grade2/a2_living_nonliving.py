from build import Sheet, Topic
from ws import (P, H, Box, Vocab, Fig, Cols, Row, Case, Links, Lines, Blanks, Match, TrueFalse, MCQ, Order, Table,
                Ans, Sort, Label, Draw, Graph, WordSearch, Q, Part, Bullets, Pics)
import art

learn = Sheet('learn', 'Living or not living?', level=1, goals=[
    'Tell the difference between living and non-living things.',
    'Sort living things into groups and explain why.',
], blocks=[
    P('Look around you. A cat, a tree and your friend are **living**. A chair, a stone and a pencil are **non-living**. How can we tell?', 'lead'),
    H('What do living things do?', 3),
    Table(['Living things…', 'Example'], [
        ['**move**', 'a fish swims; a sunflower turns to the Sun'],
        ['**breathe**', 'we breathe in air'],
        ['**feed** (need food and water)', 'a goat eats grass; a plant makes its own food'],
        ['**grow**', 'a kitten grows into a cat'],
        ['**get rid of waste**', 'animals do poo and wee'],
        ['**sense** things around them', 'a dog hears its name'],
        ['**have young** (reproduce)', 'a hen lays eggs; a mango tree makes seeds']]),
    P('A **living** thing does **all** of these things. A **non-living** thing does not. Some non-living things were **once alive**, '
      'like wood from a tree or a dry leaf.'),
    Pics([('cat', 'living'), ('deciduous tree', 'living'), ('fish', 'living'), ('rock', 'non-living'), ('chair', 'non-living'), ('wood', 'once alive')], cols=6, size='14mm'),
    Box('tip', P('A car moves and needs fuel, but it does not grow or have baby cars! So it is **non-living**.')),
    H('Sorting living things', 3),
    P('Scientists **sort** living things into groups by looking at their features. We can sort them into **plants** and **animals**, '
      'and then sort animals again: animals with **legs** and animals without legs, animals with **fur**, **feathers** or **scales**, '
      'animals that **fly**, **swim** or **walk**.'),
    Pics([('bird', 'feathers'), ('cat', 'fur'), ('fish', 'scales'), ('snake', 'scales'), ('butterfly', 'wings'), ('worm', 'no legs')], cols=6, size='14mm'),
    Box('bd', P('In the Sundarbans you can find many living things: tigers, deer, crabs, fish, mangrove trees and birds.')),
    Vocab([('living', 'moves, breathes, feeds, grows, has young'), ('non-living', 'not alive and never was, or no longer alive'),
           ('sort', 'put into groups'), ('feature', 'something you can see, like fur or wings')]),
])

facts = Sheet('facts', 'Sort them out', level=1, goals=['Sort living and non-living things.'], blocks=[
    Q('Write **living** or **non-living** under each picture.',
      Pics([('dog', Ans('living')), ('rock', Ans('non-living')), ('sunflower', Ans('living')), ('car', Ans('non-living')), ('frog', Ans('living')), ('pencil', Ans('non-living'))], cols=6, size='14mm'), marks=6),
    Q('Sort these things.', Sort(['Living', 'Non-living'], [('tree', 'Living'), ('baby', 'Living'), ('ant', 'Living'), ('ball', 'Non-living'), ('water', 'Non-living'), ('spoon', 'Non-living')]), marks=6),
    Q('True or false?', TrueFalse([('All living things grow.', True), ('A stone can have babies.', False, 'A stone is non-living; it cannot have young.'), ('Plants are living things.', True)]), marks=3),
])

think = Sheet('think', 'Tricky ones', level=2, goals=['Explain why something is living or not.', 'Sort animals by features.'], blocks=[
    Q('A toy robot can move and make sounds. Is it living? Explain.', Lines(2, 'No. It cannot grow, eat, breathe or have young.'), marks=2),
    Q('Is a seed living? Explain.', Lines(2, 'Yes. If it gets water and warmth it grows into a new plant.'), marks=2),
    Q('Sort the animals by what covers their body.', Sort(['Fur', 'Feathers', 'Scales'], [('cat', 'Fur'), ('goat', 'Fur'), ('duck', 'Feathers'), ('parrot', 'Feathers'), ('fish', 'Scales'), ('snake', 'Scales')]), marks=6),
])

investigate = Sheet('investigate', 'Living things in our school', level=2, goals=['Count and record.', 'Make a pictogram.'], blocks=[
    P('Class 2C walked around the school garden and counted the living things they saw.'),
    Q('Draw a bar chart.', Table(['Living thing', 'trees', 'birds', 'ants', 'butterflies'], [['How many', '5', '8', '20', '3']], center=True),
      Graph(['trees', 'birds', 'ants', 'butterflies'], [5, 8, 20, 3], 'How many', 'Living thing', ymax=20, step=2, width=110, height=50), marks=3),
    Q('Which living thing did they see most?', Lines(1, 'ants'), marks=1),
    Q('Name two non-living things they might see in the garden.', Lines(1, 'stones, a bench, water, a fence'), marks=2),
])

case = Sheet('case', 'A day at the village pond', level=3, goals=['Find living and non-living things in a real place.'], blocks=[
    Links('Science', 'Nature', 'Art'),
    Case('Tanvir visits his grandmother in the village. Behind her house there is a pond. Ducks swim on the water and lotus '
         'flowers float on top. Small fish dart under the water. A frog jumps from a lily pad. On the bank there are stones, an old '
         'boat and a tree.',
         'Tanvir sits very still and watches. He sees a kingfisher dive and catch a fish!',
         source='A story about a village pond.'),
    Q('Find the living and non-living things in the story.', Sort(['Living', 'Non-living'], [('ducks', 'Living'), ('lotus', 'Living'), ('fish', 'Living'), ('frog', 'Living'),
                                                                                             ('stones', 'Non-living'), ('old boat', 'Non-living'), ('water', 'Non-living')]), marks=7),
    Q('Draw the pond. Draw two living and two non-living things.', Draw('46mm', 'The pond', 'e.g. ducks and fish (living); water and stones (non-living).'), marks=2),
])

review = Sheet('review', 'Show what you know', level=3, goals=['Use science words.'], blocks=[
    Q('Find the words.', WordSearch(['LIVING', 'GROW', 'MOVE', 'FEED', 'PLANT', 'ANIMAL'], size=8, seed=203)),
    Q('Which is living?', MCQ(['a chair', 'a cat', 'a stone'], 1), marks=1),
    Q('Which do all living things do?', MCQ(['fly', 'grow', 'swim'], 1), marks=1),
    Q('**Challenge.** Write three ways you know that you are living.', Lines(3, 'I breathe, I eat and drink, I grow, I move.'), marks=3),
])

TOPIC = Topic(
    code='A2', strand='living', title='Living and Non-Living Things', short='Living and non-living',
    subtitle='What living things do, and sorting living things into groups',
    outcomes=[
        'describe the differences between living and non-living things, using knowledge of life processes.',
        'sort living things into groups using simple features, and describe the reasons for the groupings.',
    ],
    cambridge=['Stage 3 Unit 3 Living things (3.4–3.5 Sorting)', 'Stage 2 Unit 1 Going outside (1.1 Different places to live)'],
    sheets=[learn, facts, think, investigate, case, review],
    selfcheck=['say what living things do', 'sort living and non-living things', 'sort animals by their features', 'count living things and make a chart'],
    cover_art=art.pic_row(['cat', 'deciduous tree', 'rock', 'chair']),
)
