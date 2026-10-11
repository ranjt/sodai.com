from build import Sheet, Topic
from ws import (P, H, Box, Vocab, Fig, Cols, Row, Case, Links, Lines, Blanks, Match, TrueFalse, MCQ, Order, Table,
                Ans, Sort, Label, Draw, Graph, WordSearch, Q, Part, Bullets, Pics)
import art
import art4

KEY = ('Does it have legs?', ('Does it have 6 legs?', ('ant', 'ant'), ('frog', 'frog')), ('Does it live in water?', ('fish', 'fish'), ('worm', 'earthworm')))

learn = Sheet('learn', 'Habitats and adaptation', level=1, goals=[
    'Explain that animals live in habitats that suit them.',
    'Use a simple key to name living things.',
    'Explain how living things change their surroundings to meet their needs.',
], blocks=[
    P('A **habitat** is the place where an animal or plant lives. It gives the animal **food**, **water**, **shelter** and a safe place to **raise young**. Different animals live in different habitats.', 'lead'),
    Fig(art4.habitats_strip(), 'Animals in the air, in trees, in water, on land and under the ground.', width='92%'),
    H('Suited to their homes', 3),
    P('Animals have body parts that help them live in their habitat. This is called **adaptation**.'),
    Table(['Animal', 'Habitat', 'How it is suited'], [
        ['fish', 'river, pond, sea', 'gills to breathe in water; fins to swim'], ['monkey', 'trees', 'long arms and a tail for climbing'],
        ['duck', 'pond', 'webbed feet for swimming; waterproof feathers'], ['earthworm', 'soil', 'thin, slimy body for sliding through soil'],
        ['camel', 'hot desert', 'stores fat in its hump; wide feet on sand']]),
    H('Using a key', 3),
    P('A **key** asks yes/no questions to help you name a living thing. Start at the top and follow the answers.'),
    Fig(art4.key_tree(KEY), 'A simple key.', width='74%'),
    H('Changing the habitat', 3),
    P('Some animals **change** their surroundings to meet their needs. The **baya weaver** bird weaves a hanging nest from grass. **Termites** build tall mounds of mud. **Earthworms** dig tunnels. **People** build houses, dig ponds and plant gardens.'),
    Pics([('nest with eggs', 'birds build nests'), ('ant', 'ants dig tunnels'), ('worm', 'worms make burrows'), ('house', 'people build houses')], cols=4, size='14mm'),
    Box('bd', P('In the Sundarbans, fiddler crabs dig holes in the mud to hide when the tide comes in.')),
    Vocab([('habitat', 'the place where a living thing lives'), ('adaptation', 'a body part or behaviour that helps it survive'), ('key', 'yes/no questions to name a living thing'),
           ('shelter', 'a safe place to live and hide')]),
])

facts = Sheet('facts', 'Who lives where?', level=1, goals=['Match animals to habitats.', 'Use a key.'], blocks=[
    Q('Draw a line from the animal to its habitat.', Match([('fish', 'river'), ('monkey', 'forest trees'), ('camel', 'desert'), ('earthworm', 'soil'), ('polar bear', 'cold ice')]), marks=5),
    Q('Use the key on the Learn it page. Name the animal: it has legs, but not 6 legs.', Lines(1, 'frog'), marks=1),
    Q('Write the name of each animal under its habitat.', Pics([('dolphin', Ans('river or sea')), ('eagle', Ans('sky, tall trees')), ('worm', Ans('soil')), ('tiger', Ans('forest'))], cols=4, size='15mm'), marks=4),
])

think = Sheet('think', 'Why do they live there?', level=2, goals=['Explain adaptations.'], blocks=[
    Q('Why couldn\'t a fish live in a tree?', Lines(2, 'It breathes with gills in water and has fins, not legs; it would dry out.'), marks=2),
    Q('How is a duck suited to living on a pond?', Lines(2, 'Webbed feet for swimming and waterproof feathers.'), marks=2),
    Q('Make your own key to sort a bird, a snake, a cow and a fish.', Draw('46mm', 'My key', 'e.g. Does it have legs? Yes → Does it have feathers? (bird / cow). No → Does it live in water? (fish / snake).'), marks=3),
])

investigate = Sheet('investigate', 'Where do woodlice like to live?', level=2, goals=['Do a fair test.', 'Count and compare.'], blocks=[
    P('Class 3A put 10 woodlice in a tray. One end was dark and damp, the other light and dry. After 10 minutes they counted them.'),
    Q('Draw a bar chart.', Table(['Side', 'dark and damp', 'light and dry'], [['Woodlice', '9', '1']], center=True),
      Graph(['dark and damp', 'light and dry'], [9, 1], 'Number of woodlice', 'Side', ymax=10, step=1, width=90, height=46), marks=2),
    Q('Where do woodlice prefer to live?', Lines(1, 'in dark, damp places'), marks=1),
    Q('Suggest why.', Lines(2, 'They dry out easily, and dark damp places (under logs and stones) keep them safe from birds.'), marks=2),
    Q('How should they treat the woodlice afterwards?', Lines(1, 'Put them back gently where they were found.'), marks=1),
])

case = Sheet('case', 'The baya weaver\'s hanging nest', level=3, goals=['Learn how an animal changes its habitat.'], blocks=[
    Links('Science', 'Design', 'Nature'),
    Case('The **baya weaver** is a small bird found in Bangladesh. In the rainy season, the male weaves an amazing nest from strips of grass and palm leaves. It hangs from the tip of a branch, often over water.',
         'The nest has a long tube for a door at the bottom. Snakes and big birds find it very hard to reach the eggs. The weaver has changed its habitat to make a safe home for its babies.',
         source='Based on the behaviour of the baya weaver (babui pakhi).'),
    Q('How does the nest keep the eggs safe?', Lines(2, 'It hangs from a thin branch over water with a long tube entrance, so snakes and big birds cannot reach it.'), marks=2),
    Q('What materials does the weaver use?', Lines(1, 'strips of grass and palm leaves'), marks=1),
    Q('Design a safe home for an animal you like. Draw and label it.', Draw('44mm', 'My animal home', 'Any reasoned design with labels showing food, water and shelter.'), marks=3),
])

review = Sheet('review', 'Show what you know', level=3, goals=['Use habitat words.'], blocks=[
    Q('Find the words.', WordSearch(['HABITAT', 'NEST', 'SHELTER', 'KEY', 'FOOD', 'WATER'], size=9, seed=304)),
    Q('Which animal is suited to living in trees?', MCQ(['fish', 'monkey', 'camel'], 1), marks=1),
    Q('A habitat gives an animal…', MCQ(['food, water and shelter', 'only toys', 'nothing'], 0), marks=1),
    Q('**Challenge.** What might happen to the monkeys if their forest is cut down?', Lines(2, 'They lose food and shelter; they must move, or they may die.'), marks=2),
])

TOPIC = Topic(
    code='A3', strand='living', title='Habitats and Adaptation', short='Habitats',
    subtitle='Animals suited to their habitats, simple keys, and how living things change their surroundings',
    outcomes=[
        'investigate how different animals are found in different habitats and are suited to the environment in which they are found.',
        'use simple identification keys to sort and name living things.',
        'communicate understandings, supported by evidence, of how living things can adapt their environment to meet their needs.',
    ],
    cambridge=['Stage 3 Unit 3 Living things (3.4–3.5)'],
    sheets=[learn, facts, think, investigate, case, review],
    selfcheck=['say what a habitat gives an animal', 'explain how animals are suited to habitats', 'use a key', 'test where woodlice live', 'explain how animals change their homes'],
    cover_art=art4.habitats_strip(),
)
