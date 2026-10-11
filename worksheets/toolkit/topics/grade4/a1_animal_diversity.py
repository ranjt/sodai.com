from build import Sheet, Topic
from ws import (P, H, Box, Vocab, Fig, Cols, Row, Case, Links, Lines, Blanks, Match, TrueFalse, MCQ, Order, Table,
                Ans, Sort, Label, Draw, Graph, WordSearch, Q, Part, Bullets, Pics)
import art
import art4

KEY = ('Does it have legs?',
       ('Does it have more than 6 legs?', ('spider', 'spider'), ('Does it have wings?', ('honeybee', 'bee'), ('ant', 'ant'))),
       ('Does it have a shell?', ('snail', 'snail'), ('worm', 'earthworm')))

learn = Sheet('learn', 'Animals of Bangladesh: so many kinds!', level=1, goals=[
    'Name the places where animals live: in the air, in trees, in water, on land and under the ground.',
    'Sort animals into groups and use a branching key.',
    'Explain adaptation and migration with examples from Bangladesh.',
], blocks=[
    P('Bangladesh is a small country, but it is full of animals. Tigers hide in the Sundarbans, dolphins swim in the rivers, '
      'hoolock gibbons swing through the forests of Sylhet, and every winter thousands of ducks fly in from the cold north. '
      'Scientists have counted more than 1,600 kinds of animals with backbones here, and many thousands of insects. '
      'This huge variety of living things is called **biodiversity**.', 'lead'),
    Fig(art4.habitats_strip(), 'Animals live in different places. Each place gives them food, water and shelter.', width='96%'),
    Cols(
        H('Where do animals live?', 3),
        Bullets(['**Aerial** animals spend much of their life flying in the **air**: eagles, swallows, bats.',
                 '**Arboreal** animals live in **trees**: monkeys, gibbons, squirrels, many birds and snakes.',
                 '**Aquatic** animals live in **water**: fish such as the hilsa, Ganges river dolphins, crabs, frogs (for part of their life).',
                 '**Terrestrial** animals live on **land**: tigers, deer, elephants, cows and people.',
                 '**Fossorial** animals live **under the ground**: earthworms, moles, many ants and some snakes.']),
        H('Two big groups', 3),
        P('Scientists sort animals into groups by looking at their bodies. The first question is: does it have a **backbone**?'),
        P('**Vertebrates** have a backbone and a skeleton **inside** their bodies. There are five groups: **fish**, **amphibians** '
          '(frogs, toads), **reptiles** (snakes, lizards, crocodiles, turtles), **birds** and **mammals** (tigers, bats, people).'),
        Pics([('fish', 'fish'), ('frog', 'amphibian'), ('crocodile', 'reptile'), ('bird', 'bird'), ('tiger', 'mammal')], cols=5, size='14mm', small=True),
        P('**Invertebrates** have **no backbone**. Some, like insects, spiders and crabs, have a hard **exoskeleton** on the '
          '**outside**, like a suit of armour. Others, like earthworms and jellyfish, are soft. More than nine out of ten kinds '
          'of animals are invertebrates!'),
        Pics([('honeybee', 'insect: 6 legs'), ('spider', 'spider: 8 legs'), ('crab', 'crustacean'), ('snail', 'mollusc'), ('worm', 'worm')], cols=5, size='14mm', small=True),
        H('Skeletons inside us', 3),
        P('Your skeleton is a strong frame of more than 200 **bones**. It **supports** your body, **protects** soft parts '
          '(your skull protects your brain, your ribs protect your heart and lungs) and helps you **move**. **Muscles** pull on '
          'bones to move them. Muscles can only pull, so they work in pairs: one pulls the bone one way, the other pulls it back.'),
        Fig(art.skeleton(labels=art.SKELETON_PARTS), 'The human skeleton.', width='80%'),
        Box('fact', P('Sharks have no bones at all! Their skeleton is made of **cartilage**, the same bendy material as the tip of your nose.')),
        H('Branching keys', 3),
        P('A **key** helps you name a living thing by answering yes/no questions about what you can see. Start at the top and '
          'follow the answers down the branches until you reach a name.'),
        Fig(art4.key_tree(KEY), 'A branching key for some small animals.', span=True, width='86%'),
        H('Adaptation', 3),
        P('An **adaptation** is a feature that helps an animal **survive** in its habitat. The tiger\'s stripes hide it in tall '
          'grass. The Ganges river dolphin is almost blind, so it "sees" with sound (echoes) in the muddy water. Fishing cats '
          'have webbed toes for swimming. Birds\' beaks are shaped for their food: a kingfisher\'s long sharp beak catches fish, '
          'a parrot\'s strong curved beak cracks seeds.'),
        H('Migration', 3),
        P('**Migration** is when animals travel from one place to another, usually at the same time each year, to find food, '
          'warmth or a safe place to breed. Every winter, ducks and waders fly thousands of kilometres from cold lands like '
          'Siberia to the **haors** and **beels** (wetlands) of Bangladesh. Hilsa fish swim from the sea up our rivers to lay eggs.'),
        Fig(art4.migration_map(), 'Winter visitors.'),
        H('When habitats change', 3),
        P('Natural changes, such as **floods**, **droughts**, **cyclones** and rivers changing course, can change a habitat. '
          'Some animals move away or die, while others find new homes. If a habitat changes too fast, a kind of animal may '
          'disappear from an area for ever. When the last one dies everywhere, it is **extinct**, like the dodo.'),
        Box('bd', P('Some animals that once lived in Bangladesh are now gone from here, such as the Indian rhinoceros and the wild '
                    'water buffalo. The Royal Bengal tiger, the national animal, is protected in the Sundarbans.')),
    ),
    Vocab([('biodiversity', 'the variety of living things in a place'), ('vertebrate', 'an animal with a backbone'),
           ('invertebrate', 'an animal without a backbone'), ('exoskeleton', 'a hard covering on the outside of an animal'),
           ('adaptation', 'a feature that helps a living thing survive'), ('key', 'yes/no questions that help you name a living thing'),
           ('migration', 'travelling to another place at the same time each year'), ('habitat', 'the place where a living thing lives')]),
])

facts = Sheet('facts', 'Sorting animals', level=1, goals=['Sort animals by where they live.', 'Name vertebrate groups.', 'Use a key.'], blocks=[
    Q('Where does each animal live? Write **aerial**, **arboreal**, **aquatic**, **terrestrial** or **fossorial**.',
      Pics([('eagle', Ans('aerial')), ('monkey', Ans('arboreal')), ('dolphin', Ans('aquatic')), ('elephant', Ans('terrestrial')), ('worm', Ans('fossorial'))],
           cols=5, size='15mm'), marks=5),
    Q('Sort the animals.',
      Sort(['Vertebrate (backbone)', 'Invertebrate (no backbone)'], [
          ('tiger', 'Vertebrate (backbone)'), ('hilsa fish', 'Vertebrate (backbone)'), ('frog', 'Vertebrate (backbone)'), ('kingfisher', 'Vertebrate (backbone)'),
          ('spider', 'Invertebrate (no backbone)'), ('crab', 'Invertebrate (no backbone)'), ('earthworm', 'Invertebrate (no backbone)'), ('butterfly', 'Invertebrate (no backbone)')]), marks=8),
    Q('Match each animal to its vertebrate group.',
      Match([('crocodile', 'reptile'), ('toad', 'amphibian'), ('bat', 'mammal'), ('owl', 'bird'), ('shark', 'fish')]), marks=5),
    Q('Use the key on the Learn it page. Which animal has legs, but not more than 6 legs, and has wings?', Lines(1, 'the bee'), marks=1),
    Q('Fill in the gaps.',
      Blanks('Your skeleton [supports] your body. Your skull [protects] your brain. [Muscles] pull on bones to make them move. '
             'Animals that travel to another place every year [migrate].', extra=['pushes', 'eats']), marks=4),
])

think = Sheet('think', 'Adapted to survive', level=2, goals=['Explain adaptations.', 'Make your own key.'], blocks=[
    Q('Explain how each feature helps the animal survive.',
      Table(['Animal and feature', 'How it helps'], [
          ['tiger: striped coat', Ans('hides it in tall grass so it can creep up on prey')],
          ['river dolphin: uses echoes', Ans('finds fish in muddy water where it cannot see')],
          ['duck: webbed feet', Ans('pushes against the water to swim')],
          ['camel: wide feet', Ans('stops it sinking into soft sand')]], widths=['38%', '62%']), marks=4),
    Q('Look at the birds\' beaks. Match each beak to its food: **fish**, **seeds and nuts**, **nectar in flowers**, **meat**.',
      Table(['Beak', 'Food'], [['long and sharp like a spear (kingfisher)', Ans('fish')], ['short, strong and curved (parrot)', Ans('seeds and nuts')],
                               ['long and thin like a straw (sunbird)', Ans('nectar in flowers')], ['sharp and hooked (eagle)', Ans('meat')]], widths=['62%', '38%']), marks=4),
    Q('Make a branching key to sort these four animals: **fish**, **bird**, **snake**, **cow**. Write a yes/no question in each box.',
      Draw('52mm', 'My key', 'e.g. Does it have legs? Yes: Does it have feathers? (bird / cow). No: Does it live in water and have fins? (fish / snake).'), marks=4),
    Q('Why do ducks fly to Bangladesh in winter, and why do they fly back in spring?',
      Lines(3, 'In winter the lakes in the north freeze and there is no food, so they come to our warmer wetlands. In spring they fly back north to breed where there is plenty of food and space.'), marks=2),
])

investigate = Sheet('investigate', 'Minibeast hunt in the school garden', level=2, goals=['Record observations in a tally chart.', 'Draw a bar chart.', 'Make conclusions.'], blocks=[
    P('Class 4B searched two places in the school garden for 10 minutes each: under a pile of damp leaves and on a sunny path. '
      'They counted the minibeasts (small invertebrates) they found.'),
    Q('Complete the totals.',
      Table(['Minibeast', 'Under damp leaves', 'On the sunny path'], [
          ['earthworms', 'IIII I', 'I'], ['woodlice', 'IIII IIII', '0'], ['ants', 'III', 'IIII IIII II'], ['snails', 'IIII', '0'],
          ['Total', Ans('24'), Ans('13')]], center=True), marks=2),
    Q('Draw a bar chart for the damp leaves.',
      Graph(['earthworms', 'woodlice', 'ants', 'snails'], [6, 9, 3, 4], 'Number found', 'Minibeast (under damp leaves)', ymax=10, step=1, width=120, height=56), marks=3),
    Q('Which place had more kinds of minibeasts? Suggest why.',
      Lines(2, 'Under the damp leaves (4 kinds). It is damp, dark and cool, with dead leaves to eat and places to hide.'), marks=2),
    Q('Was the test fair? Name one thing they kept the same.', Lines(1, 'Yes: the same time (10 minutes) in each place.'), marks=1),
    Q('How should they look after the minibeasts?', Lines(2, 'Handle them gently, keep them damp and shady, and put them back where they were found.'), marks=1),
])

case = Sheet('case', 'Winter visitors: the birds of Tanguar Haor', level=3, goals=['Read about a real wetland.', 'Use data about bird numbers.', 'Suggest ways to protect migrating birds.'], blocks=[
    Links('Science', 'Geography', 'Maths', 'Citizenship'),
    Case('**Tanguar Haor** in Sunamganj is a huge wetland of lakes, marshes and swamp forest. In winter, when the water '
         'goes down, it becomes home to tens of thousands of **migratory birds**: ducks, geese, cranes and waders that fly from '
         'Siberia, Mongolia and the Himalayas. Because it is so important, it is a protected **Ramsar site** (a wetland of '
         'international importance).',
         'Every year, bird scientists and volunteers count the birds. The counts show how healthy the wetland is. The birds face '
         'dangers: some people hunt them or catch them with poison bait, fishing nets can trap them, and too many boats '
         'disturb them. Local people, the government and nature groups work together to protect the haor.',
         source='Based on information about Tanguar Haor and the Asian Waterbird Census. Counts below are example data.'),
    Q('A bird count at a wetland (example data).',
      Table(['Year', '2019', '2020', '2021', '2022', '2023'], [['Birds counted (thousands)', '50', '45', '60', '38', '52']], center=True),
      Graph(['2019', '2020', '2021', '2022', '2023'], [50, 45, 60, 38, 52], 'Birds (thousands)', 'Year', ymax=70, step=10, width=120, height=52),
      Part('Draw the bar chart.'),
      Part('Which year had the most birds? Which had the fewest?', Lines(1, 'most: 2021 (60 000); fewest: 2022 (38 000)')), marks=3),
    Q('Why do scientists count the birds every year?', Lines(2, 'To see if the number is going up or down, which shows whether the wetland is healthy and if the birds need more protection.'), marks=2),
    Q('What could each person do to help the birds?',
      Table(['Person', 'Action'], [['a fisher', Ans('use nets that do not trap birds; do not fish in bird areas')], ['a tourist', Ans('stay far from the birds, keep quiet, take litter home')],
                                   ['a learner like you', Ans('make posters, never buy or eat wild birds, tell others')]], widths=['30%', '70%']), marks=3),
    Q('Design a poster to protect winter visitors. Include a drawing and a short message.', Draw('40mm', 'My poster', 'e.g. a duck with "Welcome, winter guests! Do not hunt or poison our birds."'), marks=2),
])

review = Sheet('review', 'Show what you know', level=3, goals=['Use key vocabulary.', 'Answer test-style questions.'], blocks=[
    Q('Find the key words.', WordSearch(['HABITAT', 'BACKBONE', 'MAMMAL', 'REPTILE', 'INSECT', 'KEY', 'MIGRATE', 'SKELETON', 'ADAPT'], size=11, seed=401)),
    Q('Which animal is an invertebrate?', MCQ(['frog', 'snake', 'crab', 'bat'], 2), marks=1),
    Q('A **fossorial** animal lives…', MCQ(['in trees', 'under the ground', 'in the air', 'in water'], 1), marks=1),
    Q('Write the job of each part of the skeleton.',
      Table(['Part', 'Job'], [['skull', Ans('protects the brain')], ['ribs', Ans('protect the heart and lungs')], ['backbone (spine)', Ans('supports the body and protects the spinal cord')]], widths=['34%', '66%']), marks=3),
    Q('**Challenge.** A new road is built through a forest. Explain how this could change the biodiversity of the forest.',
      Lines(3, 'Trees are cut down, so animals lose food and shelter; the road splits the habitat and animals may be hit by cars; some kinds may move away or die out, so there are fewer kinds of animals.'), marks=2),
])

TOPIC = Topic(
    code='A1', strand='living', title='Animals of Bangladesh: Diversity and Classification', short='Animal diversity',
    subtitle='Where animals live, vertebrates and invertebrates, skeletons, keys, adaptation and migration',
    outcomes=[
        'observe the diversity of animals in different ecosystems of Bangladesh — aerial, arboreal, aquatic, terrestrial and fossorial.',
        'discuss adaptations as physical differences in local animal species that enable them to survive in their ecosystem.',
        'construct and use simple dichotomous keys to classify different local animal species.',
        'discuss migration as the movement of animals from one ecosystem to another, how this contributes to the diversity of animals found in local ecosystems, and why it occurs.',
        'discuss different natural changes to the ecosystem that can affect the diversity of local animal species.',
    ],
    cambridge=['Unit 1 Humans and animals (1.1–1.4 Skeletons)', 'Unit 2 Living things and environments (2.1, 2.3–2.5)'],
    sheets=[learn, facts, think, investigate, case, review],
    selfcheck=['name where animals live: aerial, arboreal, aquatic, terrestrial, fossorial', 'sort animals into vertebrates and invertebrates',
               'name the five vertebrate groups', 'use and make a branching key', 'explain adaptation and migration with examples',
               'explain how we can protect migrating birds'],
    cover_art=art4.habitats_strip(),
)
