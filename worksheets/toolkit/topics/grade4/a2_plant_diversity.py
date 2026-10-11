from build import Sheet, Topic
from ws import (P, H, Box, Vocab, Fig, Cols, Row, Case, Links, Lines, Blanks, Match, TrueFalse, MCQ, Order, Table,
                Ans, Sort, Label, Draw, Graph, WordSearch, Q, Part, Bullets, Pics)
import art
import art4

learn = Sheet('learn', 'Plants of Bangladesh and how they survive', level=1, goals=[
    'Tell the difference between flowering and non-flowering plants.',
    'Describe adaptations of plants in different habitats of Bangladesh.',
    'Explain how natural changes can affect plants.',
], blocks=[
    P('From the giant banyan tree in the village to the tiny duckweed floating on a pond, Bangladesh is green with plants. '
      'Plants give us food, wood, medicine, cloth and the oxygen we breathe. Every animal depends on them. Let\'s find out '
      'how many kinds there are, and how each one is suited to its home.', 'lead'),
    Cols(
        H('Flowering plants', 3),
        P('Most plants you know are **flowering plants**. They grow flowers, which make **seeds**, often inside a **fruit**. '
          'Rice, mango trees, lotus, sunflowers, grass and the shapla (water lily, our national flower) are all flowering plants. '
          'Even grass and rice have flowers, but they are small and green.'),
        Pics([('rice plant', 'rice'), ('lotus', 'lotus'), ('mango', 'mango tree'), ('sunflower', 'sunflower')], cols=4, size='14mm', small=True),
        H('Non-flowering plants', 3),
        P('Some plants never make flowers. **Ferns** and **mosses** grow from tiny **spores** instead of seeds. Mosses grow in '
          'damp, shady places like the walls of old buildings. **Conifers**, such as pine trees, make seeds inside **cones**, '
          'not flowers.'),
        Fig(art4.fern_moss(), 'Ferns and mosses make spores.', width='92%'),
        Box('fact', P('**Mushrooms are not plants!** They belong to a different group called **fungi**. They cannot make '
                      'their own food from sunlight.')),
        H('Adapted to their homes', 3),
        P('An **adaptation** is a feature that helps a plant survive where it lives. Bangladesh has many different habitats, '
          'and the plants in each one are adapted in different ways.'),
        H('Mangroves: living in salty mud', 3),
        P('In the **Sundarbans**, the tide covers the ground with salty water twice a day. The mud has very little air. '
          'Mangrove trees such as the **sundari** (which gives the forest its name) have **breathing roots** that poke up out '
          'of the mud like pencils to take in air. Some have **prop roots** that hold the tree steady in soft mud. Their leaves '
          'can get rid of extra salt.'),
        Fig(art4.mangrove(), 'A mangrove tree.', width='92%'),
        H('Floating plants', 3),
        P('**Water hyacinth** floats because its leaf stalks are swollen and spongy, full of air, like a float. Its roots hang '
          'down to take in minerals from the water. The **lotus** has a waxy leaf that water rolls off, and long hollow stems '
          'that carry air down to its roots in the mud.'),
        Fig(art4.water_hyacinth(), 'Water hyacinth.', width='86%'),
        H('Dry and windy places', 3),
        P('A **cactus** stores water in its thick stem and has **spines** instead of leaves, so it loses very little water. '
          'Coconut and palm trees on the coast have bendy trunks and long, split leaves, so storms do not snap them.'),
        H('Natural changes', 3),
        P('**Floods** can drown plants or bring rich new soil. **Droughts** dry them out. **Cyclones** blow trees down, and salty '
          'sea water pushed inland by storm surges can kill crops. Some plants survive; others die and new kinds may take '
          'their place. Over time the mix of plants in a place can change.'),
        Box('bd', P('After Cyclone Sidr in 2007, about a quarter of the Sundarbans was badly damaged, but the mangroves grew back over the '
                    'following years. The Sundarbans also protects villages behind it by slowing the wind and waves.')),
        Box('try', P('Look for moss on a damp wall or tree trunk near your home. Use a hand lens to find the tiny capsules on stalks '
                     'that hold the spores.')),
    ),
    Vocab([('flowering plant', 'a plant that makes flowers and seeds'), ('non-flowering plant', 'a plant with no flowers, such as a fern or moss'),
           ('spore', 'a tiny cell that can grow into a new fern or moss'), ('cone', 'the part of a pine tree that holds its seeds'),
           ('mangrove', 'a tree that grows in salty mud on the coast'), ('breathing roots', 'roots that grow up out of the mud to take in air'),
           ('adaptation', 'a feature that helps a living thing survive'), ('fungi', 'mushrooms and moulds: not plants')]),
])

facts = Sheet('facts', 'Plant groups and adaptations', level=1, goals=['Sort plants into groups.', 'Match adaptations to habitats.'], blocks=[
    Q('Sort these living things.',
      Sort(['Flowering plant', 'Non-flowering plant', 'Not a plant'], [
          ('rice', 'Flowering plant'), ('mango tree', 'Flowering plant'), ('lotus', 'Flowering plant'),
          ('fern', 'Non-flowering plant'), ('moss', 'Non-flowering plant'), ('pine tree', 'Non-flowering plant'),
          ('mushroom', 'Not a plant'), ('mould on bread', 'Not a plant')]), marks=8),
    Q('Match the plant to its adaptation.',
      Match([('mangrove', 'breathing roots that stick up out of salty mud'), ('water hyacinth', 'spongy stalks full of air to float'),
             ('cactus', 'thick stem stores water; spines instead of leaves'), ('lotus', 'waxy leaves that water rolls off'),
             ('coconut palm', 'bendy trunk that does not snap in storms')]), marks=5),
    Q('Which of these living things is not a plant?', Pics([('rice plant', None), ('mushroom', None), ('cactus', None), ('herb', None)], cols=4, size='13mm', letters=True),
      MCQ(['A', 'B', 'C', 'D'], 1), marks=1),
    Q('True or false?', TrueFalse([
        ('Ferns grow from spores.', True),
        ('Rice plants do not have flowers.', False, 'Rice has small green flowers.'),
        ('Mangrove trees live in salty water.', True),
        ('A cyclone can bring salty water onto farmland.', True)]), marks=4),
])

think = Sheet('think', 'Why plants look the way they do', level=2, goals=['Explain adaptations.', 'Predict the effects of change.'], blocks=[
    Q('Look at the mangrove.', Fig(art4.mangrove(labels=False), width='58%'),
      Part('Why does the mangrove need roots that grow **up** out of the mud?', Lines(2, 'The wet salty mud has very little air, so the roots grow up into the air to breathe.')),
      Part('How do prop roots help in a cyclone?', Lines(2, 'They spread out like legs and hold the tree firmly in the soft mud, so the wind does not knock it over.')), marks=4),
    Q('Tisha says, "A cactus would grow well in the Sundarbans." Do you agree? Explain.',
      Lines(3, 'No. A cactus is adapted to dry places; in the wet, salty, muddy Sundarbans its roots would rot and it could not survive.'), marks=2),
    Q('A farmer\'s field near the coast is flooded by salty sea water after a storm. Predict what will happen to the rice and explain.',
      Lines(3, 'The rice will probably die or grow badly, because rice is not adapted to salty water; salt stops the roots taking in water.'), marks=2),
    Q('Design a plant that could live on a sunny, windy sand bank in a river (a **char**). Draw it and label two adaptations.',
      Draw('46mm', 'My plant', 'e.g. long roots to reach water and hold the sand; small waxy leaves to save water; bendy stem for wind.'), marks=3),
])

investigate = Sheet('investigate', 'Does a waxy coat stop leaves drying out?', level=2, goals=['Carry out a fair test.', 'Measure mass.', 'Explain results using adaptation.'], blocks=[
    P('Many leaves have a **waxy** coat. Class 4A made model leaves from wet paper towels. They rubbed petroleum jelly '
      '(like wax) on some and left others plain. They weighed them, left them in the sun, and weighed them again after 3 hours.'),
    Q('Complete the plan.',
      Table(None, [['Question', Ans('Does a waxy coat stop a leaf losing water?')], ['Change', Ans('wax on the paper towel or no wax')],
                   ['Measure', Ans('mass of water lost (g)')], ['Keep the same', Ans('size of paper towel, amount of water, time, place in the sun')]],
            widths=['26%', '74%']), marks=4),
    Q('Here are the results.',
      Table(['Model leaf', 'Mass at start (g)', 'Mass after 3 hours (g)', 'Water lost (g)'], [
          ['plain 1', '20', '8', Ans('12')], ['plain 2', '20', '9', Ans('11')], ['waxy 1', '20', '17', Ans('3')], ['waxy 2', '20', '18', Ans('2')]], center=True),
      Part('Work out the water lost for each model leaf.'),
      Part('Which leaves lost less water?', Lines(1, 'the waxy ones')), marks=5),
    Q('Write a conclusion.', Lines(2, 'A waxy coat stops leaves losing so much water, so it helps plants survive in dry or sunny places.'), marks=2),
    Q('Why did they test two of each kind of model leaf?', Lines(2, 'To check the results; if both are similar the results are more reliable.'), marks=1),
])

case = Sheet('case', 'Water hyacinth: a problem or a gift?', level=3, goals=['Weigh up good and bad effects.', 'Link science to jobs and design.', 'Give a reasoned opinion.'], blocks=[
    Links('Science', 'Economics', 'Design', 'Environment'),
    Case('**Water hyacinth** (*kochuripana*) came from South America more than a hundred years ago. It grows very fast in '
         'warm, still water. It can double in size in about two weeks, covering ponds, canals and rivers like a green carpet.',
         'This causes problems. Boats get stuck, fish have less light and air, and mosquitoes can breed in the still water '
         'underneath. But people in Bangladesh have found clever uses for it. Farmers pile it up to make **floating gardens** '
         '(*dhap*) to grow vegetables during floods. It is used as **compost** and cattle food, and craft workers weave the '
         'dried stems into baskets, mats and furniture that are sold around the world.',
         source='Based on information about water hyacinth and floating gardens in Bangladesh.'),
    Q('Sort the effects.',
      Sort(['Good for people', 'Bad for people or nature'], [
          ('floating gardens', 'Good for people'), ('baskets and mats', 'Good for people'), ('compost for fields', 'Good for people'),
          ('blocks boats', 'Bad for people or nature'), ('less light for fish', 'Bad for people or nature'), ('mosquitoes breed', 'Bad for people or nature')]), marks=6),
    Q('Which adaptation helps water hyacinth to cover a pond so fast?', Lines(2, 'It floats on spongy stalks full of air and grows and spreads very quickly in warm water.'), marks=2),
    Q('**Maths.** A patch of water hyacinth covers 1 square metre. It doubles every 2 weeks. How much will it cover after 8 weeks?',
      Table(['Weeks', '0', '2', '4', '6', '8'], [['Area (square metres)', '1', Ans('2'), Ans('4'), Ans('8'), Ans('16')]], center=True), marks=2),
    Q('Your opinion: Is water hyacinth a problem or a gift? Give reasons for both sides, then decide.',
      Lines(4, 'It is a problem because it blocks rivers and harms fish, but a gift because people make gardens, compost and crafts from it. Best answer: it is useful if people harvest it and stop it spreading.'), marks=3),
])

review = Sheet('review', 'Show what you know', level=3, goals=['Use key vocabulary.', 'Answer test-style questions.'], blocks=[
    Q('Find the key words.', WordSearch(['FERN', 'MOSS', 'SPORE', 'SEED', 'FLOWER', 'MANGROVE', 'ROOTS', 'CACTUS', 'ADAPT'], size=11, seed=402)),
    Q('Which plant makes spores instead of seeds?', MCQ(['rice', 'fern', 'mango tree', 'lotus'], 1), marks=1),
    Q('Why does water hyacinth float?', MCQ(['its roots are heavy', 'its stalks are full of air', 'it has no leaves', 'it is a fungus'], 1, one_col=True), marks=1),
    Q('Draw and label a plant from a dry place and a plant from a wet place. Show one adaptation on each.',
      Row([Draw('36mm', 'dry place', 'cactus: thick stem stores water, spines')], [Draw('36mm', 'wet place', 'lotus: waxy floating leaves or mangrove: breathing roots')]), marks=4),
    Q('**Challenge.** The sea level is rising and more salty water is reaching farms in the south of Bangladesh. How could scientists help farmers?',
      Lines(3, 'They can breed rice that can grow in salty water (salt-tolerant rice), suggest crops that like salt, or build embankments to keep the sea water out.'), marks=2),
])

TOPIC = Topic(
    code='A2', strand='living', title='Plants of Bangladesh: Diversity and Adaptation', short='Plant diversity',
    subtitle='Flowering and non-flowering plants, mangroves and floating plants, and how natural changes affect plants',
    outcomes=[
        'observe plant diversity, both flowering and non-flowering, in different ecosystems of Bangladesh.',
        'discuss adaptations as physical differences in local plant species that enable them to survive in their ecosystem.',
        'discuss different natural changes to the ecosystem that can affect the diversity of local plant species.',
    ],
    sheets=[learn, facts, think, investigate, case, review],
    selfcheck=['tell flowering and non-flowering plants apart', 'explain that mushrooms are fungi, not plants',
               'describe how mangroves and floating plants are adapted', 'investigate how a waxy coat saves water',
               'explain how floods, droughts and cyclones change plant life', 'weigh up the good and bad effects of water hyacinth'],
    cover_art=art4.mangrove(),
)
