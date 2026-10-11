from build import Sheet, Topic
from ws import (P, H, Box, Fig, Q, Lines, MCQ, Draw, Pics, Ans, Case, Choose, PicMatch, PicSort, Pictograph, Trace)
import art

learn = Sheet('learn', 'Our environment', level=1, goals=['Name natural and built places.', 'Say how we use and care for our environment.'], blocks=[
    Box('adult', P('Read aloud. Ask: "Where do you live: in a city, a town or a village? What can you see near your home?"')),
    P('Our **environment** is everything around us. Some places are **natural**. Some places are **built** by people.', 'lead'),
    H('Natural places', 3),
    Pics([('deciduous tree', 'forest'), ('water wave', 'river'), ('mountain', 'hill'), ('lotus', 'wetland'), ('tiger', 'mangrove forest')], cols=5, size='19mm'),
    H('Built places', 3),
    Pics([('city', 'city'), ('hut', 'village'), ('school', 'school'), ('hospital', 'hospital')], cols=4, size='19mm'),
    H('We use our environment', 3),
    Pics([('droplet', 'water'), ('wood', 'wood'), ('fish', 'fish'), ('rice plant', 'rice')], cols=4, size='19mm'),
    P('Let us take care of it! **Reduce, reuse, recycle**: use less, use things again, and make old things into new things.'),
])

facts = Sheet('facts', 'Natural or built?', level=1, goals=['Sort natural and built places.'], blocks=[
    Q('Cut and sort: **natural** or **built by people**?', PicSort(['Natural', 'Built by people'], [
        ('water wave', 'river', 'Natural'), ('mountain', 'hill', 'Natural'), ('deciduous tree', 'forest', 'Natural'),
        ('city', 'city', 'Built by people'), ('school', 'school', 'Built by people'), ('house', 'house', 'Built by people')], height='32mm')),
    Q('Circle the things we get from nature.', Choose([('droplet', 'water'), ('car', 'car'), ('wood', 'wood'), ('fish', 'fish')], right=[0, 2, 3])),
])

think = Sheet('think', 'Caring for our world', level=2, goals=['Choose kind actions.', 'Draw my favourite place.'], blocks=[
    Q('Circle the kind things to do. Cross out the unkind ones.', Choose([('wastebasket', 'bin your rubbish'), ('no littering', 'throw rubbish on the ground'),
                                                                        ('reusable bag', 'take a cloth bag'), ('seedling', 'plant a tree')], right=[0, 2, 3])),
    Q('Draw your favourite place outside.', Draw('50mm', 'My favourite place', 'Any natural or built place: a river, a park, the village, the school.')),
])

investigate = Sheet('investigate', 'Reuse it!', level=2, goals=['Make something new from old things.'], blocks=[
    Box('adult', P('Collect clean empty bottles, boxes and jars. Help the children turn them into something useful: a pencil pot, a plant pot or a toy.')),
    Q('Match the old thing to its new use.', PicMatch([(('glass bottle', 'jar'), ('pencil', 'pencil pot')), (('plastic bottle', 'bottle'), ('seedling', 'plant pot')),
                                                       (('package', 'box'), ('car', 'toy car'))], size='15mm')),
    Q('Draw what you made.', Draw('42mm', 'I made…', 'e.g. a pencil pot from a jar.')),
])

case = Sheet('case', 'The river clean-up', level=3, goals=['Listen to a story.', 'Talk about caring for nature.'], blocks=[
    Case('The children walked to the river near their school. They saw plastic bags and bottles in the water. "The fish cannot live here!" said Rina.',
         'With their teachers, they picked up the rubbish and put it in bags. Now the river is cleaner, and the children put up a sign: "Keep our river clean!"'),
    Q('What did the children pick up? Circle.', Choose([('plastic bottle', 'bottles'), ('fish', 'fish'), ('reusable bag', 'plastic bags')], right=[0, 2], cols=3)),
])

review = Sheet('review', 'I can do it!', level=3, goals=['Trace environment words.'], blocks=[
    Q('Trace the words.', Trace([('tree', 'deciduous tree'), ('river', 'water wave')])),
    Q('Circle the **natural** place.', Choose([('city', 'city'), ('mountain', 'hill'), ('school', 'school')], right=[1], cols=3)),
])

TOPIC = Topic(
    code='B2', strand='earth', title='Our Environment', short='Environment',
    subtitle='Natural and built places, what we use from nature, and reducing, reusing and recycling',
    outcomes=[
        'give examples of human-built and natural environments — cities, villages and towns; forest, mangrove, river, mountain and wetlands.',
        'identify the basic and common components of the human-built and natural environments they have identified.',
        'talk about the things in our environment that people use, and recognize different resources in our environment and how humans use them.',
        'identify that the choices we make can have an impact on the land, water, air and other living things.',
        'consider different ways to take care of our resources, and how we can reduce, reuse and recycle.',
    ],
    sheets=[learn, facts, think, investigate, case, review],
    selfcheck=['name natural and built places', 'say what we use from nature', 'reduce, reuse and recycle'],
    cover_art=art.pic_row(['deciduous tree', 'water wave', 'mountain', 'city', 'recycling'], ['forest', 'river', 'hill', 'city', 'recycle']),
)
