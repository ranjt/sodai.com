from build import Sheet, Topic
from ws import (P, H, Box, Vocab, Fig, Cols, Row, Case, Links, Lines, Blanks, Match, TrueFalse, MCQ, Order, Table,
                Ans, Sort, Label, Draw, Graph, WordSearch, Q, Part, Bullets, Pics)
import art
import art23

learn = Sheet('learn', 'Heat and temperature', level=1, goals=[
    'Explain what heat is and name sources of heat.',
    'Describe what happens when heat is added or taken away.',
    'Explain how heat travels and how to stay safe near hot things.',
], blocks=[
    P('Rub your hands together quickly. They get warm! **Heat** is a kind of **energy** that makes things warmer. **Temperature** tells us how hot or cold something is.', 'lead'),
    H('Sources of heat', 3),
    Pics([('sun', 'the Sun'), ('fire', 'fire'), ('light bulb', 'light bulbs'), ('electric plug', 'electric heaters and irons'), ('hand', 'rubbing things together')], cols=5, size='14mm'),
    H('Measuring temperature', 3),
    P('We measure temperature in **degrees Celsius (°C)** with a **thermometer**. The liquid inside rises when it gets warmer. Ice melts at **0 °C**, your body is about **37 °C**, and water boils at **100 °C**.'),
    Fig(art23.thermometers((5, 25, 40)), 'Read the thermometers: A is 5 °C, B is 25 °C, C is 40 °C.', width='42%'),
    H('Adding and removing heat', 3),
    Table(['Adding heat', 'Removing heat (cooling)'], [['ice melts into water', 'water freezes into ice'], ['water boils and turns to steam', 'steam turns back into water drops'],
                                                       ['butter and chocolate melt', 'melted candle wax goes hard'], ['rice and eggs cook', 'hot tea gets cool']]),
    H('How heat travels', 3),
    P('Heat always moves from **hotter** places to **colder** places, in three ways:'),
    Fig(art23.heat_transfer(), 'Three ways heat travels.', width='80%'),
    Bullets(['**Conduction**: heat travels through solids. A metal spoon in hot tea gets hot all the way up.',
             '**Convection**: warm water or air rises and cool water or air sinks. This makes water move around in a pot.',
             '**Radiation**: heat travels as invisible rays, like the warmth you feel from the Sun or a fire.']),
    P('Metals let heat through easily: they are good **conductors**. Wood, plastic, cloth and air do not: they are **insulators**. That is why pot handles are wood or plastic, and why a thick kantha quilt keeps you warm in winter.'),
    H('Using heat safely', 3),
    P('We use heat to cook food, boil water to make it safe, iron clothes, dry fish (shutki) and fire clay pots. But heat can be dangerous.'),
    Box('safety', P('Keep away from fires, stoves, hot oil, irons and steam. Use oven gloves. Tie back loose clothes near a fire. If you get burnt, cool the burn under clean running water for 20 minutes and tell an adult.')),
    Vocab([('heat', 'energy that makes things warmer'), ('temperature', 'how hot or cold something is'), ('thermometer', 'measures temperature'),
           ('conductor', 'lets heat through easily'), ('insulator', 'does not let heat through easily')]),
])

facts = Sheet('facts', 'Hot and cold facts', level=1, goals=['Read thermometers.', 'Sort changes.'], blocks=[
    Q('Read the thermometers.', Fig(art23.thermometers((10, 30, 45)), width='40%'),
      Table(['A', 'B', 'C'], [[Ans('10 °C'), Ans('30 °C'), Ans('45 °C')]], center=True), marks=3),
    Q('Is heat added or removed?', Sort(['Heat added', 'Heat removed'], [('ice cream melts', 'Heat added'), ('rice cooks', 'Heat added'), ('wet clothes dry in the sun', 'Heat added'),
                                                                           ('water freezes in the freezer', 'Heat removed'), ('hot tea cools', 'Heat removed'), ('melted wax goes hard', 'Heat removed')]), marks=6),
    Q('Name the way heat travels in each picture.', Fig(art23.heat_transfer(names=False), width='72%'),
      Table(['A', 'B', 'C'], [[Ans(w) for w in art23.HEAT_WAYS]], center=True), marks=3),
])

think = Sheet('think', 'Thinking about heat', level=2, goals=['Explain conductors and insulators.'], blocks=[
    Q('Why do cooking pots have wooden or plastic handles?', Lines(2, 'Wood and plastic are insulators, so the handle does not get too hot to hold.'), marks=2),
    Q('Why do we wear several layers of clothes in winter?', Lines(2, 'Air is trapped between the layers; air is an insulator, so it keeps our body heat in.'), marks=2),
    Q('Sort the materials.', Sort(['Conductor', 'Insulator'], [('steel spoon', 'Conductor'), ('aluminium pot', 'Conductor'), ('wooden spoon', 'Insulator'), ('wool', 'Insulator'), ('plastic handle', 'Insulator')]), marks=5),
])

investigate = Sheet('investigate', 'Which cover keeps tea hot the longest?', level=2, goals=['Measure temperature.', 'Draw a bar chart and conclude.'], blocks=[
    Fig(art.insulation_cups(), width='60%'),
    P('Class 3A filled four cups with hot water at **80 °C**. They wrapped three cups in different materials. After 20 minutes they measured the temperature. (Only an adult should pour the hot water.)'),
    Q('Draw a bar chart.', Table(['Cover', 'none', 'newspaper', 'wool', 'foil'], [['Temperature after 20 min (°C)', '45', '52', '60', '55']], center=True),
      Graph(['none', 'newspaper', 'wool', 'foil'], [45, 52, 60, 55], 'Temperature (°C)', 'Cover', ymax=70, step=10, width=100, height=48), marks=3),
    Q('Which cover was the best insulator?', Lines(1, 'wool'), marks=1),
    Q('Why did the cup with no cover cool fastest?', Lines(2, 'Nothing stopped the heat escaping into the air.'), marks=2),
])

case = Sheet('case', 'Keeping warm safely in winter', level=3, goals=['Use what you know about heat to stay safe.'], blocks=[
    Links('Science', 'Health', 'Community'),
    Case('In winter, nights in the north of Bangladesh can get very cold, below **10 °C**. Many families sit around small open fires to keep warm.',
         'Every winter, some people are badly burnt when loose clothes such as a sari, orna or shawl catch fire. Doctors and fire fighters teach families how to keep warm safely: wear warm layers and use quilts, sit at a safe distance from fires, tie back loose clothes, and never leave a fire alone.',
         source='Based on winter safety advice in Bangladesh.'),
    Q('How does a fire warm people who are sitting near it?', Lines(1, 'by radiation: heat rays travel from the fire'), marks=1),
    Q('Write three safety rules for sitting near a fire.', Lines(3, 'sit at a safe distance; tie back loose clothes; never leave the fire alone; keep water or sand nearby'), marks=3),
    Q('If someone\'s clothes catch fire, they should stop, drop and roll. Draw the three steps.', Draw('34mm', 'Stop, drop, roll', 'stop moving; drop to the ground; roll over to put out the flames.'), marks=3),
])

review = Sheet('review', 'Show what you know', level=3, goals=['Use heat words.'], blocks=[
    Q('Find the words.', WordSearch(['HEAT', 'MELT', 'FREEZE', 'BOIL', 'SUN', 'FIRE', 'COOL'], size=9, seed=312)),
    Q('Temperature is measured with a…', MCQ(['ruler', 'thermometer', 'magnet'], 1), marks=1),
    Q('Heat travelling up a metal spoon is…', MCQ(['conduction', 'convection', 'radiation'], 0), marks=1),
    Q('**Challenge.** Design a box to keep a lunch of hot rice warm. What materials would you use?', Lines(2, 'a metal tiffin box wrapped in wool or cloth, inside a plastic bag; insulators trap the heat'), marks=2),
])

TOPIC = Topic(
    code='C3', strand='physical', title='Heat and Temperature', short='Heat',
    subtitle='Sources of heat, measuring temperature, heating and cooling, conduction, convection and radiation, and heat safety',
    outcomes=[
        'explain what heat is and suggest sources of heat — the Sun, fire, light bulbs, electrical appliances, and rubbing two things together.',
        'recognize how heat can be produced in many ways.',
        'investigate how adding or removing heat affects substances.',
        'demonstrate how heat travels, conducting experiments to show conduction, convection and radiation.',
        'discuss the different ways heat is used by humans, the dangers in using heat, and how to take care around objects that are hot or that produce heat.',
    ],
    sheets=[learn, facts, think, investigate, case, review],
    selfcheck=['name sources of heat', 'read a thermometer', 'say what heating and cooling do', 'explain conduction, convection and radiation', 'stay safe near hot things'],
    cover_art=art23.heat_transfer(),
)
