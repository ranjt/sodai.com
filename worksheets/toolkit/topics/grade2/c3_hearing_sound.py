from build import Sheet, Topic
from ws import (P, H, Box, Vocab, Fig, Cols, Row, Case, Links, Lines, Blanks, Match, TrueFalse, MCQ, Order, Table,
                Ans, Sort, Label, Draw, Graph, WordSearch, Q, Part, Bullets, Pics)
import art

learn = Sheet('learn', 'How we hear', level=1, goals=[
    'Name the parts of the ear and explain how we hear.',
    'Explain why hearing is important for people and animals.',
    'Talk about noise pollution and ways to block sound, and name sources of light and sound.',
], blocks=[
    P('Ring a bell, beat a dhol, sing a song. All sounds are made when something **vibrates** (shakes very quickly). The sound travels through the air to your **ears**.', 'lead'),
    H('Inside the ear', 3),
    Fig(art.ear(labels=art.EAR_PARTS), 'The parts of the ear.', width='80%'),
    Bullets(['The **outer ear** collects sound and sends it down the **ear canal**.',
             'The sound makes the **eardrum** vibrate, like a tiny drum. This is in the **middle ear**, with three **tiny bones**.',
             'In the **inner ear**, the snail-shaped **cochlea** turns the vibrations into messages.',
             'A **nerve** carries the messages to the **brain**, and the brain tells you what you hear.']),
    H('Why hearing matters', 3),
    P('Hearing helps us **talk** and **listen** to each other, enjoy **music**, and stay **safe**: we hear a car horn, a fire alarm or someone calling. '
      'Animals use hearing too: a deer listens for a tiger, an owl hunts mice by listening in the dark, and bats find insects using echoes.'),
    Pics([('deer', 'listens for danger'), ('owl', 'hunts by hearing'), ('bat', 'uses echoes'), ('dog', 'hears very quiet sounds')], cols=4, size='15mm'),
    H('Too loud!', 3),
    P('Very loud sound for a long time can **damage** your hearing. Unwanted loud sound is called **noise pollution**: horns, loudspeakers, machines and generators. '
      'We can block sound with **soft** materials like curtains, foam and ear muffs, by closing windows, or by moving further away.'),
    Pics([('loudspeaker', 'loudspeakers'), ('bus', 'horns'), ('construction', 'machines'), ('headphone', 'ear muffs block sound')], cols=4, size='15mm'),
    H('Sources of sound and light', 3),
    P('A **source** is where something comes from. **Sound sources** include drums, bells, birds and voices. **Light sources** include the Sun, lamps, torches and candles.'),
    Box('safety', P('Never put anything inside your ear. If a sound is so loud it hurts, cover your ears and move away.')),
    Vocab([('vibrate', 'shake backwards and forwards very fast'), ('eardrum', 'thin skin in the ear that vibrates'), ('cochlea', 'snail-shaped part of the inner ear'),
           ('noise pollution', 'too much unwanted loud sound'), ('source', 'where light or sound comes from')]),
])

facts = Sheet('facts', 'Parts of the ear', level=1, goals=['Label the ear.', 'Sort sources of light and sound.'], blocks=[
    Q('Label the ear.', Label(art.ear(), art.EAR_PARTS, width='70%', cols=3), marks=6),
    Q('Sort the sources.', Sort(['Sound source', 'Light source'], [('drum', 'Sound source'), ('bell', 'Sound source'), ('bird', 'Sound source'),
                                                                 ('Sun', 'Light source'), ('lamp', 'Light source'), ('candle', 'Light source')]), marks=6),
    Q('Fill in the gaps.', Blanks('Sounds are made when things [vibrate]. Sound makes the [eardrum] vibrate. A [nerve] carries messages to the brain.', extra=['nose']), marks=3),
])

think = Sheet('think', 'Listening and staying safe', level=2, goals=['Explain how hearing helps.', 'Suggest ways to block noise.'], blocks=[
    Q('How does hearing keep you safe when you cross the road?', Lines(2, 'I can hear cars and horns coming even if I cannot see them.'), marks=2),
    Q('Your classroom is next to a noisy road. Give two ways to make it quieter.', Lines(2, 'Close the windows; hang thick curtains; plant trees; put up "no horn" signs.'), marks=2),
    Q('Why do workers using loud machines wear ear muffs?', Lines(2, 'The ear muffs block loud sound and protect their hearing.'), marks=2),
])

investigate = Sheet('investigate', 'Which material blocks sound best?', level=2, goals=['Do a fair test.', 'Compare results.'], blocks=[
    P('Class 2C put a ticking clock in a box and covered it with different materials. A child stood at the same place and said how well they could hear it.'),
    Q('Complete the table and draw a bar chart (5 = very loud, 1 = very quiet).',
      Table(['Material', 'nothing', 'paper', 'cloth', 'cotton wool'], [['How loud (1–5)', '5', '4', '3', '1']], center=True),
      Graph(['nothing', 'paper', 'cloth', 'cotton wool'], [5, 4, 3, 1], 'How loud (1–5)', 'Material', ymax=5, step=1, width=100, height=46), marks=3),
    Q('Which material blocked the sound best?', Lines(1, 'cotton wool'), marks=1),
    Q('What did they keep the same?', Lines(1, 'the clock, the box, where the child stood'), marks=1),
])

case = Sheet('case', 'Quiet near the hospital', level=3, goals=['Think about noise and health.'], blocks=[
    Links('Science', 'Health', 'Citizenship'),
    Case('Near a hospital in Dhaka there is a sign: **"Silent zone. Do not use the horn."** Sick people need quiet so they can rest and get better.',
         'But many drivers still honk their horns. Children from a nearby school made posters and talked to drivers. They asked them to keep the area quiet. Some drivers stopped honking.',
         source='A story about noise near a hospital.'),
    Q('Why do people in hospital need quiet?', Lines(2, 'So they can rest, sleep and get better.'), marks=2),
    Q('What did the children do?', Lines(2, 'They made posters and asked drivers not to use their horns.'), marks=2),
    Q('Draw a poster to ask drivers to keep quiet.', Draw('40mm', 'My poster', 'e.g. a car with a cross over the horn: "Please, no horn near the hospital!"'), marks=2),
])

review = Sheet('review', 'Show what you know', level=3, goals=['Use sound words.'], blocks=[
    Q('Find the words.', WordSearch(['EAR', 'SOUND', 'LOUD', 'QUIET', 'DRUM', 'NOISE'], size=8, seed=212)),
    Q('Which part of the ear vibrates like a drum?', MCQ(['eardrum', 'nose', 'tongue'], 0), marks=1),
    Q('Which is best for blocking noise?', MCQ(['glass', 'thick cloth', 'metal'], 1), marks=1),
    Q('**Challenge.** Draw three things that make sounds in your home.', Draw('36mm', 'Sounds at home', 'e.g. a fan, a pressure cooker whistle, a phone, a doorbell.'), marks=3),
])

TOPIC = Topic(
    code='C3', strand='physical', title='Hearing and Sound', short='Hearing and sound',
    subtitle='The parts of the ear, why hearing matters, noise pollution, and sources of light and sound',
    outcomes=[
        'name the parts of the ear and explain how the ear detects sounds, using the terms outer, middle and inner ear, eardrum, cochlea, nerve and brain.',
        'explain why and how hearing is important to humans and animals.',
        'discuss sources of sound pollution and investigate different ways of insulating against sound.',
        'identify how light and sound are produced by a range of sources.',
    ],
    cambridge=['Stage 3 Unit 4 Our five senses (hearing)'],
    sheets=[learn, facts, think, investigate, case, review],
    selfcheck=['label the parts of the ear', 'explain how we hear', 'say why hearing matters', 'name ways to block noise', 'sort sources of light and sound'],
    cover_art=art.ear(labels=art.EAR_PARTS),
)
