from build import Sheet, Topic
from ws import (P, H, Box, Fig, Q, Lines, MCQ, Draw, Pics, Ans, Case, Choose, PicMatch, PicSort, Pictograph, Trace, Label)
import art

learn = Sheet('learn', 'Plants around us', level=1, goals=['Name the parts of a plant.', 'Say what plants need.'], blocks=[
    Box('adult', P('Read aloud. If you can, bring a real plant with roots to show the children each part.')),
    P('Plants are **living things**. They grow, drink water and make seeds.', 'lead'),
    Fig(art.plant_parts(labels=art.PLANT_PARTS), 'The parts of a plant.', width='52%'),
    H('Plants need…', 3),
    Pics([('sun', 'sunlight'), ('droplet', 'water'), ('wind face', 'air'), ('seedling', 'soil')], cols=4, size='22mm'),
    H('Plants help us', 3),
    Pics([('mango', 'fruit'), ('carrot', 'vegetables'), ('cooked rice', 'rice'), ('wood', 'wood'), ('deciduous tree', 'shade')], cols=5, size='19mm'),
])

facts = Sheet('facts', 'Parts of a plant', level=1, goals=['Label a plant.', 'Find what plants need.'], blocks=[
    Q('Say the parts with your teacher. Copy the words from the box.', Label(art.plant_parts(), art.PLANT_PARTS, width='44%', cols=3)),
    Q('Circle what a plant needs to grow.', Choose([('sun', 'sunlight'), ('candy', 'sweets'), ('droplet', 'water'), ('football', 'ball')], right=[0, 2])),
])

think = Sheet('think', 'From seed to plant', level=2, goals=['Order how a seed grows.', 'Draw a plant.'], blocks=[
    Q('Put the pictures in order. Write **1**, **2**, **3**.', Pics([('seedling', Ans('2')), ('sunflower', Ans('3')), ('chestnut', Ans('1'))], cols=3, size='26mm')),
    Q('Draw a plant. Draw its roots, stem, leaves and a flower.', Draw('50mm', 'My plant', 'Roots under the ground, a stem, green leaves and a flower.')),
])

investigate = Sheet('investigate', 'Light or dark?', level=2, goals=['Grow beans in light and in the dark.', 'Compare.'], blocks=[
    Box('adult', P('Plant beans in two cups. Put one cup by the window and one in a dark cupboard. Water both. Look after one week.')),
    Q('Guess: which bean plant will grow best? Circle it.', Choose([('sun', 'by the window'), ('night with stars', 'in the dark')], right=[0], cols=2)),
    Q('After one week, draw both plants.', Draw('52mm', 'By the window          |          In the dark', 'By the window: green and strong. In the dark: pale, thin and weak.')),
])

case = Sheet('case', 'The mango tree', level=3, goals=['Listen to a story.', 'Say how a tree helps us.'], blocks=[
    Case('Grandpa planted a mango seed when he was a boy. It grew and grew into a big mango tree.',
         'Now children play in its shade. Birds build nests in its branches. And every summer the family eats sweet mangoes!'),
    Q('How does the mango tree help? Circle.', Choose([('mango', 'fruit'), ('deciduous tree', 'shade'), ('car', 'car'), ('nest with eggs', 'home for birds')], right=[0, 1, 3])),
])

review = Sheet('review', 'I can do it!', level=3, goals=['Trace plant words.'], blocks=[
    Q('Trace the words.', Trace([('leaf', 'herb'), ('root', 'seedling')])),
    Q('Circle the part of the plant under the ground.', MCQ(['flower', 'roots', 'leaf'], 1)),
])

TOPIC = Topic(
    code='A3', strand='living', title='Plants Around Us', short='Plants',
    subtitle='Parts of a plant, what plants need, seeds that grow, and how plants help us',
    outcomes=[
        'name the major parts of a plant, looking at real plants and models.',
        'know that plants need light and water to grow.',
        'explore how seeds grow into flowering plants.',
        'describe how plants are a life-sustaining resource for us and other living beings.',
        'identify what local plant and animal species need in order to grow.',
    ],
    sheets=[learn, facts, think, investigate, case, review],
    selfcheck=['name the parts of a plant', 'say what plants need', 'tell how a seed grows'],
    cover_art=art.plant_parts(labels=art.PLANT_PARTS),
)
