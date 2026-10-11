from build import Sheet, Topic
from ws import (P, H, Box, Vocab, Fig, Cols, Row, Case, Links, Lines, Blanks, Match, TrueFalse, MCQ, Order, Table,
                Ans, Sort, Label, Draw, Graph, WordSearch, Q, Part, Bullets, Pics)
import art

learn = Sheet('learn', 'Our solar system', level=1, goals=[
    'Tell the difference between stars, planets, moons, meteors and satellites.',
    'Describe the solar system and make a model of it.',
    'Learn about scientists who studied the Sun, planets and stars.',
], blocks=[
    P('On a clear night, look up. You may see the Moon, thousands of stars and maybe a bright planet. The Earth is one of the planets that travel around our star, the **Sun**. Together they make the **solar system**.', 'lead'),
    Fig(art.solar_system(), 'The Sun and its eight planets (not to scale).', width='92%'),
    Table(['Object', 'What it is', 'Example'], [
        ['**star**', 'a huge ball of hot, glowing gas that makes its own light', 'the Sun'],
        ['**planet**', 'a large round object that travels around a star', 'Earth, Mars, Jupiter'],
        ['**moon**', 'an object that travels around a planet', 'our Moon'],
        ['**meteor**', 'a space rock that burns up in our air: a "shooting star"', 'meteors in August'],
        ['**satellite**', 'anything that travels around a planet. People build **artificial** satellites for TV, phones and weather', 'Bangabandhu Satellite-1']]),
    Pics([('sun', 'star'), ('ringed planet', 'planet'), ('moon', 'moon'), ('shooting star', 'meteor'), ('satellite', 'satellite')], cols=5, size='14mm'),
    H('The eight planets', 3),
    P('In order from the Sun: **Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune**. A way to remember: "**M**y **V**ery **E**asy **M**ethod **J**ust **S**peeds **U**p **N**aming." '
      'Jupiter is the biggest. Saturn has beautiful rings. Earth is the only planet we know with living things.'),
    H('How it works', 3),
    P('The planets travel around (**orbit**) the Sun. **Gravity** from the Sun keeps them in their paths. The Earth takes one **year** to go once around the Sun. The Moon orbits the Earth.'),
    H('Scientists who studied the sky', 3),
    Bullets(['**Aryabhata** (India, about 1500 years ago) said that the Earth spins, which makes the stars seem to move.',
             '**Copernicus** (Poland, 1543) said the planets go around the **Sun**, not around the Earth.',
             '**Galileo** (Italy, 1610) used a telescope and discovered four moons going around Jupiter.',
             '**Dr Jamal Nazrul Islam** (Bangladesh, 1939–2013) was a famous scientist from Chattogram who wrote about how the universe began and how it might end.']),
    Box('safety', P('Never look at the Sun, even through sunglasses or a telescope. It can damage your eyes.')),
    Vocab([('solar system', 'the Sun and everything that travels around it'), ('star', 'a ball of hot glowing gas'), ('planet', 'a large object orbiting a star'),
           ('moon', 'an object orbiting a planet'), ('orbit', 'the path around something'), ('satellite', 'an object that orbits a planet')]),
])

facts = Sheet('facts', 'Space objects', level=1, goals=['Name space objects.', 'Order the planets.'], blocks=[
    Q('Draw a line to match.', Match([('star', 'a ball of hot glowing gas'), ('planet', 'travels around a star'), ('moon', 'travels around a planet'), ('meteor', 'a shooting star'), ('satellite', 'sends TV and phone signals')]), marks=5),
    Q('Write the planets in order from the Sun.', Fig(art.solar_system(numbered=True), width='86%'),
      Table(['1', '2', '3', '4', '5', '6', '7', '8'], [[Ans(p) for p in art.PLANETS]], center=True), marks=8),
    Q('True or false?', TrueFalse([('The Sun is a star.', True), ('The Moon makes its own light.', False, 'The Moon reflects light from the Sun.'), ('Jupiter is the biggest planet.', True)]), marks=3),
])

think = Sheet('think', 'Thinking about space', level=2, goals=['Explain how the solar system works.'], blocks=[
    Q('Why does the Moon shine at night if it has no light of its own?', Lines(2, 'Sunlight bounces off (reflects from) the Moon to our eyes.'), marks=2),
    Q('What keeps the planets going around the Sun?', MCQ(['wind', 'gravity', 'magnets'], 1), marks=1),
    Q('What did Copernicus say? Why was it a big new idea?', Lines(3, 'That the Earth and planets go around the Sun. Before, people thought everything went around the Earth.'), marks=2),
])

investigate = Sheet('investigate', 'Build a model solar system', level=2, goals=['Make a model.', 'Say what a model shows and what it cannot show.'], blocks=[
    Box('need', P('balls of clay or paper in different sizes, string, card, glue, a big sheet of paper.')),
    P('Make the Sun in the middle and put the eight planets in order around it. Make Jupiter and Saturn the biggest planets and Mercury the smallest.'),
    Q('Draw your model and label the planets.', Draw('60mm', 'My solar system model', 'Sun in the middle; planets in the correct order with Jupiter biggest.'), marks=4),
    Q('What does your model show well?', Lines(1, 'the order of the planets and which are bigger'), marks=1),
    Q('What can\'t your model show?', Lines(2, 'The real sizes and huge distances; the planets moving.'), marks=1),
])

case = Sheet('case', 'Bangladesh in space: Bangabandhu Satellite-1', level=3, goals=['Learn how satellites help people.'], blocks=[
    Links('Science', 'Technology', 'History'),
    Case('In **May 2018**, Bangladesh\'s first satellite, **Bangabandhu Satellite-1**, was launched into space on a rocket from the United States. It travels far above the Earth.',
         'The satellite sends **TV** and **internet** signals to people all over Bangladesh, even on islands and in hills where it is hard to put cables. Weather satellites from other countries also help Bangladesh see cyclones coming.',
         source='Based on information about Bangabandhu Satellite-1.'),
    Q('What is an artificial satellite?', Lines(1, 'A machine people send into space to orbit the Earth.'), marks=1),
    Q('How does the satellite help people in Bangladesh?', Lines(2, 'It sends TV and internet signals to all parts of the country.'), marks=2),
    Q('Design your own satellite. What job would it do?', Draw('40mm', 'My satellite', 'e.g. a weather satellite with cameras and solar panels to warn of cyclones.'), marks=2),
])

review = Sheet('review', 'Show what you know', level=3, goals=['Use space words.'], blocks=[
    Q('Find the words.', WordSearch(['SUN', 'STAR', 'PLANET', 'MOON', 'ORBIT', 'MARS', 'EARTH'], size=9, seed=307)),
    Q('How many planets are in our solar system?', MCQ(['6', '8', '10'], 1), marks=1),
    Q('A shooting star is really a…', MCQ(['star', 'meteor', 'planet'], 1), marks=1),
    Q('**Challenge.** Why do you think there is life on Earth but not on Mercury?', Lines(2, 'Earth has water, air and the right temperature; Mercury is too hot by day and too cold by night with no air.'), marks=2),
])

TOPIC = Topic(
    code='B1', strand='earth', title='The Solar System', short='Solar system',
    subtitle='Stars, planets, moons, meteors and satellites, a model of the solar system, and scientists who studied the sky',
    outcomes=[
        'differentiate between stars, moons, planets, meteors and satellites.',
        'design and build a model of the solar system, and communicate an understanding of how the solar system works.',
        'research the lives and discoveries of scientists who explored the solar system and the stars.',
    ],
    sheets=[learn, facts, think, investigate, case, review],
    selfcheck=['tell stars, planets and moons apart', 'name the planets in order', 'explain what keeps planets in orbit', 'make a model solar system', 'name scientists who studied space'],
    cover_art=art.solar_system(),
)
