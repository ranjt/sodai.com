from build import Sheet, Topic
from ws import (P, H, Box, Vocab, Fig, Cols, Row, Case, Links, Lines, Blanks, Match, TrueFalse, MCQ, Order, Table,
                Ans, Sort, Label, Draw, Graph, WordSearch, Q, Part, Bullets, Pics)
import art
import art4

learn = Sheet('learn', 'Weather, climate and how we measure them', level=1, goals=[
    'Explain the difference between weather and climate.',
    'Explain how air moves when one place is warm and another is cool.',
    'Name weather instruments and cloud types, and use them to forecast the weather.',
], blocks=[
    P('Will it rain on Sports Day? Should the farmer harvest the rice this week? Is a storm coming? People have always '
      'watched the sky to answer questions like these. Today, scientists called **meteorologists** use instruments, '
      'satellites and computers, but you can still be a weather detective with simple tools.', 'lead'),
    Cols(
        H('Weather or climate?', 3),
        P('**Weather** is what the air is like **today or this week**: hot or cold, wet or dry, windy or calm, sunny or cloudy. '
          'It can change in a few hours. **Climate** is the **usual** weather of a place, worked out by measuring the weather '
          'for **many years** (usually 30).'),
        Box('tip', P('"It is raining in Dhaka today" is **weather**. "Dhaka has hot, wet summers and cool, dry winters" is **climate**.')),
        H('The climate of Bangladesh', 3),
        Table(['Season', 'Months (about)', 'Usual weather'], [
            ['summer (pre-monsoon)', 'March – May', 'very hot; sudden storms (*kalbaishakhi*)'],
            ['monsoon', 'June – October', 'warm, very wet, humid; most of the year\'s rain'],
            ['winter', 'November – February', 'cool, dry, foggy mornings']]),
        P('Weather and climate affect **living things**: rice is planted when the monsoon rains come, many birds arrive in '
          'winter, and people wear lighter clothes in summer. They also affect **non-living things**: heavy rain makes rivers '
          'flood, and heat and rain slowly break up rocks and roads.'),
        H('Warm places and cool places', 3),
        P('Outdoors, it is warmest in **direct sunshine**, especially on dark surfaces like roads and tin roofs. It is coolest '
          'in the **shade** of trees and near water. Indoors, rooms with sunny windows and rooms under a tin roof are warmer. '
          'Warm air **rises**, so the air near the ceiling is warmer than near the floor.'),
        H('How air moves', 3),
        P('When air is warmed it spreads out, becomes lighter and **rises**. Cooler air moves in to take its place. This moving '
          'air is **wind**. On a sunny day near the sea, the land warms up faster than the water, so a cool **sea breeze** blows '
          'from the sea to the land. At home, opening a low window and a high window lets cool air in and hot air out.'),
        Fig(art4.sea_breeze(), 'A sea breeze on a sunny day.', width='92%'),
        H('Measuring the weather', 3),
        Fig(art4.weather_instruments(), 'Weather instruments.', span=True, width='90%'),
        Table(['Instrument', 'Measures', 'Unit or reading'], [
            ['thermometer', 'temperature', 'degrees Celsius (°C)'], ['rain gauge', 'rainfall', 'millimetres (mm)'],
            ['wind vane', 'wind direction (where the wind comes **from**)', 'N, S, E, W'], ['anemometer', 'wind speed', 'km/h (or how fast the cups spin)'],
            ['barometer', 'air pressure', 'falling pressure often means a storm is coming']]),
        Box('safety', P('Put a thermometer in the **shade**, about 1.5 m above the ground. In direct sunshine it shows the temperature of the sunshine, not the air!')),
        H('Reading the clouds', 3),
        Fig(art4.cloud_types(), 'Four common cloud types.', span=True, width='90%'),
        P('Clouds give clues. **White, puffy** clouds mean fine weather. **Dark grey** clouds hold more water and often bring rain. '
          'Clouds that grow **tall** in the afternoon can become thunderstorms. If clouds move quickly, the wind is strong. A '
          'change of wind direction, falling pressure and very damp air can all mean the weather is about to change.'),
        H('Make your own forecast', 3),
        P('A **forecast** is a prediction of the weather. Scientists record measurements every day, look for **trends** (patterns '
          'over time), and compare them with what happened before. You can do the same with a class weather station.'),
        Box('bd', P('The **Bangladesh Meteorological Department** (BMD) measures the weather at stations all over the country and '
                    'gives forecasts and storm warnings on radio, TV, mobile phones and the internet.')),
    ),
    Vocab([('weather', 'what the air is like today: temperature, rain, wind, clouds'), ('climate', 'the usual weather of a place over many years'),
           ('forecast', 'a prediction of the weather'), ('rain gauge', 'collects and measures rainfall'), ('wind vane', 'shows wind direction'),
           ('anemometer', 'measures wind speed'), ('barometer', 'measures air pressure'), ('humid', 'damp air with a lot of water vapour')]),
])

facts = Sheet('facts', 'Weather words and tools', level=1, goals=['Tell weather from climate.', 'Match instruments to measurements.', 'Name cloud types.'], blocks=[
    Q('Weather or climate? Tick one.',
      Table(['Sentence', 'Weather', 'Climate'], [['It is very windy this afternoon.', Ans('✓'), Ans('')], ['Sylhet gets a lot of rain every year.', Ans(''), Ans('✓')],
                                                 ['Tomorrow will be foggy.', Ans('✓'), Ans('')], ['Bangladesh has a monsoon season every summer.', Ans(''), Ans('✓')]],
            center=True, widths=['64%', '18%', '18%']), marks=4),
    Q('Write the name of each instrument and what it measures.', Fig(art4.weather_instruments(names=False), width='88%'),
      Table(['Letter', 'Instrument', 'Measures'], [[chr(65 + i), Ans(n), Ans(m)] for i, (n, m) in enumerate(zip(art4.WEATHER_INSTRUMENTS, art4.WEATHER_MEASURES))], center=True), marks=10),
    Q('Name each cloud type.', Fig(art4.cloud_types(names=False), width='80%'),
      Table(['A', 'B', 'C', 'D'], [[Ans('cumulus'), Ans('stratus'), Ans('cirrus'), Ans('cumulonimbus')]], center=True), marks=4),
    Q('Fill in the gaps.', Blanks('Warm air [rises]. Cool air moves in to take its place. Moving air is called [wind]. '
                                  'A thermometer should be kept in the [shade].', extra=['sinks', 'sun']), marks=3),
])

think = Sheet('think', 'Thinking about air and weather', level=2, goals=['Predict warm and cool places.', 'Explain air movement.', 'Use clues to forecast.'], blocks=[
    Q('Rina measured the temperature in four places at school at 12 noon.',
      Table(['Place', 'Temperature (°C)'], [['under a big tree', '29'], ['on the tin roof of the shed', '45'], ['in the classroom (fan on)', '31'], ['on the concrete playground in sun', '38']], center=True),
      Part('Which was the warmest place? Explain why.', Lines(2, 'The tin roof (45 °C): it is dark metal in direct sunshine and takes in a lot of heat.')),
      Part('Which was the coolest place? Explain why.', Lines(2, 'Under the big tree (29 °C): the leaves shade the ground from the sun.')), marks=4),
    Q('Why do many old houses in Bangladesh have small openings high up in the walls?', Lines(2, 'Warm air rises and escapes through the high openings, and cooler air comes in lower down, keeping the house cool.'), marks=2),
    Q('The barometer is falling, the wind has changed direction and tall dark clouds are growing. What weather would you forecast? Why?',
      Lines(3, 'A storm with heavy rain and thunder, because falling pressure, changing wind and tall dark (cumulonimbus) clouds are signs of a storm.'), marks=3),
    Q('Draw a sea breeze. Label the warm land, the cool sea and arrows to show how the air moves.', Draw('40mm', 'Sea breeze', 'Air rises over warm land, moves out to sea high up, sinks over the cool sea and blows onto the land as a breeze.'), marks=3),
])

investigate = Sheet('investigate', 'A week at our weather station', level=2, goals=['Record weather data.', 'Draw a line graph.', 'Make a forecast from trends.'], blocks=[
    P('Class 4A recorded the weather at 9 o\'clock every morning for one week in June.'),
    Table(['Day', 'Sun', 'Mon', 'Tue', 'Wed', 'Thu'], [['Temperature (°C)', '31', '32', '30', '28', '27'], ['Rainfall (mm)', '0', '2', '10', '25', '30'],
                                                      ['Wind direction', 'S', 'S', 'SE', 'SE', 'SE'], ['Clouds', 'a few cumulus', 'more cumulus', 'grey sheet', 'dark, tall', 'dark, tall'],
                                                      ['Pressure', 'steady', 'falling', 'falling', 'falling', 'low']], center=True),
    Q('Draw a line graph of the temperature.', Graph(['Sun', 'Mon', 'Tue', 'Wed', 'Thu'], [31, 32, 30, 28, 27], 'Temperature (°C)', 'Day', ymax=34, ymin=24, step=1, kind='line', width=120, height=50), marks=3),
    Q('Describe the trend in rainfall during the week.', Lines(2, 'Rainfall increased every day, from 0 mm on Sunday to 30 mm on Thursday.'), marks=2),
    Q('Forecast the weather for Friday. Use at least two pieces of evidence.', Lines(3, 'Wet and cool again: rainfall is increasing, the pressure is low, the clouds are dark and tall and the wind comes from the sea (south-east), bringing monsoon rain.'), marks=3),
    Q('Why did they measure at the same time every day?', Lines(1, 'So the results can be compared fairly (temperature changes during the day).'), marks=1),
])

case = Sheet('case', 'Harvest before the flood: forecasts for haor farmers', level=3, goals=['See how forecasts help people.', 'Use rainfall data.', 'Weigh up choices.'], blocks=[
    Links('Science', 'Farming', 'Maths', 'Technology'),
    Case('In the **haor** wetlands of the north-east, farmers grow **boro rice** in the dry season. The rice is ready to harvest '
         'in **April and May**. But heavy rain in the nearby hills can send a sudden **flash flood** rushing into the haor in just '
         'a day or two, drowning the whole crop.',
         'Today, the **Bangladesh Meteorological Department** and the flood forecasting centre send warnings by radio, TV, '
         'mobile phone messages and local announcements. If a farmer knows heavy rain is coming, they can harvest early, even '
         'if the rice is not completely ripe, and save most of the crop.',
         source='Based on information about flash floods in the haors and early-warning services in Bangladesh. Data below are example values.'),
    Q('Forecast rainfall in the hills for the next five days (example).',
      Table(['Day', '1', '2', '3', '4', '5'], [['Rain forecast (mm)', '5', '10', '60', '120', '80']], center=True),
      Graph(['1', '2', '3', '4', '5'], [5, 10, 60, 120, 80], 'Rain (mm)', 'Day', ymax=130, step=10, width=110, height=50),
      Part('Draw the bar chart.'),
      Part('On which day should the farmer start harvesting? Explain.', Lines(2, 'Day 1 or 2: heavy rain starts on day 3 and the flood could come soon after, so harvest before then.')), marks=3),
    Q('A farmer says, "My rice needs one more week to ripen." What should they do? Give reasons for your answer.',
      Lines(3, 'Harvest now: slightly unripe rice still gives some food and money, but a flash flood would destroy all of it.'), marks=2),
    Q('Why are mobile phone messages a good way to warn farmers?', Lines(2, 'Almost every family has a mobile phone; messages arrive quickly and reach people in remote places.'), marks=2),
    Q('Design a simple sign that a village could put up to show the flood risk this week (low, medium, high).',
      Draw('34mm', 'Flood risk sign', 'e.g. a dial or three flags with pictures (sun / cloud / heavy rain), easy to read for everyone.'), marks=2),
])

review = Sheet('review', 'Show what you know', level=3, goals=['Use key vocabulary.', 'Answer test-style questions.'], blocks=[
    Q('Find the key words.', WordSearch(['WEATHER', 'CLIMATE', 'CLOUD', 'WIND', 'RAIN', 'GAUGE', 'FORECAST', 'MONSOON', 'VANE'], size=11, seed=407)),
    Q('Which instrument measures wind speed?', MCQ(['barometer', 'anemometer', 'thermometer', 'rain gauge'], 1), marks=1),
    Q('Which cloud is most likely to bring a thunderstorm?', MCQ(['cirrus', 'cumulus', 'cumulonimbus', 'stratus'], 2), marks=1),
    Q('Design a simple rain gauge from a plastic bottle. Draw and label it.', Draw('46mm', 'My rain gauge', 'Cut the top off a bottle and turn it upside down as a funnel; mark a ruler scale in mm on the side; put stones in the bottom so it does not blow over; place it in the open.'), marks=3),
    Q('**Challenge.** Explain how wind is made. Use the words **warm**, **rises** and **cool**.', Lines(3, 'The Sun warms the ground, which warms the air above it. Warm air rises and cooler air moves in to take its place. This moving air is wind.'), marks=2),
])

TOPIC = Topic(
    code='B1', strand='earth', title='Weather and Climate', short='Weather and climate',
    subtitle='Weather and climate, warm and cool places, moving air, weather instruments, clouds and forecasts',
    outcomes=[
        'distinguish between climate and weather, and explain the general effects of each on living and non-living things.',
        'make observations and predict where, in any given indoor or outdoor environment, one might find the warmest and coolest temperatures.',
        'explain the patterns of air movement, indoors and outdoors, that occur when one area is warm and another is cool.',
        'build and use simple devices to measure ambient temperature, wind speed, wind direction and rainfall, and use a barometer to measure atmospheric pressure.',
        'recognize common types of cloud and relate them to different weather patterns.',
        'determine possible changes to the local weather by observing cloud cover, cloud type and colour, cloud movement, changing wind direction and speed, air moisture and other measured data.',
        'make their own weather forecast by recording weather measurements over a period of time and analyzing trends.',
    ],
    sheets=[learn, facts, think, investigate, case, review],
    selfcheck=['explain weather and climate', 'predict warm and cool places', 'explain how warm and cool air move',
               'use weather instruments', 'name four cloud types', 'make a forecast from a week of data'],
    cover_art=art4.weather_instruments(),
)
