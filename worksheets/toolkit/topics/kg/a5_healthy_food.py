from build import Sheet, Topic
from ws import (P, H, Box, Fig, Q, Lines, MCQ, Draw, Pics, Ans, Case, Choose, PicMatch, PicSort, Pictograph, Trace)
import art

learn = Sheet('learn', 'Healthy food', level=1, goals=['Name healthy foods.', 'Know why we need food and water.'], blocks=[
    Box('adult', P('Read aloud. Ask: "What did you eat for breakfast? Which food helps you grow?"')),
    P('Food gives us **energy** to play and helps us **grow**. We eat different kinds of food every day.', 'lead'),
    H('Go foods give us energy', 3),
    Pics([('cooked rice', 'rice'), ('bread', 'roti and bread'), ('potato', 'potato'), ('corn', 'corn')], cols=4, size='19mm'),
    H('Grow foods help us grow strong', 3),
    Pics([('fish', 'fish'), ('egg', 'egg'), ('milk', 'milk'), ('peanuts', 'dal and nuts')], cols=4, size='19mm'),
    H('Glow foods keep us healthy', 3),
    Pics([('mango', 'fruit'), ('carrot', 'carrot'), ('leafy green', 'green vegetables'), ('banana', 'banana')], cols=4, size='19mm'),
    P('And drink lots of clean **water**! Sweets, chips and fizzy drinks are treats: just a little, not every day.'),
])

facts = Sheet('facts', 'Find the healthy food', level=1, goals=['Choose healthy foods.', 'Sort foods.'], blocks=[
    Q('Circle the **healthy** snacks.', Choose([('banana', 'banana'), ('candy', 'sweets'), ('carrot', 'carrot'), ('french fries', 'chips'),
                                                ('apple', 'apple'), ('doughnut', 'doughnut')], right=[0, 2, 4], cols=6, size='18mm')),
    Q('Cut and sort: **every day** or **only a treat**?', PicSort(['Every day', 'Only a treat'], [
        ('cooked rice', 'rice', 'Every day'), ('fish', 'fish', 'Every day'), ('tomato', 'tomato', 'Every day'),
        ('cake', 'cake', 'Only a treat'), ('lollipop', 'lollipop', 'Only a treat'), ('burger', 'burger', 'Only a treat')], height='34mm')),
])

think = Sheet('think', 'My healthy plate', level=2, goals=['Plan a healthy meal.'], blocks=[
    Q('Draw a healthy lunch on the plate: a go food, a grow food and a glow food.', Draw('70mm', 'My plate', 'e.g. rice (go), fish or dal (grow), vegetables and fruit (glow), with a glass of water.')),
    Q('What is the best drink when you are thirsty?', Choose([('cup with straw', 'fizzy drink'), ('water glass', 'water'), ('candy', 'sweets')], right=[1], cols=3)),
])

investigate = Sheet('investigate', 'Our fruit survey', level=2, goals=['Ask friends about fruit.', 'Make a picture graph.'], blocks=[
    Box('adult', P('Ask each child to choose their favourite fruit. Colour one box for each child.')),
    Q('Our favourite fruit. Colour one box for each child.', Pictograph([('mango', 'mango', 8), ('banana', 'banana', 5), ('watermelon', 'watermelon', 4), ('apple', 'apple', 3)], top=9)),
    Q('Which fruit did most children choose? Circle it.', Choose([('mango', 'mango'), ('banana', 'banana'), ('watermelon', 'watermelon'), ('apple', 'apple')], right=[0])),
])

case = Sheet('case', "Shopon's tiffin", level=3, goals=['Listen to a story.', 'Choose a healthy tiffin.'], blocks=[
    Case('Every day Shopon took chips and a fizzy drink to school. By lunchtime he felt tired and hungry.',
         'His mother packed a new tiffin: roti, an egg, a banana and a bottle of water. Shopon felt full of energy and played all afternoon!'),
    Q('Circle the food in Shopon\'s new tiffin.', Choose([('bread', 'roti'), ('egg', 'egg'), ('french fries', 'chips'), ('banana', 'banana')], right=[0, 1, 3])),
])

review = Sheet('review', 'I can do it!', level=3, goals=['Trace food words.'], blocks=[
    Q('Trace the words.', Trace([('fruit', 'apple'), ('water', 'water glass')])),
    Q('Circle the food that helps you **grow strong**.', Choose([('candy', 'sweets'), ('egg', 'egg'), ('cup with straw', 'fizzy drink')], right=[1], cols=3)),
])

TOPIC = Topic(
    code='A5', strand='living', title='Healthy Food', short='Healthy food',
    subtitle='Go, grow and glow foods, healthy snacks and treats, and drinking water',
    outcomes=[
        'know about the need for a healthy diet, including the right types of food and water.',
        'match different types of local food to the food groups they belong to.',
        'give examples of nutritious foods and tell how they contribute to growth and energy needs.',
        'suggest healthy food choices for balanced meals and for snacks.',
        'discuss the significance of making healthy food choices.',
    ],
    sheets=[learn, facts, think, investigate, case, review],
    selfcheck=['name healthy foods', 'choose a healthy snack', 'draw a healthy plate'],
    cover_art=art.pic_row(['cooked rice', 'fish', 'carrot', 'banana', 'water glass'], ['rice', 'fish', 'carrot', 'banana', 'water']),
)
