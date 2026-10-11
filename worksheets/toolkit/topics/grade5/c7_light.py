from build import Sheet, Topic
from ws import (P, H, Box, Vocab, Fig, Cols, Row, Case, Links, Lines, Blanks, Match, TrueFalse, MCQ, Order, Table,
                Ans, Sort, Label, Draw, Graph, WordSearch, Q, Part, Bullets)
import art

learn = Sheet('learn', 'Light: how we see things', level=1, goals=[
    'Explain how we see light sources and other objects.',
    'Describe reflection, lateral inversion and refraction.',
    'Describe how optical devices and the human eye work.',
], blocks=[
    P('Close your eyes and you see nothing. Open them and the world appears, full of colour and detail. What is happening? '
      'Scientists have argued about this for more than two thousand years. Today we know the answer: **we see when light '
      'enters our eyes**.', 'lead'),
    Cols(
        H('Light sources', 3),
        P('A **light source** makes its own light: the Sun, a candle flame, a light bulb, a torch, lightning and even a '
          'firefly (*jonaki*). Most things are **not** light sources. A book, a tree, your friend\'s face and even the **Moon** '
          'only **reflect** light that falls on them. The Moon looks bright at night because it reflects light from the Sun.'),
        P('We see a light source when its light travels **straight into our eyes**. We see every other object when light from a '
          'source **bounces off** (reflects from) the object and then enters our eyes.'),
        Fig(art.seeing_object(), 'How we see a book.'),
        Box('safety', P('Never look directly at the Sun, even with sunglasses. Its light is strong enough to damage your eyes for ever.')),
        H('Absorbed, reflected or refracted', 3),
        P('When light hits a material, three things can happen. Dark, dull materials **absorb** most of the light, so they look '
          'dark. Light-coloured materials **reflect** a lot of light. Transparent materials such as glass and water let light pass '
          'through, but they can bend it (**refract** it).'),
        H('Reflection and mirrors', 3),
        P('A **mirror** is very smooth and shiny, so it reflects light neatly in one direction. A ray of light hits the mirror '
          'and bounces off at the **same angle**: the angle of the incoming ray equals the angle of the reflected ray, measured '
          'from a line at right angles to the mirror called the **normal**. Rough surfaces scatter light in all directions, so '
          'they do not make a clear image.'),
        Fig(art.reflection(), 'The law of reflection.'),
        P('Your image in a mirror is the right way up but **back to front**. Raise your right hand, and the image raises its left. '
          'This is called **lateral inversion**. That is why the word AMBULANCE is painted back to front on the front of '
          'ambulances: drivers in front read it the right way round in their mirrors.'),
        Fig(art.mirror_writing(), 'Lateral inversion.'),
        P('A **periscope** uses two mirrors at 45° to let you see over a wall or round a corner. Submarines use them to see above the water.'),
        Fig(art.periscope(), 'Light reflects twice inside a periscope.', width='62%'),
        H('Refraction', 3),
        P('Light travels more slowly in water and glass than in air. When light passes from one material into another at an '
          'angle, it **changes direction**. This is **refraction**. It makes a pencil in a glass of water look broken, and it makes '
          'ponds look shallower than they really are.'),
        Row([Fig(art.refraction_glass(), 'A pencil looks bent.')], [Fig(art.refraction_ray(), 'Light bends as it enters water.')]),
        H('Optical devices', 3),
        Table(['Device', 'What it does to light'], [
            ['hand lens', 'a curved glass **lens** refracts light to make things look **bigger** (magnified)'],
            ['telescope', 'lenses or curved mirrors collect light from far away so stars and planets look **closer**'],
            ['pinhole camera', 'light travels in straight lines through a tiny hole to make an **upside-down** image'],
            ['camera', 'a lens **focuses** light onto a sensor (or film) to record an image'],
            ['kaleidoscope', 'mirrors inside a tube reflect coloured pieces again and again to make **repeating patterns**']]),
        Fig(art.optical_devices(), 'Five optical devices.', span=True, width='88%'),
        H('The human eye', 3),
        P('Your **eyelid** protects the eye and spreads tears to keep it clean. Light enters through the **pupil**, a hole that '
          'gets smaller in bright light and bigger in the dark. The **lens** focuses the light to make a tiny upside-down image on '
          'the **retina** at the back of the eye. Millions of light-sensitive cells in the retina send messages along the **optic '
          'nerve** to the **brain**, which turns the image the right way up and tells you what you are seeing.'),
        Fig(art.eye(labels=art.EYE_PARTS), 'Inside the eye (side view).'),
        Box('history', P('Around the year 1015, the scientist **Ibn al-Haytham** (born in Basra, worked in Cairo) wrote the *Book '
                         'of Optics*. Through careful experiments, including with a darkened room and a tiny hole (a pinhole '
                         'camera), he showed that we see because light **enters** our eyes, not because our eyes send out rays, '
                         'as many people believed. He is often called the father of optics.'), title='From the past'),
    ),
    Vocab([('light source', 'something that makes its own light'), ('reflect', 'bounce light off a surface'),
           ('absorb', 'take in light'), ('refraction', 'light changing direction as it passes into a different material'),
           ('normal', 'a line at right angles to a mirror or surface'), ('lateral inversion', 'a mirror image is back to front'),
           ('lens', 'curved glass or plastic that bends light'), ('retina', 'the light-sensitive layer at the back of the eye')]),
])

facts = Sheet('facts', 'Light sources, mirrors and the eye', level=1, goals=['Identify light sources.', 'Label the eye.', 'Recall what optical devices do.'], blocks=[
    Q('Sort these objects.',
      Sort(['Light source', 'Not a light source (reflects light)'], [
          ('the Sun', 'Light source'), ('a candle flame', 'Light source'), ('a firefly', 'Light source'), ('an LED bulb', 'Light source'),
          ('the Moon', 'Not a light source (reflects light)'), ('a mirror', 'Not a light source (reflects light)'),
          ('a white page', 'Not a light source (reflects light)'), ('a shiny spoon', 'Not a light source (reflects light)')]), marks=8),
    Q('Label the parts of the eye.', Label(art.eye(), art.EYE_PARTS, width='70%', cols=3), marks=5),
    Q('Match each optical device to what it does.',
      Match([('hand lens', 'makes small things look bigger'), ('telescope', 'makes far-away objects look closer'),
             ('pinhole camera', 'makes an upside-down image through a tiny hole'), ('kaleidoscope', 'uses mirrors to make repeating patterns'),
             ('periscope', 'uses two mirrors to see over a wall')]), marks=5),
    Q('True or false?', TrueFalse([
        ('The Moon is a light source.', False, 'The Moon reflects light from the Sun.'),
        ('Light hits a mirror and bounces off at the same angle.', True),
        ('Our eyes send out rays so that we can see.', False, 'Light enters our eyes from sources or reflected from objects.'),
        ('The pupil gets bigger in the dark.', True)]), marks=4),
])

think = Sheet('think', 'Tracing the path of light', level=2, goals=['Draw ray diagrams.', 'Explain reflection, refraction and lateral inversion.'], blocks=[
    Q('Draw arrows to show how Mina sees the mango. Label the light source.',
      Draw('34mm', 'Sun → mango → Mina\'s eye', 'An arrow from the Sun to the mango, then an arrow from the mango into Mina\'s eye. The Sun is labelled as the light source.'), marks=2),
    Q('A ray of light hits a mirror at an angle of 35° to the normal. What is the angle of the reflected ray? Explain.',
      Lines(2, '35°: light is reflected at the same angle as the incoming ray.'), marks=2),
    Q('Look at the periscope.',
      Fig(art.periscope(), width='25%'),
      Part('Why must both mirrors be at 45°?', Lines(2, 'So the light turns through a right angle at each mirror: first down the tube, then out to the eye.')),
      Part('Give one real use of a periscope.', Lines(1, 'seeing over a crowd or wall; seeing above water from a submarine; seeing round corners')), marks=3),
    Q('Rafi writes his name on a card and holds it up to a mirror. Describe what he sees and use the scientific term.',
      Lines(2, 'The letters are back to front (reversed left to right). This is lateral inversion.'), marks=2),
    Q('A fisherman spears a fish that looks close to the water surface, but he misses. Use refraction to explain why.',
      Lines(3, 'Light from the fish bends as it leaves the water, so the fish looks higher (shallower) than it really is. He must aim lower.'), marks=2),
    Q('Why does your pupil get smaller when you walk out into bright sunshine?',
      Lines(2, 'To let less light into the eye and protect the retina from too much light.'), marks=1),
])

investigate = Sheet('investigate', 'Investigating mirrors: angles of reflection', level=2, goals=['Measure angles with a protractor.', 'Spot a result that does not fit.', 'Draw a conclusion.'], blocks=[
    P('Class 5C shone a thin beam of light from a ray box onto a plane mirror. They drew the normal, then used a protractor to '
      'measure the angle of the incoming ray and the angle of the reflected ray.'),
    Fig(art.reflection(), width='42%'),
    Q('Here are the results.',
      Table(['Angle of incoming ray (°)', '20', '30', '40', '50', '60'], [['Angle of reflected ray (°)', '20', '31', '40', '56', '60']], center=True),
      Graph(['20°', '30°', '40°', '50°', '60°'], [20, 31, 40, 56, 60], 'Angle of reflected ray (°)', 'Angle of incoming ray', ymax=70, step=10, kind='line',
            width=140, height=56),
      Part('Plot the results as a line graph.'),
      Part('Which result does **not** fit the pattern?', Lines(1, 'At 50° the reflected ray was measured as 56°.')),
      Part('Suggest a reason for this result and what the class should do.', Lines(2, 'They may have misread the protractor or drawn the normal wrongly; they should repeat the measurement.')), marks=5),
    Q('Write a conclusion.', Lines(2, 'The angle of the reflected ray is equal to the angle of the incoming ray.'), marks=2),
    Q('Predict the angle of reflection for an incoming ray at 75°.', Lines(1, '75°'), marks=1),
    Q('Why did they use a **thin** beam of light rather than a wide torch beam?',
      Lines(2, 'A thin beam is a single clear ray, so the angles can be measured accurately.'), marks=1),
])

case = Sheet('case', 'Healthy eyes in a screen world', level=3, goals=['Use data from a survey.', 'Link eye health to the structure of the eye.', 'Plan a health campaign.'], blocks=[
    Links('Science', 'Health', 'Maths', 'Technology', 'Wellbeing'),
    Case('More and more children around the world are becoming **short-sighted** (myopic): they see near things clearly, but '
         'far things look blurred, because the image forms in front of the retina instead of on it. Scientists estimate that by '
         '2050 about **half of the world\'s people** could be short-sighted.',
         'Research suggests that spending time **outdoors in daylight** helps to protect children\'s eyes. In Taiwan, schools '
         'encouraged children to spend 120 minutes outdoors every day, and the number of short-sighted children began to fall. '
         'Eye doctors also recommend the **20-20-20 rule**: every 20 minutes of close work or screen use, look at something about '
         '6 metres (20 feet) away for 20 seconds.',
         'Food matters too. Without enough **vitamin A**, people can develop **night blindness**. Bangladesh runs a national '
         'Vitamin A campaign that gives capsules to young children, and vitamin A comes from foods such as spinach, carrots, '
         'mangoes, eggs and small fish like *mola*.',
         source='Based on research reported in the journal Ophthalmology (2016) and Taiwan school studies; Bangladesh National Vitamin A Plus Campaign.'),
    Q('Class 5C did a survey of 30 learners: "How many hours do you spend on screens each day, outside school?" (example data)',
      Table(['Hours per day', 'less than 1', '1 to 2', '2 to 3', 'more than 3'], [['Number of learners', '4', '9', '10', '7']], center=True),
      Graph(['less than 1', '1 to 2', '2 to 3', 'more than 3'], [4, 9, 10, 7], 'Number of learners', 'Hours on screens each day', ymax=12, step=1, width=130, height=56),
      Part('Draw the bar chart.'),
      Part('How many learners spend 2 hours or more on screens each day?', Lines(1, '17 learners (10 + 7)')), marks=3),
    Q('Use your knowledge of the eye to explain why a short-sighted person sees far objects as blurred.',
      Lines(2, 'The lens focuses the light in front of the retina instead of on it, so the image on the retina is not sharp.'), marks=2),
    Q('What might each person say about screens?',
      Table(['Person', 'View'], [['a learner', Ans('Screens help me learn and talk to my cousins, but my eyes get tired.')],
                                 ['a parent', Ans('I worry about too much screen time and too little outdoor play.')],
                                 ['an eye doctor', Ans('Take breaks, follow 20-20-20, play outside every day and get eyes checked.')]], widths=['26%', '74%']), marks=3),
    Q('Design a "Healthy Eyes Week" for your school. Give **three** actions and the reason for each.',
      Lines(4, 'e.g. outdoor play every break (daylight protects eyes); 20-20-20 reminders in computer lessons (rests the eye muscles); vitamin A food stall (prevents night blindness); free eye tests (find problems early).'), marks=3),
])

review = Sheet('review', 'Show what you know', level=3, goals=['Use key vocabulary.', 'Answer test-style questions.'], blocks=[
    Q('Find the key words.', WordSearch(['LIGHT', 'MIRROR', 'REFLECT', 'LENS', 'PUPIL', 'RETINA', 'SOURCE', 'IMAGE', 'NERVE'], size=11, seed=171)),
    Q('Write the letter of each optical device.', Fig(art.optical_devices(names=False), width='80%'),
      Table(['Device', 'Letter'], [['camera', Ans('D')], ['kaleidoscope', Ans('E')], ['hand lens', Ans('A')], ['pinhole camera', Ans('C')], ['telescope', Ans('B')]], center=True), marks=5),
    Q('Which part of the eye has light-sensitive cells?', MCQ(['eyelid', 'pupil', 'retina', 'lens'], 2), marks=1),
    Q('A straw in a glass of water looks bent. This is because of …', MCQ(['reflection', 'refraction', 'absorption', 'lateral inversion'], 1), marks=1),
    Q('**Challenge.** Explain how you can see this page. Use the words *source*, *reflect*, *pupil*, *retina*, *nerve* and *brain*.',
      Lines(4, 'Light from a source (the Sun or a lamp) reflects off the page and enters my eye through the pupil. The lens focuses it on the retina, which sends messages along the optic nerve to my brain.'), marks=3),
])

TOPIC = Topic(
    code='C7', strand='physical', title='Light: Sources, Reflection and Refraction', short='Light and seeing',
    subtitle='How we see, mirrors and reflection, refraction, optical devices and the human eye',
    outcomes=[
        'know that we see light sources because light from the source enters our eyes.',
        'identify a range of light sources and distinguish between objects that emit their own light and those that require an external source of light.',
        'explore why a beam of light changes direction when it is reflected from a surface.',
        'know that beams of light can be reflected by surfaces including mirrors, and that when reflected light enters our eyes we see the object.',
        'investigate the reflection of light using plane mirrors, tracing the path of light into and out of a mirror and describing the lateral inversion of the image.',
        'investigate the refraction of light using a glass of water, tracing the path of light into and out of the water and describing the refracted image.',
        'explain why light from a source is absorbed, reflected or refracted by different materials, and use this to account for what is seen.',
        'identify optical devices and describe how they affect light and the images they create — hand lens, telescope, pinhole camera, camera, kaleidoscope.',
        'explain the structure of the human eye and how an object is seen, using the terms eyelid, pupil, lens, retina, nerve and brain.',
    ],
    cambridge=['Unit 4 The way we see things (4.1–4.5)'],
    sheets=[learn, facts, think, investigate, case, review],
    selfcheck=['explain how we see light sources and other objects', 'use the law of reflection', 'explain lateral inversion and how a periscope works',
               'explain refraction with an example', 'describe what five optical devices do', 'explain how the eye works and how to keep eyes healthy'],
    cover_art=art.seeing_object(),
)
