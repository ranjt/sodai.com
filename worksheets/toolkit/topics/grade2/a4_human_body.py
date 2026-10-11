from build import Sheet, Topic
from ws import (P, H, Box, Vocab, Fig, Cols, Row, Case, Links, Lines, Blanks, Match, TrueFalse, MCQ, Order, Table,
                Ans, Sort, Label, Draw, Graph, WordSearch, Q, Part, Bullets, Pics)
import art
import art23

learn = Sheet('learn', 'My amazing body', level=1, goals=[
    'Name the outside parts of the body and what they do.',
    'Name the main organs inside the body and find them on a body outline.',
    'Explain how bones and muscles work together to hold us up and help us move.',
], blocks=[
    P('Your body is like a wonderful machine. Every part has a job, and all the parts work together so you can run, play, eat, think and grow.', 'lead'),
    H('Outside parts', 3),
    Fig(art23.body_outline(labels=art23.BODY_PARTS), 'The outside parts of the body.', width='58%'),
    P('Your **head** holds your eyes, ears, nose and mouth. Your **arms** and **hands** help you hold and carry things. Your **legs** '
      'and **feet** help you stand, walk and run. **Joints** such as your **elbows** and **knees** let you bend.'),
    H('Inside parts: organs', 3),
    Fig(art.organ_diagram(labels=art.ORGANS), 'The main organs.', width='70%'),
    Table(['Organ', 'Its job'], [
        ['**brain**', 'controls your body; helps you think and remember'], ['**heart**', 'pumps blood all around your body'],
        ['**lungs**', 'take in air when you breathe'], ['**stomach**', 'mashes up your food'],
        ['**intestines** (small and large)', 'take goodness from food into your blood; carry away waste'],
        ['**liver**', 'cleans your blood'], ['**kidneys**', 'clean your blood and make urine (wee)'], ['**bladder**', 'stores urine']]),
    H('Bones and muscles', 3),
    P('Inside your body is a **skeleton** made of more than 200 **bones**. It holds you up, gives you your shape and protects soft parts: '
      'the **skull** protects your brain and the **ribs** protect your heart and lungs. **Muscles** are joined to bones. When a muscle pulls, '
      'the bone moves. Bones and muscles work together so you can move.'),
    Fig(art.skeleton(labels=art.SKELETON_PARTS), 'Your skeleton.', width='54%'),
    Box('fact', P('Your heart beats about 100 times every minute, all day and all night, even when you are asleep!')),
    Box('try', P('Put your hand on your arm and bend your elbow. Can you feel the muscle get fat and hard? It is pulling the bone.')),
    Vocab([('organ', 'a body part with a special job, like the heart'), ('skeleton', 'all the bones in your body'),
           ('muscle', 'pulls on bones to make them move'), ('joint', 'where two bones meet and bend')]),
])

facts = Sheet('facts', 'Body parts', level=1, goals=['Label body parts.', 'Match organs to jobs.'], blocks=[
    Q('Label the body.', Label(art23.body_outline(), art23.BODY_PARTS, width='54%', cols=4), marks=11),
    Q('Draw a line to match the organ to its job.', Match([('heart', 'pumps blood'), ('lungs', 'breathe in air'), ('brain', 'thinks and controls the body'),
                                                         ('stomach', 'mashes food'), ('bladder', 'stores urine')]), marks=5),
])

think = Sheet('think', 'How does my body work?', level=2, goals=['Explain how body parts work together.'], blocks=[
    Q('Label the organs.', Label(art.organ_diagram(), art.ORGANS, width='62%', cols=3), marks=9),
    Q('Which bone protects your brain?', MCQ(['ribs', 'skull', 'backbone'], 1), marks=1),
    Q('How do your bones and muscles help you kick a ball?', Lines(2, 'Muscles in my leg pull on the leg bones, so my leg moves and kicks.'), marks=2),
    Q('Why do you breathe faster when you run?', Lines(2, 'My body needs more air, so my lungs work harder (and my heart beats faster).'), marks=1),
])

investigate = Sheet('investigate', 'Does exercise change my heartbeat?', level=2, goals=['Count and compare.', 'Find a pattern.'], blocks=[
    P('Put two fingers on your wrist or neck. Can you feel your heart beating? Count the beats for 15 seconds, then multiply by 4. Do this when you sit, after you walk, and after you jump for one minute.'),
    Q('Here are Rafi\'s results. Draw a bar chart.', Table(['Activity', 'sitting', 'walking', 'jumping'], [['Beats in 1 minute', '84', '100', '132']], center=True),
      Graph(['sitting', 'walking', 'jumping'], [84, 100, 132], 'Heartbeats in 1 minute', 'Activity', ymax=140, step=20, width=100, height=50), marks=3),
    Q('What happens to your heartbeat when you exercise?', Lines(1, 'It gets faster.'), marks=1),
    Q('Why?', Lines(2, 'My muscles are working hard and need more blood, so my heart pumps faster.'), marks=2),
])

case = Sheet('case', 'A visit to the doctor', level=3, goals=['Link body parts to a real visit.', 'Learn how doctors check our bodies.'], blocks=[
    Links('Science', 'Health'),
    Case('Nadia goes to the clinic for a check-up. The doctor uses a **stethoscope** to listen to her **heart** and **lungs**. She '
         'measures Nadia\'s **height** and **weight**, and looks in her **ears** and **mouth**.',
         'The doctor says, "Your heart is strong and your lungs are clear. You have grown 5 centimetres this year! Keep eating '
         'healthy food and playing outside."',
         source='A story about a health check-up.'),
    Q('What did the doctor listen to with the stethoscope?', Lines(1, 'Nadia\'s heart and lungs'), marks=2),
    Q('Nadia was 115 cm tall last year. How tall is she now?', Lines(1, '115 + 5 = 120 cm'), marks=1),
    Q('Draw the doctor checking Nadia.', Draw('44mm', 'At the clinic', 'Doctor with a stethoscope listening to the heart.'), marks=2),
])

review = Sheet('review', 'Show what you know', level=3, goals=['Use body words.'], blocks=[
    Q('Find the words.', WordSearch(['HEART', 'LUNGS', 'BRAIN', 'BONE', 'MUSCLE', 'SKULL'], size=8, seed=205)),
    Q('Which organ pumps blood?', MCQ(['heart', 'stomach', 'lungs'], 0), marks=1),
    Q('What pulls on bones to make them move?', MCQ(['skin', 'muscles', 'hair'], 1), marks=1),
    Q('**Challenge.** Why do you think your ribs are like a cage?', Lines(2, 'They make a strong cage that protects the heart and lungs inside.'), marks=2),
])

TOPIC = Topic(
    code='A4', strand='living', title='The Human Body: Parts and Organs', short='Human body',
    subtitle='Outside body parts, organs inside, and how bones and muscles help us move',
    outcomes=[
        'identify the major external parts of the human body, describe the function of each, and explain how they relate to each other.',
        'name the major organs of the human body — brain, heart, lungs, stomach, liver, urinary bladder, small and large intestines, kidneys — and identify them on an outline of the human body.',
        'tell that humans have an internal skeleton and muscles, and demonstrate how the skeleton and muscles work together to support the body and help it move.',
    ],
    sheets=[learn, facts, think, investigate, case, review],
    selfcheck=['name the outside parts of my body', 'name the main organs', 'say what each organ does', 'explain how bones and muscles help me move', 'count my heartbeat'],
    cover_art=art23.body_outline(labels=art23.BODY_PARTS),
)
