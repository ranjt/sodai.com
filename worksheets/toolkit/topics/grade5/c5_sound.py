from build import Sheet, Topic
from ws import (P, H, Box, Vocab, Fig, Cols, Row, Case, Links, Lines, Blanks, Match, TrueFalse, MCQ, Order, Table,
                Ans, Sort, Label, Draw, Graph, WordSearch, Q, Part, Bullets)
import art

learn = Sheet('learn', 'Sound: vibrations that travel as waves', level=1, goals=[
    'Explain that sounds are made by vibrations and travel as waves.',
    'Use a wave model to explain pitch and loudness.',
    'Describe how we hear and how to protect our hearing.',
], blocks=[
    P('Tap a dhol, pluck an ektara string, or put your fingers on your throat and hum. You will feel something moving '
      'quickly backwards and forwards. These tiny, fast movements are **vibrations**, and every sound starts with one.', 'lead'),
    Cols(
        H('How sound travels', 3),
        P('A vibrating object pushes on the particles of the air next to it. They push the next particles, and the next, '
          'passing the vibration along like a ripple. This is a **sound wave**. Sound can travel through **gases** (air), '
          '**liquids** (water) and **solids** (wood, metal, string). It cannot travel through **empty space**, because there '
          'are no particles to pass the vibration on. In space, no one can hear you shout!'),
        Table(['Material', 'Speed of sound (approximate)'], [['air', '340 metres per second'], ['water', '1500 metres per second'], ['steel', '5900 metres per second']]),
        P('Sound travels faster through solids and liquids because their particles are closer together. Light travels much '
          'faster than sound, which is why we see lightning before we hear the thunder.'),
        H('Pitch: high or low', 3),
        P('**Pitch** is how high or low a sound is. Fast vibrations make a **high** pitch; slow vibrations make a **low** pitch. '
          'The number of vibrations each second is called the **frequency**, measured in hertz (Hz). On a string instrument, a '
          '**shorter**, **tighter** or **thinner** string gives a higher pitch. On a flute (*bansuri*), covering holes makes '
          'the column of air longer and the pitch lower.'),
        H('Loudness: loud or quiet', 3),
        P('**Loudness** depends on how big the vibrations are. Hitting a drum harder makes bigger vibrations and a **louder** '
          'sound. On a wave diagram, the **height** of the wave shows loudness and how **close together** the waves are shows pitch.'),
        Fig(art.sound_waves(), 'Comparing sound waves.', span=True, width='80%'),
        H('How we hear', 3),
        P('The **outer ear** collects sound and funnels it down the **ear canal** to the **eardrum**, which vibrates. Three '
          '**tiny bones** pass the vibrations to the **cochlea**, which turns them into messages that travel along a **nerve** '
          'to the **brain**.'),
        Fig(art.ear(labels=art.EAR_PARTS)),
        H('Protect your hearing', 3),
        P('Loudness is measured in **decibels (dB)**. A whisper is about 30 dB and normal talking about 60 dB. Listening to '
          'sounds louder than about 85 dB for a long time can **permanently damage** hearing. Keep headphones turned down and '
          'cover your ears near very loud noises.'),
        Fig(art.instruments(), 'Bangladeshi instruments: a drum, a string instrument and a wind instrument.'),
    ),
    Vocab([('vibration', 'a quick movement backwards and forwards'), ('sound wave', 'vibrations passed from particle to particle'),
           ('pitch', 'how high or low a sound is'), ('frequency', 'number of vibrations each second (Hz)'), ('loudness', 'how loud or quiet a sound is'),
           ('decibel (dB)', 'unit for measuring loudness'), ('eardrum', 'thin skin in the ear that vibrates when sound reaches it')]),
])

facts = Sheet('facts', 'Making and hearing sounds', level=1, goals=['Recall how sound is made and heard.', 'Label the ear.'], blocks=[
    Q('Label the parts of the ear.', Label(art.ear(), art.EAR_PARTS, width='86%', cols=3), marks=6),
    Q('Fill in the gaps.',
      Blanks('All sounds are made by [vibrations]. Sound travels as a [wave]. It can travel through solids, liquids and '
             '[gases], but not through empty [space]. Fast vibrations make a [high] pitch.', extra=['low', 'light']), marks=5),
    Q('What vibrates to make the sound?',
      Table(['Instrument', 'What vibrates?'], [['dhol (drum)', Ans('the drum skin')], ['ektara', Ans('the string')], ['bansuri (flute)', Ans('the air inside')],
                                               ['your voice', Ans('the vocal cords in your throat')]], widths=['40%', '60%']), marks=4),
    Q('True or false?', TrueFalse([
        ('Sound travels faster through steel than through air.', True), ('A bigger vibration makes a quieter sound.', False, 'A bigger vibration makes a louder sound.'),
        ('Astronauts on the Moon can hear each other without radios.', False, 'There is no air on the Moon, so sound cannot travel.'),
        ('A shorter string makes a higher pitch.', True)]), marks=4),
])

think = Sheet('think', 'Pitch, loudness and waves', level=2, goals=['Use wave diagrams.', 'Explain pitch and loudness changes.'], blocks=[
    Q('Look at the four waves A to D.',
      Fig(art.sound_waves(numbered=True), width='64%'),
      Part('Which wave is the loudest with the lowest pitch?', Lines(1, 'A')),
      Part('Which wave is the quietest with the highest pitch?', Lines(1, 'D')),
      Part('What is the same about waves A and C? What is different?', Lines(2, 'Same height, so the same loudness; C has more waves close together, so a higher pitch.')), marks=4),
    Q('An ektara player squeezes the bamboo neck to make the string tighter. What happens to the pitch? Why?',
      Lines(2, 'The pitch gets higher, because a tighter string vibrates faster.'), marks=2),
    Q('Why do we see lightning before we hear the thunder?', Lines(2, 'Light travels much faster than sound, so it reaches us first.'), marks=2),
    Q('A string telephone works only when the string is tight. Explain.',
      Fig(art.string_phone(), width='58%'),
      Lines(2, 'Vibrations travel along a tight string from one cup to the other; a loose string does not pass the vibrations on.'), marks=2),
])

investigate = Sheet('investigate', 'Ruler twang: length and pitch', level=2, goals=['Investigate pitch with a fair test.', 'Plot and use a line graph.', 'Explain using vibrations.'], blocks=[
    P('Tania held a ruler on the edge of a table and twanged the end. She changed how much of the ruler stuck out over the '
      'edge. A sound app on a tablet counted the vibrations each second (frequency).'),
    Q('Name the variables.',
      Table(None, [['Change', Ans('length of ruler over the edge')], ['Measure', Ans('frequency (vibrations per second, Hz)')],
                   ['Keep the same', Ans('the same ruler, how hard she pressed and twanged, same table')]], widths=['24%', '76%']), marks=3),
    Q('Plot the results as a line graph.',
      Table(['Length over the edge (cm)', '10', '15', '20', '25'], [['Frequency (Hz)', '120', '55', '30', '20']], center=True),
      Graph(['10 cm', '15 cm', '20 cm', '25 cm'], [120, 55, 30, 20], 'Frequency (Hz)', 'Length over the edge', ymax=130, step=10, kind='line',
            width=140, height=56), marks=4),
    Q('Describe the pattern. Which length made the highest pitch?',
      Lines(2, 'The longer the ruler over the edge, the lower the frequency and pitch. 10 cm made the highest pitch.'), marks=2),
    Q('Predict the frequency for 12 cm.', Lines(1, 'between 55 and 120 Hz, about 85–95 Hz'), marks=1),
    Q('How could Tania test how loudness changes? Write a plan in one sentence.',
      Lines(2, 'Keep the length the same and twang the ruler with a small and a big push, measuring the loudness (dB) with the app.'), marks=2),
])

case = Sheet('case', 'Too loud! Noise in Dhaka', level=3, goals=['Use data about loudness.', 'Explain health effects of noise.', 'Evaluate solutions from different viewpoints.'], blocks=[
    Links('Science', 'Health', 'Maths', 'Citizenship', 'Ethics'),
    Case('In 2022, a United Nations Environment Programme report named **Dhaka** as one of the noisiest cities in the '
         'world. Car and bus horns, construction machines, loudspeakers and generators fill the streets with sound.',
         'Doctors say that living with loud noise every day can cause **hearing loss**, headaches, stress, high blood pressure '
         'and poor sleep. Children in noisy schools find it harder to concentrate and learn.',
         'Bangladesh has **noise rules**: areas around hospitals, schools and offices are meant to be **silent zones**, with '
         'limits as low as 50 dB in the daytime, and very loud hydraulic horns are banned. But the rules are often broken.',
         source='Sources: UNEP Frontiers Report 2022; Bangladesh Noise Pollution (Control) Rules 2006.'),
    Q('A class measured the loudness at different places with a sound meter app (example readings).',
      Table(['Place', 'school library', 'classroom', 'busy road outside school', 'bus horn nearby'], [['Loudness (dB)', '35', '60', '85', '110']], center=True),
      Graph(['library', 'classroom', 'busy road', 'bus horn'], [35, 60, 85, 110], 'Loudness (dB)', 'Place', ymax=120, step=10, width=130, height=62),
      Part('Draw the bar chart.'),
      Part('Which places are louder than the 50 dB limit for a silent zone?', Lines(1, 'classroom (60), busy road (85), bus horn (110)')),
      Part('Which place could damage hearing if people stayed there for a long time?', Lines(1, 'the busy road and near bus horns (85 dB and above)')), marks=4),
    Q('Explain why a loud horn could harm the ear, using what you know about the eardrum.',
      Lines(2, 'Very big vibrations make the eardrum and the tiny parts of the cochlea vibrate very strongly, which can damage them.'), marks=2),
    Q('What might each person say?',
      Table(['Person', 'View'], [['a bus driver', Ans('Everyone pushes in; I must honk to stay safe and keep moving.')],
                                 ['a teacher near the road', Ans('Children cannot hear me or concentrate; the noise hurts learning.')],
                                 ['a traffic police officer', Ans('Horn rules are hard to enforce; drivers need training and checks.')]], widths=['30%', '70%']), marks=3),
    Q('Design a "Quiet School Zone" plan with **three** actions.',
      Lines(3, 'e.g. "No horn" signs and speed bumps near school; plant trees and build walls to block sound; awareness campaign for drivers; fines for hydraulic horns; double windows or curtains in classrooms.'), marks=3),
])

review = Sheet('review', 'Show what you know', level=3, goals=['Use key vocabulary.', 'Answer test-style questions.'], blocks=[
    Q('Find the key words.', WordSearch(['VIBRATE', 'PITCH', 'LOUD', 'WAVE', 'EARDRUM', 'DECIBEL', 'ECHO', 'DRUM', 'STRING'], size=11, seed=141)),
    Q('Which change makes a guitar string sound higher?', MCQ(['make it longer', 'make it looser', 'make it shorter', 'pluck it more gently'], 2), marks=1),
    Q('Why can\'t sound travel in space?', MCQ(['it is too cold', 'there are no particles to pass on vibrations', 'it is too dark', 'the Sun is too loud'], 1, one_col=True), marks=1),
    Q('Draw two waves: one quiet, high-pitched sound and one loud, low-pitched sound.',
      Row([Draw('30mm', 'quiet, high pitch', 'Short waves, close together.')], [Draw('30mm', 'loud, low pitch', 'Tall waves, far apart.')]), marks=2),
    Q('**Challenge.** Whales can hear each other across hundreds of kilometres of ocean. Use what you know about sound to suggest why.',
      Lines(3, 'Sound travels well and fast through water because the particles are close together; low-pitched whale calls travel very far.'), marks=2),
])

TOPIC = Topic(
    code='C5', strand='physical', title='Sound', short='Sound',
    subtitle='Vibrations, sound waves, pitch and loudness, hearing and noise',
    outcomes=['understand that sound travels through waves.', 'model how sound travels as a wave, and relate the wave to the pitch and the loudness of the sound heard.'],
    sheets=[learn, facts, think, investigate, case, review],
    selfcheck=['explain that sounds are made by vibrations', 'explain how sound travels through solids, liquids and gases',
               'use wave diagrams to compare pitch and loudness', 'explain how we hear', 'investigate how length changes pitch',
               'explain why noise is a health problem and suggest solutions'],
    cover_art=art.sound_waves(),
)
