from build import Sheet, Topic
from ws import (P, H, Box, Vocab, Fig, Cols, Row, Case, Links, Lines, Blanks, Match, TrueFalse, MCQ, Order, Table,
                Ans, Sort, Label, Draw, Graph, WordSearch, Q, Part, Bullets, Pics, Wide)
import art

learn = Sheet('learn', 'Energy resources: renewable, non-renewable and green', level=1, goals=[
    'Classify energy resources as renewable or non-renewable.',
    'Explain why burning fossil fuels is a global problem.',
    'Use real data to compare how the world and Bangladesh make electricity.',
], blocks=[
    P('Every time you switch on a fan, the electricity comes from a **power station** using an **energy resource**. Some resources will run out. Some never will. Our choices affect the whole planet.', 'lead'),
    Cols(
        H('Non-renewable resources', 3),
        P('**Fossil fuels**: **coal**, **oil** and **natural gas**, formed from plants and animals buried for **millions of years**. We use them much faster than they form, so one day they will **run out**. **Nuclear** fuel (uranium) is also non-renewable, but it does not release carbon dioxide.'),
        H('Renewable resources', 3),
        P('**Renewable** resources are naturally replaced and will not run out: **solar** (sunlight), **wind**, **hydro** (moving water), **biomass and biogas** (plants and animal dung), **tidal** and **geothermal** (heat from inside the Earth).'),
        Pics([('solar energy', 'solar'), ('wind energy', 'wind'), ('water wave', 'hydro'), ('cow', 'biogas'), ('factory smoke', 'coal and gas')], cols=5, size='15mm', small=True),
        H('Why it is a global issue', 3),
        Bullets(['Burning fossil fuels releases **carbon dioxide (CO~2~)**, a greenhouse gas that traps heat and causes **climate change**.',
                 'Bangladesh is one of the countries most at risk: stronger cyclones, floods and sea-level rise along the coast.',
                 'Smoke from burning coal, oil and wood also pollutes the air we breathe.',
                 'About **685 million people** in the world still had **no electricity** at home in 2022, mostly in Sub-Saharan Africa.']),
        H('Green energy', 3),
        P('**Green** (clean) energy comes from renewable resources that release little or no pollution: solar, wind and hydro. Using energy **efficiently** (LED bulbs, switching off) is green too: the cleanest energy is the energy we do not waste.'),
    ),
    H('How the world made its electricity (2024)', 3),
    Table(['Coal', 'Gas', 'Other fossil', 'Nuclear', 'Hydro', 'Wind', 'Solar', 'Other renewable'], [['34%', '22%', '3%', '9%', '14%', '8%', '7%', '3%']], center=True),
    P('About **59%** came from fossil fuels and about **41%** from clean sources (renewables and nuclear). In 2024 wind and solar together made more electricity than hydro for the first time.', 'small'),
    H('How Bangladesh made its electricity (2023)', 3),
    Table(['Natural gas', 'Oil (liquid fuels)', 'Coal', 'Imports, hydro and solar'], [['55%', '20%', '14%', '11%']], center=True),
    P('Bangladesh\'s own renewables are still small: the **Kaptai** hydro plant on the Karnaphuli River and a growing amount of **solar**, including millions of solar home systems.', 'small'),
    Box('world', P('Sources (rounded): world, Ember *Global Electricity Review 2025*; Bangladesh, Power Grid Company of Bangladesh data reported by Reuters (2024); people without electricity, *Tracking SDG7: The Energy Progress Report 2024*.'), title='Where the numbers come from'),
    Vocab([('fossil fuel', 'coal, oil or gas formed over millions of years'), ('renewable', 'naturally replaced; will not run out'), ('non-renewable', 'will run out one day'),
           ('green energy', 'clean energy from renewable resources'), ('greenhouse gas', 'a gas such as CO~2~ that traps heat in the air'), ('efficiency', 'getting the job done with less energy')]),
])

facts = Sheet('facts', 'Renewable or not?', level=1, goals=['Classify energy resources.', 'Read data from a table.'], blocks=[
    Q('Sort the energy resources.', Sort(['Renewable', 'Non-renewable'], [('solar', 'Renewable'), ('wind', 'Renewable'), ('hydro', 'Renewable'), ('biogas', 'Renewable'),
                                                                       ('coal', 'Non-renewable'), ('oil', 'Non-renewable'), ('natural gas', 'Non-renewable'), ('uranium', 'Non-renewable')]), marks=8),
    Q('Draw a bar chart of the world\'s electricity in 2024.', Graph(['coal', 'gas', 'other fossil', 'nuclear', 'hydro', 'wind', 'solar', 'other ren.'], [34, 22, 3, 9, 14, 8, 7, 3],
                                                                 'Share of electricity (%)', 'Source', ymax=40, step=5, width=150, height=52), marks=4),
    Q('Use the chart.', Part('Which single source made the most electricity?', Lines(1, 'coal (34%)')),
      Part('Add up wind + solar + hydro + other renewables.', Lines(1, '8 + 7 + 14 + 3 = 32%')), marks=2),
])

think = Sheet('think', 'Weighing up energy choices', level=2, goals=['Compare advantages and disadvantages.', 'Interpret a trend.'], blocks=[
    Q('Complete the table.', Table(['Resource', 'One advantage', 'One disadvantage'], [
        ['coal', Ans('cheap and gives power all the time'), Ans('releases lots of CO₂ and smoke; will run out')],
        ['solar', Ans('free, clean sunlight'), Ans('no power at night; needs batteries')],
        ['wind', Ans('clean and renewable'), Ans('only works when it is windy')],
        ['hydro', Ans('clean and reliable'), Ans('dams flood land and move people')]], widths=['16%', '42%', '42%']), marks=8),
    Q('The share of the world\'s electricity from **wind and solar together** is shown below. Plot it as a line graph.',
      Table(['Year', '2021', '2022', '2023', '2024'], [['Wind + solar (%)', '10.3', '11.9', '13.4', '15.0']], center=True),
      Graph(['2021', '2022', '2023', '2024'], [10.3, 11.9, 13.4, 15.0], 'Share (%)', 'Year', ymin=8, ymax=16, step=1, kind='line', width=110, height=60), marks=3),
    Q('Describe the trend. Predict the share in 2025 if it continues.', Lines(2, 'It rises by about 1.5 percentage points each year; about 16.5% in 2025.'), marks=2),
])

investigate = Sheet('investigate', 'Does the number of blades change a wind turbine\'s speed?', level=2, goals=['Plan a fair test with a model.', 'Analyse results.'], blocks=[
    P('Class 5A made paper wind turbines with 2, 3, 4, 6 and 8 blades. They put each one 1 m in front of the same fan and counted the turns in 30 seconds (three tries each).'),
    Q('Complete the table: work out the mean (average) of the three tries.', Table(['Blades', 'Try 1', 'Try 2', 'Try 3', 'Mean turns'], [
        ['2', '38', '40', '42', Ans('40')], ['3', '54', '57', '57', Ans('56')], ['4', '62', '60', '61', Ans('61')], ['6', '52', '55', '55', Ans('54')], ['8', '45', '43', '44', Ans('44')]], center=True), marks=5),
    Q('Draw a bar chart of the mean turns.', Graph(['2', '3', '4', '6', '8'], [40, 56, 61, 54, 44], 'Mean turns in 30 s', 'Number of blades', ymax=70, step=10, width=110, height=58), marks=3),
    Q('Describe the pattern. Which number of blades worked best?', Lines(2, 'Speed rose up to 4 blades, then fell. 4 blades worked best: more blades catch more wind, but too many add weight and block the air.'), marks=2),
    Q('Why did they do three tries and find the mean?', Lines(2, 'To make the results more reliable and reduce the effect of odd results.'), marks=1),
    P('*Data: example results for practice.*', 'small muted'),
])

case = Sheet('case', 'Bangladesh\'s energy future', level=3, goals=['Use data to evaluate a big decision.', 'Consider different viewpoints.'], blocks=[
    Links('Science', 'Geography', 'Economics', 'Citizenship'),
    Case('Bangladesh needs much more electricity for its homes, factories and growing cities. In 2023 it made over 85% of its electricity from fossil fuels: mostly natural gas, plus oil and a fast-growing amount of coal. Its own gas fields are running down, so it must buy more fuel from other countries, which is expensive.',
         'At the same time, Bangladesh is one of the countries hit hardest by climate change. Many people say the country should build much more **solar** (on rooftops, over ponds and on unused land) and **wind** power along the coast, while saving energy. Others worry that solar needs a lot of land in a crowded country and does not work at night without batteries.',
         source='Based on Power Grid Company of Bangladesh data (2023) and public debate about Bangladesh\'s energy plans.'),
    Q('Why must Bangladesh buy more fuel from other countries?', Lines(2, 'Its own natural gas fields are running down, but it needs more electricity.'), marks=2),
    Q('Complete the viewpoints.', Table(['Person', 'What might they want? Why?'], [
        ['a coastal farmer', Ans('clean energy, because climate change brings cyclones and salty water to their fields')],
        ['a factory owner', Ans('reliable, cheap power all day so the factory never stops')],
        ['a city child with asthma', Ans('less coal and oil burning, so the air is cleaner')]], widths=['30%', '70%']), marks=3),
    Q('Write a short plan (3 actions) for green energy in Bangladesh. Use evidence.', Lines(4, 'e.g. rooftop solar on schools and factories; wind farms on the coast; LED lights and efficient fans to save energy; use gas, not coal, while renewables grow.'), marks=4),
])

review = Sheet('review', 'Show what you know', level=3, goals=['Use key vocabulary.', 'Answer test-style questions.'], blocks=[
    Q('Find the words.', WordSearch(['SOLAR', 'WIND', 'HYDRO', 'COAL', 'GAS', 'BIOGAS', 'CLIMATE', 'GREEN'], size=10, seed=520)),
    Q('True or false?', TrueFalse([('Natural gas is a renewable resource.', False, 'It is a fossil fuel and will run out.'),
                                   ('Most of Bangladesh\'s electricity in 2023 came from natural gas.', True),
                                   ('Nuclear power releases a lot of carbon dioxide.', False, 'It releases almost none, but its fuel is non-renewable and its waste is dangerous.')]), marks=3),
    Q('About what share of the world\'s electricity came from fossil fuels in 2024?', MCQ(['about 20%', 'about 59%', 'about 90%'], 1), marks=1),
    Q('**Challenge.** Your school wants to cut its electricity bill and its carbon footprint. Suggest three changes and explain each.',
      Lines(4, 'Solar panels on the roof (free, clean electricity); LED bulbs (use less energy); switch off fans and lights in empty rooms (no waste).'), marks=3),
])

TOPIC = Topic(
    code='C10', strand='physical', title='Energy Resources: Renewable, Non-renewable and Green Energy', short='Energy resources',
    subtitle='Fossil fuels and renewables, climate change and energy access as global issues, and green energy, with real data',
    outcomes=[
        'distinguish between renewable and non-renewable energy sources, and give examples of each.',
        'investigate how different energy sources generate electricity.',
        'analyse data about how electricity is generated in the world and in Bangladesh.',
        'explain how burning fossil fuels contributes to climate change, and why energy is a global issue.',
        'evaluate green energy choices and ways to use energy efficiently.',
    ],
    sheets=[learn, facts, think, investigate, case, review],
    selfcheck=['sort renewable and non-renewable resources', 'read energy data and charts', 'explain why fossil fuels are a global issue', 'compare energy choices', 'plan green energy actions'],
    cover_art=art.pic_row(['solar energy', 'wind energy', 'water wave', 'factory smoke'], ['solar', 'wind', 'hydro', 'fossil fuels']),
)
