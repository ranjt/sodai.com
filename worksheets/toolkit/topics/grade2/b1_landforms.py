from build import Sheet, Topic
from ws import (P, H, Box, Vocab, Fig, Cols, Row, Case, Links, Lines, Blanks, Match, TrueFalse, MCQ, Order, Table,
                Ans, Sort, Label, Draw, Graph, WordSearch, Q, Part, Bullets, Pics)
import art
import art23

learn = Sheet('learn', 'Mountains, rivers and islands', level=1, goals=[
    'Name landforms: mountains, hills, valleys, caves, plains and islands.',
    'Find landforms in Bangladesh and in other countries.',
    'Explain how wind and water change the land, quickly or slowly.',
], blocks=[
    P('The land is not flat everywhere. There are high mountains, round hills, deep valleys and islands in the sea. These shapes of the land are called **landforms**.', 'lead'),
    Fig(art23.landforms(), 'Six landforms.', width='88%'),
    Table(['Landform', 'What it is'], [['**mountain**', 'very high land with steep sides'], ['**hill**', 'raised land, lower and rounder than a mountain'],
                                       ['**valley**', 'low land between hills or mountains, often with a river'], ['**cave**', 'a big hole in rock, under the ground or in a hill'],
                                       ['**plain**', 'wide, flat land'], ['**island**', 'land with water all around it']]),
    H('Landforms in Bangladesh', 3),
    P('Most of Bangladesh is a huge, flat **plain**, made by rivers. In the south-east there are **hills** in Chattogram, Rangamati and Bandarban. '
      'There are many **islands**, such as Saint Martin\'s Island and Bhola. Other countries have different landforms: Nepal has the '
      'tallest **mountains** in the world, including Mount Everest.'),
    H('Wind and water change the land', 3),
    P('**Rivers** carry away soil from their banks and drop it in other places, making new land called **chars**. **Rain** washes soil down hills. '
      '**Waves** wear away the coast. **Wind** blows sand into dunes on beaches.'),
    H('Fast and slow changes', 3),
    Table(['Fast changes', 'Slow changes'], [['**earthquakes** shake the ground', 'rivers slowly wear away rock'], ['**volcanoes** erupt with hot lava', 'wind slowly moves sand'],
                                            ['**floods** and **landslides** happen in a day', 'mountains take millions of years to grow']]),
    P('Changes can be **good**: floods bring rich new soil for crops. They can be **bad**: river banks fall in and people lose their homes.'),
    Box('bd', P('Keokradong in Bandarban is one of the highest hills in Bangladesh, about 1000 metres high.')),
    Vocab([('landform', 'a natural shape of the land'), ('plain', 'flat land'), ('island', 'land with water all round'), ('erosion', 'land worn away by water or wind')]),
])

facts = Sheet('facts', 'Name the landform', level=1, goals=['Name landforms.'], blocks=[
    Q('Write the name of each landform.', Fig(art23.landforms(names=False), width='86%'),
      Table(['A', 'B', 'C', 'D', 'E', 'F'], [[Ans('mountain'), Ans('hill'), Ans('valley'), Ans('cave'), Ans('plain'), Ans('island')]], center=True), marks=6),
    Q('Draw a line to match.', Match([('island', 'land with water all round'), ('valley', 'low land between hills'), ('mountain', 'very high land'), ('plain', 'wide flat land')]), marks=4),
    Q('Fast or slow?', Sort(['Fast change', 'Slow change'], [('earthquake', 'Fast change'), ('landslide', 'Fast change'), ('a river wearing away rock', 'Slow change'), ('a mountain growing', 'Slow change')]), marks=4),
])

think = Sheet('think', 'Changing land', level=2, goals=['Explain how water and wind change land.'], blocks=[
    Q('How can a river make a new island (char)?', Lines(2, 'The river drops sand and mud in the middle, and it builds up into new land.'), marks=2),
    Q('A flood brings new mud to a farmer\'s field. Is this good or bad? Why?', Lines(2, 'Good: the mud makes the soil rich for crops. (But floods can also damage homes.)'), marks=2),
    Q('Draw a landform you have seen. Label it.', Draw('44mm', 'A landform I have seen', 'e.g. a river and its bank, a hill, the beach.'), marks=2),
])

investigate = Sheet('investigate', 'Rain on a sand hill', level=2, goals=['Make a model.', 'Observe and explain.'], blocks=[
    P('Class 2B made two sand hills on trays. They covered one with grass. Then they poured the same amount of water on top of each one, like rain.'),
    Q('What do you think will happen? Predict.', Lines(1, 'The bare hill will wash away more.'), marks=1),
    Q('Results: draw the two hills after the "rain".', Row([Draw('30mm', 'bare sand hill', 'flatter, sand washed down')], [Draw('30mm', 'hill with grass', 'still mostly the same shape')]), marks=2),
    Q('Which hill washed away more? Why?', Lines(2, 'The bare hill; grass roots hold the sand together.'), marks=2),
])

case = Sheet('case', 'A new island in the river', level=3, goals=['Learn about chars in Bangladesh.'], blocks=[
    Links('Science', 'Geography', 'People'),
    Case('In the big rivers of Bangladesh, sand and mud slowly pile up to make new islands called **chars**. After a few years, '
         'grass grows on them. Then families come to live there. They grow rice, keep cows and catch fish.',
         'But the river is always moving. Sometimes it washes part of a char away, and families must move their houses. Char people are very good at changing their plans when the river changes.',
         source='Based on life on river chars in Bangladesh.'),
    Q('How is a char made?', Lines(2, 'The river drops sand and mud, which piles up into new land.'), marks=2),
    Q('What do families do on a char?', Lines(1, 'grow rice, keep cows, catch fish'), marks=2),
    Q('Is a char a fast change or a slow change? Explain.', Lines(2, 'Mostly slow: it builds up over years (but parts can wash away quickly in floods).'), marks=1),
])

review = Sheet('review', 'Show what you know', level=3, goals=['Use landform words.'], blocks=[
    Q('Find the words.', WordSearch(['HILL', 'CAVE', 'RIVER', 'ISLAND', 'PLAIN', 'VALLEY'], size=8, seed=208)),
    Q('Land with water all around it is…', MCQ(['a valley', 'an island', 'a cave'], 1), marks=1),
    Q('Most of Bangladesh is…', MCQ(['a flat plain', 'high mountains', 'desert'], 0), marks=1),
    Q('**Challenge.** Draw a picture with a mountain, a valley and a river.', Draw('46mm', 'My landscape', 'Mountain with a valley below and a river flowing through it.'), marks=3),
])

TOPIC = Topic(
    code='B1', strand='earth', title='Landforms and Changes', short='Landforms',
    subtitle='Mountains, hills, valleys, caves, plains and islands, and how wind and water change the land',
    outcomes=[
        'identify a variety of the Earth\'s surface features that are landforms — mountains, valleys, hills, caves, flatlands and islands.',
        'identify and describe natural landforms found in their local area, within Bangladesh and in other countries, and note the similarities and differences between them.',
        'discuss how landform changes are brought about, and how those changes can be positive or negative for humans, animals and plants.',
        'explain how wind and water change the Earth.',
        'identify events that occur quickly or slowly on Earth — for example volcanic activity, earthquakes and erosion.',
        'discuss how the environment affects humans and other living things.',
    ],
    cambridge=['Stage 2 Unit 1 Going outside (1.2–1.4)'],
    sheets=[learn, facts, think, investigate, case, review],
    selfcheck=['name six landforms', 'find landforms in Bangladesh', 'explain how water and wind change the land', 'sort fast and slow changes', 'model rain on a hill'],
    cover_art=art23.landforms(),
)
