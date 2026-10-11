from build import Sheet, Topic
from ws import (P, H, Box, Vocab, Fig, Cols, Row, Case, Links, Lines, Blanks, Match, TrueFalse, MCQ, Order, Table,
                Ans, Sort, Label, Draw, Graph, WordSearch, Q, Part, Bullets)
import art

learn = Sheet('learn', 'Mixing, dissolving, separating and changing', level=1, goals=[
    'Separate mixtures by sieving, filtering, using a magnet and evaporating.',
    'Explain dissolving and why a dissolved substance is still there.',
    'Tell the difference between reversible and irreversible changes.',
], blocks=[
    P('Think about a cup of cha: tea leaves, water, milk and sugar. Some things mix and can be separated again; some '
      'dissolve and seem to disappear; and some changes, like cooking an egg, can never be undone.', 'lead'),
    Cols(
        H('Mixtures', 3),
        P('A **mixture** is two or more materials mixed together but not joined. Rice with small stones, sand with water, '
          'and iron nails with sawdust are all mixtures. Because the materials keep their own properties, we can use those '
          'properties to **separate** them.'),
        Fig(art.separation_methods(), 'Four ways to separate mixtures.'),
        Bullets(['**Sieving:** separates solid pieces of different sizes, for example stones from rice, or lumps from flour.',
                 '**Using a magnet:** pulls out magnetic materials such as iron and steel.',
                 '**Filtering:** separates an **insoluble** solid (one that does not dissolve) from a liquid, for example sand from water. The liquid passes through tiny holes in the filter paper; the solid stays behind. It is like a very fine sieve.',
                 '**Evaporating:** gets a **dissolved** solid back from a solution. The water evaporates; the solid is left.']),
        Box('bd', P('Farmers use a flat bamboo tray called a **kula** to separate rice from its light husks. They toss the rice '
                    'in the breeze: the heavy grains fall back, and the wind carries the light husks away.')),
        H('Dissolving', 3),
        P('When you stir sugar into water, the sugar seems to disappear. It has **dissolved**: it has broken into pieces far too '
          'small to see and spread through the water to make a **solution**. The sugar is still there. You can taste it, '
          'and the mass of the solution equals the mass of the water plus the mass of the sugar. Materials that dissolve are '
          '**soluble** (salt, sugar); materials that do not are **insoluble** (sand, chalk, flour). Stirring, using **warmer** '
          'water and using **smaller** pieces make things dissolve faster.'),
        Fig(art.filtering(labels=art.FILTER_PARTS), 'Filtering sandy water.'),
        H('Reversible and irreversible changes', 3),
        P('A **reversible change** can be undone: melting and freezing, dissolving (evaporate the water to get the solid back), '
          'and mixing and separating. No new material is made.'),
        P('An **irreversible change** cannot be undone, because **new materials** are made: cooking an egg, baking a cake, '
          'burning wood or paper, iron **rusting**, and cement setting. Signs of a new material include bubbles of gas, a '
          'colour change, a new smell, and heat or light being given out.'),
        Box('safety', P('Never taste anything in a science lesson, and ask an adult to help with heating.')),
    ),
    Vocab([('mixture', 'materials mixed together but not joined'), ('dissolve', 'break up and spread through a liquid'),
           ('solution', 'a liquid with something dissolved in it'), ('soluble', 'able to dissolve'), ('insoluble', 'not able to dissolve'),
           ('filtering', 'separating an insoluble solid from a liquid'), ('reversible change', 'a change that can be undone'),
           ('irreversible change', 'a change that makes new materials and cannot be undone')]),
])

facts = Sheet('facts', 'Separating and changing', level=1, goals=['Choose a separation method.', 'Sort reversible and irreversible changes.'], blocks=[
    Q('Label the filtering equipment.', Label(art.filtering(), art.FILTER_PARTS, width='80%'), marks=5),
    Q('Which method would you use to separate each mixture?',
      Table(['Mixture', 'Method'], [['small stones from rice', Ans('sieving (or picking out by hand)')], ['iron filings from sand', Ans('using a magnet')],
                                    ['sand from water', Ans('filtering')], ['salt from salty water', Ans('evaporating')]], widths=['55%', '45%']), marks=4),
    Q('Sort the materials.',
      Sort(['Soluble in water', 'Insoluble in water'], [('sugar', 'Soluble in water'), ('salt', 'Soluble in water'), ('instant coffee', 'Soluble in water'),
                                                        ('sand', 'Insoluble in water'), ('chalk', 'Insoluble in water'), ('flour', 'Insoluble in water')]), marks=6),
    Q('Sort the changes.',
      Sort(['Reversible', 'Irreversible'], [('ice melting', 'Reversible'), ('sugar dissolving', 'Reversible'), ('water freezing', 'Reversible'),
                                            ('frying an egg', 'Irreversible'), ('burning paper', 'Irreversible'), ('a nail rusting', 'Irreversible')]), marks=6),
])

think = Sheet('think', 'Solving separation problems', level=2, goals=['Plan how to separate a complex mixture.', 'Explain dissolving and new materials.'], blocks=[
    Q('Rana knocked over a jar. Now sand, salt and iron nails are all mixed together. Explain step by step how to get all three back.',
      Lines(5, '1 Use a magnet to pull out the iron nails. 2 Add water and stir: the salt dissolves, the sand does not. 3 Filter: the sand stays in the filter paper. 4 Evaporate the water from the salty water to get the salt crystals back.'), marks=4),
    Q('Sumi says, "When sugar dissolves it disappears, so it is gone." Use evidence to explain why she is wrong.',
      Lines(3, 'The water tastes sweet; the solution weighs the same as the water plus the sugar; if you evaporate the water, the sugar is left behind.'), marks=2),
    Q('How can you tell that baking a cake makes a new material? Give two signs.',
      Lines(2, 'Bubbles of gas make it rise; colour changes to brown; a new smell; you cannot get the eggs and flour back.'), marks=2),
    Q('Why does filtering not separate salt from salty water?',
      Lines(2, 'The salt is dissolved into tiny pieces that pass through the filter paper with the water.'), marks=2),
])

investigate = Sheet('investigate', 'Does warm water dissolve sugar faster?', level=2, goals=['Identify variables.', 'Plot and read a line graph.', 'Make a prediction from a pattern.'], blocks=[
    P('Class 5B timed how long one teaspoon of sugar took to dissolve in 100 ml of water at different temperatures, stirring '
      'the same way each time.'),
    Q('Name the variables.',
      Table(None, [['Change', Ans('temperature of the water')], ['Measure', Ans('time for the sugar to dissolve (seconds)')],
                   ['Keep the same', Ans('amount of sugar and water, type of sugar, stirring, size of cup')]], widths=['24%', '76%']), marks=3),
    Q('Plot the results as a line graph.',
      Table(['Water temperature (°C)', '10', '25', '40', '60'], [['Time to dissolve (s)', '180', '95', '50', '25']], center=True),
      Graph(['10 °C', '25 °C', '40 °C', '60 °C'], [180, 95, 50, 25], 'Time to dissolve (s)', 'Water temperature', ymax=200, step=20, kind='line',
            width=140, height=56), marks=4),
    Q('Describe the pattern.', Lines(2, 'The warmer the water, the faster the sugar dissolves (the shorter the time).'), marks=2),
    Q('Predict the time at 50 °C. Explain how you decided.', Lines(2, 'About 35–40 seconds: between the times for 40 °C (50 s) and 60 °C (25 s).'), marks=1),
    Q('How could they make the results more reliable?', Lines(2, 'Repeat each temperature three times and work out an average.'), marks=1),
])

case = Sheet('case', 'Khejur gur: winter sweetness and a hidden danger', level=3, goals=['Identify reversible and irreversible changes in a real process.', 'Explain a health risk using science.', 'Communicate a safety message.'], blocks=[
    Links('Science', 'Health', 'Culture', 'Economics'),
    Case('On cold winter nights in Jashore and other districts, skilled climbers called *gachhi* cut the bark of date palm trees '
         'and hang clay pots to collect the sweet **sap**. In the morning the sap is **filtered** through cloth to remove '
         'insects and bits of bark, then **boiled** for hours in wide pans. Water **evaporates**, the sap gets thicker, and '
         'the sugar turns golden brown. Poured into moulds, it sets as **khejur gur** (date palm molasses), used to make '
         'pitha and payesh.',
         'But raw, unboiled sap can be dangerous. Fruit bats sometimes drink from the pots at night and can leave behind the '
         '**Nipah virus**, which causes a serious brain illness. Health experts in Bangladesh warn: **never drink raw date '
         'palm sap**. Boiling kills the virus, so properly made gur is safe.',
         source='Health advice from IEDCR (Institute of Epidemiology, Disease Control and Research), Bangladesh.'),
    Q('Find the separating methods and changes in the story. Complete the table.',
      Table(['Step', 'What happens', 'Reversible or irreversible?'], [
          ['filtering through cloth', Ans('removes solid bits (insects, bark) from the sap'), Ans('reversible (separating)')],
          ['boiling: water evaporates', Ans('water leaves as vapour; the sap gets thicker'), Ans('reversible (could add water back)')],
          ['sugar turns golden brown', Ans('new substances with new colour and taste form (caramelising)'), Ans('irreversible')],
          ['gur sets in moulds', Ans('the hot thick liquid cools and becomes solid'), Ans('reversible (it can be melted again)')]],
            widths=['26%', '46%', '28%']), marks=8),
    Q('Why is filtering through cloth not enough to make raw sap safe to drink?',
      Lines(2, 'Viruses are far too small to be stopped by cloth; only boiling kills them.'), marks=2),
    Q('Write a short safety message (radio or poster) for families in your area about date palm sap.',
      Draw('28mm', 'My message', 'e.g. "Love khejur gur? Enjoy it cooked! Never drink raw date palm sap: it can carry Nipah virus."'), marks=2),
])

review = Sheet('review', 'Show what you know', level=3, goals=['Use key vocabulary.', 'Answer test-style questions.'], blocks=[
    Q('Find the key words.', WordSearch(['MIXTURE', 'SIEVE', 'FILTER', 'MAGNET', 'DISSOLVE', 'SOLUTION', 'SOLUBLE', 'RUST', 'BURN'], size=11, seed=111)),
    Q('Which of these is an irreversible change?', MCQ(['melting chocolate', 'dissolving salt', 'burning a match', 'freezing juice'], 2), marks=1),
    Q('Which method separates sand from water?', MCQ(['evaporating', 'filtering', 'using a magnet', 'dissolving'], 1), marks=1),
    Q('Write the letter of each separation method.', Fig(art.separation_methods(names=False), width='80%'),
      Table(['Method', 'Letter'], [['filtering', Ans('C')], ['evaporating', Ans('D')], ['sieving', Ans('A')], ['magnet', Ans('B')]], center=True), marks=4),
    Q('**Challenge.** Is making a cup of cha with sugar and milk a reversible or irreversible change? Explain your thinking.',
      Lines(3, 'Mostly reversible mixing and dissolving (the water could be evaporated), but hot water also draws new flavours out of the tea leaves, so it is hard to fully undo. Accept reasoned answers.'), marks=2),
])

TOPIC = Topic(
    code='C2', strand='physical', title='Mixtures, Solutions and Changes', short='Mixtures and changes',
    subtitle='Separating mixtures, dissolving and solutions, reversible and irreversible changes',
    outcomes=[
        'distinguish between reversible and irreversible changes.',
        'explore how solids can be mixed and how it is often possible to separate them again.',
        'observe, describe, record and begin to explain the changes that occur when some solids are added to water.',
        'explore how, when solids do not dissolve or react with water, they can be separated by filtering, which is similar to sieving.',
        'explore how some solids dissolve in water to form solutions and, although the solid cannot be seen, the substance is still present.',
    ],
    cambridge=['Unit 3 States of matter: 3.4 Investigating evaporation from a solution'],
    sheets=[learn, facts, think, investigate, case, review],
    selfcheck=['choose a method to separate a mixture', 'explain filtering and why it is like sieving', 'explain that a dissolved solid is still there',
               'sort changes into reversible and irreversible', 'investigate what makes things dissolve faster', 'explain why raw date palm sap is unsafe'],
    cover_art=art.separation_methods(),
)
