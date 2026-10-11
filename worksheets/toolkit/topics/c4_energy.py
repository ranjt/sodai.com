from build import Sheet, Topic
from ws import (P, H, Box, Vocab, Fig, Cols, Row, Case, Links, Lines, Blanks, Match, TrueFalse, MCQ, Order, Table,
                Ans, Sort, Label, Draw, Graph, WordSearch, Q, Part, Bullets)
import art

learn = Sheet('learn', 'Energy: it moves and changes but is never lost', level=1, goals=[
    'Name different forms of energy and describe energy transfers.',
    'Explain that energy cannot be created or destroyed.',
    'Explain how temperature changes when an object gains or loses heat.',
], blocks=[
    P('A rickshaw puller pedals through traffic. A ceiling fan spins. Rice cooks on a gas stove. A phone lights up. In every '
      'case, **energy** is moving from one place to another and changing from one form to another. Energy is what makes '
      'things happen.', 'lead'),
    Cols(
        H('Forms of energy', 3),
        Table(['Form', 'Examples'], [
            ['kinetic (movement)', 'a moving bus, flowing river, spinning fan'], ['potential (stored)', 'water held behind a dam, a stretched rubber band, a book on a high shelf'],
            ['chemical (stored)', 'food, fuel (gas, petrol, wood), batteries'], ['thermal (heat)', 'a hot cup of cha, the Sun\'s warmth'],
            ['light', 'the Sun, a bulb, a firefly'], ['sound', 'a dhol, a car horn, your voice'], ['electrical', 'current flowing in wires']]),
        H('Energy transfers and chains', 3),
        P('Energy is **transferred** from one thing to another, and **transformed** (changed) from one form to another. We '
          'can show this with an **energy chain**:'),
        Fig(art.energy_chain([('chemical', 'in the battery'), ('electrical', 'in the wires'), ('light + heat', 'from the bulb')]), 'A torch.', span=True, width='80%'),
        Bullets(['A rickshaw puller: chemical energy (food) → kinetic energy (moving rickshaw) + heat.',
                 'A solar panel: light energy → electrical energy.',
                 'A gas stove: chemical energy (gas) → thermal energy (heat) + light.']),
        H('Energy is conserved', 3),
        P('Energy **cannot be created or destroyed**. It only moves from place to place or changes form. So where does energy '
          '"go" when a fan is switched off? It has spread out into the surroundings, mostly as **heat** and **sound**. We often '
          'call this energy **wasted**, because it is not useful to us. An **efficient** machine wastes less energy. An LED '
          'bulb gives the same light as an old filament bulb but uses only about one fifth of the electricity, because it '
          'wastes much less as heat.'),
        H('Heat and temperature', 3),
        P('**Temperature** tells us how hot or cold something is, measured in °C with a **thermometer**. **Heat** is energy '
          'that moves from a **hotter** object to a **colder** one. When an object **gains** heat, its temperature **rises**; '
          'when it **loses** heat, its temperature **falls**. A hot cup of tea cools down until it reaches the temperature of '
          'the room.'),
        P('Materials that let heat pass easily are **thermal conductors** (metals). Materials that slow heat down are '
          '**thermal insulators** (wood, plastic, wool, air). Cooking pots are metal, but their handles are wood or plastic.'),
        H('Energy drives cycles', 3),
        P('Energy from the Sun drives the **water cycle** (it evaporates water) and powers **food chains** (plants use light to '
          'make food). As energy flows through, **matter** (water, nutrients) goes round and round.'),
        Box('bd', P('Millions of homes in rural Bangladesh use **solar home systems**: a solar panel on the roof charges a battery '
                    'that powers lights, fans and phone chargers at night.')),
    ),
    Vocab([('energy', 'what makes things happen'), ('kinetic energy', 'energy of movement'), ('potential energy', 'stored energy'),
           ('transfer', 'energy moving from one place or object to another'), ('transform', 'energy changing from one form to another'),
           ('efficient', 'wasting little energy'), ('thermal conductor', 'a material that lets heat pass through easily'),
           ('thermal insulator', 'a material that slows down heat moving through it')]),
])

facts = Sheet('facts', 'Forms of energy', level=1, goals=['Identify forms of energy.', 'Complete energy chains.'], blocks=[
    Q('Sort the examples by the main form of energy.',
      Sort(['Kinetic', 'Chemical (stored)', 'Light or sound'], [('a moving bus', 'Kinetic'), ('a spinning fan', 'Kinetic'), ('a battery', 'Chemical (stored)'),
                                                                ('a plate of rice', 'Chemical (stored)'), ('a firefly', 'Light or sound'), ('a drum beat', 'Light or sound')]), marks=6),
    Q('Complete the energy chains.',
      Table(['Device', 'Energy in', 'Useful energy out', 'Wasted energy'], [
          ['electric fan', Ans('electrical'), Ans('kinetic (moving air)'), Ans('heat, sound')], ['solar panel', Ans('light'), Ans('electrical'), Ans('heat')],
          ['radio', Ans('electrical'), Ans('sound'), Ans('heat')], ['gas stove', Ans('chemical'), Ans('heat (thermal)'), Ans('light, heat to the room')]], center=True), marks=8),
    Q('Fill in the gaps.',
      Blanks('Energy cannot be [created] or destroyed. Heat moves from [hotter] objects to [colder] ones. When an object '
             'gains heat its temperature [rises]. Metals are good thermal [conductors].', extra=['falls', 'insulators']), marks=5),
])

think = Sheet('think', 'Following the energy', level=2, goals=['Explain energy transfers.', 'Explain heating and cooling.'], blocks=[
    Q('Describe the energy changes when a rickshaw puller rides up a bridge and then freewheels down.',
      Lines(4, 'Chemical energy from food → kinetic energy of the rickshaw; going up, kinetic energy changes into (gravitational) potential energy; coming down, potential energy changes back into kinetic energy. Some energy is wasted as heat and sound.'), marks=3),
    Q('"When a ball stops bouncing, its energy has been destroyed." Do you agree? Explain.',
      Lines(3, 'No: energy cannot be destroyed; it has been transferred to the surroundings as heat and sound each time the ball hits the ground.'), marks=2),
    Q('Explain why a metal spoon in hot tea gets hot quickly, but a wooden spoon does not.',
      Lines(2, 'Metal is a thermal conductor, so heat moves through it easily; wood is an insulator, so heat moves slowly.'), marks=2),
    Q('A cold bottle of water and a hot cup of tea are left on a table. What happens to their temperatures? Explain using the word *heat*.',
      Lines(3, 'The tea loses heat to the room and cools down; the cold water gains heat from the room and warms up; both end at room temperature.'), marks=2),
    Q('Why is an LED bulb more efficient than a filament bulb?',
      Lines(2, 'It changes more of its electrical energy into light and wastes less as heat.'), marks=1),
])

investigate = Sheet('investigate', 'Which wrapping keeps tea hottest?', level=2, goals=['Plan a fair test.', 'Plot several lines on a graph.', 'Explain results using insulation.'], blocks=[
    Fig(art.insulation_cups(), width='80%'),
    P('Class 5D poured 200 ml of water at 80 °C into four identical cups, wrapped three of them in different materials, and '
      'measured the temperature every 5 minutes.'),
    Q('Name the variables.',
      Table(None, [['Change', Ans('the wrapping material')], ['Measure', Ans('temperature every 5 minutes (°C)')],
                   ['Keep the same', Ans('volume and starting temperature of water, type of cup, room, time, thermometer')]], widths=['24%', '76%']), marks=3),
    Q('Here are the results. Plot all four on one line graph (use a different line or symbol for each).',
      Table(['Time (min)', '0', '5', '10', '15', '20'], [['no cover', '80', '72', '64', '58', '52'], ['newspaper', '80', '75', '70', '65', '60'],
                                                         ['wool', '80', '77', '74', '71', '68'], ['foil', '80', '74', '68', '63', '58']], center=True),
      Graph(['0', '5', '10', '15', '20'], [[80, 72, 64, 58, 52], [80, 75, 70, 65, 60], [80, 77, 74, 71, 68], [80, 74, 68, 63, 58]],
            'Temperature (°C)', 'Time (minutes)', ymin=40, ymax=80, step=5, kind='line',
            series_names=['no cover', 'newspaper', 'wool', 'foil'], width=150, height=70), marks=4),
    Q('Which material was the best insulator? Use numbers in your answer.',
      Lines(2, 'Wool: the water only cooled by 12 °C (80 → 68) in 20 minutes, compared with 28 °C for no cover.'), marks=2),
    Q('Why do you think wool works so well?', Lines(2, 'Wool traps lots of air, and air is a poor conductor of heat, so heat escapes slowly.'), marks=1),
    Q('Suggest a real use for what the class found out.', Lines(2, 'e.g. wrapping a tiffin box or a flask; warm woollen clothes in winter; insulating a roof.'), marks=1),
])

case = Sheet('case', 'Power from the sun: solar home systems', level=3, goals=['Trace energy transfers in a real system.', 'Use maths to plan energy use.', 'Weigh benefits and problems.'], blocks=[
    Links('Science', 'Maths', 'Economics', 'Environment', 'Technology'),
    Fig(art.solar_home(), width='62%'),
    Case('Twenty years ago, millions of village homes in Bangladesh had no electricity. At night families used **kerosene '
         'lamps**, which give dim light, smoky air and a risk of fire. Since the early 2000s, millions of homes have bought '
         '**solar home systems**, making Bangladesh one of the world\'s biggest users of small solar systems.',
         'A solar panel on the roof turns sunlight into electricity during the day. This charges a **battery**. At night the '
         'battery powers **LED lights**, a small **fan**, a **phone charger** and sometimes a TV. Children can study after dark, '
         'and shops can stay open longer.',
         'Problems include the **cost** of buying a system, batteries that wear out after a few years and must be **recycled** '
         'safely (old batteries contain harmful lead or chemicals), and less power on cloudy monsoon days.',
         source='Based on reports about Bangladesh\'s solar home system programme (IDCOL, World Bank).'),
    Q('Write the energy chain for an LED light powered by a solar home system at night.',
      Lines(2, 'light (Sun) → electrical (panel) → chemical (stored in battery) → electrical → light (+ heat) from the LED'), marks=3),
    Q('Energy maths. A 50 W panel gets 5 hours of good sunshine a day.',
      Part('How many watt-hours (Wh) of energy can it make in a day? (W × hours)', Lines(1, '50 × 5 = 250 Wh')),
      Part('A family uses 3 LED bulbs of 5 W for 4 hours. How much energy is that?', Lines(1, '3 × 5 × 4 = 60 Wh')),
      Part('They also use a 20 W fan for 6 hours. Total energy used?', Lines(1, '20 × 6 = 120 Wh; total 60 + 120 = 180 Wh')),
      Part('Is there enough energy left to charge a phone (10 Wh)?', Lines(1, 'Yes: 250 − 180 = 70 Wh left, more than 10 Wh.')), marks=4),
    Q('Give **two** ways solar lights are better than kerosene lamps.',
      Lines(2, 'No smoke, so healthier lungs; brighter light for studying; no fire risk; no fuel to buy; no carbon dioxide while working.'), marks=2),
    Q('Old batteries contain harmful materials. Suggest a way to deal with them safely.',
      Lines(2, 'Return them to the seller or a recycling centre so the materials are recovered and do not pollute soil and water.'), marks=1),
])

review = Sheet('review', 'Show what you know', level=3, goals=['Use key vocabulary.', 'Answer test-style questions.'], blocks=[
    Q('Find the key words.', WordSearch(['ENERGY', 'KINETIC', 'HEAT', 'LIGHT', 'SOUND', 'SOLAR', 'BATTERY', 'INSULATOR', 'STORED'], size=11, seed=131)),
    Q('Which form of energy is stored in food?', MCQ(['kinetic', 'chemical', 'sound', 'light'], 1), marks=1),
    Q('A hot iron is left on a cold table. Which is true?', MCQ(['the iron gains heat', 'heat moves from the iron to the table', 'cold moves into the iron', 'the temperatures stay the same'], 1, one_col=True), marks=1),
    Q('Draw an energy chain for a person playing a dhol (drum).',
      Draw('30mm', 'My energy chain', 'chemical (food) → kinetic (moving hands and drum skin) → sound (+ heat)'), marks=2),
    Q('**Challenge.** "We should save energy, but energy cannot be destroyed." Explain why both statements can be true.',
      Lines(3, 'Energy is never destroyed, but useful energy (like fuel or electricity) gets spread out as heat that we cannot use again; saving energy means using less of the useful stored energy (fuel), which is limited and costs money.'), marks=3),
])

TOPIC = Topic(
    code='C4', strand='physical', title='Energy and Its Transformations', short='Energy',
    subtitle='Forms of energy, energy chains, conservation of energy, heat and temperature',
    outcomes=[
        'understand that energy cannot be created or destroyed — it only moves between one place and another, between objects and fields, or between systems.',
        'describe how energy drives the cycling of matter within and between systems.',
        'explain how a change in the temperature of an object is related to the gain or loss of heat by the object.',
        'describe changes in a system in terms of energy and matter.',
    ],
    sheets=[learn, facts, think, investigate, case, review],
    selfcheck=['name forms of energy with examples', 'draw energy chains', 'explain that energy is conserved but can be wasted',
               'explain how temperature changes when heat is gained or lost', 'test which materials are good insulators',
               'explain how a solar home system works'],
    cover_art=art.energy_chain([('light', 'from the Sun'), ('electrical', 'from the panel'), ('chemical', 'in the battery'), ('light', 'from the LED')]),
)
