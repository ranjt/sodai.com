from build import Sheet, Topic
from ws import (P, H, Box, Vocab, Fig, Cols, Row, Case, Links, Lines, Blanks, Match, TrueFalse, MCQ, Order, Table,
                Ans, Sort, Label, Draw, Graph, WordSearch, Q, Part, Bullets)
import art

learn = Sheet('learn', 'Earth, Sun and Moon: days, years and seasons', level=1, goals=[
    'Explain day and night and the apparent movement of the Sun.',
    'Explain why different places have different seasons.',
    'Describe the solar system and how scientists came to understand it.',
], blocks=[
    P('Every morning the Sun seems to rise in the **east**, climb across the sky and set in the **west**. For thousands of '
      'years people believed the Sun travelled around the Earth. Today we know it is the **Earth that moves**.', 'lead'),
    Cols(
        H('Day and night: the Earth spins', 3),
        P('The Earth spins on an imaginary line through the North and South Poles called its **axis**. One complete spin '
          '(a **rotation**) takes **24 hours**. The half of the Earth facing the Sun has **day**; the half facing away has '
          '**night**. Because the Earth spins from west to east, the Sun *appears* to move from east to west.'),
        Fig(art.day_night()),
        H('The Sun\'s path and shadows', 3),
        P('In the morning the Sun is low in the east and shadows are long, pointing west. At midday the Sun is highest and '
          'shadows are shortest. In the evening shadows are long again, pointing east.'),
        Fig(art.sun_path(), span=True, width='85%'),
        H('A year: the Earth orbits the Sun', 3),
        P('The Earth travels around the Sun in a path called an **orbit**. One orbit takes about **365¼ days**, which is one '
          '**year**. The extra quarter day adds up to one extra day every four years: a **leap year** with 29 February.'),
        H('Why are there seasons?', 3),
        P('The Earth\'s axis is **tilted** by about 23.5°. As the Earth orbits, the northern half is tilted **towards** the '
          'Sun for part of the year: sunlight hits it more directly, days are longer, and it is **summer**. Six months later '
          'it is tilted **away**: sunlight is spread out, days are shorter, and it is **winter**. When it is summer in '
          'Bangladesh, it is winter in Australia!'),
        Fig(art.seasons_orbit(), span=True, width='85%'),
        P('Places near the **equator**, such as Singapore, have about 12 hours of daylight all year and no real summer or '
          'winter. Places near the **poles** have the biggest changes: in summer the Sun never sets (the "midnight sun"), and '
          'in winter it never rises. Bangladesh is near the **Tropic of Cancer**, which actually passes through the country.'),
        H('The Moon', 3),
        P('The Moon orbits the Earth about once a month. It does not make its own light: we see it because it **reflects** '
          'sunlight. As it orbits, we see different amounts of its lit half, so its shape seems to change. These are its '
          '**phases**, from new moon to full moon and back in about 29½ days. The Islamic calendar follows the Moon.'),
        H('The solar system', 3),
        P('The Sun is a **star**. Eight **planets** orbit it: Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus and Neptune. '
          'A sentence can help you remember the order: "**M**y **V**ery **E**asy **M**ethod **J**ust **S**peeds **U**p **N**aming".'),
        Fig(art.solar_system(), span=True),
        H('Stars and how scientists learned', 3),
        P('Stars are huge, hot balls of gas, like the Sun but much further away. Groups of stars that make patterns are '
          '**constellations**. In Bangla, Orion is *Kalpurush* and the Great Bear\'s seven bright stars are *Saptarshi Mandal*. '
          'Around 1500 years ago the Indian astronomer **Aryabhata** suggested the Earth spins. In 1543 **Copernicus** argued that '
          'the Earth goes around the Sun, and in 1610 **Galileo** used a telescope to see moons orbiting Jupiter, which was '
          'strong evidence that not everything orbits the Earth.'),
    ),
    Vocab([('axis', 'imaginary line the Earth spins around'), ('rotation', 'one complete spin (24 hours)'),
           ('orbit', 'the path of one object around another'), ('tilt', 'the lean of the Earth\'s axis (about 23.5°)'),
           ('equator', 'imaginary line around the middle of the Earth'), ('phases of the Moon', 'the changing shapes of the Moon we see'),
           ('planet', 'a large body that orbits a star'), ('constellation', 'a pattern of stars')]),
])

facts = Sheet('facts', 'Days, years and planets', level=1, goals=['Recall facts about the Earth, Sun and Moon.', 'Order the planets.'], blocks=[
    Q('Fill in the gaps.',
      Blanks('The Earth spins on its [axis] once every [24] hours, causing day and night. It orbits the Sun once every '
             '[365¼] days. The Moon [reflects] light from the Sun. The Sun rises in the [east] and sets in the [west].',
             extra=['12', 'north']), marks=6),
    Q('Number the planets in order from the Sun (1 = closest).',
      Order(art.PLANETS, seed=9), marks=4),
    Q('True or false?', TrueFalse([
        ('The Sun moves around the Earth every day.', False, 'The Earth spins; the Sun only appears to move.'),
        ('The Moon makes its own light.', False, 'It reflects sunlight.'),
        ('When it is summer in Bangladesh it is winter in Australia.', True),
        ('Shadows are shortest at midday.', True),
        ('The Sun is a star.', True)]), marks=5),
    Q('Match each word to its meaning.',
      Match([('rotation', 'one spin of the Earth on its axis'), ('orbit', 'the path of the Earth around the Sun'),
             ('leap year', 'a year with 366 days'), ('constellation', 'a pattern of stars')]), marks=4),
])

think = Sheet('think', 'Explaining what we see', level=2, goals=['Explain day, night and seasons with diagrams.', 'Use models.'], blocks=[
    Q('Shade the night side of the Earth and label day and night.',
      Draw('45mm', 'Sun on the left, Earth on the right', 'The half of the Earth facing away from the Sun is shaded and labelled night; the half facing the Sun is labelled day.'), marks=2),
    Q('Explain why it is daytime in Dhaka when it is night-time in New York.',
      Lines(3, 'They are on opposite sides of the Earth: when Dhaka faces the Sun, New York faces away from it.'), marks=2),
    Q('Explain why Bangladesh is hotter in June than in December. Use the words *tilted*, *direct* and *longer*.',
      Lines(3, 'In June the northern half of the Earth is tilted towards the Sun, so sunlight is more direct and the days are longer, giving more heat.'), marks=3),
    Q('A model: you shine a torch (Sun) at a ball (Earth) with a stick through it (axis) and turn the ball.',
      Part('What does turning the ball show?', Lines(1, 'day and night (rotation)')),
      Part('Give **one** way this model is not like the real Earth and Sun.', Lines(2, 'Sizes and distances are wrong; the torch only lights one direction, but the Sun shines in all directions; the ball is not moving around the torch.')), marks=3),
    Q('Why does the Moon seem to change shape?',
      Lines(2, 'As it orbits the Earth we see different amounts of its sunlit half.'), marks=2),
])

investigate = Sheet('investigate', 'How does day length change through the year?', level=2, goals=['Plot a line graph.', 'Identify a pattern.', 'Explain it using the Earth\'s tilt.'], blocks=[
    P('These are approximate hours of daylight in **Dhaka** in the middle of each month.'),
    Table(['Month', 'J', 'F', 'M', 'A', 'M', 'J', 'J', 'A', 'S', 'O', 'N', 'D'],
          [['Daylight (hours)', '10.9', '11.4', '12.0', '12.7', '13.3', '13.6', '13.4', '12.9', '12.2', '11.6', '11.0', '10.7']], center=True),
    Q('Plot a line graph of daylight hours.',
      Graph(['J', 'F', 'M', 'A', 'M', 'J', 'J', 'A', 'S', 'O', 'N', 'D'], [10.9, 11.4, 12.0, 12.7, 13.3, 13.6, 13.4, 12.9, 12.2, 11.6, 11.0, 10.7],
            'Daylight (hours)', 'Month', ymax=14, step=1, kind='line', width=150, height=70), marks=4),
    Q('Answer using your graph.',
      Part('Which month has the longest days? the shortest?', Lines(1, 'longest: June; shortest: December')),
      Part('Describe the pattern.', Lines(2, 'Days get longer from December to June, then shorter again: a pattern that repeats every year.')),
      Part('How much longer is a day in June than in December?', Lines(1, '13.6 − 10.7 = 2.9 hours (almost 3 hours)')), marks=4),
    Q('Predict the daylight hours in Singapore (on the equator) in June and in December. Explain.',
      Lines(2, 'About 12 hours in both months: near the equator day length hardly changes during the year.'), marks=2),
    Q('**Shadow stick.** Plan how you would measure the shadow of a stick at different times of day. What would you keep the same?',
      Lines(3, 'Same stick, same place, measure at 9 am, 11 am, 1 pm, 3 pm with a metre stick; record length and direction; repeat on another sunny day.'), marks=2),
])

case = Sheet('case', 'Six seasons, one planet', level=3, goals=['Compare seasons in different places.', 'Link seasons to culture and farming.', 'Explain using the Earth\'s tilt and position.'], blocks=[
    Links('Science', 'Geography', 'Culture', 'Maths', 'Agriculture'),
    Case('Bengali tradition divides the year into **six seasons** (*ritu*): *Grishmo* (summer), *Borsha* (monsoon), *Shorot* '
         '(early autumn), *Hemonto* (late autumn), *Sheet* (winter) and *Boshonto* (spring). Farming follows the seasons: '
         '*Aman* rice grows in the monsoon and is harvested in Hemonto, celebrated with the **Nabanna** festival of new rice, '
         'while *Boro* rice grows in the dry winter with water from tube-wells.',
         'Other places have very different seasons. In **Singapore**, near the equator, it is hot all year and every day has '
         'about 12 hours of daylight. In **Tromsø**, Norway, far to the north, the Sun does not set for about two months in '
         'summer and does not rise for about two months in winter. In **Sydney**, Australia, south of the equator, December '
         'is the middle of summer.',
         source='Day-length facts from standard astronomical tables (approximate).'),
    Q('Complete the table.',
      Table(['Place', 'Where it is', 'What its seasons are like'], [
          ['Dhaka', Ans('north of the equator, near the Tropic of Cancer'), Ans('hot, wet summer (monsoon); mild, dry winter; days 11–13.5 h')],
          ['Singapore', Ans('on the equator'), Ans('hot all year; about 12 h daylight every day')],
          ['Tromsø', Ans('far north, near the Arctic'), Ans('midnight sun in summer, polar night in winter')],
          ['Sydney', Ans('south of the equator'), Ans('summer in December, winter in June')]], widths=['16%', '36%', '48%']), marks=6),
    Q('Explain why Sydney has summer in December, when Dhaka has winter.',
      Lines(3, 'In December the southern half of the Earth is tilted towards the Sun (summer there), while the northern half, with Dhaka, is tilted away (winter).'), marks=2),
    Q('Choose one Bangladeshi festival or food linked to a season. Explain the link.',
      Lines(3, 'e.g. Nabanna: celebrates the new Aman rice harvest in Hemonto; pitha in winter made with new rice and date-palm molasses; mangoes in Grishmo.'), marks=2),
    Q('Why does Boro rice need water from tube-wells, but Aman rice does not?',
      Lines(2, 'Boro grows in the dry winter with little rain; Aman grows in the monsoon when rain supplies the water.'), marks=2),
])

review = Sheet('review', 'Show what you know', level=3, goals=['Use key vocabulary.', 'Answer test-style questions.'], blocks=[
    Q('Find the key words.', WordSearch(['ORBIT', 'AXIS', 'TILT', 'SEASON', 'PLANET', 'MOON', 'STAR', 'EQUATOR', 'SUN'], size=10, seed=81)),
    Q('What causes day and night?', MCQ(['the Earth orbiting the Sun', 'the Earth spinning on its axis', 'the Moon blocking the Sun', 'clouds'], 1, one_col=True), marks=1),
    Q('What causes the seasons?', MCQ(['the Earth\'s distance from the Moon', 'the tilt of the Earth\'s axis as it orbits the Sun', 'the Sun getting hotter', 'the wind'], 1, one_col=True), marks=1),
    Q('Label the planets with numbers 1 to 8 from the Sun, then write the name of the largest planet.',
      Fig(art.solar_system(numbered=True)), Lines(1, 'Jupiter'), marks=2),
    Q('**Challenge.** Galileo saw moons going around Jupiter. Why was this important evidence?',
      Lines(3, 'It showed that not everything orbits the Earth, which supported the idea that the Earth and planets orbit the Sun.'), marks=2),
])

TOPIC = Topic(
    code='B4', strand='earth', title='Earth, Sun and Moon: Days, Years and Seasons', short='Earth and space',
    subtitle='Day and night, the Sun\'s path, years, seasons around the world, the Moon, planets and stars',
    outcomes=['explain why different regions of Earth experience different seasonal conditions.'],
    cambridge=['Unit 6 Earth\'s movements (6.1–6.7)'],
    sheets=[learn, facts, think, investigate, case, review],
    selfcheck=['explain day and night', 'explain why the Sun appears to move across the sky', 'explain why we have seasons',
               'explain why different places have different seasons', 'name the planets in order', 'plot and read a line graph of day length'],
    cover_art=art.seasons_orbit(),
)
