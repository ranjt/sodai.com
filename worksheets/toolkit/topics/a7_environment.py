from build import Sheet, Topic
from ws import (P, H, Box, Vocab, Fig, Cols, Row, Case, Links, Lines, Blanks, Match, TrueFalse, MCQ, Order, Table,
                Ans, Sort, Label, Draw, Graph, WordSearch, Q, Part, Bullets)
import art

learn = Sheet('learn', 'Habitats, food webs and our place in nature', level=1, goals=[
    'Compare the living things found in different habitats.',
    'Use a food web to explain how energy and matter move through an ecosystem.',
    'Evaluate how human activities affect ecosystems, and how nature inspires design.',
], blocks=[
    P('A pond, a mango orchard, a tea garden in Sylhet, the coral reef at St Martin\'s Island and the mangrove forest of the '
      'Sundarbans are all **habitats**: places where living things find food, water and shelter. All the living things in a '
      'habitat, together with the non-living things around them (water, soil, light, air), make an **ecosystem**.', 'lead'),
    Cols(
        H('Biodiversity', 3),
        P('**Biodiversity** means the variety of living things in a place. A rainforest or a coral reef has huge biodiversity. '
          'A field with only one crop has very little. Ecosystems with high biodiversity are usually healthier and recover '
          'better from problems such as disease or floods.'),
        H('Food chains and food webs', 3),
        P('Every food chain starts with a **producer**, a green plant or alga that makes its own food using light energy from '
          'the Sun. **Consumers** eat other living things: **herbivores** eat plants, **carnivores** eat animals and '
          '**omnivores** eat both. A carnivore that is not eaten by anything else is a **top predator**.'),
        P('In a real habitat, most animals eat more than one kind of food, so food chains join together into a **food web**. '
          'The arrows show the direction in which **energy** moves: from the food to the animal that eats it.'),
        Fig(art.food_web(), 'A simplified food web in the Sundarbans.', width='88%', span=True),
        H('Energy flows, matter cycles', 3),
        P('Energy enters the ecosystem as sunlight and passes along the food chains. At each step, much of the energy is used '
          'for living (moving, keeping warm), so there is less for the next animal. That is why there are fewer tigers than '
          'deer. **Matter** is different: it goes round and round. When plants and animals die, **decomposers** such as '
          'fungi, bacteria and earthworms break them down, returning nutrients to the soil for new plants.'),
        H('Living things depend on each other', 3),
        P('Bees pollinate flowers; birds spread seeds; trees give shelter to monkeys and birds; crabs clean up dead leaves. '
          'When one species disappears, others are affected. Reproduction is important too: if a species cannot breed, '
          'its numbers fall and the whole web changes.'),
        H('Humans and ecosystems', 3),
        P('People change habitats by cutting forests, building, farming, fishing and polluting rivers and seas with chemicals '
          'and plastic. We can also protect them: national parks, tree planting, fishing rules and cleaner factories all help.'),
        H('Learning from nature', 3),
        P('Engineers often copy nature. This is called **biomimicry**. The hooks on burrs inspired **Velcro**. The shape of the '
          'kingfisher\'s beak inspired the quiet nose of Japan\'s bullet train. Termite mounds inspired buildings that stay cool '
          'without air conditioning. Lotus leaves inspired self-cleaning paints.'),
        Box('bd', P('Bangladesh has more than 700 species of birds, fish and mammals living in its rivers, haors, hills and '
                    'mangroves. The Sundarbans is a UNESCO World Heritage Site and home to the Royal Bengal tiger.')),
    ),
    Vocab([('habitat', 'the place where a living thing lives'), ('ecosystem', 'living things and their surroundings working together'),
           ('biodiversity', 'the variety of living things in a place'), ('producer', 'a plant or alga that makes its own food'),
           ('consumer', 'an animal that eats other living things'), ('decomposer', 'a living thing that breaks down dead material'),
           ('food web', 'food chains linked together'), ('biomimicry', 'copying nature to solve problems')]),
])

facts = Sheet('facts', 'Habitats and food webs', level=1, goals=['Use the key vocabulary.', 'Read a food web.'], blocks=[
    Q('Match each word to its meaning.',
      Match([('producer', 'makes its own food using light'), ('herbivore', 'eats only plants'), ('carnivore', 'eats only animals'),
             ('omnivore', 'eats plants and animals'), ('decomposer', 'breaks down dead plants and animals'),
             ('habitat', 'the place where an organism lives')]), marks=6),
    Q('Use the food web on the "Learn it" page to answer.',
      Part('Name the two producers.', Lines(1, 'mangrove leaves and algae')),
      Part('Write one food chain with four links.', Lines(1, 'algae → shrimp → fish → kingfisher (or algae → fish → otter, etc.)')),
      Part('Name a top predator.', Lines(1, 'tiger (or kingfisher / otter)')),
      Part('What do crabs eat?', Lines(1, 'mangrove leaves')), marks=4),
    Q('True or false?', TrueFalse([
        ('Every food chain starts with a producer.', True),
        ('The arrows in a food web point from the eater to the food.', False, 'They point from the food to the eater (direction of energy).'),
        ('Decomposers return nutrients to the soil.', True),
        ('A field with one crop has high biodiversity.', False, 'It has low biodiversity.')]), marks=4),
    Q('Fill in the gaps.',
      Blanks('Energy enters a food web as [sunlight]. Plants use it to make [food]. Energy passes to [consumers] when they eat. '
             'Copying ideas from nature is called [biomimicry].', extra=['rain', 'soil']), marks=4),
])

think = Sheet('think', 'What happens if…?', level=2, goals=['Predict changes in a food web.', 'Explain energy flow.',
                                                           'Link features of living things to designs.'], blocks=[
    Q('Use the Sundarbans food web. Predict what would happen and explain why.',
      Part('If many deer died from disease, what would happen to the tigers?', Lines(2, 'Tigers would have less food, so their numbers might fall, or they would eat more monkeys.')),
      Part('If an oil spill killed the algae, which animals would be affected? Explain.', Lines(3, 'Shrimp and fish (which eat algae) would have less food, then kingfishers and otters that eat them would be affected too.')), marks=4),
    Q('Why are there far fewer tigers than deer in the Sundarbans?',
      Lines(3, 'Energy is lost at each step of the food chain (used for moving and keeping warm), so there is only enough energy for a few top predators.'), marks=2),
    Q('Complete the table about biomimicry.',
      Table(['Feature in nature', 'What it does', 'Human invention'], [
          ['burr hooks', Ans('catch on fur to spread seeds'), Ans('Velcro')],
          ['kingfisher beak', Ans('enters water smoothly with little splash'), Ans('bullet train nose')],
          ['termite mound', Ans('keeps the nest cool with air channels'), Ans('naturally cooled buildings')]], widths=['24%', '42%', '34%']), marks=6),
    Q('Design a solution by mimicking nature. A school roof gets very hot. Which animal or plant could give you an idea? Explain your design.',
      Lines(3, 'e.g. like a termite mound: tall chimneys/vents let hot air escape; or like a tree: a roof garden or shade leaves; light colours like reflective shells.'), marks=2),
])

investigate = Sheet('investigate', 'Comparing two habitats', level=2, goals=[
    'Use a quadrat to sample plants fairly.', 'Compare biodiversity using data.', 'Explain differences between habitats.'], blocks=[
    Row([P('Class 5A compared two habitats in the school grounds: the **football field** and the **garden by the pond**. In '
           'each habitat they threw a 1 m × 1 m **quadrat** at random three times and counted the different kinds of plants '
           'and small animals inside.'),
         Box('tip', P('Throwing the quadrat at random makes the test fair: you do not choose only the interesting spots.'))],
        [Fig(art.quadrat(), width='85%')], widths=[1.6, 1]),
    Q('Here are the results. Work out the totals.',
      Table(['Kind of living thing', 'Football field', 'Pond garden'], [
          ['grass', '✔', '✔'], ['clover', '✔', '✔'], ['dandelion', '', '✔'], ['fern', '', '✔'], ['moss', '', '✔'],
          ['ant', '✔', '✔'], ['earthworm', '', '✔'], ['snail', '', '✔'], ['spider', '', '✔'],
          ['**Number of different kinds**', Ans('3'), Ans('9')]], center=True), marks=2),
    Q('Draw a bar chart comparing the number of different kinds of living things.',
      Graph(['football field', 'pond garden'], [3, 9], 'Number of kinds', 'Habitat', ymax=10, step=1, width=110, height=62), marks=3),
    Q('Which habitat has greater biodiversity? Suggest **two** reasons.',
      Lines(3, 'The pond garden: it has water, shade, different plants and is not trampled or mowed, so there are more kinds of food and shelter.'), marks=3),
    Q('Why did the class use the quadrat three times in each habitat?',
      Lines(2, 'One sample might not be typical; repeating gives more reliable results.'), marks=1),
    Q('Suggest **one** way the school could increase biodiversity on the field.',
      Lines(2, 'e.g. leave a wild strip unmowed, plant native flowers and trees, make a small pond or log pile.'), marks=1),
])

case = Sheet('case', 'The Sundarbans: a forest that protects us', level=3, goals=[
    'Explain why an ecosystem matters to people.', 'Evaluate the effect of a human activity, using evidence.',
    'Argue for a way to reduce harm.'], blocks=[
    Links('Science', 'Geography', 'Economics', 'Ethics', 'Climate change'),
    Case('The **Sundarbans** is the largest mangrove forest in the world, about 10 000 km², shared by Bangladesh (about 60%) '
         'and India. Mangrove trees such as *sundari* and *keora* grow in salty, muddy water and have special roots that poke '
         'up out of the mud to breathe.',
         'The forest is home to Royal Bengal tigers, spotted deer, crocodiles, river dolphins and hundreds of kinds of birds '
         'and fish. Hundreds of thousands of people depend on it for fish, crabs, honey and wood.',
         'The Sundarbans also **protects** people. When cyclones such as **Sidr** (2007) and **Aila** (2009) struck, the '
         'mangroves slowed the wind and the storm surge, protecting villages behind them.',
         'But the forest faces threats. In **December 2014**, an oil tanker sank in the Shela River inside the forest, spilling '
         'about 350 000 litres of heavy oil. Oil coated mud, roots and animals. Rising sea levels, more salt in the water, '
         'shipping, cutting of trees and poaching are other dangers.',
         source='Sources: UNESCO World Heritage listing; UNEP/UN assessment of the 2014 Shela River oil spill.'),
    Q('Give **three** ways the Sundarbans helps people.',
      Lines(3, 'It protects villages from cyclones and storm surges; gives fish, crabs, honey and wood for jobs and food; supports tourism; stores carbon.'), marks=3),
    Q('Explain how an oil spill could harm the food web, starting with the producers.',
      Lines(3, 'Oil coats leaves, roots and algae so producers cannot get light/air and may die; animals that eat them lose food; oil also poisons fish and crabs, so predators are affected.'), marks=3),
    Q('Different people want different things from the river. Complete the table.',
      Table(['Person', 'What they want'], [['a ship owner', Ans('a short, cheap route through the forest rivers')],
                                           ['a fisher', Ans('clean water so there are plenty of fish and crabs')],
                                           ['a conservation scientist', Ans('to protect tigers, dolphins and the mangroves')]], widths=['32%', '68%']), marks=3),
    Q('**Argue from evidence.** Should cargo ships be allowed to travel through the Sundarbans? Give your opinion, one '
      'piece of evidence and one way to reduce harm.',
      Lines(5, 'Accept a reasoned opinion, e.g. "No, or only with strict rules: the 2014 spill harmed the forest. Ships could use another route, be double-hulled, travel slowly and carry spill-cleaning equipment."'), marks=4),
])

review = Sheet('review', 'Show what you know', level=3, goals=['Use key vocabulary.', 'Answer test-style questions.'], blocks=[
    Q('Find the key words.', WordSearch(['HABITAT', 'PRODUCER', 'CONSUMER', 'PREDATOR', 'PREY', 'ENERGY', 'DECOMPOSER', 'MANGROVE', 'TIGER'], size=12, seed=7)),
    Q('In the chain grass → deer → tiger, the deer is:', MCQ(['a producer', 'a herbivore', 'a carnivore', 'a decomposer'], 1), marks=1),
    Q('Which is an example of biomimicry?', MCQ(['planting trees', 'Velcro copied from burrs', 'a food chain', 'a national park'], 1), marks=1),
    Q('Draw a food web with at least **five** living things from a pond. Use arrows correctly.',
      Draw('55mm', 'My pond food web', 'e.g. algae → tadpole → fish → heron; pond weed → snail → duck; algae → water flea → fish. Arrows from food to eater.'), marks=4),
    Q('**Challenge.** Explain why matter is recycled in an ecosystem but energy is not.',
      Lines(3, 'Decomposers break dead things into nutrients that plants use again, so matter goes round. Energy is used up/given off as heat at each step and must keep coming in from the Sun.'), marks=2),
])

TOPIC = Topic(
    code='A7', strand='living', title='Living Things in Their Environment', short='Environments',
    subtitle='Habitats, biodiversity, food webs, human impact and learning from nature',
    outcomes=[
        'make observations of plants and animals to compare the diversity of life in different habitats.',
        'analyse a food web to explain how energy and matter move through an ecosystem, building on the food chains constructed in Grade 4.',
        'evaluate the effect of a human activity on an ecosystem and argue, from evidence, for a way of reducing the harm.',
        'use materials to design a solution to a problem by mimicking how plants and animals use their features.',
        'understand that living systems are open, self-organizing life forms that interact with their environment.',
    ],
    sheets=[learn, facts, think, investigate, case, review],
    selfcheck=['compare the variety of living things in two habitats', 'read and draw a food web with correct arrows',
               'explain how energy flows and matter cycles in an ecosystem', 'predict what happens when one living thing disappears',
               'explain how a human activity harms an ecosystem and argue for a solution', 'give examples of biomimicry'],
    cover_art=art.food_web(),
)
