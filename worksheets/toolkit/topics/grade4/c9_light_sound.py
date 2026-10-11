from build import Sheet, Topic
from ws import (P, H, Box, Vocab, Fig, Cols, Row, Case, Links, Lines, Blanks, Match, TrueFalse, MCQ, Order, Table,
                Ans, Sort, Label, Draw, Graph, WordSearch, Q, Part, Bullets, Pics)
import art
import art4

learn = Sheet('learn', 'Light and sound: absorbed, reflected and refracted', level=1, goals=[
    'Explain how sound is made and how it travels through solids, liquids and gases.',
    'Explain loudness and pitch, and how sounds can be muffled.',
    'Show how light and sound can be absorbed, reflected and refracted.',
], blocks=[
    P('Light and sound both bring us news about the world. Light lets us see the Pohela Boishakh procession; sound lets us '
      'hear the dhol and the songs. Both travel from a **source** to our senses, and both change when they meet different objects.', 'lead'),
    Cols(
        H('How sound is made', 3),
        P('All sounds are made by **vibrations**: very fast movements backwards and forwards. Pluck an ektara string and you can see '
          'it vibrate. Put your fingers on your throat and hum: you can feel your voice box vibrate.'),
        H('How sound travels', 3),
        P('The vibrating object makes the particles next to it vibrate, and they pass the vibration on, like a ripple. Sound can '
          'travel through **gases** (air), **liquids** (water) and **solids** (wood, metal, string). It travels best through '
          '**solids**, because their particles are close together. Sound cannot travel through empty space, because there are no '
          'particles to pass on the vibration.'),
        Fig(art.string_phone(), 'A string telephone: sound travels along the tight string.', width='86%'),
        H('Loud and soft sounds', 3),
        P('A **bigger** vibration makes a **louder** sound. Hit a drum gently and it is soft; hit it hard and it is loud. Sounds get '
          'quieter as they travel further away. Loudness is measured in **decibels** (dB).'),
        H('High and low sounds', 3),
        P('**Pitch** is how high or low a sound is. **Fast** vibrations make a **high** pitch; **slow** vibrations make a **low** pitch.'),
        Bullets(['**Strings**: a shorter, tighter or thinner string gives a higher pitch.', '**Drums**: a smaller or tighter drum skin gives a higher pitch.',
                 '**Wind instruments** (like the *banshi*): a shorter column of air gives a higher pitch.']),
        Fig(art.sound_waves(), 'Comparing sounds as waves.', span=True, width='72%'),
        H('Muffling sound', 3),
        P('Soft, thick materials such as cloth, foam, curtains and egg boxes **absorb** sound, so less sound gets through. This is '
          'called **muffling**. Ear defenders protect workers in noisy places. Hard, smooth surfaces such as walls and cliffs '
          '**reflect** sound, which can make an **echo**.'),
        H('Light: absorbed, reflected, refracted', 3),
        P('Light travels from a **source** (the Sun, a lamp, a flame) in straight lines. When it meets an object:'),
        Bullets(['Dark, dull objects **absorb** most of the light, so they look dark.',
                 'Light-coloured and shiny objects **reflect** light. A mirror reflects light neatly, so we see a clear image.',
                 'Transparent materials such as water and glass let light through, but **refract** it (bend it) as it goes in and out. That is why a pencil in water looks broken.']),
        Row([Fig(art.reflection(), 'Reflection.')], [Fig(art.refraction_glass(), 'Refraction.')]),
        P('We see objects when light from a source reflects off them and enters our eyes. How things look depends on the **light '
          'source** (bright or dim, near or far) and on the **object** (its colour, whether it is shiny, see-through or rough).'),
        Box('fact', P('Light is the fastest thing there is: about 300 000 km every second. Sound in air travels at only about 340 metres '
                      'a second. That is why you see lightning before you hear the thunder.')),
    ),
    Vocab([('vibration', 'a fast movement backwards and forwards'), ('pitch', 'how high or low a sound is'), ('loudness', 'how loud or soft a sound is'),
           ('muffle', 'make a sound quieter by absorbing it'), ('echo', 'a sound reflected back to you'), ('absorb', 'take in light or sound'),
           ('reflect', 'bounce off a surface'), ('refract', 'bend light as it passes into a different material')]),
])

facts = Sheet('facts', 'Sound and light facts', level=1, goals=['Recall how sound is made and travels.', 'Use absorb, reflect and refract.'], blocks=[
    Q('What vibrates to make the sound?', Table(['Instrument', 'What vibrates?'], [['dhol (drum)', Ans('the drum skin')], ['ektara', Ans('the string')], ['banshi (flute)', Ans('the air inside')], ['your voice', Ans('your vocal cords')]], widths=['45%', '55%']), marks=4),
    Q('Absorbed, reflected or refracted?', Table(['What happens', 'Absorbed, reflected or refracted?'], [['you see yourself in a mirror', Ans('reflected')], ['a black shirt gets hot in the sun', Ans('absorbed')],
                                                                                                        ['a straw looks bent in a glass of water', Ans('refracted')], ['thick curtains make a room quieter', Ans('absorbed')], ['you hear an echo in a big empty hall', Ans('reflected')]],
                                             widths=['60%', '40%']), marks=5),
    Q('Fill in the gaps.', Blanks('Sounds are made by [vibrations]. Sound travels best through [solids]. A bigger vibration makes a [louder] sound. '
                                  'Faster vibrations make a [higher] pitch.', extra=['lower', 'gases']), marks=4),
    Q('True or false?', TrueFalse([('Sound can travel through water.', True), ('Sound can travel through empty space.', False, 'There are no particles to pass the vibration on.'),
                                   ('A shorter string makes a higher pitch.', True)]), marks=3),
])

think = Sheet('think', 'Explaining sound and light', level=2, goals=['Explain pitch and loudness.', 'Explain what we see.'], blocks=[
    Q('A Baul singer tightens the string of the ektara. What happens to the pitch? Why?', Lines(2, 'It gets higher, because a tighter string vibrates faster.'), marks=2),
    Q('Why can you hear a train coming sooner if you put your ear to the railway track? (Never try this!)', Lines(2, 'Sound travels faster and better through solid steel than through air.'), marks=2),
    Q('Why do recording studios have soft foam on the walls?', Lines(2, 'Soft foam absorbs sound, so there are no echoes and outside noise is muffled.'), marks=2),
    Q('A white cat and a black cat sit in the sun. Which one looks brighter, and which one gets hotter? Explain.', Lines(3, 'The white cat looks brighter because it reflects more light; the black cat gets hotter because it absorbs more light.'), marks=2),
    Q('Draw arrows to show how you see a mango on a table in a sunny room.', Draw('32mm', 'Seeing a mango', 'Arrow from the Sun to the mango, then from the mango to the eye.'), marks=2),
])

investigate = Sheet('investigate', 'Which material muffles sound best?', level=2, goals=['Plan a fair test.', 'Measure loudness in decibels.', 'Draw conclusions.'], blocks=[
    P('Class 4D put a phone playing a beep at the same volume inside a box. They covered the box with different materials and measured the loudness 1 metre away with a sound meter app.'),
    Q('Complete the plan.', Table(None, [['Change', Ans('the material covering the box')], ['Measure', Ans('loudness (dB) at 1 m')],
                                         ['Keep the same', Ans('the phone, the beep and its volume, the box, the distance, the same quiet room')]], widths=['26%', '74%']), marks=3),
    Q('Draw a bar chart.',
      Table(['Material', 'no cover', 'newspaper', 'foil', 'bubble wrap', 'cotton wool'], [['Loudness (dB)', '80', '68', '72', '60', '52']], center=True),
      Graph(['none', 'newspaper', 'foil', 'bubble wrap', 'cotton wool'], [80, 68, 72, 60, 52], 'Loudness (dB)', 'Material', ymax=90, ymin=40, step=5, width=120, height=50), marks=3),
    Q('Which material muffled the sound best? Suggest why.', Lines(2, 'Cotton wool (52 dB): it is soft and thick with lots of air spaces that absorb the vibrations.'), marks=2),
    Q('Why did they measure "no cover" first?', Lines(1, 'To compare: it shows how loud the sound is without any muffling.'), marks=1),
    Q('Which material would you use to make ear defenders? Why?', Lines(1, 'Cotton wool or foam, because it absorbed the most sound.'), marks=1),
])

case = Sheet('case', 'The music of the Bauls', level=3, goals=['Apply sound science to traditional instruments.', 'Link science with culture.', 'Design an instrument.'], blocks=[
    Links('Science', 'Music', 'Culture', 'Design'),
    Case('The **Bauls** are wandering singers of Bengal. Their songs, like those of **Lalon Shah**, talk about love, humanity and '
         'living simply. In **2005**, UNESCO recognised Baul songs as a treasure of the world\'s culture.',
         'Bauls play simple instruments, often made by hand. The **ektara** has one string stretched over a hollow gourd; squeezing '
         'its bamboo neck changes the tension and the pitch. The **dotara** has more strings. The **dugi** (a small drum) is beaten '
         'by hand, and the **ghungur** (ankle bells) jingle as the singer dances. The hollow bodies of these instruments make the '
         'sound louder by vibrating with the strings.',
         source='Based on information about Baul music of Bangladesh (UNESCO Intangible Cultural Heritage).'),
    Q('Complete the table.', Table(['Instrument', 'What vibrates?', 'How do you change the pitch?'], [['ektara', Ans('the string'), Ans('squeeze the neck to change the string tension')],
                                                                                                      ['dugi (drum)', Ans('the drum skin'), Ans('tighten the skin or use a smaller drum')],
                                                                                                      ['banshi (flute)', Ans('the air inside'), Ans('cover holes to change the length of the air column')]], widths=['22%', '30%', '48%']), marks=6),
    Q('Why does the ektara have a hollow gourd at the bottom?', Lines(2, 'The hollow gourd vibrates with the string and makes the sound louder.'), marks=2),
    Q('Design your own instrument from recycled materials. Draw it and explain how to make a high note and a low note.',
      Draw('44mm', 'My instrument', 'e.g. rubber bands of different thickness over a box: thin/tight bands give high notes; thick/loose bands give low notes.'), marks=3),
])

review = Sheet('review', 'Show what you know', level=3, goals=['Use key vocabulary.', 'Answer test-style questions.'], blocks=[
    Q('Find the key words.', WordSearch(['SOUND', 'LIGHT', 'PITCH', 'LOUD', 'ECHO', 'MIRROR', 'ABSORB', 'REFLECT', 'VIBRATE'], size=10, seed=419)),
    Q('Which material is best at absorbing sound?', MCQ(['glass', 'metal', 'thick cloth', 'tiles'], 2), marks=1),
    Q('A pencil in water looks bent because light is…', MCQ(['absorbed', 'reflected', 'refracted', 'stopped'], 2), marks=1),
    Q('Draw two waves: a loud low sound and a soft high sound.', Row([Draw('28mm', 'loud, low', 'tall waves, far apart')], [Draw('28mm', 'soft, high', 'short waves, close together')]), marks=2),
    Q('**Challenge.** Astronauts on the Moon talk to each other by radio, even when standing side by side. Explain why.', Lines(3, 'There is no air on the Moon, so there are no particles to carry sound vibrations; radio signals can travel through empty space.'), marks=2),
])

TOPIC = Topic(
    code='C9', strand='physical', title='Light and Sound', short='Light and sound',
    subtitle='Vibrations, how sound travels, loudness and pitch, muffling, and how light and sound are absorbed, reflected and refracted',
    outcomes=[
        'illustrate how light and sound can be absorbed, reflected and refracted.',
        'understand that the properties of light and sound depend on their source and on the objects with which they interact.',
    ],
    cambridge=['Unit 4 Sound (4.1–4.9)'],
    sheets=[learn, facts, think, investigate, case, review],
    selfcheck=['explain how sounds are made', 'explain how sound travels through solids, liquids and gases', 'explain loudness and pitch',
               'test which materials muffle sound', 'explain absorb, reflect and refract for light', 'explain how Baul instruments make music'],
    cover_art=art.sound_waves(),
)
