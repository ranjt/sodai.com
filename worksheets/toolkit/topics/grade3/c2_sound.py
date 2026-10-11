from build import Sheet, Topic
from ws import (P, H, Box, Vocab, Fig, Cols, Row, Case, Links, Lines, Blanks, Match, TrueFalse, MCQ, Order, Table,
                Ans, Sort, Label, Draw, Graph, WordSearch, Q, Part, Bullets, Pics)
import art
import art23

learn = Sheet('learn', 'Sound: vibrations, loudness and pitch', level=1, goals=[
    'Explain that sounds are made by vibrations.',
    'Measure loudness in decibels and describe how sound travels.',
    'Explain pitch and how musical instruments change it.',
], blocks=[
    P('Put your fingers on your throat and hum. Can you feel a tingle? That is a **vibration**: a very fast shaking. **Every sound is made by something vibrating.**', 'lead'),
    Bullets(['When you hit a **dhol**, its skin vibrates.', 'When you pluck an **ektara**, its string vibrates.', 'When you blow a **bansuri**, the air inside it vibrates.', 'When you talk, your **voice box** in your throat vibrates.']),
    Fig(art.instruments(), 'Instruments from Bangladesh.', width='70%'),
    H('How sound travels', 3),
    P('The vibrations pass from one tiny particle to the next until they reach your **ear**. Sound can travel through **gases** (air), **liquids** (water) and **solids** (wood, metal, string). '
      'It travels better through solids: put your ear on a desk while a friend taps the other end! Sound cannot travel through empty **space**, where there is no air.'),
    Fig(art.string_phone(), 'A string telephone.', width='72%'),
    H('How loud?', 3),
    P('**Loudness** (volume) is measured in **decibels (dB)** with a **sound level meter**. Many mobile phones have a sound meter app. Sounds louder than about **85 dB** can damage your hearing if you listen for a long time.'),
    Fig(art23.decibel_scale(), 'Everyday sounds on the decibel scale.', width='96%'),
    P('Soft, thick materials such as **foam**, **cloth**, **curtains** and **egg boxes** soak up sound. They stop it from travelling through. This is called **sound insulation**. Ear defenders use it to protect workers\' ears.'),
    H('High and low: pitch', 3),
    P('**Pitch** is how **high** or **low** a sound is. A bird tweets with a high pitch; a big drum booms with a low pitch. High and low sounds can each be loud or soft.'),
    Table(['Higher pitch', 'Lower pitch'], [['short, thin or tight strings', 'long, thick or loose strings'], ['small drums, tight drum skins', 'big drums, loose drum skins'],
                                            ['short tube of air (cover fewer holes on a flute)', 'long tube of air (cover more holes)']]),
    Fig(art23.bottle_pitch(), 'Tap bottles with different amounts of water.', width='62%'),
    Vocab([('vibrate', 'shake very fast'), ('volume', 'how loud a sound is'), ('decibel (dB)', 'the unit for measuring loudness'),
           ('pitch', 'how high or low a sound is'), ('sound insulation', 'a material that stops sound travelling through')]),
])

facts = Sheet('facts', 'What vibrates?', level=1, goals=['Name what vibrates.', 'Read the decibel scale.'], blocks=[
    Q('Draw a line to match the instrument to the part that vibrates.', Match([('dhol', 'the drum skin'), ('ektara', 'the string'), ('bansuri', 'the air inside'), ('your voice', 'the voice box in your throat')]), marks=4),
    Q('Write the loudness of each sound.', Fig(art23.decibel_scale(values=False), width='92%'),
      Table(['leaves', 'birds', 'talking', 'traffic', 'loud music', 'plane'], [[Ans('20 dB'), Ans('40 dB'), Ans('60 dB'), Ans('80 dB'), Ans('100 dB'), Ans('120 dB')]], center=True), marks=3),
    Q('True or false?', TrueFalse([('Sound can travel through water.', True), ('Sound travels through space.', False, 'There is no air in space to carry it.'), ('A loud sound always has a high pitch.', False, 'Loudness and pitch are different.')]), marks=3),
])

think = Sheet('think', 'Thinking about sound', level=2, goals=['Explain pitch and loudness.'], blocks=[
    Q('Which bottle makes the highest note when tapped? Which makes the lowest?', Fig(art23.bottle_pitch(numbered=True), width='56%'),
      Lines(1, 'Highest: A (least water). Lowest: D (most water).'), marks=2),
    Q('An ektara player presses the string to make it shorter. What happens to the pitch?', Lines(1, 'It gets higher.'), marks=1),
    Q('Why do people who work with loud machines wear ear defenders?', Lines(2, 'Loud sounds above 85 dB can damage hearing; ear defenders block the sound.'), marks=2),
    Q('A string phone only works when the string is tight. Why?', Lines(2, 'A tight string carries the vibrations; a loose string does not vibrate well.'), marks=2),
])

investigate = Sheet('investigate', 'Which material blocks sound best?', level=2, goals=['Measure sound in decibels.', 'Draw a bar chart and conclude.'], blocks=[
    P('Class 3C put a ringing alarm clock inside a box and wrapped it in different materials. They measured the sound 1 metre away with a sound meter app.'),
    Q('Draw a bar chart.', Table(['Material', 'none', 'foil', 'newspaper', 'towel', 'foam'], [['Sound (dB)', '70', '66', '60', '50', '45']], center=True),
      Graph(['none', 'foil', 'newspaper', 'towel', 'foam'], [70, 66, 60, 50, 45], 'Sound (dB)', 'Material', ymax=80, step=10, width=110, height=48), marks=3),
    Q('Which material blocked the sound best?', Lines(1, 'foam'), marks=1),
    Q('What kind of materials are good sound insulators?', Lines(2, 'soft, thick materials like foam and towels'), marks=2),
    Q('What did they keep the same to make it fair?', Lines(1, 'same alarm clock, same box, same distance (1 metre)'), marks=1),
])

case = Sheet('case', 'Too much noise!', level=3, goals=['Use what you know about sound to solve a real problem.'], blocks=[
    Links('Science', 'Health', 'Citizenship'),
    Case('Dhaka is one of the noisiest cities in the world. On busy roads the sound is often above **85 dB** because of car horns, buses, building work and loudspeakers. Traffic police stand in this noise all day.',
         'Too much noise can damage hearing and make it hard to sleep, learn and think. Bangladesh has rules: very loud hydraulic horns are not allowed, and roads near **schools and hospitals** are **silent zones** where drivers must not honk.',
         source='Based on reports about noise pollution in Dhaka and Bangladesh\'s noise rules.'),
    Q('Name three things that make Dhaka noisy.', Lines(1, 'car horns, buses, building work, loudspeakers'), marks=3),
    Q('Why are roads near hospitals and schools silent zones?', Lines(2, 'Sick people need rest; children need quiet to learn.'), marks=2),
    Q('Make a "Do not honk" sign for your school gate.', Draw('34mm', 'Silent zone sign', 'e.g. a horn with a line through it: "Silent zone: no horns".'), marks=2),
])

review = Sheet('review', 'Show what you know', level=3, goals=['Use sound words.'], blocks=[
    Q('Find the words.', WordSearch(['VIBRATE', 'PITCH', 'LOUD', 'EAR', 'DRUM', 'NOISE', 'DECIBEL'], size=9, seed=311)),
    Q('Loudness is measured in…', MCQ(['metres', 'decibels', 'grams'], 1), marks=1),
    Q('A short, tight string makes a…', MCQ(['high pitch', 'low pitch', 'no sound'], 0), marks=1),
    Q('**Challenge.** Design a quiet corner for your classroom. Which materials would you use?', Lines(2, 'curtains, carpet, cushions, foam on the walls: soft, thick materials soak up sound.'), marks=2),
])

TOPIC = Topic(
    code='C2', strand='physical', title='Sound', short='Sound',
    subtitle='Vibrations, decibels, how sound travels, sound insulation, and pitch in musical instruments',
    outcomes=[
        'explore how sounds are made when objects, materials or air vibrate, and measure the volume of a sound in decibels using a sound level meter.',
        'investigate how sound travels through different materials to the ear.',
        'investigate how some materials are effective in preventing sound from travelling through them.',
        'investigate the way pitch describes how high or low a sound is, and that high and low sounds can be loud or soft.',
        'explore how pitch can be changed in musical instruments in a range of ways.',
    ],
    cambridge=['Stage 3 Unit 4 Our five senses (hearing)'],
    sheets=[learn, facts, think, investigate, case, review],
    selfcheck=['explain that sounds come from vibrations', 'measure sound in decibels', 'say which materials block sound', 'explain pitch', 'change the pitch of an instrument'],
    cover_art=art.instruments(),
)
