from build import Sheet, Topic
from ws import (P, H, Box, Vocab, Fig, Q, Lines, Blanks, Match, TrueFalse, MCQ, Table, Ans, Sort, Draw, Graph, WordSearch, Bullets, Pics,
                Choose, PicMatch, PicSort, Pictograph, Trace, Case)
import art
import art23

learn = Sheet('learn', 'The Sun, the Moon and the stars', level=1, goals=['Say how the Sun seems to move.', 'Explain day and night.'], blocks=[
    P('Every morning the **Sun rises** in the east. It climbs high in the sky at midday, and in the evening it **sets** in the west.', 'lead'),
    Fig(art.sun_path(), 'The Sun seems to move across the sky. Shadows change too.', width='76%'),
    P('Shadows are **long** in the morning and evening, and **short** at midday when the Sun is high.'),
    H('Why do we have day and night?', 3),
    P('The Sun does not really move. **The Earth spins!** The side facing the Sun has **day**. The side facing away has **night**. You can show this with a torch and a ball.'),
    Fig(art.day_night(), 'Day and night on the spinning Earth.', width='60%'),
    H('The Moon and stars', 3),
    P('At night we can see the **Moon** and the **stars**. The Moon also rises and sets. Its shape seems to change during the month.'),
    Fig(art23.moon_phases(), 'The Moon\'s shapes in one month.', width='88%'),
    Box('bd', P('The Sun and Moon matter to people. Muslims break their fast at **sunset** during Ramadan, and **Eid** begins when the new Moon is seen. **Pohela Boishakh** welcomes the new year of the Bangla calendar.')),
    Box('safety', P('Never look straight at the Sun. It can hurt your eyes.')),
])

facts = Sheet('facts', 'Sky facts', level=1, goals=['Recall sky facts.'], blocks=[
    Q('Fill in the gaps.', Blanks('The Sun rises in the [east] and sets in the [west]. The Earth [spins], so we have day and night.', extra=['north', 'stops'])),
    Q('Day or night?', PicSort(['Day', 'Night'], [('sun', 'Sun', 'Day'), ('sunrise', 'sunrise', 'Day'), ('moon', 'Moon', 'Night'), ('star', 'stars', 'Night')], height='28mm')),
    Q('True or false?', TrueFalse([('Shadows are shortest at midday.', True), ('The Moon makes its own light.', False, 'It reflects light from the Sun.')])),
])

think = Sheet('think', 'Explain it', level=2, goals=['Explain day and night.'], blocks=[
    Q('Use a torch and a ball to show day and night. Draw it.', Draw('45mm', 'My model', 'A torch shining on a ball; the lit side is day, the dark side is night.')),
    Q('Why is it night in some countries when it is day in Bangladesh?', Lines(2, 'The Earth spins, so the other side is facing away from the Sun.')),
])

investigate = Sheet('investigate', 'Shadow watch', level=2, goals=['Measure a shadow through the day.', 'Find a pattern.'], blocks=[
    Box('adult', P('Put a stick in the ground in a sunny place. Measure its shadow with hand spans at 9 o\'clock, 12 o\'clock and 3 o\'clock.')),
    Q('Our shadow results.', Table(['Time', '9 o\'clock', '12 o\'clock', '3 o\'clock'], [['Shadow (hand spans)', '6', '1', '5']], center=True),
      Graph(['9 o\'clock', '12 o\'clock', '3 o\'clock'], [6, 1, 5], 'Hand spans', 'Time', ymax=7, step=1, width=80, height=44)),
    Q('When was the shadow shortest?', MCQ(['9 o\'clock', '12 o\'clock', '3 o\'clock'], 1)),
    Q('Why?', Lines(1, 'The Sun was highest in the sky at midday.')),
])

case = Sheet('case', 'Waiting for the new Moon', level=3, goals=['Read about the Moon in our culture.'], blocks=[
    Case('On the last evening of Ramadan, Imran\'s family went up to the roof after sunset. Everyone looked at the western sky.',
         '"There it is!" shouted Imran. A very thin new Moon was shining low in the sky. "Eid Mubarak!" said his grandmother. Tomorrow would be Eid.'),
    Q('Where did the family look for the Moon?', Lines(1, 'in the western sky, after sunset')),
    Q('Why was seeing the new Moon important?', Lines(2, 'It showed that Ramadan was over and Eid would start tomorrow.')),
])

review = Sheet('review', 'Show what you know', level=3, goals=['Use sky words.'], blocks=[
    Q('Find the words.', WordSearch(['SUN', 'MOON', 'STAR', 'DAY', 'NIGHT'], size=7, seed=105)),
    Q('We have day and night because…', MCQ(['the Sun goes out', 'the Earth spins'], 1)),
])

TOPIC = Topic(
    code='B1', strand='earth', title='The Sun, Moon and Stars', short='Sun and Moon',
    subtitle='The Sun across the sky, shadows, day and night, the Moon and stars, and what they mean to people',
    outcomes=[
        'explore how the Sun appears to move during the day, and how shadows change.',
        'model how the spin of the Earth leads to day and night — for example with different sized balls and a torch.',
        'observe, describe and predict patterns in the motion of the Sun, Moon and stars in the sky.',
        'identify the appearance of the Sun, Moon and stars — sunrise and sunset, moonrise and moonset.',
        'discuss how the Sun and the Moon are important in different cultures, with respect to customs and traditions.',
    ],
    sheets=[learn, facts, think, investigate, case, review],
    selfcheck=['say how the Sun seems to move', 'explain day and night', 'measure a shadow'],
    cover_art=art.day_night(),
)
