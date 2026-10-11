from build import Sheet, Topic
from ws import (P, H, Box, Vocab, Fig, Cols, Row, Case, Links, Lines, Blanks, Match, TrueFalse, MCQ, Order, Table,
                Ans, Sort, Label, Draw, Graph, WordSearch, Q, Part, Bullets, Pics)
import art
import art4

learn = Sheet('learn', 'Magnets and electromagnets', level=1, goals=[
    'Observe how magnets behave and which materials they attract.',
    'Describe magnetic poles and how magnets attract and repel.',
    'Explain how electromagnets work and how magnets are used every day.',
], blocks=[
    P('More than two thousand years ago, people found strange stones that could pull bits of iron towards them. They called '
      'them **lodestones**. Hung on a thread, a lodestone always turned to point north. These were the first **magnets**, and '
      'the first **compasses** helped sailors cross the oceans.', 'lead'),
    Cols(
        H('What do magnets attract?', 3),
        P('Magnets **attract** (pull) things made of **iron**, **steel** (which contains iron), **nickel** and **cobalt**. These are '
          '**magnetic materials**. Most other metals are **not** magnetic: aluminium, copper, brass, gold and silver. Non-metals '
          'such as wood, plastic, glass and paper are not magnetic either.'),
        Box('tip', P('**Not all metals are magnetic!** A magnet picks up a steel paper clip, but not an aluminium can or a copper wire.')),
        H('Poles', 3),
        P('Every magnet has two ends called **poles**: a **north (N) pole** and a **south (S) pole**. The magnetic force is '
          'strongest at the poles.'),
        Fig(art4.bar_magnets(), 'Like poles repel; unlike poles attract.', width='76%'),
        Bullets(['**Unlike** poles (N and S) **attract** each other.', '**Like** poles (N and N, or S and S) **repel** (push each other away).']),
        H('Magnetic force works at a distance', 3),
        P('Magnetism is a **non-contact force**. A magnet can pull a paper clip without touching it, and the force passes through '
          'paper, plastic, water and even your hand. The space around a magnet where it has an effect is its **magnetic field**.'),
        H('Strong and weak magnets', 3),
        P('Some magnets are stronger than others. A stronger magnet can hold more paper clips, or pull a paper clip through more '
          'sheets of paper. Size does not always tell you the strength: some tiny magnets are very strong.'),
        H('Earth is a giant magnet', 3),
        P('The Earth behaves like a huge magnet. A **compass** needle is a small magnet that swings round to point **north**. '
          'Fishers on the Bay of Bengal, pilots and hikers use compasses to find their way.'),
        H('Electromagnets', 3),
        P('Wrap a long wire many times around an **iron nail** and connect it to a battery. Electricity flowing through the coil '
          'turns the nail into a magnet: an **electromagnet**. Switch off the electricity and the magnetism disappears. More coils '
          'or more cells make a stronger electromagnet.'),
        Fig(art4.electromagnet(), 'A simple electromagnet.', width='86%'),
        H('Magnets in everyday life', 3),
        Pics([('compass', 'compass'), ('loudspeaker', 'speakers'), ('fan', 'electric motors'), ('bell', 'electric bells'),
              ('recycling', 'sorting cans'), ('mobile phone', 'phones'), ('hospital', 'MRI scanners'), ('key', 'door catches')], cols=4, size='12mm', small=True),
        P('Fridge doors use magnetic strips to stay closed. Recycling plants use magnets to pull steel cans out of rubbish. Huge '
          'electromagnets on cranes lift scrap iron and drop it when the current is switched off.'),
        Box('safety', P('Keep strong magnets away from phones, bank cards and computers, and never let small children swallow magnets.')),
    ),
    Vocab([('magnet', 'an object that attracts iron and steel'), ('magnetic material', 'a material attracted to a magnet: iron, steel, nickel, cobalt'),
           ('pole', 'one end of a magnet, north or south'), ('attract', 'pull towards'), ('repel', 'push away'),
           ('magnetic field', 'the space around a magnet where it has an effect'), ('compass', 'a magnetic needle that points north'),
           ('electromagnet', 'a magnet made by electricity flowing in a coil')]),
])

facts = Sheet('facts', 'Attract or not?', level=1, goals=['Predict which materials are magnetic.', 'Use pole rules.'], blocks=[
    Q('Sort the objects.', Sort(['Attracted to a magnet', 'Not attracted'], [('steel paper clip', 'Attracted to a magnet'), ('iron nail', 'Attracted to a magnet'), ('steel spoon', 'Attracted to a magnet'),
                                                                          ('aluminium can', 'Not attracted'), ('copper wire', 'Not attracted'), ('gold ring', 'Not attracted'), ('plastic ruler', 'Not attracted'), ('wooden pencil', 'Not attracted')]), marks=8),
    Q('Attract or repel?', Table(['Poles facing each other', 'Attract or repel?'], [['N and S', Ans('attract')], ['N and N', Ans('repel')], ['S and S', Ans('repel')], ['S and N', Ans('attract')]], center=True), marks=4),
    Q('True or false?', TrueFalse([('All metals are magnetic.', False, 'Only some metals, such as iron, steel and nickel, are magnetic.'),
                                   ('A magnet can attract a paper clip through paper.', True), ('An electromagnet stops working when the electricity is switched off.', True),
                                   ('A compass needle points north.', True)]), marks=4),
    Q('Fill in the gaps.', Blanks('The ends of a magnet are called [poles]. Like poles [repel]. A [compass] helps us find north. An electromagnet is made with a coil of [wire] around an iron nail.',
                                  extra=['attract', 'plastic']), marks=4),
])

think = Sheet('think', 'Magnet puzzles', level=2, goals=['Explain magnet behaviour.', 'Use electromagnets to solve problems.'], blocks=[
    Q('Rafi has a bag of mixed aluminium and steel cans for recycling. How could he separate them quickly? Explain.', Lines(2, 'Use a magnet: it attracts the steel cans but not the aluminium ones.'), marks=2),
    Q('A magnet has lost its N and S labels. How could you find which end is north, using a labelled magnet?', Lines(3, 'Bring the N pole of the labelled magnet near one end. If it repels, that end is N; if it attracts, that end is S.'), marks=2),
    Q('Why does a scrap-yard crane use an electromagnet and not an ordinary magnet?', Lines(2, 'It can be switched off to drop the scrap where it is needed; an ordinary magnet would not let go.'), marks=2),
    Q('Suggest two ways to make an electromagnet stronger.', Lines(2, 'Wrap more coils of wire; use more cells (more electricity); use a thicker iron core.'), marks=2),
    Q('Draw a magnet picking up a chain of paper clips. Label the poles and show where the force is strongest.', Draw('34mm', 'Magnet and clips', 'Bar magnet with N and S at the ends; clips hanging from the poles, not the middle.'), marks=2),
])

investigate = Sheet('investigate', 'How strong are our magnets?', level=2, goals=['Plan a fair test.', 'Record and present results.', 'Draw conclusions.'], blocks=[
    P('Class 4B tested four magnets. They counted how many sheets of paper each magnet could hold a steel paper clip through.'),
    Q('Complete the plan.', Table(None, [['Change', Ans('the magnet')], ['Measure', Ans('number of sheets of paper the force passes through')],
                                         ['Keep the same', Ans('the same paper clip, same paper, same way of holding the magnet')]], widths=['26%', '74%']), marks=3),
    Q('Complete the table and draw a bar chart.',
      Table(['Magnet', 'Try 1', 'Try 2', 'Try 3', 'Mean'], [['bar magnet', '12', '14', '13', Ans('13')], ['horseshoe magnet', '18', '17', '19', Ans('18')],
                                                           ['fridge magnet', '3', '3', '3', Ans('3')], ['small round magnet', '20', '22', '21', Ans('21')]], center=True),
      Graph(['bar', 'horseshoe', 'fridge', 'round'], [13, 18, 3, 21], 'Sheets of paper (mean)', 'Magnet', ymax=24, step=2, width=110, height=50), marks=4),
    Q('Which magnet was strongest? Was it the biggest?', Lines(2, 'The small round magnet (21 sheets). No: it was small, so size does not tell you the strength.'), marks=2),
    Q('Why did they do three tries for each magnet?', Lines(1, 'To make the results more reliable and find a mean.'), marks=1),
])

case = Sheet('case', 'Giant magnets in the ship-breaking yards', level=3, goals=['See how magnets are used in industry.', 'Use numbers.', 'Think about workers\' safety and recycling.'], blocks=[
    Links('Science', 'Economics', 'Environment', 'Ethics'),
    Case('Along the beach at **Sitakunda**, near Chattogram, old ships from all over the world are taken apart in some of the '
         'biggest **ship-breaking yards** in the world. The steel from the ships is cut into pieces and **recycled**. Much of the '
         'steel used for building in Bangladesh comes from these old ships.',
         'In steel yards and scrap yards, cranes with huge **electromagnets** lift piles of iron and steel. When the operator '
         'switches the current on, the scrap jumps up to the magnet; switching it off drops the scrap onto a truck. Ship breaking '
         'gives many people jobs, but it can be **dangerous** for workers and can **pollute** the beach and sea with oil and '
         'chemicals, so there are rules to make it safer and cleaner.',
         source='Based on reports about the ship-recycling industry in Bangladesh.'),
    Q('Why is an electromagnet useful for lifting scrap steel?', Lines(2, 'It attracts the magnetic steel and can be switched off to drop it exactly where it is needed.'), marks=2),
    Q('Would the electromagnet pick up the copper cables and aluminium parts from a ship? Why?', Lines(2, 'No, because copper and aluminium are not magnetic.'), marks=2),
    Q('**Maths.** A crane magnet lifts 2 tonnes of steel each time. How many lifts are needed to load 30 tonnes?', Lines(1, '30 ÷ 2 = 15 lifts'), marks=1),
    Q('Recycling ship steel is good, but there are problems. Complete the table.',
      Table(['Good points', 'Problems'], [[Ans('saves iron ore and energy; cheap steel for buildings; jobs'), Ans('dangerous work; oil and chemicals pollute the beach and sea')]], widths=['50%', '50%']), marks=2),
    Q('Suggest two rules that would make ship breaking safer for workers.', Lines(2, 'e.g. helmets, gloves and boots for everyone; training; no children working; remove oil and gas safely before cutting.'), marks=2),
])

review = Sheet('review', 'Show what you know', level=3, goals=['Use key vocabulary.', 'Answer test-style questions.'], blocks=[
    Q('Find the key words.', WordSearch(['MAGNET', 'POLE', 'NORTH', 'SOUTH', 'ATTRACT', 'REPEL', 'IRON', 'STEEL', 'COMPASS'], size=10, seed=417)),
    Q('Which object would a magnet attract?', MCQ(['a copper coin', 'an aluminium can', 'an iron nail', 'a glass marble'], 2), marks=1),
    Q('Two north poles are pushed together. They will…', MCQ(['attract', 'repel', 'stick together', 'become weaker'], 1), marks=1),
    Q('Design a game that uses magnets (e.g. a fishing game). Draw it and explain how the magnets work.', Draw('40mm', 'My magnet game', 'e.g. paper fish with steel paper clips; a rod with a magnet on a string attracts them.'), marks=3),
    Q('**Challenge.** Explain how you could make an electromagnet that is strong enough to lift 10 paper clips, and how you would test it fairly.',
      Lines(3, 'Wrap many coils of wire around an iron nail and use two cells. Test by counting how many clips it lifts with 10, 20 and 30 coils, keeping the same nail, clips and cells.'), marks=2),
])

TOPIC = Topic(
    code='C7', strand='physical', title='Magnets and Electromagnets', short='Magnets',
    subtitle='Magnetic materials, poles, attraction and repulsion, magnet strength, compasses, electromagnets and uses',
    outcomes=[
        'observe the behaviour of magnets on objects, and identify ways in which magnets are used in everyday life.',
        'conduct investigations with different electrical circuits that operate lights, a small motor or induced magnetism, to determine what happens when the components of the circuit are altered.',
    ],
    cambridge=['Unit 5 Electricity and magnetism (5.7–5.10)'],
    sheets=[learn, facts, think, investigate, case, review],
    selfcheck=['predict which materials are magnetic', 'explain attract and repel', 'test the strength of magnets',
               'explain how a compass works', 'make and explain an electromagnet', 'describe how magnets are used in industry'],
    cover_art=art4.bar_magnets(),
)
