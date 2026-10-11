from build import Sheet, Topic
from ws import (P, H, Box, Vocab, Fig, Cols, Row, Case, Links, Lines, Blanks, Match, TrueFalse, MCQ, Order, Table,
                Ans, Sort, Label, Draw, Graph, WordSearch, Q, Part, Bullets, Pics)
import art

learn = Sheet('learn', 'Materials and their properties', level=1, goals=[
    'Describe materials using property words: hard, soft, shiny, dull and more.',
    'Sort materials by their properties, including magnetic and non-magnetic.',
    'Explain why a material is chosen for a job.',
], blocks=[
    P('Look around your classroom. The door is made of **wood**, the window of **glass**, the fan of **metal** and **plastic**, your shirt of **cotton**. These are all **materials**: what things are made of.', 'lead'),
    Pics([('wood', 'wood'), ('key', 'metal'), ('plastic bottle', 'plastic'), ('glass bottle', 'glass'), ('shirt', 'fabric'), ('brick', 'clay brick'), ('rock', 'stone'), ('newspaper', 'paper')], cols=8, size='12mm'),
    H('Properties', 3),
    P('A **property** tells us what a material is like. Every material has its own properties.'),
    Table(['Property words', 'Opposite', 'Example'], [
        ['**hard**: does not dent', '**soft**: easy to squash', 'stone is hard; cotton wool is soft'],
        ['**shiny**: reflects light', '**dull**: not shiny', 'a steel spoon is shiny; wood is dull'],
        ['**flexible**: bends easily', '**stiff**: does not bend', 'rubber is flexible; a brick is stiff'],
        ['**transparent**: you can see through it', '**opaque**: you cannot see through it', 'glass is transparent; wood is opaque'],
        ['**waterproof**: keeps water out', '**absorbent**: soaks up water', 'plastic is waterproof; a towel is absorbent'],
        ['**strong**: hard to break', '**weak**: breaks easily', 'steel is strong; paper is weak']]),
    H('Magnetic or not?', 3),
    P('A magnet pulls (attracts) things made of **iron** or **steel**. These are **magnetic** materials. Most materials are **not** magnetic: wood, plastic, glass, paper, fabric and even some metals such as **aluminium**, **copper**, gold and silver.'),
    Box('try', P('Use a fridge magnet to test things at home: a spoon, a key, a coin, a foil tray. Which ones stick?')),
    H('Choosing the right material', 3),
    P('We choose a material because its properties are right for the job.'),
    Table(['Object', 'Material', 'Why?'], [
        ['window', 'glass', 'transparent, so light comes in'], ['umbrella', 'plastic or waxed cloth', 'waterproof'],
        ['cooking pot', 'metal (aluminium or steel)', 'strong and does not melt on the stove'], ['pot handle', 'wood or plastic', 'does not get too hot to hold'],
        ['towel', 'cotton', 'soft and absorbent'], ['shopping bag', 'jute', 'strong, and it rots away when thrown out']]),
    Box('bd', P('Bangladesh uses many natural materials: **jute** for bags and rope, **bamboo** for homes and bridges, **clay** for pots and bricks, and **cotton** for nakshi kantha quilts.')),
    Vocab([('material', 'what an object is made of'), ('property', 'what a material is like'), ('transparent', 'you can see through it'),
           ('opaque', 'you cannot see through it'), ('waterproof', 'does not let water through'), ('magnetic', 'pulled by a magnet')]),
])

facts = Sheet('facts', 'Sorting materials', level=1, goals=['Use property words.', 'Sort materials.'], blocks=[
    Q('Write the material each object is made of.', Pics([('key', Ans('metal')), ('window', Ans('glass')), ('chair', Ans('wood')), ('socks', Ans('fabric (cotton)'))], cols=4, size='16mm'), marks=4),
    Q('Sort these materials.', Sort(['Hard', 'Soft'], [('stone', 'Hard'), ('steel', 'Hard'), ('glass', 'Hard'), ('cotton wool', 'Soft'), ('sponge', 'Soft'), ('wool', 'Soft')]), marks=6),
    Q('Will a magnet attract it?', Table(['Object', 'Material', 'Magnetic?'], [['nail', 'iron', Ans('yes')], ['drink can', 'aluminium', Ans('no')], ['paper clip', 'steel', Ans('yes')],
                                                                         ['ruler', 'plastic', Ans('no')], ['coin', 'brass or steel', Ans('test it! some are, some are not')]], center=True), marks=5),
])

think = Sheet('think', 'The right material for the job', level=2, goals=['Explain choices of materials.'], blocks=[
    Q('Why is a window made of glass, not wood?', Lines(2, 'Glass is transparent so light can come in; wood is opaque.'), marks=2),
    Q('Why would a paper umbrella be a bad idea?', Lines(2, 'Paper is absorbent and weak; it would get soggy and tear in the rain.'), marks=2),
    Q('Odd one out. Circle it and say why.', Table(['', 'A', 'B', 'C', 'D'], [['group', 'iron nail', 'steel pin', 'aluminium can', 'paper clip']], center=True),
      Lines(1, 'C, aluminium can: it is the only one that is not magnetic.'), marks=2),
    Q('Design a raincoat for a school trip. Label the materials and say why you chose them.', Draw('42mm', 'My raincoat', 'e.g. plastic coat (waterproof), cotton lining (soft), shiny strips (easy to see).'), marks=3),
])

investigate = Sheet('investigate', 'Which material soaks up the most water?', level=2, goals=['Do a fair test.', 'Draw a bar chart and conclude.'], blocks=[
    P('Class 3A put a 10 cm square of each material into a dish with 50 ml of water. After one minute they lifted it out and measured how much water was left in the dish.'),
    Q('Complete the table: how much water did each material soak up?', Table(['Material', 'Water left (ml)', 'Water soaked up (ml)'],
      [['cotton towel', '20', Ans('30')], ['paper towel', '30', Ans('20')], ['newspaper', '40', Ans('10')], ['plastic', '50', Ans('0')]], center=True), marks=4),
    Q('Draw a bar chart of the water soaked up.', Graph(['towel', 'paper towel', 'newspaper', 'plastic'], [30, 20, 10, 0], 'Water soaked up (ml)', 'Material', ymax=35, step=5, width=100, height=48), marks=3),
    Q('How did they make it a fair test?', Lines(2, 'Same size of material, same amount of water, same time.'), marks=2),
    Q('Which material would you use to mop up a spill? Why?', Lines(1, 'the cotton towel: it is the most absorbent'), marks=1),
])

case = Sheet('case', 'Jute: the golden fibre', level=3, goals=['See how properties make a material useful.'], blocks=[
    Links('Science', 'Farming', 'Environment'),
    Case('**Jute** is a tall plant that grows well in the warm, wet fields of Bangladesh. Farmers soak the stems in water, then peel off long, shiny, golden threads called **fibres**. Because of its colour and value, jute is called the **golden fibre**.',
         'Jute fibres are **strong** and **flexible**, so they are made into rope, sacks, mats and bags. Unlike plastic, jute **rots away** in the soil when it is thrown out. Bangladeshi scientists have also made a thin, plastic-like bag from jute, so that fewer plastic bags end up in rivers and drains.',
         source='Based on information about jute farming and jute products in Bangladesh.'),
    Q('Write two properties of jute fibre.', Lines(1, 'strong, flexible (also shiny, golden)'), marks=2),
    Q('Why is a jute bag better for the environment than a plastic bag?', Lines(2, 'It rots away in the soil; plastic stays for hundreds of years and blocks drains.'), marks=2),
    Q('Name two things made from jute.', Lines(1, 'rope, sacks, bags, mats, carpets'), marks=2),
])

review = Sheet('review', 'Show what you know', level=3, goals=['Use material words.'], blocks=[
    Q('Find the words.', WordSearch(['HARD', 'SOFT', 'SHINY', 'METAL', 'GLASS', 'WOOD', 'JUTE'], size=9, seed=310)),
    Q('Which material is transparent?', MCQ(['wood', 'glass', 'brick'], 1), marks=1),
    Q('Which material is magnetic?', MCQ(['plastic', 'aluminium', 'iron'], 2), marks=1),
    Q('**Challenge.** A builder needs a material for a bridge. Which properties must it have?', Lines(2, 'strong, stiff, waterproof, does not rot or rust easily'), marks=2),
])

TOPIC = Topic(
    code='C1', strand='physical', title='Material Properties', short='Materials',
    subtitle='Property words, sorting materials, magnetic materials and choosing the right material for the job',
    outcomes=[
        'know that every material has specific properties, for example hard, soft and shiny.',
        'sort materials according to their properties.',
        'explore how some materials are magnetic but many are not.',
        'discuss why materials are chosen for specific purposes on the basis of their properties.',
    ],
    cambridge=['Stage 3 Unit 5 Materials (5.1–5.4)'],
    sheets=[learn, facts, think, investigate, case, review],
    selfcheck=['describe materials with property words', 'sort materials', 'test which materials are magnetic', 'explain why a material is chosen', 'run a fair test on materials'],
    cover_art=art.pic_row(['wood', 'key', 'glass bottle', 'shirt']),
)
