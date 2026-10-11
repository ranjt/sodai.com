from build import Sheet, Topic
from ws import (P, H, Box, Vocab, Fig, Cols, Row, Case, Links, Lines, Blanks, Match, TrueFalse, MCQ, Order, Table,
                Ans, Sort, Label, Draw, Graph, WordSearch, Q, Part, Bullets, Pics)
import art
import art23

learn = Sheet('learn', 'Skeletons, muscles and medicines', level=1, goals=[
    'Explain how skeletons support and protect the body and grow as we grow.',
    'Explain how muscles contract in pairs to move bones.',
    'Explain what medicines are and how to keep the body healthy and safe.',
], blocks=[
    P('Without a skeleton you would flop like a jellyfish! Humans and many animals, such as dogs, birds, fish and frogs, have a **skeleton of bones** inside their bodies.', 'lead'),
    Fig(art.skeleton(labels=art.SKELETON_PARTS), 'The human skeleton.', width='54%'),
    H('What the skeleton does', 3),
    Bullets(['**Supports** the body and gives it shape.', '**Protects** soft organs: the skull protects the brain; the ribs protect the heart and lungs; the backbone protects the spinal cord.',
             'Helps us **move**: muscles are attached to bones.']),
    P('A new baby has about 300 small bones. As you grow, some join together, so adults have **206** bones. Bones grow longer and stronger as you grow, so you get taller.'),
    H('Muscles move bones', 3),
    P('**Muscles** are joined to bones. A muscle can only **pull**. When it **contracts** (gets shorter and fatter) it pulls the bone. Muscles work in **pairs**: '
      'to bend your arm, the **biceps** contracts and the **triceps** relaxes. To straighten it, the triceps contracts and the biceps relaxes.'),
    Fig(art23.arm_muscles(labels=art23.ARM_PARTS), 'Muscles work in pairs.', width='60%'),
    H('Medicines', 3),
    P('**Drugs** are substances that change how the body works. **Medicines** are drugs that help us when we are ill: they can stop pain, fight infections or help the body heal. '
      'But medicines can be harmful if they are used wrongly.'),
    Box('safety', P('Only take medicine given by a parent, carer or doctor. Take the right amount at the right time. Never share medicines. Never take medicine that looks like sweets without asking an adult.')),
    H('Keeping healthy and safe', 3),
    Pics([('cooked rice', 'eat well'), ('milk', 'milk and small fish for strong bones'), ('person running', 'exercise'), ('bed', 'sleep'), ('soap', 'wash hands'), ('bicycle', 'wear a helmet')], cols=6, size='13mm'),
    Vocab([('skeleton', 'the frame of bones inside the body'), ('support', 'hold up'), ('protect', 'keep safe'), ('contract', 'get shorter and pull'),
           ('relax', 'get longer and stop pulling'), ('medicine', 'a drug that helps when we are ill')]),
])

facts = Sheet('facts', 'Bones and muscles', level=1, goals=['Label the skeleton.', 'Match bones to jobs.'], blocks=[
    Q('Label the skeleton.', Label(art.skeleton(), art.SKELETON_PARTS, width='54%', cols=3), marks=len(art.SKELETON_PARTS)),
    Q('Draw a line to match.', Match([('skull', 'protects the brain'), ('ribs', 'protect the heart and lungs'), ('backbone', 'holds the body up'), ('muscles', 'pull bones to move them')]), marks=4),
    Q('True or false?', TrueFalse([('Muscles can push and pull.', False, 'Muscles can only pull.'), ('Adults have 206 bones.', True), ('It is safe to share medicine with a friend.', False, 'Never share medicine.')]), marks=3),
])

think = Sheet('think', 'How do we move?', level=2, goals=['Explain muscle pairs.'], blocks=[
    Q('Label the arm muscles.', Label(art23.arm_muscles(), art23.ARM_PARTS, width='56%', cols=2), marks=4),
    Q('What happens to the biceps when you bend your arm?', Lines(2, 'It contracts (gets shorter and fatter) and pulls the lower arm up.'), marks=2),
    Q('Why do muscles have to work in pairs?', Lines(2, 'A muscle can only pull, so another muscle is needed to pull the bone back.'), marks=2),
    Q('Why are some medicines kept in cupboards high up?', Lines(1, 'So small children cannot reach them and take them by mistake.'), marks=1),
])

investigate = Sheet('investigate', 'Do longer arms throw further?', level=2, goals=['Look for a pattern.', 'Measure length.'], blocks=[
    P('Class 3B measured the arm length of five children and how far each could throw a bean bag (best of three throws).'),
    Q('Draw a bar chart.', Table(['Child', 'Ana', 'Bilu', 'Chandni', 'Dipu', 'Eva'], [['Arm length (cm)', '48', '52', '50', '55', '46'], ['Throw (m)', '8', '10', '7', '11', '9']], center=True),
      Graph(['Ana', 'Bilu', 'Chandni', 'Dipu', 'Eva'], [8, 10, 7, 11, 9], 'Throw (m)', 'Child', ymax=12, step=1, width=110, height=48), marks=3),
    Q('Did the child with the longest arms throw furthest?', Lines(1, 'Yes: Dipu (55 cm) threw 11 m.'), marks=1),
    Q('Is there a clear pattern? Explain.', Lines(2, 'Not always: Eva has the shortest arms but threw further than Chandni, so other things matter too (strength, practice).'), marks=2),
])

case = Sheet('case', 'Strong bones from small fish', level=3, goals=['Link food to strong bones.', 'Use numbers.'], blocks=[
    Links('Science', 'Health', 'Food', 'Maths'),
    Case('Bones need **calcium** to grow strong. Milk, yoghurt (*doi*) and green leafy vegetables have calcium. In Bangladesh, tiny fish such as **mola** and **dhela** '
         'are eaten whole, with their bones, so they give lots of calcium too.',
         'Scientists and nutrition workers in Bangladesh have encouraged farmers to grow mola fish in their ponds, so that children get more calcium and vitamins.',
         source='Based on nutrition research about small fish in Bangladesh.'),
    Q('Circle the foods that help build strong bones.', Pics([('milk', 'milk'), ('fish', 'small fish'), ('leafy green', 'green leaves'), ('lollipop', 'sweets')], cols=4, size='14mm'), Lines(1, 'milk, small fish, green leaves'), marks=3),
    Q('Why are small fish eaten whole so good for bones?', Lines(2, 'You eat the bones too, and fish bones contain calcium.'), marks=2),
    Q('A child needs 3 glasses of milk a day. How many in a week?', Lines(1, '3 × 7 = 21 glasses'), marks=1),
])

review = Sheet('review', 'Show what you know', level=3, goals=['Use body words.'], blocks=[
    Q('Find the words.', WordSearch(['BONE', 'SKULL', 'RIBS', 'MUSCLE', 'PULL', 'MEDICINE'], size=9, seed=302)),
    Q('Which bones protect the heart?', MCQ(['skull', 'ribs', 'leg bones'], 1), marks=1),
    Q('When a muscle contracts, it…', MCQ(['gets longer', 'gets shorter and pulls', 'pushes'], 1), marks=1),
    Q('**Challenge.** Animals like worms and jellyfish have no bones. How are their bodies different from ours?', Lines(2, 'They are soft and bendy; they cannot stand up tall; they need water or soil to hold them.'), marks=2),
])

TOPIC = Topic(
    code='A1', strand='living', title='Skeletons, Muscles and Medicines', short='Skeletons and medicines',
    subtitle='How skeletons support and protect us, how muscles work in pairs, and using medicines safely',
    outcomes=[
        'know that humans, and some animals, have bony skeletons inside their bodies.',
        'know how skeletons grow as humans grow, and how they support and protect the body.',
        'know that animals with skeletons have muscles attached to the bones.',
        'know how a muscle has to contract, or shorten, to make a bone move, and that muscles act in pairs.',
        'explain the role of drugs as medicines.',
        'describe simple ways of keeping the body healthy and safe.',
    ],
    cambridge=['Stage 3 Unit 2 Looking after ourselves (2.1–2.4)'],
    sheets=[learn, facts, think, investigate, case, review],
    selfcheck=['say what the skeleton does', 'name important bones', 'explain how muscles work in pairs', 'use medicines safely', 'name foods for strong bones'],
    cover_art=art.skeleton(labels=art.SKELETON_PARTS),
)
