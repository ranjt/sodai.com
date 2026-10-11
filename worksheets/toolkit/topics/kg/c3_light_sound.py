from build import Sheet, Topic
from ws import (P, H, Box, Fig, Q, Lines, MCQ, Draw, Pics, Ans, Case, Choose, PicMatch, PicSort, Pictograph, Trace)
import art

learn = Sheet('learn', 'Light and sound', level=1, goals=['Name things that give light.', 'Name ways to make sounds.'], blocks=[
    Box('adult', P('Read aloud. Turn off the lights for a moment, then switch on a torch. Then make sounds with a drum, a bottle and a shaker.')),
    P('Light helps us **see**. Things that give light are **light sources**.', 'lead'),
    Pics([('sun', 'Sun'), ('light bulb', 'lamp'), ('flashlight', 'torch'), ('candle', 'candle'), ('fire', 'fire'), ('star', 'stars')], cols=6, size='18mm'),
    P('Sound helps us **hear**. We hear sounds with our **ears**.', 'lead'),
    H('Ways to make sounds', 3),
    Pics([('drum', 'hit a drum'), ('flute', 'blow a flute'), ('maracas', 'shake a shaker'), ('guitar', 'pluck strings'), ('clapping hands', 'clap')], cols=5, size='19mm'),
    P('Sounds get **quieter** when we move **far away** from them.'),
])

facts = Sheet('facts', 'Light or sound?', level=1, goals=['Find light sources.', 'Sort light and sound.'], blocks=[
    Q('Circle the things that **give light**.', Choose([('sun', 'Sun'), ('teddy bear', 'teddy'), ('candle', 'candle'), ('football', 'ball'),
                                                       ('flashlight', 'torch'), ('chair', 'chair')], right=[0, 2, 4], cols=6, size='18mm')),
    Q('Cut and sort: makes **light** or makes **sound**?', PicSort(['Light', 'Sound'], [('light bulb', 'lamp', 'Light'), ('star', 'stars', 'Light'), ('fire', 'fire', 'Light'),
                                                                                    ('drum', 'drum', 'Sound'), ('bell', 'bell', 'Sound'), ('dog', 'barking dog', 'Sound')], height='32mm')),
])

think = Sheet('think', 'How do we make sounds?', level=2, goals=['Match sounds to actions.'], blocks=[
    Q('Match each instrument to how you play it.', PicMatch([(('drum', 'drum'), ('hand', 'hit')), (('flute', 'flute'), ('wind face', 'blow')),
                                                             (('maracas', 'shaker'), ('clapping hands', 'shake'))], size='15mm')),
    Q('Which is louder: a bell near you or far away?', MCQ(['near me', 'far away'], 0)),
])

investigate = Sheet('investigate', 'Make a shaker', level=2, goals=['Make shakers.', 'Compare their sounds.'], blocks=[
    Box('adult', P('Fill small bottles with rice, dal, sand or stones. Close them tightly. Shake each one: which is the loudest?')),
    Q('How loud was each shaker? Colour boxes: more boxes = louder.', Pictograph([('cooked rice', 'rice', 3), ('peanuts', 'dal', 4), ('rock', 'stones', 7), ('droplet', 'sand', 2)], top=8)),
    Q('Which shaker was the loudest? Circle it.', Choose([('cooked rice', 'rice'), ('peanuts', 'dal'), ('rock', 'stones'), ('droplet', 'sand')], right=[2])),
])

case = Sheet('case', 'The power cut', level=3, goals=['Listen to a story.', 'Think about light sources.'], blocks=[
    Case('One evening the lights went out. Everything was dark! Babu could not see his toys.',
         'Mother lit a candle and Father switched on a torch. Now Babu could see again. Outside, the stars were shining in the sky.'),
    Q('Circle the light sources in the story.', Choose([('candle', 'candle'), ('flashlight', 'torch'), ('teddy bear', 'toys'), ('star', 'stars')], right=[0, 1, 3])),
    Box('safety', P('Only a grown-up should light a candle. Never look straight at the Sun.')),
])

review = Sheet('review', 'I can do it!', level=3, goals=['Trace light and sound words.'], blocks=[
    Q('Trace the words.', Trace([('light', 'light bulb'), ('sound', 'bell')])),
    Q('Circle what we use to **hear**.', Choose([('eye', 'eyes'), ('ear', 'ears'), ('hand', 'hands')], right=[1], cols=3)),
])

TOPIC = Topic(
    code='C3', strand='physical', title='Light and Sound', short='Light and sound',
    subtitle='Light sources, ways to make sounds, and hearing sounds near and far',
    outcomes=[
        'identify different sources of light and sound.',
        'explore different ways to produce sound using familiar objects and actions — striking, blowing, scraping and shaking.',
        'identify many sources of sound, and know that we hear when sound enters our ear.',
        'recognise that as sound travels from a source it becomes fainter.',
    ],
    sheets=[learn, facts, think, investigate, case, review],
    selfcheck=['name light sources', 'make sounds in different ways', 'say why far sounds are quiet'],
    cover_art=art.pic_row(['sun', 'flashlight', 'candle', 'drum', 'bell'], ['Sun', 'torch', 'candle', 'drum', 'bell']),
)
