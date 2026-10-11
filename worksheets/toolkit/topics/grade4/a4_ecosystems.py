from build import Sheet, Topic
from ws import (P, H, Box, Vocab, Fig, Cols, Row, Case, Links, Lines, Blanks, Match, TrueFalse, MCQ, Order, Table,
                Ans, Sort, Label, Draw, Graph, WordSearch, Q, Part, Bullets, Pics)
import art
import art4

learn = Sheet('learn', 'Ecosystems: everything is connected', level=1, goals=[
    'Explain what an ecosystem is and sort its parts into living and non-living.',
    'Give examples of interactions in an ecosystem and explain them.',
    'Describe the levels from a single cell up to the whole biosphere.',
], blocks=[
    P('Sit quietly beside a village pond. Fish dart under the water, a frog sits on a lily pad, a duck dabbles for snails, '
      'and the Sun warms the water. All these things, living and non-living, work together. Together they make an '
      '**ecosystem**.', 'lead'),
    Fig(art4.pond_ecosystem(labels=art4.POND_PARTS), 'A pond ecosystem.', width='88%'),
    Cols(
        H('What is an ecosystem?', 3),
        P('An **ecosystem** is all the **living things** in a place together with the **non-living things** around them, and '
          'all the ways they affect each other. A pond, a rice field, a forest, a haor and even a rotting log are ecosystems.'),
        Table(['Living (biotic)', 'Non-living (abiotic)'], [['plants, animals, fungi, tiny microbes', 'sunlight, water, air, soil, rocks, temperature']]),
        P('How can you tell if something is living? Living things **move**, **grow**, **feed**, **breathe**, **get rid of waste**, '
          '**sense** things around them and **reproduce** (have young). Non-living things do not do all of these.'),
        H('Living things and non-living things', 3),
        Bullets(['Plants use **sunlight**, **water** and **air** to make their food.',
                 'Fish take in **oxygen** that is dissolved in the **water**.',
                 'Earthworms mix the **soil** and make it better for roots.',
                 'Trees give **shade**, which keeps the ground cooler and damper.']),
        H('Living things and other living things', 3),
        Bullets(['**Feeding:** a kingfisher eats fish; a cow eats grass.',
                 '**Competing:** two plants grow side by side and compete for light and water.',
                 '**Helping each other:** bees get nectar from flowers and carry pollen for them.',
                 '**Shelter:** birds nest in trees; crabs hide in mangrove roots.']),
        Box('think', P('Why do these interactions happen? Every living thing needs **food**, **water**, **shelter**, **light** '
                       '(for plants) and a place to **raise young**. Interactions are how they get them.')),
        H('From cells to the whole Earth', 3),
        P('Living things are made of tiny **cells**. Cells work together as **tissues**, tissues make **organs** (like the heart), '
          'and organs work together in **organ systems**. A whole living thing is an **organism**.'),
        P('Living things also form bigger groups: all the deer of one kind in a forest are a **population**; all the different '
          'populations living together are a **community**; the community plus the non-living things is an **ecosystem**; and '
          'all the ecosystems on Earth make the **biosphere**.'),
        Fig(art4.levels_big(), 'Bigger and bigger levels.', span=True, width='92%'),
        H('Ecosystems are systems', 3),
        P('A **system** is a group of parts that work together. If one part changes, the others change too. If a pond dries up, '
          'the fish die, the kingfishers must fly away, and the frogs cannot lay their eggs. Studying ecosystems as systems '
          'helps scientists predict what will happen when something changes.'),
        Box('bd', P('Bangladesh has many kinds of ecosystem: mangrove forest in the Sundarbans, hill forests in Chattogram, '
                    'haors and beels in the north-east, coral around Saint Martin\'s Island, rivers, rice fields and city parks.')),
        Box('try', P('Lift a stone or a log in a garden. Write a list of the living things and the non-living things you find. '
                     'Put it back gently afterwards!')),
    ),
    Vocab([('ecosystem', 'living and non-living things in a place, and how they affect each other'), ('interaction', 'when one thing affects another'),
           ('compete', 'try to get the same thing as another living thing'), ('population', 'all the living things of one kind in a place'),
           ('community', 'all the populations living together in a place'), ('biosphere', 'all the ecosystems on Earth'),
           ('organism', 'a whole living thing'), ('system', 'parts that work together')]),
])

facts = Sheet('facts', 'Parts of an ecosystem', level=1, goals=['Sort living and non-living parts.', 'Order the levels of life.'], blocks=[
    Q('Look at the pond. Write the name of each numbered part and say if it is living or non-living.',
      Fig(art4.pond_ecosystem(), width='76%'),
      Table(['Number', 'Name', 'Living or non-living?'], [[str(i + 1), Ans(n), Ans('living' if i in (2, 3, 6, 7) else 'non-living')] for i, n in enumerate(art4.POND_PARTS)], center=True), marks=8),
    Q('Put these levels in order, from smallest to biggest.',
      Order(['cell', 'tissue', 'organ', 'organism', 'population', 'community', 'ecosystem', 'biosphere']), marks=4),
    Q('Match each interaction to its type.',
      Match([('a heron eats a frog', 'feeding'), ('two trees grow towards the same patch of light', 'competing'),
             ('a bee carries pollen while it drinks nectar', 'helping each other'), ('a crab hides between mangrove roots', 'shelter')]), marks=4),
])

think = Sheet('think', 'When something changes', level=2, goals=['Explain interactions.', 'Predict the effects of change.'], blocks=[
    Q('Explain how each non-living thing helps the living things in a pond.',
      Table(['Non-living thing', 'How it helps'], [['sunlight', Ans('plants use it to make food; it warms the water')], ['water', Ans('fish live in it and take in oxygen from it; frogs lay eggs in it')],
                                                    ['mud at the bottom', Ans('roots of lotus grow in it; worms and snails live in it')]], widths=['30%', '70%']), marks=3),
    Q('A factory pours hot water into a pond. The water gets much warmer and holds less oxygen. Predict what happens to:',
      Part('the fish', Lines(1, 'Some fish die or swim away because there is not enough oxygen.')),
      Part('the kingfishers that eat the fish', Lines(1, 'They have less food, so they leave or have fewer young.')),
      Part('the people who fish in the pond', Lines(1, 'They catch fewer fish, so they have less food and money.')), marks=3),
    Q('Is a pond a system? Explain using the word **parts**.', Lines(2, 'Yes. Its parts (water, plants, fish, birds, sunlight) work together, and changing one part changes the others.'), marks=2),
    Q('Rafi found a dry seed. It does not move or grow. Is it living or non-living? Explain.',
      Lines(2, 'It is living (but resting). If it gets water and warmth it will germinate and grow.'), marks=2),
])

investigate = Sheet('investigate', 'Do snails prefer damp or dry places?', level=2, goals=['Use a choice chamber.', 'Record results over time.', 'Explain results using habitats.'], blocks=[
    P('Class 4D put 10 garden snails in the middle of a tray. One half of the tray had damp paper towel; the other half had '
      'dry paper towel. Every 5 minutes they counted the snails on each side. Then they put the snails back in the garden.'),
    Q('Here are the results.',
      Table(['Time (minutes)', '0', '5', '10', '15', '20'], [['Snails on the damp side', '0', '3', '6', '8', '9'], ['Snails on the dry side', '0', '2', '2', '1', '1']], center=True),
      Graph(['0', '5', '10', '15', '20'], [[0, 3, 6, 8, 9], [0, 2, 2, 1, 1]], 'Number of snails', 'Time (minutes)', ymax=10, step=1, kind='line',
            series_names=['damp side', 'dry side'], width=130, height=54),
      Part('Plot both lines on the graph.'),
      Part('Describe what happened.', Lines(2, 'More and more snails moved to the damp side; after 20 minutes 9 were on the damp side and only 1 on the dry side.')), marks=5),
    Q('Why do snails prefer damp places?', Lines(2, 'Their soft bodies dry out easily, so they need damp places; they also find food there.'), marks=2),
    Q('Why did they start with all the snails in the middle?', Lines(1, 'So the snails could choose either side fairly.'), marks=1),
    Q('How could they make the results more reliable?', Lines(1, 'Repeat with different snails, or use more snails.'), marks=1),
])

case = Sheet('case', 'Rice and fish: farming partners', level=3, goals=['Find interactions in a farm ecosystem.', 'Use data to compare farms.', 'Explain the benefits for people and nature.'], blocks=[
    Links('Science', 'Farming', 'Maths', 'Economics'),
    Case('In many parts of Bangladesh, farmers keep **fish in their rice fields**. This is called **rice-fish farming**. The field '
         'is flooded with water, the rice plants grow, and small fish swim between them.',
         'The rice and the fish help each other. The fish eat insects and weeds that would harm the rice, so the farmer uses less '
         '**pesticide**. Fish droppings act as **fertiliser** for the rice. The rice plants give the fish **shade** and shelter. '
         'At the end of the season the farmer harvests both rice and fish, which means more food and more money.',
         source='Based on research on integrated rice-fish farming in Bangladesh (WorldFish and the Bangladesh Rice Research Institute). Numbers below are example data.'),
    Q('Find the interactions in the rice-fish field.',
      Table(['Who helps?', 'How?'], [['fish help rice', Ans('eat insects and weeds; droppings are fertiliser')], ['rice helps fish', Ans('gives shade and shelter')],
                                     ['water helps both', Ans('the fish live in it; the rice roots need it')]], widths=['30%', '70%']), marks=3),
    Q('Two farms (example data).',
      Table(['Farm', 'Rice harvested (kg)', 'Fish harvested (kg)', 'Pesticide used (litres)'], [['rice only', '500', '0', '6'], ['rice and fish', '520', '60', '2']], center=True),
      Part('How much more rice did the rice-fish farm harvest?', Lines(1, '20 kg more')),
      Part('Why did the rice-fish farm use less pesticide?', Lines(1, 'The fish ate the insects and weeds.')), marks=3),
    Q('Why is using less pesticide good for the ecosystem?', Lines(2, 'Pesticides can kill helpful insects, fish and birds and pollute the water; less pesticide keeps the ecosystem healthy.'), marks=2),
    Q('Draw a diagram showing three interactions in a rice-fish field. Use arrows and labels.',
      Draw('44mm', 'Rice-fish field', 'e.g. fish → eats insects; fish droppings → feed rice; rice → shades fish; sun → rice.'), marks=3),
])

review = Sheet('review', 'Show what you know', level=3, goals=['Use key vocabulary.', 'Answer test-style questions.'], blocks=[
    Q('Find the key words.', WordSearch(['ECOSYSTEM', 'LIVING', 'WATER', 'SOIL', 'SUNLIGHT', 'COMMUNITY', 'SYSTEM', 'ORGAN', 'CELL'], size=11, seed=404)),
    Q('Which is a non-living part of an ecosystem?', MCQ(['frog', 'rock', 'grass', 'mushroom'], 1), marks=1),
    Q('All the hilsa fish in the Meghna river are a…', MCQ(['community', 'population', 'biosphere', 'organ'], 1), marks=1),
    Q('Draw an ecosystem near your home or school. Label two living and two non-living things, and draw one interaction arrow.',
      Draw('50mm', 'My ecosystem', 'Any ecosystem, e.g. school garden: tree, bird (living); soil, sunlight (non-living); arrow from bird to tree: nests in it.'), marks=4),
    Q('**Challenge.** Explain why scientists say "you cannot change just one thing in an ecosystem".',
      Lines(3, 'Everything is connected. Changing one part (for example, removing trees) changes the food, shelter, light and water for the other parts.'), marks=2),
])

TOPIC = Topic(
    code='A4', strand='living', title='Ecosystems and Interactions', short='Ecosystems',
    subtitle='Living and non-living parts, interactions, levels from cell to biosphere, and ecosystems as systems',
    outcomes=[
        'explain what an ecosystem is, identify its various components, and classify those components as living or non-living.',
        'give examples of interactions between the living and non-living components of an ecosystem, and suggest reasons for the interactions.',
        'give examples of interactions that occur among living things in an ecosystem, and suggest reasons for the interactions.',
        'understand that living things and non-living things are often organized into different levels — organelle, cells, tissues, organs, organ systems, organisms, populations, communities, ecosystem, biosphere.',
        'understand that interactions between and within systems enhance the understanding of connections in environments.',
        'understand that studying systems in nature helps us recognize how they work, and how the parts influence and interact with one another to perform a function.',
    ],
    cambridge=['Unit 2 Living things and environments (2.2 A habitat for snails)'],
    sheets=[learn, facts, think, investigate, case, review],
    selfcheck=['explain what an ecosystem is', 'sort living and non-living parts', 'give examples of interactions and explain them',
               'put the levels from cell to biosphere in order', 'investigate what conditions snails prefer', 'explain how rice and fish help each other'],
    cover_art=art4.pond_ecosystem(labels=art4.POND_PARTS),
)
