from build import Sheet, Topic
from ws import (P, H, Box, Vocab, Fig, Q, Lines, Blanks, Match, TrueFalse, MCQ, Table, Ans, Sort, Draw, Graph, WordSearch, Bullets, Pics,
                Choose, PicMatch, PicSort, Pictograph, Trace, Case)
import art

learn = Sheet('learn', 'What makes something living?', level=1, goals=['Name what all living things do.', 'Say what living things need.'], blocks=[
    P('A cat, a mango tree and you are all **living things**. A rock and a chair are not. What is the difference?', 'lead'),
    H('All living things…', 3),
    Pics([('person running', 'move'), ('wind face', 'breathe'), ('eye', 'feel and notice'), ('seedling', 'grow'), ('baby chick', 'have young'),
          ('toilet', 'get rid of waste'), ('cooked rice', 'need food')], cols=7, size='16mm'),
    P('Plants do these things too! A plant grows towards the light, takes in water through its roots and makes seeds. Inside animals, **blood** carries food and air around the body.'),
    H('Living things need…', 3),
    Pics([('cooked rice', 'food'), ('droplet', 'water'), ('wind face', 'air'), ('sun', 'light and warmth'), ('house', 'shelter')], cols=5, size='18mm'),
    Vocab([('living', 'alive: it grows, moves, feeds and has young'), ('non-living', 'never alive, like a stone'), ('needs', 'things it must have to stay alive')]),
])

facts = Sheet('facts', 'Living or non-living?', level=1, goals=['Sort living and non-living things.'], blocks=[
    Q('Cut and sort the pictures.', PicSort(['Living', 'Non-living'], [('goat', 'goat', 'Living'), ('sunflower', 'flower', 'Living'), ('worm', 'worm', 'Living'),
                                                                     ('bicycle', 'bicycle', 'Non-living'), ('rock', 'stone', 'Non-living'), ('teddy bear', 'teddy', 'Non-living')], height='30mm')),
    Q('Fill in the gaps.', Blanks('All living things [grow]. They need [food] and [water].', extra=['toys'])),
    Q('True or false?', TrueFalse([('A tree is a living thing.', True), ('A car is living because it moves.', False, 'A car cannot grow, feed or have young.')])),
])

think = Sheet('think', 'Is it living?', level=2, goals=['Explain why something is living.'], blocks=[
    Q('A toy robot can move and make sounds. Is it living? Why?', Lines(2, 'No. It cannot grow, eat or have young.')),
    Q('What do a fish and a mango tree both need?', Choose([('droplet', 'water'), ('candy', 'sweets'), ('sun', 'sunlight'), ('teddy bear', 'toys')], right=[0, 2])),
    Q('Draw a living thing and a non-living thing.', Draw('40mm', 'Living          |          Non-living', 'e.g. a cat and a chair.')),
])

investigate = Sheet('investigate', 'Do seeds need water?', level=2, goals=['Do a simple test.', 'Record results.'], blocks=[
    P('Class 1 put bean seeds on two plates of cotton wool. They watered one plate every day and kept the other dry.'),
    Q('After one week, how many seeds grew?', Table(['', 'watered', 'dry'], [['Seeds that grew', '9', '0']], center=True),
      Graph(['watered', 'dry'], [9, 0], 'Seeds that grew', '', ymax=10, step=2, width=70, height=44)),
    Q('What did the seeds need to grow?', Lines(1, 'water')),
])

case = Sheet('case', 'Is the stone alive?', level=3, goals=['Read a story.', 'Use what you know.'], blocks=[
    Case('Arif found a smooth stone by the river. "It is alive," he said, "because it rolled down the hill!"',
         'His sister Lina laughed. "Does it eat? Does it grow? Can it have babies?" Arif thought hard. "No," he said. "The stone is not alive. The water pushed it."'),
    Q('Why did Arif first think the stone was alive?', Lines(1, 'because it moved (rolled)')),
    Q('Which questions helped Arif? Tick them.', Table(['Question', 'Helpful?'], [['Does it eat?', Ans('yes')], ['Is it shiny?', Ans('no')], ['Does it grow?', Ans('yes')]], widths=['70%', '30%'])),
])

review = Sheet('review', 'Show what you know', level=3, goals=['Use living things words.'], blocks=[
    Q('Find the words.', WordSearch(['GROW', 'FOOD', 'AIR', 'WATER', 'MOVE'], size=7, seed=102)),
    Q('Which is a living thing?', MCQ(['a chair', 'a frog', 'a car'], 1)),
])

TOPIC = Topic(
    code='A1', strand='living', title='Living Things and What They Need', short='Living things',
    subtitle='What all living things do, and the food, water, air, light and shelter they need',
    outcomes=[
        'name the characteristics of all living things and cite examples of how these are shown in local organisms — how plants and animals grow, reproduce, respire, move and respond to stimuli, excrete, circulate fluids and obtain food.',
        'identify and describe examples of the external features and basic needs of living things.',
        'analyse how investigations can help us understand how living things survive.',
        'identify and describe the changes in living things.',
    ],
    sheets=[learn, facts, think, investigate, case, review],
    selfcheck=['name what living things do', 'say what living things need', 'test if seeds need water'],
    cover_art=art.pic_row(['goat', 'sunflower', 'fish', 'rock', 'bicycle'], ['goat', 'flower', 'fish', 'stone', 'bicycle']),
)
