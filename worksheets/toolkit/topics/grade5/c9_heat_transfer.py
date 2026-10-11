from build import Sheet, Topic
from ws import (P, H, Box, Vocab, Fig, Cols, Row, Case, Links, Lines, Blanks, Match, TrueFalse, MCQ, Order, Table,
                Ans, Sort, Label, Draw, Graph, WordSearch, Q, Part, Bullets, Pics, Wide)
import art
import art4
import art23

learn = Sheet('learn', 'How heat travels', level=1, goals=[
    'Explain the difference between heat and temperature.',
    'Describe conduction, convection and radiation using the particle model.',
    'Explain how conductors, insulators and colours are used to control heat.',
], blocks=[
    P('Hold a cup of hot tea and your hands warm up. Stand in the sun and your face feels hot. Heat is always on the move, from **hotter** things to **colder** things, until they reach the same temperature.', 'lead'),
    Cols(
        H('Heat and temperature', 3),
        P('**Heat** is energy that moves because of a difference in temperature. **Temperature** (in °C) tells us how hot something is: how fast its particles are moving. A bucket of warm water holds more heat than a cup of boiling water, even though the cup is hotter.'),
        Fig(art23.heat_transfer(), 'The three ways heat travels.', span=True),
        H('1. Conduction', 3),
        P('In a **solid**, heat passes from particle to particle. The hot particles vibrate faster and bump into their neighbours, passing the energy along. A metal spoon in hot tea soon feels hot at the handle.'),
        P('**Conductors** let heat through easily: metals such as copper, aluminium and steel. **Insulators** do not: wood, plastic, cloth, wool and especially **trapped air**.'),
        H('2. Convection', 3),
        P('In **liquids and gases**, warm parts **expand**, become less dense and **rise**. Cooler, denser parts **sink** to take their place. This loop is a **convection current**. It stirs a pot of water on the stove and makes the daytime **sea breeze**.'),
        Fig(art4.sea_breeze(), 'A sea breeze is a convection current.', span=True),
        H('3. Radiation', 3),
        P('Heat can travel as invisible **infrared rays**, even through empty space. That is how the Sun\'s energy reaches Earth. **Dark, dull** surfaces absorb radiation well and heat up. **Light, shiny** surfaces reflect it.'),
        H('Putting it together: a vacuum flask', 3),
        Fig(art.vacuum_flask(labels=art.FLASK_PARTS), 'A vacuum flask slows all three kinds of heat transfer.'),
        P('The **vacuum** has no particles, so no conduction or convection can cross it. The **shiny walls** reflect radiation. The **stopper** stops warm air rising out by convection. The same flask keeps cold drinks cold!'),
    ),
    Box('bd', P('Traditional homes in Bangladesh use these ideas: thick mud walls and thatched roofs are good insulators, high ceilings let hot air rise away, and trees shade roofs from radiation.')),
    Vocab([('conduction', 'heat passing through a solid, particle to particle'), ('convection', 'heat carried by moving liquid or gas'),
           ('radiation', 'heat travelling as infrared rays'), ('conductor', 'lets heat through easily'), ('insulator', 'slows the flow of heat'),
           ('convection current', 'a loop of rising warm and sinking cool fluid')]),
])

facts = Sheet('facts', 'Conduction, convection or radiation?', level=1, goals=['Identify the type of heat transfer.', 'Classify conductors and insulators.'], blocks=[
    Q('Which kind of heat transfer is it?', Table(['Example', 'Conduction, convection or radiation?'], [
        ['A metal pan handle gets hot.', Ans('conduction')], ['Warm air rises from a heater.', Ans('convection')], ['The Sun warms your face.', Ans('radiation')],
        ['Your feet feel cold on a tiled floor.', Ans('conduction')], ['A hot-air balloon rises.', Ans('convection')], ['You feel warm in front of a fire.', Ans('radiation')]], widths=['62%', '38%']), marks=6),
    Q('Sort these materials.', Sort(['Good conductor', 'Good insulator'], [('copper', 'Good conductor'), ('steel', 'Good conductor'), ('aluminium', 'Good conductor'),
                                                                        ('wool', 'Good insulator'), ('wood', 'Good insulator'), ('trapped air', 'Good insulator')]), marks=6),
    Q('Label the vacuum flask.', Label(art.vacuum_flask(), art.FLASK_PARTS, width='62%', cols=2), marks=5),
])

think = Sheet('think', 'Explaining heat in daily life', level=2, goals=['Explain with the particle model.', 'Apply ideas to design.'], blocks=[
    Q('Explain, using particles, why a metal spoon in hot dal gets hot all the way up.', Lines(3, 'The particles at the hot end vibrate faster and bump into their neighbours, passing energy along the metal to the handle (conduction). Metal is a good conductor.'), marks=3),
    Q('Why are heaters put near the floor but air conditioners high on the wall?', Lines(3, 'Warm air rises, so a low heater sets up a convection current that warms the whole room; cool air sinks, so a high air conditioner cools the room as the cold air falls.'), marks=3),
    Q('Why do people in hot countries often wear white or light-coloured clothes?', Lines(2, 'Light colours reflect radiation from the Sun, so they absorb less heat.'), marks=2),
    Q('A cook\'s pan has a copper base and a plastic handle. Explain both choices.', Lines(2, 'Copper conducts heat quickly to the food; plastic is an insulator so the handle stays cool.'), marks=2),
])

investigate = Sheet('investigate', 'Which colour heats up fastest in the sun?', level=2, goals=['Plan a fair test.', 'Plot and interpret a line graph.'], blocks=[
    P('Class 5B wrapped three identical cans of water in black paper, white paper and shiny foil. They put them in the sun and measured the water temperature every 10 minutes.'),
    Q('Name the variables.', Part('Changed:', Lines(1, 'the colour/covering of the can')), Part('Measured:', Lines(1, 'the water temperature')),
      Part('Kept the same:', Lines(1, 'same cans, same amount of water, same starting temperature, same place in the sun, same times')), marks=3),
    Q('Plot the three lines on one graph (use a key).', Table(['Time (min)', '0', '10', '20', '30', '40'], [['black (°C)', '28', '33', '38', '42', '45'],
                                                                                                         ['white (°C)', '28', '30', '32', '34', '35'],
                                                                                                         ['shiny foil (°C)', '28', '29', '30', '31', '32']], center=True),
      Graph(['0', '10', '20', '30', '40'], [[28, 33, 38, 42, 45], [28, 30, 32, 34, 35], [28, 29, 30, 31, 32]], 'Temperature (°C)', 'Time (min)', ymin=25, ymax=46, step=3,
            kind='line', series_names=['black', 'white', 'shiny foil'], width=130, height=54), marks=4),
    Q('Which heated fastest? Explain why using the word **radiation**.', Lines(2, 'The black can: dark, dull surfaces absorb radiation from the Sun best. Shiny foil reflects most of it.'), marks=2),
    Q('Use your results to choose a colour for a water tank on a roof that should stay cool.', Lines(2, 'White or shiny, because it reflects radiation and absorbs least heat.'), marks=2),
    P('*Data: example results for practice.*', 'small muted'),
])

case = Sheet('case', 'Keeping cool in a hotter Dhaka', level=3, goals=['Apply heat transfer to a real problem.', 'Compare solutions using data.'], blocks=[
    Links('Science', 'Design and technology', 'Health', 'Maths'),
    Case('Many homes in Dhaka have thin **tin (corrugated iron) roofs**. On a sunny day the dark metal absorbs radiation and conducts heat straight into the room below. Inside, it can be much hotter than outside, which is dangerous for babies and older people during a heatwave.',
         'Some families have tried cheap ideas: painting the roof **white**, adding a **ceiling of jute or bamboo** with an air gap, and growing **creepers or trees** for shade. A community group measured the temperature inside four rooms at 2 pm on the same hot day.',
         source='Example data based on cool-roof trials in hot cities; numbers are illustrative.'),
    Q('Draw a bar chart of the results.', Table(['Room', 'bare tin roof', 'white-painted roof', 'jute ceiling with air gap', 'tree shade + white roof'], [['Temperature at 2 pm (°C)', '41', '36', '35', '32']], center=True),
      Graph(['bare tin', 'white roof', 'jute ceiling', 'shade + white'], [41, 36, 35, 32], 'Temperature (°C)', 'Room', ymin=25, ymax=42, step=3, width=116, height=44), marks=3),
    Q('Explain why the white roof was cooler, using **radiation**.', Lines(2, 'White reflects more of the Sun\'s radiation, so the roof absorbs less heat.'), marks=2),
    Q('Explain why the jute ceiling with an air gap helped, using **conduction**.', Lines(2, 'Jute and trapped air are insulators, so less heat is conducted from the hot roof into the room.'), marks=2),
    Q('Recommend one solution for a poor family. Give a scientific and a money reason.', Lines(2, 'e.g. white paint: cheap, quick, reflects radiation; or plant a tree: free shade, also cleans the air.'), marks=3),
])

review = Sheet('review', 'Show what you know', level=3, goals=['Use key vocabulary.', 'Answer test-style questions.'], blocks=[
    Q('Find the words.', WordSearch(['CONDUCTION', 'CONVECTION', 'RADIATION', 'INSULATOR', 'METAL', 'VACUUM', 'HEAT'], size=11, seed=519)),
    Q('Heat travels through empty space by…', MCQ(['conduction', 'convection', 'radiation'], 2), marks=1),
    Q('Which is the best insulator?', MCQ(['copper', 'steel', 'wool'], 2), marks=1),
    Q('**Challenge.** Design a lunch box that keeps rice hot for 4 hours. Label how it reduces conduction, convection and radiation.',
      Draw('50mm', 'My hot lunch box', 'e.g. double walls with an air gap (conduction), a tight lid (convection), shiny inner lining (radiation), wool cover.'), marks=4),
])

TOPIC = Topic(
    code='C9', strand='physical', title='Heat Transfer: Conduction, Convection and Radiation', short='Heat transfer',
    subtitle='How heat moves through solids, liquids, gases and empty space, and how we control it with conductors, insulators and colours',
    outcomes=[
        'demonstrate how heat travels, conducting experiments to show conduction, convection and radiation.',
        'investigate different conductors and insulators of heat, and explain their uses.',
        'explain heat transfer using the particle model of matter.',
        'discuss the different ways heat is used by humans, the dangers in using heat, and how we design objects and buildings to control it.',
    ],
    sheets=[learn, facts, think, investigate, case, review],
    selfcheck=['explain heat and temperature', 'describe conduction, convection and radiation', 'choose conductors and insulators', 'plot a line graph of heating', 'design ways to keep cool'],
    cover_art=art23.heat_transfer(),
)
