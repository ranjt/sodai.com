from build import Sheet, Topic
from ws import (P, H, Box, Vocab, Fig, Cols, Row, Case, Links, Lines, Blanks, Match, TrueFalse, MCQ, Order, Table,
                Ans, Sort, Label, Draw, Graph, WordSearch, Q, Part, Bullets, Pics)
import art
import art23

learn = Sheet('learn', 'Day, night, seasons and the Moon', level=1, goals=[
    'Explain day and night using the spinning Earth.',
    'Explain why we have seasons.',
    'Describe the phases of the Moon and why they matter.',
], blocks=[
    P('Every morning the Sun seems to rise in the east, and every evening it seems to set in the west. But the Sun is not really moving across the sky. **The Earth is spinning!**', 'lead'),
    H('Day and night', 3),
    P('The Earth **spins** (rotates) on its **axis**, an imaginary line through the North and South Poles. It turns once every **24 hours**. The side facing the Sun has **day**; the side facing away has **night**.'),
    Fig(art.day_night(), 'Day and night.', width='72%'),
    H('The Sun across the sky', 3),
    P('Because the Earth spins, the Sun seems to move from **east** to **west**. A **shadow stick** or **sundial** shows this: the shadow is long in the morning, short at midday and long again in the evening.'),
    Fig(art.sun_path(), 'A shadow stick through the day.', width='78%'),
    H('A year and the seasons', 3),
    P('The Earth also **travels around** (orbits) the Sun. One trip takes a **year**: 365¼ days. The Earth is **tilted**. When our part of the Earth leans towards the Sun, the Sun is **high** in the sky, its light is strong and we have **summer**. When we lean away, the Sun is **lower** and we have **winter**.'),
    Fig(art.seasons_orbit(), 'The tilted Earth travels around the Sun.', width='72%'),
    P('Seasons affect living things: farmers plant crops at the right season, some birds fly to Bangladesh in winter, and trees grow new leaves in spring.'),
    H('The Moon and its phases', 3),
    P('The Moon travels around the Earth about once a month. It has no light of its own; it **reflects** sunlight. As it moves, we see different amounts of its lit side. These shapes are called **phases**.'),
    Fig(art23.moon_phases(), 'The phases of the Moon.', width='92%'),
    P('The Moon matters: its pull makes the **tides** go up and down, which fishers watch carefully. The Islamic months, and the dates of **Eid**, begin when the new crescent moon is seen. Some sea animals, like corals, lay eggs at the full moon.'),
    Box('bd', P('Bangladesh has **six seasons** (*ritu*): grishma (summer), barsha (rainy), sharat (autumn), hemanta (late autumn), sheet (winter) and basanta (spring).')),
    Vocab([('rotate', 'spin around'), ('axis', 'an imaginary line the Earth spins around'), ('orbit', 'travel around'), ('season', 'part of the year with its own weather'),
           ('phase', 'the shape of the lit part of the Moon we see'), ('tide', 'the sea going up and down each day')]),
])

facts = Sheet('facts', 'Earth, Sun and Moon', level=1, goals=['Recall key facts.', 'Name Moon phases.'], blocks=[
    Q('Fill in the gaps.', Blanks('The Earth spins once every [24] hours. This makes day and [night]. The Earth goes around the Sun once a [year]. The Moon goes around the [Earth].', extra=['week', 'Sun']), marks=4),
    Q('Name the Moon phases.', Fig(art23.moon_phases(names=False), width='88%'),
      Table([str(i + 1) for i in range(8)], [[Ans(p) for p in art23.MOON_PHASES]], center=True), marks=4),
    Q('True or false?', TrueFalse([('The Sun moves around the Earth every day.', False, 'The Earth spins; the Sun only seems to move.'), ('The Moon makes its own light.', False, 'It reflects sunlight.'), ('Shadows are shortest at midday.', True)]), marks=3),
])

think = Sheet('think', 'Explaining patterns', level=2, goals=['Explain day and night and seasons.'], blocks=[
    Q('When it is day in Bangladesh, it is night in America. Why?', Lines(2, 'Bangladesh faces the Sun while America is on the other side of the spinning Earth, facing away.'), marks=2),
    Q('Why is it hotter in summer than in winter?', Lines(2, 'In summer the Sun is higher in the sky, so its light is stronger.'), marks=2),
    Q('Draw a shadow stick at 9 am, 12 noon and 4 pm.', Draw('40mm', 'Shadow stick', 'Long shadow in the morning (pointing west), short at noon, long in the afternoon (pointing east).'), marks=3),
])

investigate = Sheet('investigate', 'Make a shadow stick', level=2, goals=['Measure shadows through the day.', 'Find a pattern.'], blocks=[
    P('Push a stick into the ground in a sunny place. Measure the length of its shadow every two hours.'),
    Q('Here are Class 3A\'s results. Draw a bar chart.', Table(['Time', '8 am', '10 am', '12 noon', '2 pm', '4 pm'], [['Shadow (cm)', '80', '40', '15', '35', '75']], center=True),
      Graph(['8 am', '10 am', '12 noon', '2 pm', '4 pm'], [80, 40, 15, 35, 75], 'Shadow (cm)', 'Time', ymax=90, step=10, width=110, height=48), marks=3),
    Q('When was the shadow shortest? Why?', Lines(2, 'At 12 noon, because the Sun was highest in the sky.'), marks=2),
    Q('Predict the shadow at 5 pm.', Lines(1, 'longer than 75 cm'), marks=1),
])

case = Sheet('case', 'The Moon and the fishers', level=3, goals=['Learn why the Moon matters to people.'], blocks=[
    Links('Science', 'Work', 'Culture'),
    Case('Fishers on the coast of Bangladesh watch the Moon carefully. At **full moon** and **new moon**, the tides are very high and very low. These are called **spring tides**. The fishers plan when to go out and when to bring their boats in.',
         'Families also watch for the thin **crescent moon** after the new moon. When it is seen, a new month of the Islamic calendar begins, and everyone knows when **Eid** will be celebrated.',
         source='Based on tides and moon sighting in Bangladesh.'),
    Q('Why do fishers watch the Moon?', Lines(2, 'The Moon causes the tides; they plan their fishing trips with the tides.'), marks=2),
    Q('Which Moon phase begins a new month in the Islamic calendar?', Lines(1, 'the new crescent moon'), marks=1),
    Q('Draw the Moon tonight, or the last time you saw it. Which phase was it?', Draw('34mm', 'The Moon I saw', 'Any phase, labelled.'), marks=2),
])

review = Sheet('review', 'Show what you know', level=3, goals=['Use Earth and Moon words.'], blocks=[
    Q('Find the words.', WordSearch(['DAY', 'NIGHT', 'SPIN', 'ORBIT', 'MOON', 'SEASON', 'TIDE'], size=9, seed=308)),
    Q('Why do we have day and night?', MCQ(['the Sun goes around the Earth', 'the Earth spins', 'clouds cover the Sun'], 1), marks=1),
    Q('How long does the Earth take to go around the Sun?', MCQ(['one day', 'one month', 'one year'], 2), marks=1),
    Q('**Challenge.** Use a torch and a ball to explain day and night to a friend. Draw how you would set it up.', Draw('36mm', 'My model', 'Torch shining on a ball; turn the ball slowly; the lit side is day.'), marks=2),
])

TOPIC = Topic(
    code='B2', strand='earth', title='Day, Night, Seasons and the Moon', short='Day, night and Moon',
    subtitle='The spinning Earth, the Sun\'s path, seasons, and the phases of the Moon',
    outcomes=[
        'understand that Earth rotates on its axis while revolving around the Sun, and that the Moon revolves around the Earth.',
        'demonstrate and explain how the Earth\'s rotation results in the cyclical change from day to night, and build a device such as a sundial or shadow stick to plot the apparent movement of the Sun across a day.',
        'explain seasonal changes as a result of the angle of the Sun above the Earth\'s horizon determining how much of the Sun\'s energy is received at different times of the year, and how the seasons affect humans, plants and animals.',
        'identify the phases of the Earth\'s moon, describe each phase, and explain why this cycle matters to humans and to some animals and plants.',
        'use observations of the Sun, Moon and stars to describe patterns that can be predicted.',
        'understand that natural phenomena can be observable on Earth as a result of movements and rotations.',
    ],
    cambridge=['Stage 2 Unit 6 The Earth and the Sun (6.1–6.3)'],
    sheets=[learn, facts, think, investigate, case, review],
    selfcheck=['explain day and night', 'make a shadow stick', 'explain seasons', 'name the Moon phases', 'say why the Moon matters'],
    cover_art=art.day_night(),
)
