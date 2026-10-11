from build import Sheet, Topic
from ws import (P, H, Box, Vocab, Fig, Cols, Row, Case, Links, Lines, Blanks, Match, TrueFalse, MCQ, Order, Table,
                Ans, Sort, Label, Draw, Graph, WordSearch, Q, Part, Bullets, Pics)
import art
import art4

learn = Sheet('learn', 'Mixing and separating', level=1, goals=[
    'Observe and describe what happens when different substances are mixed.',
    'Choose and use ways to separate mixtures.',
    'Explain how melting and freezing help us recycle materials.',
], blocks=[
    P('In the kitchen, mixtures are everywhere: rice with tiny stones, dal soaking in water, sugar stirred into cha, spices '
      'ground together. Cooks are clever scientists. They know how to mix things and how to separate them again.', 'lead'),
    Cols(
        H('What happens when we mix?', 3),
        P('When we mix substances, different things can happen. Look carefully and describe what you see.'),
        Table(['Mixture', 'What happens'], [
            ['sugar + water', 'the sugar **dissolves** and seems to disappear'],
            ['sand + water', 'the sand does not dissolve; it **sinks** to the bottom'],
            ['oil + water', 'they do not mix; the oil **floats** on top'],
            ['vinegar + baking soda', 'it **fizzes**: a new gas is made'],
            ['flour + water', 'a thick **paste** forms']]),
        Box('safety', P('Never taste or smell mixtures in science lessons unless your teacher says it is safe.')),
        H('Ways to separate mixtures', 3),
        P('We separate mixtures by using the different **properties** of the things in them: size, whether they dissolve, '
          'whether they are magnetic, or whether they float.'),
        Fig(art.separation_methods(), 'Four ways to separate a mixture.', span=True, width='82%'),
        Bullets(['**Picking out**: removing stones from rice by hand.',
                 '**Sieving**: a sieve lets small bits through and keeps big bits back (flour from lumps).',
                 '**Winnowing**: tossing rice on a *kula* so the wind blows the light husks away.',
                 '**Using a magnet**: pulling iron pins out of sand.',
                 '**Pouring off** (decanting): letting mud sink, then pouring the water off the top.',
                 '**Filtering**: pouring muddy water through filter paper or cloth; the water passes through, the mud stays behind.',
                 '**Evaporating**: leaving salty water in the sun; the water evaporates and the salt is left.']),
        H('Recycling with heat', 3),
        P('Changes of state help us **recycle**. Plastic, glass and metals such as aluminium and iron can be **melted** by heating '
          'them, poured into a **mould**, and left to cool and **freeze** (become solid again) in a new shape. Old cans can become '
          'new pots; broken glass can become new bottles.'),
        Fig(art4.recycle_melt(), 'Melting and moulding to recycle.', span=True, width='80%'),
        Box('bd', P('In Old Dhaka, small workshops melt scrap aluminium and pour it into sand moulds to make cooking pots (*hari* '
                    'and *patil*). Collectors called *bhangari* buy old metal, paper and plastic from homes so they can be recycled.')),
        Box('try', P('Mix a spoon of sand, a spoon of salt and some water in a cup. Can you get the sand back? Can you get the salt back? (Hint: filter, then leave the water in the sun.)')),
    ),
    Vocab([('mixture', 'two or more substances mixed but not joined'), ('dissolve', 'break up and spread through a liquid'),
           ('sieve', 'a mesh that separates big and small pieces'), ('filter', 'separates bits of solid from a liquid'),
           ('evaporate', 'a liquid turns into a gas'), ('winnowing', 'using wind to blow light husks away from grain'),
           ('mould', 'a hollow shape that liquid is poured into'), ('recycle', 'make used materials into new things')]),
])

facts = Sheet('facts', 'Choose a method', level=1, goals=['Match mixtures to separation methods.', 'Describe mixing.'], blocks=[
    Q('Which method separates each mixture?',
      Table(['Mixture', 'Method'], [['stones in rice', Ans('picking out or sieving')], ['iron pins in sand', Ans('using a magnet')], ['sand in water', Ans('filtering (or pouring off)')],
                                    ['salt in water', Ans('evaporating')], ['husks and rice grains', Ans('winnowing')]], widths=['50%', '50%']), marks=5),
    Q('Name each method.', Fig(art.separation_methods(names=False), width='76%'),
      Table(['A', 'B', 'C', 'D'], [[Ans('sieving'), Ans('using a magnet'), Ans('filtering'), Ans('evaporating')]], center=True), marks=4),
    Q('What happens? Write **dissolves**, **sinks**, **floats** or **fizzes**.',
      Table(['Mixture', 'What happens'], [['salt in water', Ans('dissolves')], ['a stone in water', Ans('sinks')], ['oil in water', Ans('floats')], ['vinegar and baking soda', Ans('fizzes')]], widths=['55%', '45%']), marks=4),
    Q('Put the steps of recycling a metal can in order.', Order(['collect old cans', 'heat them until they melt', 'pour the liquid metal into a mould', 'let it cool and become solid', 'take out the new pot']), marks=3),
])

think = Sheet('think', 'Separation puzzles', level=2, goals=['Plan how to separate a mixture.', 'Explain using properties.'], blocks=[
    Q('Mina spilled a mixture of sand, salt, iron pins and dried peas. Plan how to get each one back. Explain each step.',
      Lines(5, '1 Pick out or sieve the big peas. 2 Use a magnet for the iron pins. 3 Add water and stir: the salt dissolves. 4 Filter: the sand stays in the paper. 5 Evaporate the water to get the salt.'), marks=5),
    Q('Why can\'t you separate salt from water with a sieve or a filter?', Lines(2, 'The salt has dissolved into tiny pieces that pass through the holes with the water.'), marks=2),
    Q('Why must a mould be made of something with a much higher melting point than the metal poured into it?', Lines(2, 'Otherwise the hot liquid metal would melt the mould.'), marks=2),
    Q('Is mixing vinegar and baking soda a good way to make something you can separate again? Explain.', Lines(2, 'No: a new gas is made and escapes; you cannot get the vinegar and baking soda back.'), marks=1),
])

investigate = Sheet('investigate', 'Which filter cleans muddy water best?', level=2, goals=['Compare materials fairly.', 'Use a rating scale.', 'Draw conclusions.'], blocks=[
    P('Class 4C poured 100 ml of the same muddy water through four different filters in funnels. They rated how clear the water '
      'was from **1** (still very muddy) to **5** (very clear).'),
    Q('Complete the plan.', Table(None, [['Change', Ans('the filter material')], ['Measure', Ans('how clear the water is (rating 1–5)')],
                                         ['Keep the same', Ans('the amount and type of muddy water, the funnel, the amount of filter material')]], widths=['26%', '74%']), marks=3),
    Q('Draw a bar chart.',
      Table(['Filter', 'cotton cloth', 'sand', 'filter paper', 'sand + charcoal'], [['Clearness (1–5)', '2', '3', '4', '5']], center=True),
      Graph(['cloth', 'sand', 'paper', 'sand + charcoal'], [2, 3, 4, 5], 'Clearness (1–5)', 'Filter', ymax=5, step=1, width=100, height=48), marks=3),
    Q('Which filter was best? Suggest why.', Lines(2, 'Sand and charcoal: the tiny gaps between sand grains trap mud and the charcoal traps even smaller bits.'), marks=2),
    Q('The water from the best filter looks clear. Is it safe to drink? Explain.', Lines(2, 'Not necessarily: germs and dissolved poisons like arsenic are too small to see and can pass through; it should be boiled or treated.'), marks=2),
])

case = Sheet('case', 'The SONO filter: clean water from a Bangladeshi invention', level=3, goals=['Apply filtering to a real problem.', 'Understand how a scientist designed a solution.', 'Evaluate the solution.'], blocks=[
    Links('Science', 'Health', 'Design', 'Economics'),
    Case('Millions of tube-wells in Bangladesh give water that is free of the germs found in ponds. But scientists discovered '
         'that the water from many wells contains **arsenic**, a poison that dissolves into the water from rocks deep '
         'underground. You cannot see, smell or taste it, and drinking it for years can cause serious illness.',
         '**Dr Abul Hussam**, a chemist born in Kushtia, designed a simple filter called **SONO**. Water trickles through buckets '
         'filled with layers of **sand**, **brick chips**, **charcoal** and a special **iron mixture** that grabs the arsenic. It '
         'needs no electricity. In 2007 his invention won a major international prize for engineering, and many thousands of '
         'families have used it.',
         source='Based on information about arsenic in groundwater in Bangladesh and the SONO filter.'),
    Q('Match each filter layer to its job.',
      Match([('sand and brick chips', 'trap bits of mud and sand'), ('iron mixture', 'grabs the dissolved arsenic'), ('charcoal', 'removes smells and tiny bits')]), marks=3),
    Q('Why can\'t ordinary cloth filter remove arsenic?', Lines(2, 'The arsenic is dissolved, so it is in pieces far too small to be trapped by cloth.'), marks=2),
    Q('Give two reasons why the SONO filter is a good design for villages.', Lines(2, 'It needs no electricity; it is made from cheap local materials; it is simple to use and repair.'), marks=2),
    Q('What might each person think?',
      Table(['Person', 'View'], [['a mother', Ans('I want safe water for my children without walking far.')], ['a scientist', Ans('We must test each well and check the filters work.')],
                                 ['a shopkeeper selling filters', Ans('Filters must be cheap enough for poor families to buy.')]], widths=['30%', '70%']), marks=3),
])

review = Sheet('review', 'Show what you know', level=3, goals=['Use key vocabulary.', 'Answer test-style questions.'], blocks=[
    Q('Find the key words.', WordSearch(['SIEVE', 'FILTER', 'MAGNET', 'DISSOLVE', 'MIXTURE', 'MOULD', 'MELT', 'SALT', 'SAND'], size=10, seed=412)),
    Q('Which method gets salt back from salty water?', MCQ(['sieving', 'filtering', 'evaporating', 'using a magnet'], 2), marks=1),
    Q('A farmer tosses rice on a *kula* in the wind. This is called…', MCQ(['winnowing', 'filtering', 'melting', 'dissolving'], 0), marks=1),
    Q('Draw and label equipment to filter muddy water.', Draw('40mm', 'Filtering', 'Funnel with filter paper, beaker underneath; mud left in the paper, clear water in the beaker.'), marks=3),
    Q('**Challenge.** Explain why recycling a metal pot by melting it is a reversible change, but burning paper is not.',
      Lines(3, 'Melting is a change of state: the liquid metal can become solid again. Burning makes new substances (ash, smoke, gases) so the paper cannot be got back.'), marks=2),
])

TOPIC = Topic(
    code='C2', strand='physical', title='Mixtures and Separation', short='Mixtures',
    subtitle='What happens when substances mix, ways to separate mixtures, and recycling by melting and moulding',
    outcomes=[
        'observe and describe different mixtures.',
        'investigate what happens when different substances are mixed.',
        'design and conduct investigations to separate various mixtures, and report on the results.',
        'explore how changes from solid to liquid and from liquid to solid can help us recycle materials.',
    ],
    sheets=[learn, facts, think, investigate, case, review],
    selfcheck=['describe what happens when substances are mixed', 'choose a method to separate a mixture', 'plan how to separate a mixture of four things',
               'test which filter works best', 'explain recycling by melting and moulding', 'explain how the SONO filter works'],
    cover_art=art.separation_methods(),
)
