from build import Sheet, Topic
from ws import (P, H, Box, Fig, Q, Lines, MCQ, Draw, Pics, Ans, Case, Choose, PicMatch, PicSort, Pictograph, Trace)
import art

learn = Sheet('learn', 'Clean and safe places', level=1, goals=['Tell clean from dirty places.', 'Spot dangers and stay safe.'], blocks=[
    Box('adult', P('Read aloud. Walk around the classroom together: what keeps it clean and safe?')),
    P('A **clean** place has no rubbish and smells fresh. A **safe** place has nothing that can hurt us.', 'lead'),
    H('We keep places clean', 3),
    Pics([('wastebasket', 'use the bin'), ('broom', 'sweep'), ('soap', 'wash hands'), ('toothbrush', 'brush teeth')], cols=4, size='19mm'),
    H('Danger! Keep away', 3),
    Pics([('fire', 'fire'), ('electric plug', 'plugs and sockets'), ('kitchen knife', 'sharp knives'), ('water wave', 'deep water'), ('pill', 'medicine')], cols=5, size='19mm'),
    H('Rules and signs keep us safe', 3),
    Pics([('traffic light', 'wait for green'), ('stop sign', 'stop'), ('warning', 'take care'), ('police officer', 'ask for help')], cols=4, size='19mm'),
    P('**Think before you act!** If something looks dangerous, stop, keep away and tell a grown-up.'),
])

facts = Sheet('facts', 'Safe or not safe?', level=1, goals=['Find dangers.', 'Sort clean and dirty.'], blocks=[
    Q('Cross out the things that can hurt you.', Choose([('teddy bear', 'teddy'), ('fire', 'fire'), ('kitchen knife', 'knife'), ('football', 'ball'),
                                                        ('electric plug', 'socket'), ('crayon', 'crayon')], right=[1, 2, 4], cols=6, size='18mm', mark='cross')),
    Q('Circle the things that help keep us clean.', Choose([('soap', 'soap'), ('candy', 'sweets'), ('toothbrush', 'toothbrush'), ('broom', 'broom')], right=[0, 2, 3])),
])

think = Sheet('think', 'What should I do?', level=2, goals=['Choose the safe thing to do.', 'Draw a clean classroom.'], blocks=[
    Q('You see a fire. What should you do? Circle.', Choose([('person running', 'go near it'), ('police officer', 'tell a grown-up and keep away')], right=[1], cols=2)),
    Q('The light is red. What should you do? Circle.', Choose([('stop sign', 'stop and wait'), ('person walking', 'cross the road')], right=[0], cols=2)),
    Q('Draw yourself helping to keep the classroom clean.', Draw('40mm', '', 'e.g. putting rubbish in the bin or tidying toys.')),
])

investigate = Sheet('investigate', 'Clean-up detectives', level=2, goals=['Look for rubbish.', 'Make a picture graph.'], blocks=[
    Box('adult', P('Walk around the playground with gloves. Count the rubbish you find before cleaning it up. Colour one box for each thing.')),
    Q('Rubbish we found. Colour one box for each.', Pictograph([('newspaper', 'paper', 6), ('plastic bottle', 'bottles', 3), ('candy', 'sweet wrappers', 7), ('tin can', 'cans', 2)], top=8)),
    Q('Where should rubbish go? Circle.', Choose([('wastebasket', 'bin'), ('water wave', 'river'), ('deciduous tree', 'under a tree')], right=[0], cols=3)),
    Box('safety', P('Wear gloves. Never pick up glass or sharp things: ask a grown-up.')),
])

case = Sheet('case', 'Ayaan and the hot pan', level=3, goals=['Listen to a story.', 'Learn a safety rule.'], blocks=[
    Case('Ayaan saw a pan on the stove. It smelled yummy! He reached up to touch it.',
         '"Stop!" said his big sister. "The pan is very hot. It can burn you." Ayaan stepped back. Now he always keeps away from the stove.'),
    Q('Why must Ayaan keep away from the stove? Circle.', Choose([('fire', 'it is hot'), ('ice cube', 'it is cold')], right=[0], cols=2)),
])

review = Sheet('review', 'I can do it!', level=3, goals=['Trace safety words.'], blocks=[
    Q('Trace the words.', Trace([('safe', 'stop sign'), ('clean', 'soap')])),
    Q('Circle the clean, safe choice.', Choose([('no littering', 'litter'), ('wastebasket', 'use the bin'), ('fire', 'play with fire')], right=[1], cols=3)),
])

TOPIC = Topic(
    code='B3', strand='earth', title='Clean and Safe Spaces', short='Clean and safe',
    subtitle='Clean and dirty places, common dangers, and rules and signs that keep us safe',
    outcomes=[
        'use observation skills to identify the differences between clean and unclean spaces in their school and homes.',
        'recognise objects or conditions in spaces that make them safe or unsafe, and explain why and what could be done about it.',
        'identify and participate in activities that keep spaces clean and safe and help improve the quality of their immediate spaces.',
        'observe and identify the potential and common dangers in human-built and natural environments, and suggest how best to respond.',
        'use cause-and-effect thinking to judge what to do when they meet a common danger — obey rules and signs, avoid dangerous situations, think before you act.',
    ],
    sheets=[learn, facts, think, investigate, case, review],
    selfcheck=['keep my space clean', 'spot dangers', 'follow safety rules and signs'],
    cover_art=art.pic_row(['wastebasket', 'soap', 'traffic light', 'stop sign'], ['bin', 'soap', 'traffic light', 'stop']),
)
