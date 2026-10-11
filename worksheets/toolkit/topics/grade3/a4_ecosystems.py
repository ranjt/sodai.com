from build import Sheet, Topic
from ws import (P, H, Box, Vocab, Fig, Cols, Row, Case, Links, Lines, Blanks, Match, TrueFalse, MCQ, Order, Table,
                Ans, Sort, Label, Draw, Graph, WordSearch, Q, Part, Bullets, Pics)
import art
import art4

learn = Sheet('learn', 'Ecosystems of Bangladesh', level=1, goals=[
    'Explain what an ecosystem is and sort its parts into living and non-living.',
    'Describe land and water ecosystems found in Bangladesh.',
    'Explain how non-living features decide which plants and animals can live there.',
], blocks=[
    P('An **ecosystem** is a place where **living things** (plants, animals and tiny microbes) live together with **non-living things** (water, soil, rocks, air, sunlight). They all depend on each other.', 'lead'),
    Fig(art4.pond_ecosystem(labels=art4.POND_PARTS), 'A pond ecosystem.', width='80%'),
    H('Ecosystems in Bangladesh', 3),
    Table(['Ecosystem', 'Where', 'Some living things'], [
        ['**wetland** (haor, beel)', 'Sylhet, Sunamganj', 'water lilies, fish, ducks, frogs'],
        ['**broadleaf forest**', 'Lawachara, Sylhet hills', 'tall trees, gibbons, birds, insects'],
        ['**pine forest**', 'planted on some hills', 'pine trees, birds, insects'],
        ['**grassland**', 'river chars, coastal areas', 'grasses, cattle, birds, grasshoppers'],
        ['**stream**', 'hill areas', 'small fish, crabs, insects, water plants'],
        ['**mangrove**', 'Sundarbans', 'sundari trees, tigers, deer, crabs, crocodiles'],
        ['**sea grass beds**', 'shallow sea near the coast', 'sea grass, fish, turtles, sea cucumbers'],
        ['**coral reef**', 'Saint Martin\'s Island', 'corals, colourful fish, sea snails']]),
    Pics([('lotus', 'wetland'), ('deciduous tree', 'broadleaf forest'), ('evergreen tree', 'pine forest'), ('herb', 'grassland'), ('water wave', 'stream'), ('coral', 'coral reef')], cols=6, size='13mm'),
    H('Non-living things decide who lives there', 3),
    P('The **non-living** features of a place decide which plants and animals can live there: how much **water**, **light** and **heat** there is, the kind of **soil**, and whether the water is **salty** or fresh. '
      'Only special trees can grow in the salty mud of the Sundarbans. Coral needs warm, clear, salty water. Water lilies need fresh water and sunlight.'),
    Box('try', P('Look at a place near your home: a pond, a garden or a field. List the living and non-living things you can see.')),
    Vocab([('ecosystem', 'living and non-living things in a place, depending on each other'), ('aquatic', 'in water'), ('terrestrial', 'on land'),
           ('wetland', 'land covered with water for much of the year'), ('coral reef', 'a hard home built by tiny sea animals called corals')]),
])

facts = Sheet('facts', 'Living or non-living?', level=1, goals=['Sort parts of ecosystems.', 'Match ecosystems to places.'], blocks=[
    Q('Sort the parts of a pond.', Sort(['Living', 'Non-living'], [('fish', 'Living'), ('water lily', 'Living'), ('frog', 'Living'), ('duck', 'Living'), ('water', 'Non-living'), ('mud', 'Non-living'), ('sunlight', 'Non-living'), ('stones', 'Non-living')]), marks=8),
    Q('Draw a line to match the ecosystem to the place.', Match([('mangrove', 'Sundarbans'), ('coral reef', 'Saint Martin\'s Island'), ('wetland', 'Sunamganj haors'), ('broadleaf forest', 'Lawachara')]), marks=4),
    Q('Aquatic or terrestrial?', Sort(['Aquatic (water)', 'Terrestrial (land)'], [('coral reef', 'Aquatic (water)'), ('stream', 'Aquatic (water)'), ('sea grass bed', 'Aquatic (water)'), ('grassland', 'Terrestrial (land)'), ('pine forest', 'Terrestrial (land)')]), marks=5),
])

think = Sheet('think', 'Why here?', level=2, goals=['Explain how non-living features decide what lives there.'], blocks=[
    Q('Why can\'t a water lily grow in a dry field?', Lines(2, 'It needs to grow in water; the dry field has no water for it.'), marks=2),
    Q('Why can\'t most trees grow in the Sundarbans?', Lines(2, 'The mud is salty and wet; only mangrove trees are suited to it.'), marks=2),
    Q('Draw an ecosystem you know. Label two living and two non-living things.', Draw('48mm', 'My ecosystem', 'e.g. a pond with fish and water lilies (living), water and stones (non-living).'), marks=4),
])

investigate = Sheet('investigate', 'Shady or sunny: where do more plants grow?', level=2, goals=['Count plants.', 'Compare two places.'], blocks=[
    P('Class 3B put a 1 metre square of string on the ground in a sunny place and in a shady place under a tree. They counted the plants inside.'),
    Q('Draw a bar chart.', Table(['Place', 'sunny', 'shady'], [['Number of plants', '32', '12']], center=True), Graph(['sunny', 'shady'], [32, 12], 'Number of plants', 'Place', ymax=35, step=5, width=80, height=46), marks=2),
    Q('Where did more plants grow? Why?', Lines(2, 'In the sunny place; plants need light to grow.'), marks=2),
    Q('Name one other non-living thing that might be different in the two places.', Lines(1, 'water in the soil, temperature'), marks=1),
])

case = Sheet('case', 'Saving the coral of Saint Martin\'s Island', level=3, goals=['Learn about a special ecosystem.', 'Suggest ways to protect it.'], blocks=[
    Links('Science', 'Geography', 'Citizenship'),
    Case('**Saint Martin\'s Island** is the only coral island in Bangladesh. Around it live corals, colourful fish, sea snails and turtles. Corals are tiny animals that build hard homes that grow very slowly.',
         'Every year many tourists visit. Some walk on the coral, break pieces to take home or leave plastic rubbish. Boats and new hotels also harm the reef. The government has made rules to protect the island.',
         source='Based on information about Saint Martin\'s Island, Bangladesh.'),
    Q('Why is the coral reef important?', Lines(2, 'It is a home and food place for many fish, snails and turtles.'), marks=2),
    Q('Write two rules for tourists to protect the coral.', Lines(2, 'Do not walk on or break the coral; take all rubbish home; do not collect shells or coral.'), marks=2),
    Q('Make a poster to protect the coral.', Draw('38mm', 'Protect our coral', 'e.g. picture of fish and coral: "Look, do not touch!"'), marks=2),
])

review = Sheet('review', 'Show what you know', level=3, goals=['Use ecosystem words.'], blocks=[
    Q('Find the words.', WordSearch(['WETLAND', 'FOREST', 'CORAL', 'STREAM', 'MANGROVE', 'SOIL'], size=9, seed=305)),
    Q('Which is a non-living part of an ecosystem?', MCQ(['a fish', 'sunlight', 'a tree'], 1), marks=1),
    Q('Where is the coral reef in Bangladesh?', MCQ(['Sylhet', 'Saint Martin\'s Island', 'Dhaka'], 1), marks=1),
    Q('**Challenge.** What would happen to a pond ecosystem if the pond dried up?', Lines(3, 'Fish and water plants would die; frogs could not lay eggs; ducks and kingfishers would fly away.'), marks=2),
])

TOPIC = Topic(
    code='A4', strand='living', title='Ecosystems of Bangladesh', short='Ecosystems',
    subtitle='Living and non-living parts, land and water ecosystems of Bangladesh, and who lives where',
    outcomes=[
        'explain what an ecosystem is and identify the general components of an ecosystem, distinguishing living from non-living things.',
        'identify and describe examples of aquatic and terrestrial ecosystems in Bangladesh — wetland, broadleaf forest, pine forest, grassland, stream, mangrove, sea grass beds and coral reef.',
        'investigate and observe the non-living features of a local ecosystem that help determine which plants and animals successfully live there.',
        'identify the different types of animals and plants that live in different local ecosystems.',
    ],
    sheets=[learn, facts, think, investigate, case, review],
    selfcheck=['explain what an ecosystem is', 'sort living and non-living parts', 'name ecosystems of Bangladesh', 'explain why plants and animals live where they do', 'compare plants in sun and shade'],
    cover_art=art4.pond_ecosystem(labels=art4.POND_PARTS),
)
