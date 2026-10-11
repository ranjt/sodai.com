from build import Sheet, Topic
from ws import (P, H, Box, Vocab, Fig, Cols, Row, Case, Links, Lines, Blanks, Match, TrueFalse, MCQ, Order, Table,
                Ans, Sort, Label, Draw, Graph, WordSearch, Q, Part, Bullets)
import art

learn = Sheet('learn', 'Staying healthy and stopping disease', level=1, goals=[
    'Identify what we need for a healthy lifestyle.',
    'Explain how germs cause and spread diseases.',
    'Describe habits and choices that prevent disease.',
], blocks=[
    P('Being healthy means your body and mind work well. Doctors say that to stay healthy we need **clean surroundings, '
      'clean air and safe water, good personal hygiene, nutritious food, exercise and enough sleep**. When these needs '
      'are not met, people are more likely to become ill.', 'lead'),
    Cols(
        H('Six things a healthy body needs', 3),
        Bullets(['**Clean surroundings:** rubbish and dirty water attract flies, rats and mosquitoes that spread germs.',
                 '**Clean air and safe water:** dirty water can carry germs that cause diarrhoea, cholera and typhoid.',
                 '**Hygiene:** washing hands with soap, brushing teeth and bathing remove germs.',
                 '**Nutritious food:** a balanced diet helps the body grow and fight infection.',
                 '**Exercise:** keeps the heart, lungs, muscles and bones strong. Children need about one hour of activity a day.',
                 '**Sleep:** children aged 6 to 12 need about 9 to 12 hours of sleep to grow, learn and stay well.']),
        H('What are germs?', 3),
        P('**Germs** (microbes) are living things so small that we need a microscope to see them. Most are harmless, and some '
          'are even useful, but some cause **disease**. Germs include **bacteria**, **viruses**, **fungi** and **parasites**.'),
        H('How do diseases spread?', 3),
        Table(['Way germs spread', 'Examples of diseases'], [
            ['dirty water and food', 'diarrhoea, cholera, typhoid'], ['coughs and sneezes (air)', 'flu, colds, tuberculosis'],
            ['insect bites', 'dengue and malaria (mosquitoes)'], ['touching people or dirty surfaces', 'skin infections, eye infections']]),
        P('Diseases that spread from person to person are **infectious**. Others, such as diabetes and heart disease, do '
          'not spread. They are linked to **lifestyle**: for example, too little exercise or too much sugar and fat.'),
        H('How can we prevent disease?', 3),
        Bullets(['Wash hands with soap for **20 seconds**, especially before eating and after using the toilet.',
                 'Drink safe water: boiled, filtered or from a safe tube-well.', 'Use a clean toilet (latrine).',
                 'Cover coughs and sneezes with a tissue or your elbow.', 'Get **vaccinated**: vaccines train the body to fight a germ before it attacks.',
                 'Stop mosquitoes breeding: empty containers of standing water at least once a week.']),
        Fig(art.handwash_steps(), 'Six steps for washing your hands properly.'),
        Box('bd', P('In the 1960s and 1970s, scientists at the cholera research hospital in Dhaka (today called **icddr,b**) '
                    'helped show that a simple drink of clean water, salt and sugar could save people with severe diarrhoea. '
                    'This **oral rehydration solution (ORS)** has since saved millions of lives around the world.')),
        Box('fact', P('Bangladesh\'s vaccination programme reaches the great majority of children, protecting them from '
                      'diseases such as measles, polio and tetanus.')),
    ),
    Vocab([('hygiene', 'keeping clean to stay healthy'), ('germ', 'tiny living thing that can cause disease'),
           ('infectious disease', 'a disease that spreads from person to person'), ('vaccine', 'medicine that trains the body to fight a germ'),
           ('symptom', 'a sign of illness, such as fever or cough'), ('ORS', 'oral rehydration solution: water, salts and sugar'),
           ('risk factor', 'something that makes a disease more likely')]),
])

facts = Sheet('facts', 'Healthy habits and germs', level=1, goals=['Recall what we need to stay healthy.', 'Link diseases to how they spread.'], blocks=[
    Q('Fill in the gaps.',
      Blanks('To stay healthy we need clean air and safe [water], good [hygiene], nutritious food, [exercise] and enough '
             '[sleep]. Tiny living things that cause disease are called [germs]. A [vaccine] trains the body to fight a germ.',
             extra=['sugar', 'television']), marks=6),
    Q('Sort the diseases by how they spread.',
      Sort(['Dirty water or food', 'Air (coughs, sneezes)', 'Mosquito bites'],
           [('cholera', 'Dirty water or food'), ('typhoid', 'Dirty water or food'), ('diarrhoea', 'Dirty water or food'),
            ('flu', 'Air (coughs, sneezes)'), ('tuberculosis', 'Air (coughs, sneezes)'), ('common cold', 'Air (coughs, sneezes)'),
            ('dengue', 'Mosquito bites'), ('malaria', 'Mosquito bites')]), marks=4),
    Q('True or false?', TrueFalse([
        ('All germs cause disease.', False, 'Most germs are harmless; some are useful.'),
        ('Washing hands with soap for 20 seconds removes most germs.', True),
        ('Diabetes spreads from person to person.', False, 'Diabetes is not infectious; it is linked to lifestyle and genes.'),
        ('Children aged 10 need about 9 to 12 hours of sleep.', True),
        ('Mosquitoes breed in standing water.', True)]), marks=5),
    Q('Put the handwashing steps in order.',
      Order(['Wet your hands with clean water.', 'Add soap.', 'Rub palms, backs of hands and between fingers.',
             'Scrub nails and thumbs.', 'Rinse well.', 'Dry with a clean cloth.'], seed=12), marks=3),
])

think = Sheet('think', 'Causes, risks and choices', level=2, goals=['Link unhealthy conditions to diseases.',
                                                                   'Suggest behaviours that prevent disease.'], blocks=[
    Q('For each problem, name a disease it could cause and a way to prevent it.',
      Table(['Problem', 'Possible disease', 'How to prevent it'], [
          ['drinking pond water', Ans('diarrhoea / cholera'), Ans('drink boiled, filtered or tube-well water')],
          ['flower tubs full of old rainwater', Ans('dengue'), Ans('empty and clean the tubs every week')],
          ['eating without washing hands', Ans('diarrhoea, worms'), Ans('wash hands with soap before eating')],
          ['sitting with screens all day, eating crisps and sweets', Ans('obesity, diabetes later'), Ans('exercise every day; eat a balanced diet')]],
            widths=['34%', '26%', '40%']), marks=8),
    Q('Explain why a vaccine protects not only you but also other people.',
      Lines(3, 'If you cannot catch the disease, you cannot pass it on; when many people are vaccinated the germ cannot spread easily, protecting babies and sick people too.'), marks=2),
    Q('A child has diarrhoea and is losing a lot of water. Why is ORS more helpful than plain water?',
      Lines(2, 'ORS replaces the salts the body has lost as well as water, and the sugar helps the body absorb the salts and water.'), marks=2),
    Q('Rafi says, "I slept for 5 hours, but I\'m fine." Explain why sleep matters for children.',
      Lines(2, 'Sleep helps the body grow and repair, helps the brain learn and remember, and helps the body fight infection.'), marks=2),
])

investigate = Sheet('investigate', 'How well do we wash our hands?', level=2, goals=[
    'Plan a fair test using a model of germs.', 'Present results in a bar chart.', 'Draw a conclusion and evaluate the method.'], blocks=[
    P('Germs are too small to see, so Class 5C used a **model**: they rubbed a teaspoon of cooking oil mixed with '
      'glitter onto their hands. The glitter stood for germs. Then they washed in different ways and counted the glitter '
      'pieces left on one hand.'),
    Q('Name the variables.',
      Table(None, [['What we change', Ans('the way of washing (water only / soap 5 s / soap 20 s)')],
                   ['What we measure', Ans('the number of glitter pieces left on the hand')],
                   ['What we keep the same', Ans('amount of oil and glitter, water temperature, same hand, same person counting')]],
            widths=['32%', '68%']), marks=3),
    Q('Here are the results (average of 3 learners for each method).',
      Table(['Method', 'water only', 'soap, 5 seconds', 'soap, 20 seconds'], [['Glitter left', '64', '30', '6']], center=True),
      Graph(['water only', 'soap 5 s', 'soap 20 s'], [64, 30, 6], 'Glitter pieces left', 'Washing method', ymax=70, step=10,
            width=140, height=66), marks=4),
    Q('Write a conclusion.', Lines(2, 'Washing with soap removes more "germs" than water alone, and washing for 20 seconds works best.'), marks=2),
    Q('How is the glitter model **like** real germs, and how is it **different**?',
      Part('Like real germs:', Lines(1, 'it sticks to hands and spreads to things we touch; soap helps remove it')),
      Part('Different from real germs:', Lines(1, 'glitter is much bigger and visible; it is not alive and cannot multiply')), marks=2),
])

case = Sheet('case', 'Dengue: a city fights a mosquito', level=3, goals=[
    'Explain how a disease spreads using a life cycle.', 'Interpret data about cases over the year.',
    'Argue for actions that reduce risk.'], blocks=[
    Links('Science', 'Health', 'Maths', 'Geography', 'Citizenship'),
    Fig(art.mosquito_cycle(), 'Life cycle of the Aedes mosquito. From egg to adult takes about 7 to 10 days in warm weather.', width='85%'),
    Case('**Dengue** is a disease caused by a virus. It is spread by the bite of the female **Aedes** mosquito, which has '
         'black and white stripes and often bites in the daytime. Symptoms include a high fever, headache and pain in the '
         'muscles and joints. Most people recover with rest and fluids, but some become seriously ill and need hospital care.',
         'Aedes mosquitoes lay their eggs in small amounts of **clean, still water**: flower tubs, old tyres, plastic '
         'containers, rooftop gardens and building sites. The eggs can survive dry for months and hatch when it rains.',
         'Dengue cases in Bangladesh rise during and after the monsoon. **2023 was the worst dengue year on record in the '
         'country.** City corporations spray to kill mosquitoes and run "clean-up" campaigns, but experts say every '
         'household must help by removing breeding places.',
         source='Information: Directorate General of Health Services (DGHS) and WHO dengue fact sheets.'),
    Q('Use the life cycle to explain why emptying water containers every week stops mosquitoes.',
      Lines(3, 'Mosquitoes need water to grow from egg to larva to pupa (about 7–10 days). Emptying the water every week kills the young stages before they become adults.'), marks=2),
    Q('This chart shows example numbers of dengue patients in one city hospital each month.',
      Graph(['Jan', 'Mar', 'May', 'Jul', 'Sep', 'Nov'], [10, 15, 40, 260, 380, 150], 'Patients', 'Month', ymax=400, step=50,
            width=150, height=66, show_data_in_key=True),
      Table(['Month', 'Jan', 'Mar', 'May', 'Jul', 'Sep', 'Nov'], [['Patients', '10', '15', '40', '260', '380', '150']], center=True),
      Part('Draw the bars on the chart.'),
      Part('In which months are there most cases? Suggest why.', Lines(2, 'July to September (monsoon): lots of rain leaves water in containers where mosquitoes breed.')),
      Part('How many more patients were there in September than in May?', Lines(1, '380 − 40 = 340')), marks=5),
    Q('Who is responsible for stopping dengue? Give one job for each.',
      Table(['Who', 'What they can do'], [['each family', Ans('empty water containers weekly; use nets and repellent; cover water tanks')],
                                          ['schools', Ans('check the grounds and roof for standing water; teach learners')],
                                          ['the city', Ans('clean drains, remove rubbish, spray, inspect building sites')]],
            widths=['28%', '72%']), marks=3),
    Q('Design a short poster message (no more than 12 words) to persuade your neighbours to act.',
      Draw('30mm', 'Your message', 'e.g. "Empty it, cover it, clean it: no water, no dengue!"'), marks=2),
])

review = Sheet('review', 'Show what you know', level=3, goals=['Use key vocabulary.', 'Answer test-style questions.'], blocks=[
    Q('Find the key words.', WordSearch(['GERM', 'VIRUS', 'HYGIENE', 'SOAP', 'VACCINE', 'SLEEP', 'DENGUE', 'WATER', 'EXERCISE'], size=11, seed=31)),
    Q('Which disease is spread by mosquitoes?', MCQ(['cholera', 'dengue', 'flu', 'typhoid'], 1), marks=1),
    Q('Which is the best way to make pond water safer to drink?', MCQ(['let it stand for an hour', 'boil it', 'add sugar', 'put it in the fridge'], 1), marks=1),
    Q('Choose **one** disease you learned about. Write its cause, one risk factor and how to prevent it.',
      Table(None, [['Disease', Ans('e.g. cholera')], ['Cause', Ans('bacteria in dirty water or food')],
                   ['Risk factor', Ans('drinking unsafe water; poor sanitation')], ['Prevention', Ans('safe water, latrines, handwashing, vaccine')]],
            widths=['30%', '70%']), marks=4),
    Q('**Challenge.** Explain why a city with good drains, clean water and toilets has fewer cases of diarrhoea.',
      Lines(3, 'Diarrhoea germs spread through dirty water and human waste. Good drains, toilets and clean water keep waste away from drinking water and food.'), marks=2),
])

TOPIC = Topic(
    code='A3', strand='living', title='Staying Healthy', short='Staying healthy',
    subtitle='A healthy lifestyle, germs and disease, hygiene and prevention',
    outcomes=[
        'identify the conditions required to maintain a healthy lifestyle — clean surroundings, air and water, good personal hygiene, nutritious foods, exercise and sleep.',
        'link diseases that may result when the conditions for maintaining a healthy lifestyle are not being met.',
        'demonstrate positive personal hygiene and health care habits.',
        'discuss selected diseases in terms of their causes and risk factors, and suggest choices and behaviours which will prevent acquiring the disease.',
    ],
    sheets=[learn, facts, think, investigate, case, review],
    selfcheck=['list six conditions for a healthy lifestyle', 'explain how germs spread disease',
               'wash my hands properly and explain why', 'link diseases to their causes and risk factors',
               'explain how to stop mosquitoes spreading dengue', 'use a model and say how it is like and unlike the real thing'],
    cover_art=art.handwash_steps(),
)
