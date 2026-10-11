from build import Sheet, Topic
from ws import (P, H, Box, Vocab, Fig, Cols, Row, Case, Links, Lines, Blanks, Match, TrueFalse, MCQ, Order, Table,
                Ans, Sort, Label, Draw, Graph, WordSearch, Q, Part, Bullets, Pics)
import art
import art4

learn = Sheet('learn', 'Food chains: producers, consumers and decomposers', level=1, goals=[
    'Explain the jobs of producers, consumers and decomposers.',
    'Build food chains from what we observe.',
    'Predict what happens when one living thing changes.',
], blocks=[
    P('Every living thing needs food for energy. A **food chain** shows who eats whom. The arrows point from the food to the animal that eats it.', 'lead'),
    Fig(art4.food_chain([('herb', 'grass'), ('cricket', 'grasshopper'), ('frog', 'frog'), ('snake', 'snake')], roles=['producer', 'consumer', 'consumer', 'consumer']), 'A food chain in a rice field.', width='82%'),
    H('Producers', 3),
    P('**Producers** are green plants. They **make their own food** using **sunlight**, water and air. Every food chain starts with a producer.'),
    H('Consumers', 3),
    P('**Consumers** are animals. They **eat** living plants or animals. A goat eats grass. A frog eats grasshoppers. A tiger eats deer.'),
    H('Decomposers: nature\'s recyclers', 3),
    P('When plants and animals die, or leaves fall, **decomposers** break them down. **Moulds**, **mushrooms** (fungi), **worms**, some **insects** and tiny **microbes** are decomposers. '
      'They turn dead things back into goodness in the **soil**, which helps new plants grow. Without decomposers, dead leaves and animals would pile up everywhere!'),
    Pics([('mushroom', 'mushrooms'), ('worm', 'earthworms'), ('fly', 'flies and beetles'), ('microbe', 'microbes and mould')], cols=4, size='14mm'),
    H('When something changes', 3),
    P('If one living thing in a food chain disappears, the others change too. If farmers kill all the frogs, the grasshoppers have no predator, so there will be **more grasshoppers**, which eat **more rice**. And the snakes will have **less food**.'),
    Box('tip', P('Patterns help us predict: when a predator goes, its prey often increases.')),
    Vocab([('producer', 'a plant that makes its own food using sunlight'), ('consumer', 'an animal that eats other living things'),
           ('decomposer', 'breaks down dead things into the soil'), ('predator', 'an animal that hunts others'), ('prey', 'an animal that is eaten')]),
])

facts = Sheet('facts', 'Who does what?', level=1, goals=['Sort producers, consumers and decomposers.', 'Build food chains.'], blocks=[
    Q('Sort them.', Sort(['Producer', 'Consumer', 'Decomposer'], [('grass', 'Producer'), ('mango tree', 'Producer'), ('goat', 'Consumer'), ('tiger', 'Consumer'), ('frog', 'Consumer'), ('mushroom', 'Decomposer'), ('earthworm', 'Decomposer'), ('mould', 'Decomposer')]), marks=8),
    Q('Put these in order to make a food chain.', Pics([('tiger', 'tiger'), ('herb', 'grass'), ('deer', 'deer')], cols=3, size='16mm'), Lines(1, 'grass → deer → tiger'), marks=2),
    Q('Fill in the gaps.', Blanks('Plants are [producers]. Animals that eat food are [consumers]. Worms and mushrooms are [decomposers].', extra=['predators']), marks=3),
])

think = Sheet('think', 'What if…?', level=2, goals=['Predict changes in food chains.'], blocks=[
    Q('In the chain **grass → grasshopper → frog → snake**, what would happen if all the frogs were gone?',
      Part('to the grasshoppers?', Lines(1, 'There would be more of them.')), Part('to the grass?', Lines(1, 'More of it would be eaten.')), Part('to the snakes?', Lines(1, 'They would have less food.')), marks=3),
    Q('Why are decomposers important?', Lines(2, 'They break down dead things and put goodness back in the soil for new plants.'), marks=2),
    Q('Draw a food chain you can see near your school.', Draw('36mm', 'My food chain', 'e.g. leaves → caterpillar → bird.'), marks=2),
])

investigate = Sheet('investigate', 'What makes bread go mouldy?', level=2, goals=['Do a fair test.', 'Observe changes over time.'], blocks=[
    P('Class 3C put three slices of bread in bags: one dry, one damp, one damp in the fridge. They looked every day for a week.'),
    Q('Results: days until mould appeared.', Table(['Bread', 'dry', 'damp (warm room)', 'damp (fridge)'], [['Days', 'no mould after 7 days', '3', '7']], center=True), marks=1),
    Q('Which bread went mouldy first? Why?', Lines(2, 'The damp bread in the warm room: mould grows best where it is damp and warm.'), marks=2),
    Q('Is mould a producer, consumer or decomposer?', Lines(1, 'a decomposer'), marks=1),
    Box('safety', P('Never open the bags or smell mouldy bread. Throw them away sealed.')),
])

case = Sheet('case', 'The frogs and the rice field', level=3, goals=['Use a food chain to explain a real problem.'], blocks=[
    Links('Science', 'Farming', 'Environment'),
    Case('Frogs live in many rice fields in Bangladesh. They eat insects that damage the rice. Some years ago, many people caught frogs to sell, and many farmers sprayed strong poisons (pesticides).',
         'Fewer frogs meant more insects, so farmers sprayed even more poison. Now many farmers protect frogs and use fewer pesticides, so the frogs can help them again.',
         source='Based on information about frogs and pest control in rice farming.'),
    Q('Write the food chain from the story.', Lines(1, 'rice → insects → frogs'), marks=1),
    Q('What happened when there were fewer frogs?', Lines(2, 'There were more insects that damaged the rice.'), marks=2),
    Q('How can frogs help farmers?', Lines(2, 'They eat insect pests, so farmers need less poison.'), marks=2),
])

review = Sheet('review', 'Show what you know', level=3, goals=['Use food chain words.'], blocks=[
    Q('Find the words.', WordSearch(['PRODUCER', 'CONSUMER', 'WORM', 'MOULD', 'CHAIN', 'SUN'], size=9, seed=306)),
    Q('Every food chain starts with a…', MCQ(['plant', 'tiger', 'mushroom'], 0), marks=1),
    Q('Which is a decomposer?', MCQ(['goat', 'mushroom', 'grass'], 1), marks=1),
    Q('**Challenge.** Where does the energy in a food chain first come from?', Lines(1, 'the Sun'), marks=1),
])

TOPIC = Topic(
    code='A5', strand='living', title='Food Chains and Energy Roles', short='Food chains',
    subtitle='Producers, consumers and decomposers, building food chains and predicting changes',
    outcomes=[
        'explain the roles of different organisms in a food chain — producers that make their own food using sunlight, consumers that eat living plants or animals, and decomposers such as moulds, fungi, insects and worms that reuse and recycle materials that were formerly living.',
        'observe the interactions for obtaining food among organisms in a local ecosystem, and construct food chains on the basis of those observations.',
        'predict the possible impact of a change in the occurrence of one organism in an ecosystem on the other organisms of that ecosystem.',
        'understand that patterns can be used to make predictions, to support cause-and-effect relations, and as evidence to support ideas.',
    ],
    sheets=[learn, facts, think, investigate, case, review],
    selfcheck=['sort producers, consumers and decomposers', 'build a food chain', 'explain why decomposers matter', 'predict what happens when one animal disappears', 'test what makes bread mouldy'],
    cover_art=art4.food_chain([('herb', 'grass'), ('cricket', 'grasshopper'), ('frog', 'frog')]),
)
