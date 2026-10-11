from build import Sheet, Topic
from ws import (P, H, Box, Vocab, Fig, Cols, Row, Case, Links, Lines, Blanks, Match, TrueFalse, MCQ, Order, Table,
                Ans, Sort, Label, Draw, Graph, WordSearch, Q, Part, Bullets, Pics)
import art
import art4

learn = Sheet('learn', 'Wind, water and our changing land', level=1, goals=[
    'Explain how wind and water change the shape of the land.',
    'Compare different ways to slow or stop erosion.',
    'Explain what a system is, using examples.',
], blocks=[
    P('Every year in Bangladesh, rivers eat away their banks and whole villages can fall into the water. At the same time, '
      'new islands of sand called **chars** appear in the middle of the rivers. The land is always changing shape. Moving '
      'water and wind are the main reasons.', 'lead'),
    Cols(
        H('Weathering, erosion and deposition', 3),
        Bullets(['**Weathering**: rocks and soil are broken into small pieces by rain, heat, plant roots and ice.',
                 '**Erosion**: the pieces are **carried away** by moving water or wind.',
                 '**Deposition**: when the water or wind slows down, it **drops** the pieces in a new place.']),
        H('Water changes the land', 3),
        P('Fast-flowing rivers carry huge amounts of mud and sand. On the outside of a bend, the water flows fastest and wears '
          'away the bank. On the inside of a bend, and where the river meets the sea, the water slows down and drops the mud, '
          'building new land. Most of Bangladesh was built over thousands of years from mud carried by the **Padma (Ganges)**, '
          '**Jamuna (Brahmaputra)** and **Meghna** rivers. Waves wear away coasts, and heavy rain can wash soil off bare hills '
          'and cause **landslides**.'),
        Fig(art.river_landscape(labels=art.RIVER_PARTS), 'A river wears away land in some places and builds it up in others.', width='96%'),
        H('Wind changes the land', 3),
        P('Wind picks up dry sand and dust, especially where there are no plants. It can blow sand onto farmland and build '
          '**sand dunes** along beaches, like at Cox\'s Bazar and Kuakata.'),
        H('Slowing erosion down', 3),
        P('People have invented many ways to protect the land. Each has good and bad points.'),
        Fig(art4.erosion_fixes(), 'Four ways to slow erosion.', span=True, width='92%'),
        Table(['Solution', 'How it works', 'Good points', 'Problems'], [
            ['plant trees and grass', 'roots hold the soil; leaves break the fall of rain and wind', 'cheap; helps wildlife', 'takes years to grow'],
            ['embankment', 'a wall of earth or concrete keeps the river or sea back', 'protects big areas', 'expensive; can break in floods'],
            ['geo-bags', 'big bags of sand placed along a river bank', 'quick to place', 'can be washed away'],
            ['terraces', 'steps cut into hills slow the water running down', 'good for farming on hills', 'hard work to build'],
            ['windbreaks', 'rows of trees slow the wind near the ground', 'protect fields and homes', 'take space from crops']]),
        H('Thinking in systems', 3),
        P('A **system** is a group of parts that work together to do a job that no single part can do alone. A **river** is a '
          'system: rain, streams, the main river, its banks and the sea all work together to move water and mud. A **coastal '
          'defence** is a system too: a mangrove belt slows the waves, an embankment holds back the water, and **sluice gates** '
          'let rain water flow out but stop the sea coming in. If one part fails, the whole system is weaker.'),
        Box('bd', P('Bangladesh has built thousands of kilometres of embankments around low land near the coast, called **polders**. '
                    'The Coastal Embankment Project began in the 1960s.')),
        Box('try', P('Pour water slowly from a jug onto a pile of soil, and onto a pile of soil covered with grass or leaves. Which one washes away faster?')),
    ),
    Vocab([('weathering', 'breaking rocks and soil into smaller pieces'), ('erosion', 'carrying away soil and rock by water or wind'),
           ('deposition', 'dropping soil, sand and mud in a new place'), ('char', 'a sand island that forms in a river'),
           ('embankment', 'a long raised bank that holds back water'), ('landslide', 'soil and rock sliding down a hill'),
           ('windbreak', 'a row of trees or a fence that slows the wind'), ('system', 'parts working together to do a job')]),
])

facts = Sheet('facts', 'Erosion words and solutions', level=1, goals=['Use erosion vocabulary.', 'Name ways to slow erosion.'], blocks=[
    Q('Match the word to its meaning.',
      Match([('weathering', 'breaking rocks into small pieces'), ('erosion', 'carrying away soil and rock'), ('deposition', 'dropping mud and sand in a new place'),
             ('landslide', 'soil and rocks sliding down a hill')]), marks=4),
    Q('Name each solution.', Fig(art4.erosion_fixes(names=False), width='86%'),
      Table(['A', 'B', 'C', 'D'], [[Ans('plant trees and grass'), Ans('embankment'), Ans('geo-bags'), Ans('terraces')]], center=True), marks=4),
    Q('Sort the causes.', Sort(['Water erosion', 'Wind erosion'], [('waves hitting a cliff', 'Water erosion'), ('a river bank falling in', 'Water erosion'), ('rain washing soil off a hill', 'Water erosion'),
                                                                  ('sand blown onto a field', 'Wind erosion'), ('dust storms in dry land', 'Wind erosion'), ('sand dunes moving on a beach', 'Wind erosion')]), marks=6),
    Q('True or false?', TrueFalse([
        ('Plant roots help hold soil in place.', True),
        ('Rivers only take land away; they never build new land.', False, 'Rivers drop mud and sand that builds new land, such as chars.'),
        ('A system is a group of parts that work together.', True)]), marks=3),
])

think = Sheet('think', 'Choosing the best solution', level=2, goals=['Compare solutions.', 'Explain using evidence.'], blocks=[
    Q('Why is erosion worse on a hill where all the trees have been cut down?', Lines(3, 'With no roots to hold the soil and no leaves to slow the rain, rain washes the soil straight down the hill, causing erosion and landslides.'), marks=2),
    Q('A village is beside a fast river that is eating away its bank. Compare two solutions and choose the best one. Explain why.',
      Table(['', 'Solution 1: ________', 'Solution 2: ________'], [['good points', Ans('geo-bags: quick, cheaper'), Ans('trees: cheap, natural')], ['problems', Ans('can be washed away'), Ans('too slow for a fast river now')]],
            widths=['22%', '39%', '39%']),
      Lines(2, 'e.g. geo-bags now, because they work quickly; then plant grass and trees behind them for the future.'), marks=4),
    Q('A coastal defence system has mangroves, an embankment and sluice gates. What would happen if the sluice gates were left open during a storm surge?',
      Lines(2, 'Sea water would flow through the gates into the fields behind the embankment, flooding them and making the soil salty.'), marks=2),
    Q('Draw a river bend. Show where erosion happens and where deposition happens.', Draw('40mm', 'River bend', 'Erosion on the outside of the bend (fast water); deposition (sand bar) on the inside (slow water).'), marks=2),
])

investigate = Sheet('investigate', 'Does a windbreak stop sand blowing away?', level=2, goals=['Carry out a fair test.', 'Measure mass.', 'Evaluate a solution.'], blocks=[
    P('Class 4B put 200 g of dry sand in each of three trays. They blew air across each tray with a fan for 1 minute, then weighed '
      'the sand that was left. Tray A had nothing, tray B had a row of small sticks (a model windbreak), and tray C had a row of sticks '
      'and the sand was damp.'),
    Q('Complete the plan.',
      Table(None, [['Change', Ans('what protects the sand (nothing, sticks, sticks and damp)')], ['Measure', Ans('mass of sand left (g)')],
                   ['Keep the same', Ans('amount of sand, fan speed, distance from the fan, time')]], widths=['26%', '74%']), marks=3),
    Q('Complete the table and draw a bar chart of the sand lost.',
      Table(['Tray', 'Sand at start (g)', 'Sand left (g)', 'Sand lost (g)'], [['A: nothing', '200', '110', Ans('90')], ['B: windbreak', '200', '170', Ans('30')], ['C: windbreak + damp', '200', '195', Ans('5')]], center=True),
      Graph(['A', 'B', 'C'], [90, 30, 5], 'Sand lost (g)', 'Tray', ymax=100, step=10, width=100, height=50), marks=4),
    Q('Write a conclusion.', Lines(2, 'A windbreak greatly reduces wind erosion, and damp sand blows away even less.'), marks=2),
    Q('How could farmers use these results?', Lines(1, 'Plant rows of trees around fields and keep soil covered or damp.'), marks=1),
])

case = Sheet('case', 'Living with a moving river', level=3, goals=['Understand river erosion in Bangladesh.', 'Use data about land loss.', 'Compare solutions from different viewpoints.'], blocks=[
    Links('Science', 'Geography', 'Maths', 'Economics', 'Citizenship'),
    Case('The **Jamuna** and **Padma** are among the biggest rivers in the world. Each monsoon they carry enormous amounts of water '
         'and sand. Their banks can collapse suddenly, and thousands of families lose their homes and fields to the river every year. '
         'People who lose their land often move to new chars or to the cities.',
         'Engineers protect important places, such as towns and the Padma Bridge, with **concrete blocks**, **geo-bags** and walls '
         'along the banks. This is called **river training**. But it is expensive, and protecting one place can make the river '
         'push harder somewhere else.',
         source='Based on reports about riverbank erosion in Bangladesh. Data below are example values.'),
    Q('Land lost to the river at one village (example data).',
      Table(['Year', '2019', '2020', '2021', '2022', '2023'], [['Land lost (hectares)', '12', '30', '8', '22', '10']], center=True),
      Graph(['2019', '2020', '2021', '2022', '2023'], [12, 30, 8, 22, 10], 'Land lost (hectares)', 'Year', ymax=35, step=5, width=110, height=50),
      Part('Draw the bar chart.'),
      Part('What is the total land lost in five years?', Lines(1, '12 + 30 + 8 + 22 + 10 = 82 hectares')),
      Part('The worst years had very big monsoon floods. Why does this make sense?', Lines(2, 'More fast-moving water has more energy to wear away the banks.')), marks=4),
    Q('What might each person want?',
      Table(['Person', 'View'], [['a farmer on the bank', Ans('Protect my village now with geo-bags; I will lose everything.')],
                                 ['an engineer', Ans('Concrete works but is costly; we must check it does not push the river onto other villages.')],
                                 ['a family on a new char', Ans('The river gave us new land, but floods can wash it away again.')]], widths=['30%', '70%']), marks=3),
    Q('If you were in charge of the money, how would you protect the village? Explain your plan.',
      Lines(3, 'e.g. geo-bags at the worst places now, plant grass and trees on the bank, move the school away from the edge, and an early warning when the bank is cracking.'), marks=2),
])

review = Sheet('review', 'Show what you know', level=3, goals=['Use key vocabulary.', 'Answer test-style questions.'], blocks=[
    Q('Find the key words.', WordSearch(['EROSION', 'RIVER', 'WIND', 'SOIL', 'ROOTS', 'CHAR', 'SAND', 'SYSTEM', 'BANK'], size=10, seed=409)),
    Q('Which is the best way to stop soil washing off a bare hill?', MCQ(['cut down more trees', 'plant trees and grass', 'build a road', 'burn the grass'], 1, one_col=True), marks=1),
    Q('Where does a river drop most of its mud?', MCQ(['where it flows fastest', 'where it slows down', 'at the top of a waterfall', 'on the outside of a bend'], 1, one_col=True), marks=1),
    Q('Draw a coastal defence system with three parts. Label each part and its job.',
      Draw('44mm', 'Coastal defence system', 'mangroves (slow waves) → embankment (holds back sea) → sluice gate (lets rain water out, keeps sea out).'), marks=3),
    Q('**Challenge.** Why might protecting one part of a river bank make erosion worse further down the river?', Lines(3, 'The water cannot wear away the protected bank, so it is pushed with more force against the next unprotected bank, eroding it faster.'), marks=2),
])

TOPIC = Topic(
    code='B3', strand='earth', title='Changing Landscapes', short='Changing landscapes',
    subtitle='Weathering, erosion and deposition by water and wind, solutions to slow erosion, and systems',
    outcomes=[
        'compare multiple solutions designed to slow or prevent wind or water from changing the shape of the land.',
        'understand that a system is a group of related parts that make up a whole, which can carry out functions its individual parts cannot.',
    ],
    sheets=[learn, facts, think, investigate, case, review],
    selfcheck=['explain weathering, erosion and deposition', 'describe how rivers and wind change the land', 'compare ways to slow erosion',
               'test a model windbreak', 'explain what a system is', 'suggest how to protect a village from river erosion'],
    cover_art=art4.erosion_fixes(),
)
