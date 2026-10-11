from build import Sheet, Topic
from ws import (P, H, Box, Vocab, Fig, Cols, Row, Case, Links, Lines, Blanks, Match, TrueFalse, MCQ, Order, Table,
                Ans, Sort, Label, Draw, Graph, WordSearch, Q, Part, Bullets)
import art

learn = Sheet('learn', 'Shadows and light intensity', level=1, goals=[
    'Explain that light travels in straight lines and how shadows form.',
    'Classify materials as transparent, translucent or opaque.',
    'Explain how shadows change and how light intensity is measured.',
], blocks=[
    P('On a sunny afternoon your shadow stretches out long and thin across the school field. At midday it shrinks to a '
      'small dark patch around your feet. Why do shadows form, and why do they change?', 'lead'),
    Cols(
        H('Light travels in straight lines', 3),
        P('Light travels from a source in **straight lines**. You can see this when sunbeams shine through a gap in the curtains '
          'into a dusty room, or when a torch beam cuts through mist. It is also why you cannot see round corners.'),
        H('Transparent, translucent and opaque', 3),
        Bullets(['**Transparent** materials let almost all light pass straight through, so you can see clearly through them: clear glass, clear plastic, water.',
                 '**Translucent** (partly transparent) materials let some light through but scatter it, so things look blurred: tracing paper, frosted glass, thin cotton cloth.',
                 '**Opaque** materials let no light through: wood, cardboard, metal, your body.']),
        Fig(art.transparency(), 'How light passes through different materials.'),
        H('How shadows form', 3),
        P('A **shadow** forms when an **opaque** object **blocks** light travelling from a source. Because light travels in straight '
          'lines, it cannot bend round the object, so a dark area is left behind it. A shadow has the same **outline shape** as the '
          'object, but it shows no colour or detail.'),
        Fig(art.shadow_setup(), 'An opaque object blocks light to make a shadow.'),
        P('The **closer** an object is to the light source, the **bigger** its shadow, because it blocks more of the light. Moving '
          'the object further from the source makes the shadow smaller and sharper. Turning the object changes the shadow\'s shape.'),
        Box('bd', P('Shadow puppet shows use cut-out shapes held between a lamp and a cloth screen. In many places, including '
                    'Bangladesh, the times of some daily prayers were traditionally worked out by measuring the length of shadows.')),
        H('Shadows during the day', 3),
        P('The Sun seems to move across the sky from **east** to **west** (really, the Earth is spinning). In the **morning** and '
          '**evening** the Sun is low, so shadows are **long**. At **midday** the Sun is highest, so shadows are **shortest**. '
          'Shadows always point **away** from the Sun, so they move round during the day. A **sundial** uses this to tell the time.'),
        Fig(art.sun_path(), 'Shadows of a stick during one day.', span=True, width='78%'),
        H('Measuring light intensity', 3),
        P('**Light intensity** is how bright light is. It is measured with a **light meter** (or a light sensor on a tablet) in '
          'units called **lux**. A light meter gives a number, which is fairer and more accurate than saying "quite bright".'),
        Row([Fig(art.light_meter(450), 'A light meter.')],
            [Table(['Place', 'Light intensity (about)'], [['sunny day outdoors', '50 000–100 000 lux'], ['cloudy day outdoors', '1000–10 000 lux'],
                                                         ['well-lit classroom', '300–500 lux'], ['full moon', 'less than 1 lux']])], widths=['24%', '76%']),
        Box('history', P('People once thought light arrived instantly. In **1676**, the Danish astronomer **Ole Rømer** noticed that '
                         'one of Jupiter\'s moons appeared from behind the planet later than expected when Earth was further away. '
                         'He realised that light **takes time** to travel. In **1849**, **Hippolyte Fizeau** in France measured the '
                         'speed of light on Earth using a spinning toothed wheel and a mirror 8 km away. Today we know light travels '
                         'about **300 000 km every second**. Sunlight takes about 8 minutes to reach us.'), title='How scientists measured light'),
    ),
    Vocab([('transparent', 'lets light through clearly'), ('translucent', 'lets some light through but scatters it'),
           ('opaque', 'lets no light through'), ('shadow', 'a dark area where light is blocked'), ('light intensity', 'how bright light is'),
           ('lux', 'the unit of light intensity'), ('light meter', 'an instrument that measures light intensity'), ('sundial', 'a clock that uses a shadow')]),
])

facts = Sheet('facts', 'Light, materials and shadows', level=1, goals=['Classify materials.', 'Recall how shadows form and change.'], blocks=[
    Q('Sort the materials.',
      Sort(['Transparent', 'Translucent', 'Opaque'], [
          ('clear glass', 'Transparent'), ('water', 'Transparent'), ('clear plastic bottle', 'Transparent'),
          ('tracing paper', 'Translucent'), ('frosted glass', 'Translucent'), ('thin cotton cloth', 'Translucent'),
          ('wood', 'Opaque'), ('cardboard', 'Opaque'), ('steel tray', 'Opaque')]), marks=9),
    Q('Why can you read a book through clear glass but not through tracing paper or cardboard?',
      Fig(art.transparency(), width='64%'),
      Lines(3, 'Glass is transparent: light passes straight through. Tracing paper is translucent: it scatters the light so the words look blurred. Cardboard is opaque: no light gets through.'), marks=3),
    Q('Fill in the gaps.',
      Blanks('Light travels in [straight] lines. A shadow forms when an [opaque] object blocks the light. Shadows are '
             '[longest] in the morning and evening and [shortest] at midday. Light intensity is measured in [lux].',
             extra=['curved', 'metres']), marks=5),
    Q('True or false?', TrueFalse([
        ('A shadow shows the colours of the object.', False, 'A shadow only shows the outline shape.'),
        ('Moving an object closer to the torch makes its shadow bigger.', True),
        ('Shadows point towards the Sun.', False, 'Shadows point away from the Sun.'),
        ('A light meter measures how bright light is.', True)]), marks=4),
])

think = Sheet('think', 'Changing shadows', level=2, goals=['Explain shadow size and shape.', 'Interpret shadow data from a day.'], blocks=[
    Q('Look at the torch, object and screen.', Fig(art.shadow_setup(), width='60%'),
      Part('What would happen to the shadow if you moved the object closer to the torch?', Lines(1, 'It would get bigger (and a little more blurred).')),
      Part('How could you make the shadow a different shape without changing the object?', Lines(1, 'Turn the object round or tilt it.')),
      Part('Why is the shadow the same shape as the object?', Lines(2, 'Light travels in straight lines, so it is blocked exactly by the outline of the object.')), marks=4),
    Q('Why can you not see a clear shadow on a very cloudy day?', Lines(2, 'Clouds scatter the sunlight so light comes from all directions; nothing blocks all of it.'), marks=1),
    Q('Nadia measured the shadow of a 1 metre stick in the school yard.',
      Table(['Time', '8 am', '10 am', '12 noon', '2 pm', '4 pm'], [['Shadow length (cm)', '210', '80', '30', '75', '190']], center=True),
      Graph(['8 am', '10 am', '12 noon', '2 pm', '4 pm'], [210, 80, 30, 75, 190], 'Shadow length (cm)', 'Time of day', ymax=220, step=20, width=130, height=56),
      Part('Draw a bar chart of the results.'),
      Part('Describe the pattern and explain it.', Lines(3, 'The shadow was long in the morning, shortest at noon and long again in the afternoon, because the Sun is low in the morning and evening and highest at midday.')),
      Part('In which direction did the shadow point at 8 am? Why?', Lines(2, 'West, because the Sun was in the east and shadows point away from the Sun.')), marks=6),
])

investigate = Sheet('investigate', 'How does distance from the torch change shadow size?', level=2, goals=['Plan a fair test.', 'Plot a line graph.', 'Use the pattern to predict.'], blocks=[
    P('Jamal put a torch on a table and a screen 60 cm away. He held a card puppet 10 cm tall at different distances from the '
      'torch and measured the height of the shadow on the screen.'),
    Q('Complete the plan.',
      Table(None, [['Question', Ans('How does the distance between the torch and the puppet change the size of the shadow?')],
                   ['Change', Ans('distance of the puppet from the torch')], ['Measure', Ans('height of the shadow (cm)')],
                   ['Keep the same', Ans('the same puppet and torch, screen distance, room darkness')],
                   ['Prediction', Ans('The closer the puppet is to the torch, the bigger the shadow.')]], widths=['24%', '76%']), marks=5),
    Q('Plot the results as a line graph.',
      Table(['Distance from torch (cm)', '10', '20', '30', '40', '50'], [['Shadow height (cm)', '60', '30', '20', '15', '12']], center=True),
      Graph(['10', '20', '30', '40', '50'], [60, 30, 20, 15, 12], 'Shadow height (cm)', 'Distance from torch (cm)', ymax=70, step=10, kind='line',
            width=140, height=50), marks=4),
    Q('Describe the pattern. Did the results support Jamal\'s prediction?',
      Lines(2, 'The closer the puppet was to the torch, the taller the shadow. Yes, the results support the prediction.'), marks=2),
    Q('Predict the shadow height when the puppet is 15 cm from the torch.', Lines(1, 'about 40 cm (between 60 cm and 30 cm)'), marks=1),
    Q('Why can the shadow never be smaller than 10 cm in this test?',
      Lines(1, 'Next to the screen, the shadow is the same size as the puppet (10 cm).'), marks=1),
])

case = Sheet('case', 'A brighter, cooler classroom', level=3, goals=['Use light intensity data.', 'Apply knowledge of materials to a design problem.', 'Weigh up costs and benefits.'], blocks=[
    Links('Science', 'Design', 'Maths', 'Environment', 'Economics'),
    Case('In Bangladesh, classrooms can get very **hot** from April to October. Teachers often close the curtains to keep out the '
         'heat and glare, but then the room gets **dark** and the lights must be switched on, which uses electricity. Some '
         'learners at the back cannot see the board clearly.',
         'Experts recommend about **300 to 500 lux** for reading and writing in classrooms. Too little light strains the eyes; '
         'direct sunlight on desks causes **glare** and heat. Good classroom design uses daylight wisely: light-coloured walls '
         'and ceilings **reflect** light around the room, **translucent** blinds let light in but block direct sun, and trees or '
         'shades outside block heat from the walls and windows.',
         source='Example readings below; lighting levels based on common school lighting guidelines.'),
    Q('Grade 5 measured light intensity around their classroom with a light meter app at 11 am, with the curtains closed and lights off.',
      Table(['Place', 'by the window', 'middle desk', 'board', 'back corner'], [['Light (lux)', '650', '280', '220', '120']], center=True),
      Graph(['window', 'middle', 'board', 'back corner'], [650, 280, 220, 120], 'Light intensity (lux)', 'Place', ymax=700, step=50, width=130, height=56),
      Part('Draw the bar chart.'),
      Part('Which places are below 300 lux?', Lines(1, 'middle desk (280), board (220), back corner (120)')), marks=3),
    Q('For each idea, explain the science.',
      Table(['Idea', 'How it helps (use the words reflect, translucent or opaque)'], [
          ['paint the walls white', Ans('White surfaces reflect more light, so the room is brighter.')],
          ['translucent blinds', Ans('They let some light in but scatter it, so less glare and heat.')],
          ['plant trees outside the windows', Ans('Opaque leaves block direct sunlight and shade the walls, keeping the room cooler.')]], widths=['30%', '70%']), marks=3),
    Q('What might each person think?',
      Table(['Person', 'View'], [['the head teacher', Ans('White paint is cheap, but new blinds cost money.')],
                                 ['a learner at the back', Ans('I need more light to see the board.')],
                                 ['the school caretaker', Ans('Using daylight saves electricity bills.')]], widths=['30%', '70%']), marks=3),
    Q('Draw and label your design for a brighter, cooler classroom.', Draw('44mm', 'My classroom design', 'Labels such as white walls and ceiling, translucent blinds, tree shade, windows on two sides, LED lights for cloudy days.'), marks=3),
])

review = Sheet('review', 'Show what you know', level=3, goals=['Use key vocabulary.', 'Answer test-style questions.'], blocks=[
    Q('Find the key words.', WordSearch(['SHADOW', 'OPAQUE', 'LUX', 'BLOCK', 'SUNDIAL', 'TORCH', 'STRAIGHT', 'METER', 'NOON'], size=11, seed=181)),
    Q('Which material would make the darkest shadow?', MCQ(['clear glass', 'tracing paper', 'cardboard', 'water'], 2), marks=1),
    Q('When is your shadow shortest on a sunny day?', MCQ(['early morning', 'midday', 'late afternoon', 'at sunset'], 1), marks=1),
    Q('Draw the shadow of the stick at 9 am and at 4 pm. Label east and west.',
      Draw('36mm', 'Stick shadows', '9 am: long shadow pointing west (Sun in the east). 4 pm: long shadow pointing east (Sun in the west).'), marks=2),
    Q('**Challenge.** How did Ole Rømer show that light takes time to travel? Why was this an important idea?',
      Lines(3, 'Jupiter\'s moon appeared later when the Earth was further from Jupiter, so the light needed extra time to travel the extra distance. It proved light has a speed and is not instant.'), marks=2),
])

TOPIC = Topic(
    code='C8', strand='physical', title='Light: Shadows and Intensity', short='Shadows',
    subtitle='Straight-line travel, transparent, translucent and opaque, shadows, and measuring light',
    outcomes=[
        'know that light intensity can be measured.',
        'investigate how light travels, understanding that light travels in a straight line.',
        'classify materials as transparent, partly transparent (translucent) or opaque.',
        'observe that shadows are formed when light travelling from a source is blocked.',
        'create shadows and investigate how the size and shape of a shadow can be changed.',
        'observe that shadows change in length and position throughout the day.',
    ],
    cambridge=['Unit 5 Shadows (5.1–5.7)'],
    sheets=[learn, facts, think, investigate, case, review],
    selfcheck=['explain that light travels in straight lines', 'sort materials as transparent, translucent or opaque',
               'explain how a shadow forms', 'investigate how shadow size changes', 'explain how shadows change during the day',
               'measure light intensity in lux'],
    cover_art=art.shadow_setup(),
)
