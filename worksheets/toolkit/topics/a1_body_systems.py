from build import Sheet, Topic
from ws import (P, H, Box, Vocab, Fig, Cols, Row, Case, Links, Lines, Blanks, Match, TrueFalse, MCQ, Order, Table,
                Ans, Sort, Label, Draw, Graph, WordSearch, Q, Part, Bullets)
import art

learn = Sheet('learn', 'Inside your body: organs and organ systems', level=1, goals=[
    'Name the major organs, find them in the body and say what they do.',
    'Describe the six main organ systems.',
    'Explain how organ systems work together to keep us alive.',
], blocks=[
    P('Your body is busy every second, even while you sleep. Your heart beats about 100 000 times a day, your lungs '
      'breathe in and out about 20 000 times, and your brain controls it all. These jobs are done by **organs**. An organ '
      'is a body part with a special job, such as the heart or the stomach. Organs that work together form an '
      '**organ system**.', 'lead'),
    Fig(art.organ_diagram(labels=art.ORGANS), 'Major organs of the human body (the kidneys are at the back).', width='88%'),
    Cols(
        H('1. Digestive system: food into fuel', 3),
        P('Food is broken down into tiny pieces (**nutrients**) that the body can use. Teeth chew food in the **mouth**. '
          'The food pipe (**oesophagus**) carries it to the **stomach**, where acids churn it into a soup. In the **small '
          'intestine** the nutrients pass into the blood. The **large intestine** takes back water, and waste leaves the '
          'body. The **liver** helps digestion and cleans the blood.'),
        H('2. Respiratory system: breathing', 3),
        P('Air enters through the nose and mouth and travels down the **windpipe** (trachea) into the two **lungs**. In the '
          'lungs, **oxygen** passes into the blood and **carbon dioxide** (a waste gas) passes out to be breathed out. '
          'A sheet of muscle under the lungs, the **diaphragm**, helps you breathe.'),
        H('3. Circulatory system: transport', 3),
        P('The **heart** is a muscle that pumps **blood** through tubes called **blood vessels**: arteries, veins and tiny '
          'capillaries. Blood carries oxygen and nutrients to every cell and takes waste away. Your **pulse** is the beat of '
          'blood being pushed through an artery.'),
        Fig(art.heart_lungs_loop(), 'The heart pumps blood to the lungs and then around the body.'),
        H('4. Excretory system: removing waste', 3),
        P('Cells make waste. The two **kidneys** filter the blood and make **urine**, which is stored in the **bladder**. '
          'The lungs remove carbon dioxide and the skin removes some waste in sweat.'),
        H('5. Skeletal system: support and protection', 3),
        P('An adult skeleton has 206 **bones**. Bones hold the body up, **protect** soft organs (the skull protects the '
          'brain; the ribs protect the heart and lungs) and work with **muscles** so we can move. Bones meet at **joints**.'),
        H('6. Nervous system: control', 3),
        P('The **brain**, the **spinal cord** and the **nerves** carry messages around the body at high speed. Sense organs '
          '(eyes, ears, nose, tongue, skin) send information to the brain; the brain decides what to do and sends messages '
          'to the muscles.'),
        Box('think', P('**Systems work together.** When you run, your brain sends messages to your muscles, your lungs '
                       'breathe faster to take in more oxygen, and your heart beats faster to carry it to your muscles.')),
        Box('fact', P('Laid out flat, the inside of your small intestine would cover about 30 square metres, roughly half a '
                      'badminton court, because it is lined with millions of tiny finger-like folds that soak up food.')),
    ),
    Vocab([('organ', 'a body part with a special job'), ('organ system', 'organs working together'),
           ('nutrients', 'useful substances from food'), ('oxygen', 'gas from the air that cells need'),
           ('carbon dioxide', 'waste gas we breathe out'), ('blood vessel', 'tube that carries blood'),
           ('pulse', 'the beat of blood in an artery'), ('excretion', 'getting rid of waste made by the body'),
           ('joint', 'where two bones meet')]),
])

facts = Sheet('facts', 'Organs and their jobs', level=1, goals=['Label the major organs.', 'Match organs to systems and jobs.'], blocks=[
    Q('Label the organs.', Label(art.organ_diagram(), art.ORGANS, width='92%', cols=3), marks=9),
    Q('Write the organ system each organ belongs to.',
      Table(['Organ', 'Organ system'], [['heart', Ans('circulatory')], ['lungs', Ans('respiratory')],
                                        ['stomach', Ans('digestive')], ['kidneys', Ans('excretory')],
                                        ['brain', Ans('nervous')], ['skull', Ans('skeletal')]], widths=['40%', '60%']), marks=6),
    Q('Match each organ to its job.',
      Match([('heart', 'pumps blood around the body'), ('lungs', 'take in oxygen and remove carbon dioxide'),
             ('small intestine', 'nutrients pass into the blood'), ('kidneys', 'filter blood and make urine'),
             ('brain', 'controls the body and processes messages'), ('ribs', 'protect the heart and lungs')]), marks=6),
    Q('Fill in the gaps.',
      Blanks('Blood is carried in tubes called [blood vessels]. The beat you can feel in your wrist is your [pulse]. '
             'Urine is stored in the [bladder]. The [diaphragm] is a muscle that helps us breathe.',
             extra=['stomach', 'nerve']), marks=4),
])

think = Sheet('think', 'How the systems work together', level=2, goals=[
    'Order the journey of food through the body.', 'Explain links between organ systems.', 'Interpret pulse data.'], blocks=[
    Q('Number the stages of digestion from 1 to 6.',
      Order(['Teeth chew food in the mouth.', 'Food travels down the oesophagus.', 'The stomach churns food with acid.',
             'Nutrients pass into the blood in the small intestine.', 'Water is taken back in the large intestine.',
             'Waste leaves the body.']), marks=3),
    Q('Which bones protect which organs? Complete the table.',
      Fig(art.skeleton(labels=art.SKELETON_PARTS), width='55%'),
      Table(['Bone', 'Organ it protects'], [['skull', Ans('brain')], ['ribs', Ans('heart and lungs')],
                                            ['spine (backbone)', Ans('spinal cord')]], widths=['40%', '60%']), marks=3),
    Q('Explain why the circulatory system and the respiratory system must work together.',
      Lines(3, 'The lungs take oxygen into the blood; the heart pumps that blood to all the cells. Blood brings carbon dioxide back to the lungs to be breathed out.'), marks=2),
    Q('A boy touches a hot pan and quickly pulls his hand away. Describe the path of the message.',
      Lines(3, 'Nerves in the skin of his hand send a message to the spinal cord/brain; a message is sent back along nerves to the arm muscles, which move the hand away.'), marks=2),
    Q('Why do you breathe faster and your heart beat faster when you exercise?',
      Lines(3, 'Working muscles need more oxygen and energy; faster breathing takes in more oxygen and a faster heartbeat carries it to the muscles more quickly (and removes more carbon dioxide).'), marks=2),
])

investigate = Sheet('investigate', 'How does exercise change my pulse?', level=2, goals=[
    'Measure pulse rate accurately.', 'Present results in a bar chart.', 'Explain a pattern using body systems.'], blocks=[
    Box('need', P('a stopwatch or clock with a second hand, space to exercise safely')),
    Box('tip', P('Find your pulse on the inside of your wrist, below your thumb, using two fingers (not your thumb). '
                 'Count the beats for **15 seconds**, then multiply by 4 to get **beats per minute**.')),
    Q('Practise the maths. Work out each pulse rate in beats per minute.',
      Table(['Beats counted in 15 s', '× 4', 'Beats per minute'], [['20', '× 4', Ans('80')], ['23', '× 4', Ans('92')],
                                                                    ['31', '× 4', Ans('124')]], center=True), marks=3),
    Q('Arif measured his pulse after different activities. He measured each one three times.',
      Table(['Activity (1 minute)', 'Test 1', 'Test 2', 'Test 3', 'Average'], [
          ['sitting still', '80', '76', '78', Ans('78')], ['walking', '96', '100', '98', Ans('98')],
          ['jogging', '120', '124', '122', Ans('122')], ['skipping fast', '148', '152', '150', Ans('150')]], center=True),
      Part('Calculate the averages and write them in the table.'),
      Part('Why did Arif repeat each measurement three times?', Lines(2, 'To make the results more reliable and to check for mistakes.'))),
    Q('Draw a bar chart of the average pulse rates.',
      Graph(['sitting', 'walking', 'jogging', 'skipping'], [78, 98, 122, 150], 'Pulse (beats per minute)', 'Activity',
            ymax=160, step=20, width=150, height=68), marks=4),
    Q('Describe the pattern and explain it.',
      Lines(3, 'The harder the exercise, the faster the pulse. Muscles need more oxygen and energy, so the heart pumps faster to deliver more blood.'), marks=2),
    Q('What could Arif investigate next? Write a question he could test.',
      Lines(2, 'e.g. How long does it take for my pulse to return to normal after exercise? Do fitter people recover faster?'), marks=1),
])

case = Sheet('case', 'Dhaka\'s air and our lungs', level=3, goals=[
    'Use data to judge air quality.', 'Explain how air pollution affects body systems.',
    'Consider different points of view and suggest actions.'], blocks=[
    Links('Science', 'Health', 'Maths', 'Geography', 'Citizenship'),
    Case('Dhaka is one of the busiest cities in the world, and in winter it is often listed among the cities with the '
         '**most polluted air**. Smoke from brick kilns, exhaust from vehicles, dust from building sites and burning rubbish '
         'add tiny particles to the air. The smallest, called **PM2.5**, are about 30 times thinner than a human hair. '
         'They travel deep into the lungs and some even pass into the blood.',
         'Doctors say that breathing polluted air for a long time can cause coughing, asthma attacks and lung infections, '
         'and can strain the heart. Children breathe faster than adults, so they take in more polluted air for their size.',
         'Scientists use an **Air Quality Index (AQI)** to tell people how clean the air is.',
         source='AQI categories follow the widely used US EPA scale.'),
    Table(['AQI', '0–50', '51–100', '101–150', '151–200', '201–300', '301+'],
          [['Air quality', 'Good', 'Moderate', 'Unhealthy for sensitive groups', 'Unhealthy', 'Very unhealthy', 'Hazardous']], center=True),
    Q('A school in Dhaka recorded the AQI each morning for one week in January.',
      Table(['Day', 'Sun', 'Mon', 'Tue', 'Wed', 'Thu'], [['AQI', '168', '212', '245', '186', '140']], center=True),
      Part('On which day was the air the most polluted? What was its category?', Lines(1, 'Tuesday (245): very unhealthy.')),
      Part('On how many days was the air "unhealthy" or worse (151 or more)?', Lines(1, '4 days (Sun, Mon, Tue, Wed).')),
      Part('Suggest why the head teacher might cancel outdoor sports on Tuesday.', Lines(2, 'During exercise children breathe faster and deeper, taking more polluted air into their lungs.')),
      marks=4),
    Q('Which two organ systems are harmed most by air pollution? Explain.',
      Lines(3, 'Respiratory system: particles damage the lungs and airways. Circulatory system: tiny particles enter the blood and strain the heart.'), marks=2),
    Q('Complete the table to show different points of view.',
      Table(['Person', 'What they might say'], [
          ['brick kiln owner', Ans('My business gives people jobs; cleaner kilns cost money.')],
          ['a parent of a child with asthma', Ans('The smoke makes my child ill; we need cleaner air now.')],
          ['a city traffic officer', Ans('Old vehicles make a lot of smoke; we need better buses and checks.')]],
            widths=['35%', '65%']), marks=3),
    Q('Suggest **three** actions that could reduce air pollution or protect people\'s lungs.',
      Lines(3, 'e.g. cleaner (modern) brick kilns or alternative blocks; check vehicles for smoke; plant trees; cover building sites and spray water on dust; stop burning rubbish; wear a mask on very polluted days.'), marks=3),
])

review = Sheet('review', 'Show what you know', level=3, goals=['Use key vocabulary.', 'Answer test-style questions.'], blocks=[
    Q('Find the key words.', WordSearch(['HEART', 'LUNGS', 'BRAIN', 'KIDNEY', 'STOMACH', 'LIVER', 'NERVE', 'BONE', 'BLOOD', 'PULSE'], size=11, seed=21)),
    Q('Which organ system includes the windpipe and the lungs?', MCQ(['digestive', 'respiratory', 'nervous', 'skeletal'], 1), marks=1),
    Q('Which organ filters the blood to make urine?', MCQ(['liver', 'bladder', 'kidney', 'heart'], 2), marks=1),
    Q('Sort the organs into the correct systems.',
      Sort(['Digestive', 'Circulatory', 'Nervous'],
           [('stomach', 'Digestive'), ('small intestine', 'Digestive'), ('oesophagus', 'Digestive'), ('heart', 'Circulatory'),
            ('blood vessels', 'Circulatory'), ('brain', 'Nervous'), ('spinal cord', 'Nervous'), ('nerves', 'Nervous')]), marks=4),
    Q('**Challenge.** A person can live with one kidney but not without a heart. Explain why.',
      Lines(3, 'One kidney can filter enough blood on its own, but nothing else can pump blood; without the heart, oxygen and nutrients would not reach the cells.'), marks=2),
])

TOPIC = Topic(
    code='A1', strand='living', title='Human Body Systems', short='Body systems',
    subtitle='The major organs and the digestive, respiratory, circulatory, excretory, skeletal and nervous systems',
    outcomes=[
        'use scientific names for some major organs of body systems.',
        'identify the position of major organs in the body.',
        'describe the main functions of the major organs of the body.',
        'explain how the functions of the major organs are essential.',
        'describe the basic function of the different organ systems in the human body: digestive, excretory, circulatory, skeletal, nervous and respiratory.',
    ],
    sheets=[learn, facts, think, investigate, case, review],
    selfcheck=['name and find the major organs of the body', 'say what each major organ does',
               'describe the six main organ systems', 'explain how systems work together when I exercise',
               'measure my pulse and calculate beats per minute', 'explain how air pollution harms the lungs and heart'],
    cover_art=art.organ_diagram(labels=art.ORGANS, w='78%'),
)
