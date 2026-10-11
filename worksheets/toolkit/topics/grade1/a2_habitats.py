from build import Sheet, Topic
from ws import (P, H, Box, Vocab, Fig, Q, Lines, Blanks, Match, TrueFalse, MCQ, Table, Ans, Sort, Draw, Graph, WordSearch, Bullets, Pics,
                Choose, PicMatch, PicSort, Pictograph, Trace, Case)
import art

learn = Sheet('learn', 'Habitats of Bangladesh', level=1, goals=['Name five kinds of habitat.', 'Say how a habitat meets an animal\'s needs.'], blocks=[
    P('A **habitat** is the home of a plant or animal. It gives them food, water, air and shelter. Bangladesh has many habitats.', 'lead'),
    Table(['Habitat', 'Where?', 'Who lives there?'], [
        ['**aerial**', 'in the air and sky', 'birds, bats, butterflies'],
        ['**arboreal**', 'in trees', 'monkeys, squirrels, parrots'],
        ['**aquatic**', 'in water: ponds, rivers, the sea', 'fish, frogs, ducks, crabs'],
        ['**terrestrial**', 'on land: fields, forests', 'cows, tigers, ants, snakes'],
        ['**fossorial**', 'under the ground', 'earthworms, rats, ants']]),
    Pics([('bird', 'aerial'), ('monkey', 'arboreal'), ('fish', 'aquatic'), ('tiger', 'terrestrial'), ('worm', 'fossorial')], cols=5, size='18mm'),
    H('A habitat meets needs', 3),
    P('A pond gives a frog water to swim in, insects to eat and plants to hide under. A tree gives a monkey fruit to eat and branches to climb and sleep in.'),
    Vocab([('habitat', 'the home of a living thing'), ('aquatic', 'living in water'), ('arboreal', 'living in trees'), ('fossorial', 'living under the ground')]),
])

facts = Sheet('facts', 'Who lives where?', level=1, goals=['Match animals to habitats.'], blocks=[
    Q('Match each animal to its habitat.', PicMatch([(('fish', 'fish'), ('water wave', 'water')), (('monkey', 'monkey'), ('deciduous tree', 'tree')),
                                                     (('worm', 'earthworm'), ('seedling', 'underground')), (('bird', 'bird'), ('cloud', 'sky'))], size='14mm')),
    Q('Circle the **aquatic** animals.', Choose([('crab', 'crab'), ('cow', 'cow'), ('frog', 'frog'), ('duck', 'duck'), ('monkey', 'monkey'), ('fish', 'fish')], right=[0, 2, 3, 5], cols=6, size='17mm')),
])

think = Sheet('think', 'Why live there?', level=2, goals=['Explain how a habitat helps.'], blocks=[
    Q('How does a pond help a frog?', Lines(2, 'It gives water to swim in, insects to eat and plants to hide under.')),
    Q('Could a fish live in a tree? Why not?', Lines(2, 'No. A fish needs water to breathe and swim.')),
    Q('Draw an animal in its habitat.', Draw('40mm', '', 'e.g. a monkey in a tree eating fruit.')),
])

investigate = Sheet('investigate', 'Pond or garden?', level=2, goals=['Count living things in two habitats.', 'Compare.'], blocks=[
    Box('adult', P('Visit a pond and a garden. Count the animals you see in 5 minutes. Look, do not touch.')),
    Q('Animals we saw. Colour one box for each.', Pictograph([('frog', 'frogs (pond)', 3), ('fish', 'fish (pond)', 6), ('ant', 'ants (garden)', 8), ('butterfly', 'butterflies (garden)', 4)], top=9)),
    Q('Name one animal we found in both places.', Lines(1, 'e.g. birds or insects like dragonflies')),
    Q('Which habitat had water animals?', MCQ(['the pond', 'the garden'], 0)),
])

case = Sheet('case', 'Homes in the Sundarbans', level=3, goals=['Read about a special habitat.'], blocks=[
    Case('The Sundarbans is a big forest by the sea. Its trees grow in salty mud. Tigers and deer walk on the land. Monkeys climb the trees.',
         'Crabs dig holes in the mud. Fish and crocodiles swim in the rivers. Birds fly above. It has every kind of habitat!'),
    Q('Find an animal for each habitat in the story.', Table(['Habitat', 'Animal'], [['terrestrial (land)', Ans('tiger or deer')], ['arboreal (trees)', Ans('monkey')],
                                                                                   ['fossorial (underground)', Ans('crab')], ['aquatic (water)', Ans('fish or crocodile')], ['aerial (air)', Ans('birds')]], widths=['50%', '50%'])),
])

review = Sheet('review', 'Show what you know', level=3, goals=['Use habitat words.'], blocks=[
    Q('Find the words.', WordSearch(['POND', 'TREE', 'SKY', 'LAND', 'HOME'], size=7, seed=103)),
    Q('An animal that lives in trees is…', MCQ(['aquatic', 'arboreal', 'fossorial'], 1)),
])

TOPIC = Topic(
    code='A2', strand='living', title='Habitats of Bangladesh', short='Habitats',
    subtitle='Aerial, arboreal, aquatic, terrestrial and underground homes, and how habitats meet needs',
    outcomes=[
        'describe the different types of habitat found in Bangladesh — aerial, arboreal, aquatic, terrestrial and fossorial — and make comparisons between them.',
        'make observations of a habitat in a local ecosystem and identify the living organisms occupying it.',
        'explain how the habitat observed supports the characteristics of the living things found there.',
        'identify similarities and differences between local environments, and know some of the ways these affect the animals and plants found there.',
        'describe how different places meet the needs of living things.',
    ],
    sheets=[learn, facts, think, investigate, case, review],
    selfcheck=['name five kinds of habitat', 'match animals to habitats', 'say how a habitat helps'],
    cover_art=art.pic_row(['bird', 'monkey', 'fish', 'tiger', 'worm'], ['air', 'trees', 'water', 'land', 'underground']),
)
