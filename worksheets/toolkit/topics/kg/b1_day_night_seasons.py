from build import Sheet, Topic
from ws import (P, H, Box, Fig, Q, Lines, MCQ, Draw, Pics, Ans, Case, Choose, PicMatch, PicSort, Pictograph, Trace)
import art

learn = Sheet('learn', 'Day, night and the weather', level=1, goals=['Talk about day and night.', 'Name kinds of weather and seasons.'], blocks=[
    Box('adult', P('Read aloud. Ask: "What do you do in the day? What do you do at night?"')),
    P('In the **day**, the Sun shines and the sky is bright. At **night**, the sky is dark. We may see the **Moon** and the **stars**.', 'lead'),
    Pics([('sunrise', 'morning'), ('sun', 'day'), ('night with stars', 'night'), ('moon', 'Moon')], cols=4, size='22mm'),
    H('Weather changes', 3),
    Pics([('sun', 'sunny'), ('cloud', 'cloudy'), ('rain cloud', 'rainy'), ('wind face', 'windy'), ('thunder cloud', 'stormy')], cols=5, size='19mm'),
    H('Seasons in Bangladesh', 3),
    P('In **summer** it is hot. In the **rainy season** it rains a lot. In **winter** it is cool and we wear warm clothes.'),
    Pics([('hot face', 'summer'), ('umbrella with rain', 'rainy season'), ('cold face', 'winter')], cols=3, size='22mm'),
    P('Families celebrate at special times: Pohela Boishakh welcomes the new year, and Eid begins when people see the new Moon.'),
])

facts = Sheet('facts', 'Day or night?', level=1, goals=['Sort day and night things.', 'Match weather to clothes.'], blocks=[
    Q('Cut and sort: **day** or **night**?', PicSort(['Day', 'Night'], [('sun', 'Sun', 'Day'), ('school', 'school', 'Day'), ('sunrise', 'sunrise', 'Day'),
                                                                     ('moon', 'Moon', 'Night'), ('bed', 'bed', 'Night'), ('star', 'stars', 'Night')], height='32mm')),
    Q('Match the weather to what you need.', PicMatch([(('rain cloud', 'rainy'), ('umbrella', 'umbrella')), (('sun', 'sunny'), ('water glass', 'cool water')),
                                                       (('cold face', 'cold'), ('scarf', 'warm scarf'))], size='15mm')),
])

think = Sheet('think', 'What do I do?', level=2, goals=['Order my day.', 'Draw the weather.'], blocks=[
    Q('Put my day in order. Write **1**, **2**, **3**.', Pics([('bed', Ans('3')), ('sunrise', Ans('1')), ('school', Ans('2'))], cols=3, size='24mm')),
    Q('Look outside. Draw today\'s weather.', Draw('50mm', 'Today the weather is…', 'Any weather, e.g. a Sun for sunny or clouds and rain for rainy.')),
])

investigate = Sheet('investigate', 'Our weather chart', level=2, goals=['Watch the weather every day.', 'Make a picture graph.'], blocks=[
    Box('adult', P('Each morning for two weeks, look at the sky together and colour one box for that kind of weather.')),
    Q('Our weather for two weeks. Colour one box each day.', Pictograph([('sun', 'sunny', 5), ('cloud', 'cloudy', 3), ('rain cloud', 'rainy', 2)], top=10)),
    Q('What weather did we have the most? Circle it.', Choose([('sun', 'sunny'), ('cloud', 'cloudy'), ('rain cloud', 'rainy')], right=[0], cols=3)),
])

case = Sheet('case', 'Mitu watches the Moon', level=3, goals=['Listen to a story.', 'Notice patterns in the sky.'], blocks=[
    Case('Every night Mitu looked at the Moon from her window. Some nights it was a thin smile. Some nights it was round and bright.',
         'One evening the whole family looked for a very thin new Moon. "There it is!" said Mitu. "Tomorrow is Eid!"'),
    Q('When do we see the Moon? Circle.', Choose([('sun', 'in the day'), ('night with stars', 'at night')], right=[1], cols=2)),
    Q('Draw the Moon you saw last night.', Draw('38mm', '', 'Any Moon shape: thin crescent, half or full Moon.')),
])

review = Sheet('review', 'I can do it!', level=3, goals=['Trace sky words.'], blocks=[
    Q('Trace the words.', Trace([('Sun', 'sun'), ('Moon', 'moon')])),
    Q('Circle what you need on a **rainy** day.', Choose([('umbrella', 'umbrella'), ('sun', 'Sun'), ('ice cream', 'ice cream')], right=[0], cols=3)),
])

TOPIC = Topic(
    code='B1', strand='earth', title='Day, Night and Seasons', short='Day and night',
    subtitle='Day and night, the Sun, Moon and stars, weather, and the seasons of Bangladesh',
    outcomes=[
        'make observations at different times of the day, week and year to relate the amount of daylight to the time of year.',
        'identify different aspects of patterns and cycles in their authentic environments — for example weather, night and day, and the seasons.',
        'make connections between cycles and changes in the environment and other cultural perspectives.',
    ],
    sheets=[learn, facts, think, investigate, case, review],
    selfcheck=['say what happens in the day and at night', 'name kinds of weather', 'keep a weather chart'],
    cover_art=art.pic_row(['sunrise', 'sun', 'rain cloud', 'night with stars', 'moon'], ['morning', 'day', 'rain', 'night', 'Moon']),
)
