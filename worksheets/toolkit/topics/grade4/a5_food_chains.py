from build import Sheet, Topic
from ws import (P, H, Box, Vocab, Fig, Cols, Row, Case, Links, Lines, Blanks, Match, TrueFalse, MCQ, Order, Table,
                Ans, Sort, Label, Draw, Graph, WordSearch, Q, Part, Bullets, Pics)
import art
import art4

learn = Sheet('learn', 'Food chains and food webs', level=1, goals=[
    'Show feeding relationships as food chains, in words and diagrams.',
    'Use the words producer, consumer, predator and prey.',
    'Build food webs and predict what happens when a living thing is removed.',
], blocks=[
    P('What did you eat today? Perhaps rice, dal and fish. The rice grew using light from the Sun. The fish ate tiny plants '
      'in the water. So, in a way, your lunch came from the Sun! Every living thing needs **energy** from food, and food '
      'chains show how that energy passes from one living thing to the next.', 'lead'),
    Fig(art4.food_chain([('herb', 'grass'), ('deer', 'spotted deer'), ('tiger', 'tiger')], roles=['producer', 'consumer (prey)', 'consumer (predator)']),
        'A Sundarbans food chain. The arrow means "is eaten by" and shows the way the energy goes.', width='72%'),
    Cols(
        H('Producers', 3),
        P('Every food chain begins with a **plant**. Plants are **producers**: they **make their own food** using energy from '
          '**sunlight**, plus water and air. Grass, rice, mangrove leaves and the tiny green **algae** in ponds are producers.'),
        H('Consumers', 3),
        P('Animals cannot make their own food. They are **consumers**: they get energy by eating plants or other animals.'),
        Bullets(['**Herbivores** eat only plants (deer, cows, caterpillars).',
                 '**Carnivores** eat only animals (tigers, kingfishers).',
                 '**Omnivores** eat plants and animals (monkeys, crows, people).']),
        H('Predators and prey', 3),
        P('A **predator** hunts and eats other animals. The animal that is eaten is the **prey**. In the chain above, the tiger is '
          'the predator and the deer is its prey. An animal can be both: a frog is a predator of grasshoppers but prey for a snake.'),
        H('Reading and writing food chains', 3),
        P('Always start with the producer and draw the arrows **towards the eater**:'),
        P('**rice plant → grasshopper → frog → snake → eagle**'),
        Box('tip', P('The arrow does **not** mean "eats". It means "**is eaten by**" or "gives energy to". It points from the food to the animal that eats it.')),
        H('Food webs', 3),
        P('Most animals eat more than one kind of food, and are eaten by more than one predator. When we join many food chains '
          'together we get a **food web**. A food web shows all the feeding relationships in a habitat.'),
        Fig(art4.food_web_pics(), 'A Sundarbans food web.', span=True, width='80%'),
        H('What if one is removed?', 3),
        P('Everything in a food web is connected. If one living thing is removed or dies out, others are affected:'),
        Bullets(['Its **predators** have less food. They may go hungry, move away or eat more of something else.',
                 'Its **prey** may increase, because fewer of them are being eaten.',
                 'Then the prey may eat too much of **their** food, and so on through the web.']),
        Box('bd', P('In the Sundarbans, if too many spotted deer are hunted by people, tigers have less food. Hungry tigers may then '
                    'come closer to villages looking for goats and cows. Protecting the deer also helps protect people and tigers.')),
        Box('try', P('Write a food chain for your dinner tonight. Start with the producer. For example: grass → cow → milk → me!')),
    ),
    Vocab([('food chain', 'shows what eats what, starting with a plant'), ('producer', 'a plant that makes its own food using sunlight'),
           ('consumer', 'an animal that eats other living things'), ('predator', 'an animal that hunts other animals'),
           ('prey', 'an animal that is hunted and eaten'), ('herbivore', 'eats only plants'), ('carnivore', 'eats only animals'),
           ('food web', 'many food chains joined together')]),
])

facts = Sheet('facts', 'Who eats whom?', level=1, goals=['Build food chains.', 'Use food chain vocabulary.'], blocks=[
    Q('Put the living things in order to make a food chain. Draw the arrows.',
      Pics([('snake', 'snake'), ('rice plant', 'rice plant'), ('eagle', 'eagle'), ('cricket', 'grasshopper'), ('frog', 'frog')], cols=5, size='14mm'),
      Lines(1, 'rice plant → grasshopper → frog → snake → eagle'), marks=3),
    Q('Use the food chain in question 1.',
      Table(['Question', 'Answer'], [['Which is the producer?', Ans('rice plant')], ['Which is a herbivore?', Ans('grasshopper')],
                                     ['Name a predator and its prey.', Ans('frog (predator) and grasshopper (prey)')], ['Where does the energy come from first?', Ans('the Sun')]], widths=['55%', '45%']), marks=4),
    Q('Sort the animals.',
      Sort(['Herbivore', 'Carnivore', 'Omnivore'], [('cow', 'Herbivore'), ('deer', 'Herbivore'), ('caterpillar', 'Herbivore'),
                                                    ('tiger', 'Carnivore'), ('kingfisher', 'Carnivore'), ('crocodile', 'Carnivore'),
                                                    ('crow', 'Omnivore'), ('monkey', 'Omnivore'), ('person', 'Omnivore')]), marks=9),
    Q('True or false?', TrueFalse([
        ('Every food chain starts with a plant.', True),
        ('The arrow in a food chain points to the food.', False, 'The arrow points from the food to the animal that eats it.'),
        ('An animal can be both a predator and prey.', True)]), marks=3),
])

think = Sheet('think', 'Exploring a food web', level=2, goals=['Read a food web.', 'Predict effects of removing a living thing.'], blocks=[
    Q('Look at the Sundarbans food web.', Fig(art4.food_web_pics(), width='70%'),
      Part('Write two food chains from the web.', Lines(2, 'mangrove leaves → spotted deer → tiger; algae → fish → crocodile (or algae → crab → kingfisher)')),
      Part('Name an animal that eats more than one kind of food.', Lines(1, 'tiger (deer and monkeys) or kingfisher (crabs and fish) or crab')),
      Part('What would happen to the kingfishers if all the fish died? Explain.', Lines(2, 'They would have less food; they would eat more crabs, so crab numbers might fall, or some kingfishers might leave or die.')),
      Part('What would happen to the crabs if all the kingfishers died?', Lines(2, 'There might be more crabs because fewer are being eaten.')), marks=7),
    Q('Why do almost all food chains begin with a green plant?', Lines(2, 'Only plants can make their own food using energy from sunlight; all the energy in the chain starts there.'), marks=2),
])

investigate = Sheet('investigate', 'Counting a rice field food chain', level=2, goals=['Record and present survey data.', 'Spot a pattern.', 'Explain the pattern.'], blocks=[
    P('Scientists counted the living things in one small part of a rice field (example data).'),
    Q('Draw a bar chart.',
      Table(['Living thing', 'rice plants', 'grasshoppers', 'frogs', 'snakes'], [['Number counted', '400', '60', '8', '1']], center=True),
      Graph(['rice plants', 'grasshoppers', 'frogs', 'snakes'], [400, 60, 8, 1], 'Number counted', 'Living thing', ymax=400, step=50, width=120, height=54), marks=3),
    Q('Describe the pattern as you go along the food chain.', Lines(2, 'There are fewer and fewer living things at each step of the food chain.'), marks=2),
    Q('Suggest why there are so few snakes.', Lines(2, 'Each snake needs to eat many frogs to get enough energy, so the field can only feed a few snakes.'), marks=2),
    Q('Farmers sprayed a poison that killed most of the frogs. Predict what would happen to:',
      Part('the grasshoppers', Lines(1, 'They would increase because fewer are eaten.')),
      Part('the rice plants', Lines(1, 'They would be damaged because more grasshoppers eat them.')),
      Part('the snakes', Lines(1, 'They would go hungry and their numbers would fall.')), marks=3),
])

case = Sheet('case', 'When the vultures disappeared', level=3, goals=['Use a real food web problem.', 'Interpret data about a falling population.', 'Evaluate solutions.'], blocks=[
    Links('Science', 'Health', 'Maths', 'Citizenship'),
    Case('**Vultures** are large birds that eat the bodies of dead animals. They are nature\'s cleaners: a group of vultures can '
         'clean a dead cow in less than an hour, stopping germs from spreading.',
         'Since the 1990s, the number of vultures in South Asia has fallen by **more than 95 out of every 100**. Scientists found '
         'the cause: a medicine called **diclofenac** that was given to sick cattle. When a treated cow died and vultures ate it, '
         'the medicine poisoned the vultures.',
         'With fewer vultures, dead animals lay rotting for longer. More stray dogs and rats came to eat them, and diseases can '
         'spread more easily. Bangladesh **banned diclofenac** for animals in 2010 and set up **Vulture Safe Zones** in 2014, '
         'where vultures are fed safe food and the medicines are checked.',
         source='Based on research by vulture conservation groups (e.g. IUCN Bangladesh, SAVE). Numbers below are example data.'),
    Q('Vultures counted at one site (example data).',
      Table(['Year', '1990', '2000', '2010', '2020'], [['Vultures', '200', '40', '10', '25']], center=True),
      Graph(['1990', '2000', '2010', '2020'], [200, 40, 10, 25], 'Number of vultures', 'Year', ymax=200, step=20, width=110, height=50),
      Part('Draw the bar chart.'),
      Part('What happened after 2010? Suggest why.', Lines(2, 'The number went up a little, because diclofenac was banned and safe zones were made.')), marks=3),
    Q('Complete the chain of effects.',
      Order(['farmers give sick cattle diclofenac', 'vultures eat dead cattle and are poisoned', 'fewer vultures', 'dead animals rot for longer',
             'more stray dogs and rats, and more disease']), marks=3),
    Q('Who can help vultures? Suggest one action for each.',
      Table(['Person', 'Action'], [['a vet', Ans('use safe medicines such as meloxicam, not diclofenac')], ['a farmer', Ans('leave dead cattle in safe places for vultures; use safe medicines')],
                                   ['a learner', Ans('tell others why vultures matter; make a poster')]], widths=['26%', '74%']), marks=3),
])

review = Sheet('review', 'Show what you know', level=3, goals=['Use key vocabulary.', 'Answer test-style questions.'], blocks=[
    Q('Find the key words.', WordSearch(['PRODUCER', 'CONSUMER', 'PREDATOR', 'PREY', 'CHAIN', 'WEB', 'ENERGY', 'PLANT', 'SUN'], size=10, seed=405)),
    Q('In the food chain **grass → goat → tiger**, which is the prey?', MCQ(['grass', 'goat', 'tiger', 'the Sun'], 1), marks=1),
    Q('What do all food chains start with?', MCQ(['a predator', 'a herbivore', 'a producer', 'a carnivore'], 2), marks=1),
    Q('Draw a food chain with four living things from a pond. Label the producer, a predator and its prey.',
      Draw('36mm', 'My pond food chain', 'e.g. algae → small fish → big fish → kingfisher; algae = producer; kingfisher = predator, big fish = prey.'), marks=3),
    Q('**Challenge.** Explain why protecting the producers is the most important way to protect a whole food web.',
      Lines(3, 'All the energy in a food web starts with the producers. Without them the herbivores starve, then the carnivores, so the whole web collapses.'), marks=2),
])

TOPIC = Topic(
    code='A5', strand='living', title='Food Chains and Food Webs', short='Food chains',
    subtitle='Producers and consumers, predators and prey, food webs and what happens when living things are removed',
    outcomes=[
        'know how food chains can be used to represent feeding relationships in a habitat, and present these in text and diagrams.',
        'know that food chains begin with a plant, the producer, which uses energy from the Sun.',
        'understand and use the terms producer, consumer, predator and prey.',
        'explore and construct food chains in a particular habitat.',
        'construct food webs to illustrate interactions based on food-getting activities among living things.',
        'predict the effects when living things are removed from, or die out of, a food web or food chain.',
    ],
    sheets=[learn, facts, think, investigate, case, review],
    selfcheck=['build a food chain with arrows the right way', 'use producer, consumer, predator and prey', 'sort herbivores, carnivores and omnivores',
               'read a food web', 'predict what happens when one living thing is removed', 'explain why vultures matter'],
    cover_art=art4.food_chain([('herb', 'grass'), ('deer', 'deer'), ('tiger', 'tiger')]),
)
