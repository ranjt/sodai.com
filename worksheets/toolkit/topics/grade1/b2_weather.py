from build import Sheet, Topic
from ws import (P, H, Box, Vocab, Fig, Q, Lines, Blanks, Match, TrueFalse, MCQ, Table, Ans, Sort, Draw, Graph, WordSearch, Bullets, Pics,
                Choose, PicMatch, PicSort, Pictograph, Trace, Case)
import art

learn = Sheet('learn', 'Weather watching', level=1, goals=['Name kinds of weather.', 'Record the weather.'], blocks=[
    P('**Weather** is what the air outside is like: hot or cold, wet or dry, still or windy. It changes from day to day.', 'lead'),
    Pics([('sun', 'sunny'), ('cloud', 'cloudy'), ('rain cloud', 'rainy'), ('wind face', 'windy'), ('thunder cloud', 'stormy'), ('fog', 'foggy')], cols=6, size='17mm'),
    H('Measuring the weather', 3),
    Table(['We want to know…', 'We use…'], [['how hot or cold', 'a **thermometer**'], ['how much rain', 'a **rain gauge** (a bottle that collects rain)'], ['which way the wind blows', 'a **wind sock** or a flag']]),
    Pics([('thermometer', 'thermometer'), ('glass bottle', 'rain gauge'), ('flag', 'wind flag')], cols=3, size='20mm'),
    H('Patterns in the weather', 3),
    P('In Bangladesh, the weather follows a pattern through the year: hot **summer**, the wet **rainy season** (monsoon), and cool **winter**. Weather forecasters use patterns to tell us what tomorrow will be like.'),
    Vocab([('weather', 'what the air outside is like each day'), ('season', 'a time of year with its own weather'), ('forecast', 'telling what the weather will be')]),
])

facts = Sheet('facts', 'Weather words', level=1, goals=['Match weather to symbols and clothes.'], blocks=[
    Q('Match the weather to what you wear or use.', PicMatch([(('rain cloud', 'rainy'), ('umbrella', 'umbrella')), (('sun', 'sunny'), ('glasses', 'sun hat and glasses')),
                                                              (('cold face', 'cold'), ('scarf', 'scarf and jumper'))], size='15mm')),
    Q('Fill in the gaps.', Blanks('We measure how hot it is with a [thermometer]. We measure rain with a [rain gauge].', extra=['ruler'])),
])

think = Sheet('think', 'Weather and us', level=2, goals=['Explain how weather changes what we do.'], blocks=[
    Q('How does the rainy season change what farmers do?', Lines(2, 'They plant rice when the fields have water; they wait for rain.')),
    Q('Draw what you do on a hot sunny day.', Draw('42mm', '', 'e.g. drink water, sit in the shade, wear a hat.')),
])

investigate = Sheet('investigate', 'Our weather chart', level=2, goals=['Record the weather for two weeks.', 'Read a bar chart.'], blocks=[
    P('Class 1 looked at the sky every morning for 10 school days.'),
    Q('Our results. Draw the bars.', Table(['Weather', 'sunny', 'cloudy', 'rainy'], [['Days', '5', '3', '2']], center=True),
      Graph(['sunny', 'cloudy', 'rainy'], [5, 3, 2], 'Days', 'Weather', ymax=6, step=1, width=78, height=44)),
    Q('What was the most common weather?', MCQ(['sunny', 'cloudy', 'rainy'], 0)),
    Q('Make a rain gauge: cut the top off a bottle and mark a ruler on the side. Draw it.', Draw('36mm', '', 'A bottle with the top turned upside down as a funnel and marks for centimetres.')),
])

case = Sheet('case', 'The monsoon comes', level=3, goals=['Read about the rainy season.'], blocks=[
    Case('In June, dark clouds fill the sky over Bangladesh. Then the rain comes: the **monsoon**! Rivers fill up and the fields turn green.',
         'Farmers plant rice. Children float paper boats. But too much rain can bring floods, so people listen to the weather forecast on the radio.'),
    Q('Write one good thing about the monsoon.', Lines(1, 'water for rice fields; the land turns green')),
    Q('Write one problem the monsoon can bring.', Lines(1, 'floods')),
])

review = Sheet('review', 'Show what you know', level=3, goals=['Use weather words.'], blocks=[
    Q('Find the words.', WordSearch(['RAIN', 'SUN', 'WIND', 'CLOUD', 'HOT'], size=7, seed=106)),
    Q('Which tool measures rain?', MCQ(['thermometer', 'rain gauge', 'clock'], 1)),
])

TOPIC = Topic(
    code='B2', strand='earth', title='Weather Watching', short='Weather',
    subtitle='Kinds of weather, measuring and recording the weather, and seasonal patterns',
    outcomes=[
        'observe and talk about the weather, recording reports of weather data.',
        'identify different aspects of patterns and cycles in the environment around them.',
        'identify water as a resource that cycles through the environment.',
    ],
    sheets=[learn, facts, think, investigate, case, review],
    selfcheck=['name kinds of weather', 'keep a weather chart', 'say how weather changes through the year'],
    cover_art=art.pic_row(['sun', 'cloud', 'rain cloud', 'wind face', 'thunder cloud'], ['sunny', 'cloudy', 'rainy', 'windy', 'stormy']),
)
