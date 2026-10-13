"""Export the picture library for the question bank (run from the repository root):
    python3 question-bank/tools/images.py
Writes question-bank/images/diagrams/<name>.svg (diagrams drawn for the InquiryMind worksheets), question-bank/images/openmoji/<name>.svg
(OpenMoji line pictures, CC BY-SA 4.0) and question-bank/images/index.json (alt text and answer keys for every diagram)."""
import json
import os
import re
import shutil
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TK = os.path.join(ROOT, 'worksheets', 'toolkit')
sys.path.insert(0, TK)
import art  # noqa: E402
import art4  # noqa: E402
import art23  # noqa: E402
import openmoji  # noqa: E402

OUT = os.path.join(ROOT, 'question-bank', 'images')


def numbered(parts):
    return '; '.join(f'{i} = {p}' for i, p in enumerate(parts, 1))


def lettered(parts):
    return '; '.join(f'{chr(65 + i)} = {p}' for i, p in enumerate(parts))


# name: (svg, alt text, key: what the numbers/letters in the picture mean, or what it shows)
DIAGRAMS = {
    # plants
    'plant-parts-labelled': (art.plant_parts(labels=art.PLANT_PARTS), 'A plant with its flower, leaf, stem, roots and fruit labelled.', 'labelled'),
    'plant-parts-numbered': (art.plant_parts(), 'A plant with five parts numbered 1 to 5.', numbered(art.PLANT_PARTS)),
    'flower-parts-numbered': (art.flower_section(), 'Cross-section of a flower with parts numbered.', numbered(art.FLOWER_PARTS)),
    'plant-life-cycle-numbered': (art.life_cycle(numbered=True), 'The life cycle of a flowering plant with stages numbered.', numbered(art.LIFE_CYCLE_STAGES)),
    'bean-seed-numbered': (art.bean_seed(), 'Inside a bean seed, parts numbered.', numbered(art.BEAN_PARTS)),
    'plant-needs': (art.plant_needs(), 'Four potted plants: healthy (light, water, warmth, air), wilted (no water), pale (no light), small (too cold).', 'healthy; no water: wilted; no light: pale; too cold: small'),
    'celery-stem': (art23.celery_stem(), 'A white flower stem standing in coloured water; the colour travels up the stem to the petals.', 'water moves up the stem'),
    # living things and bodies
    'body-numbered': (art23.body_outline(), 'Outline of a child with body parts numbered 1 to 11.', numbered(art23.BODY_PARTS)),
    'skeleton-numbered': (art.skeleton(), 'A human skeleton with bones numbered.', numbered(art.SKELETON_PARTS)),
    'arm-muscles-numbered': (art23.arm_muscles(), 'An arm showing the bone, biceps, triceps and elbow joint, numbered.', numbered(art23.ARM_PARTS)),
    'animal-cell-numbered': (art.animal_cell(), 'An animal cell with parts numbered.', numbered(art.CELL_PARTS)),
    'ear-numbered': (art.ear(), 'Cross-section of the ear with parts numbered.', numbered(art.EAR_PARTS)),
    'eye-numbered': (art.eye(), 'Cross-section of the eye with parts numbered.', numbered(art.EYE_PARTS)),
    'frog-life-cycle': (art4.cycle(art4.FROG_CYCLE), 'Life cycle of a frog: eggs (frogspawn), tadpole, froglet, adult frog.', 'eggs → tadpole → froglet → adult frog'),
    'butterfly-life-cycle': (art4.cycle(art4.BUTTERFLY_CYCLE), 'Life cycle of a butterfly: eggs, caterpillar, chrysalis, adult butterfly.', 'eggs → caterpillar (larva) → chrysalis (pupa) → adult'),
    'chicken-life-cycle': (art4.cycle(art4.CHICKEN_CYCLE), 'Life cycle of a chicken: egg, hatching, chick, adult hen.', 'egg → hatching → chick → hen'),
    'food-chain-rice-field': (art4.food_chain([('herb', 'grass'), ('cricket', 'grasshopper'), ('frog', 'frog'), ('snake', 'snake')]), 'Food chain: grass → grasshopper → frog → snake.', 'producer: grass; consumers: grasshopper, frog, snake (top predator)'),
    'food-chain-sundarbans': (art4.food_chain([('herb', 'leaves'), ('deer', 'deer'), ('tiger', 'tiger')]), 'Food chain: leaves → deer → tiger.', 'producer: leaves; herbivore: deer; carnivore: tiger'),
    'pond-ecosystem-numbered': (art4.pond_ecosystem(), 'A pond ecosystem with parts numbered.', numbered(art4.POND_PARTS)),
    'mangrove': (art4.mangrove(), 'A mangrove tree with breathing roots and prop roots in salty mud.', 'labelled: breathing roots, prop roots, salty mud, salty water'),
    # earth and space
    'day-night': (art.day_night(), 'The Sun lights one half of the spinning Earth: day on the side facing the Sun, night on the other.', 'day side faces the Sun'),
    'sun-path': (art.sun_path(), 'A stick and its shadow at morning, midday and evening as the Sun moves across the sky.', 'shadow long in morning and evening, shortest at midday'),
    'seasons-orbit': (art.seasons_orbit(), 'The tilted Earth at different places in its orbit around the Sun.', 'tilt towards the Sun = summer for that half'),
    'solar-system-numbered': (art.solar_system(numbered=True), 'The Sun and eight planets numbered 1 to 8 (not to scale).', numbered(art.PLANETS)),
    'moon-phases-numbered': (art23.moon_phases(names=False), 'Eight shapes of the Moon numbered 1 to 8.', numbered(art23.MOON_PHASES)),
    'water-cycle-numbered': (art.water_cycle(), 'The water cycle with stages numbered.', numbered(art.WATER_CYCLE)),
    'soil-layers-numbered': (art.soil_layers(), 'Layers of soil numbered from the top.', numbered(art.SOIL_LAYERS)),
    'river-landscape-numbered': (art.river_landscape(), 'A river from hills to the sea with processes numbered.', numbered(art.RIVER_PARTS)),
    'landforms-lettered': (art23.landforms(names=False), 'Six landforms lettered A to F.', lettered(art23.LANDFORMS)),
    'rocks-lettered': (art23.rock_types(names=False), 'Five kinds of rock lettered A to E.', lettered(art23.ROCKS)),
    'weather-instruments-lettered': (art4.weather_instruments(names=False), 'Five weather instruments lettered A to E.', lettered(art4.WEATHER_INSTRUMENTS)),
    'cloud-types-lettered': (art4.cloud_types(names=False), 'Cloud types lettered.', lettered([c for c, _ in art4.CLOUD_TYPES])),
    'cyclone-numbered': (art4.cyclone_diagram(), 'A tropical cyclone seen from above with parts numbered.', numbered(art4.CYCLONE_PARTS)),
    'sea-breeze': (art4.sea_breeze(), 'Daytime sea breeze: warm air rises over the land and cooler air moves in from the sea.', 'convection current'),
    # materials and heat
    'states-particles': (art.states_particles(), 'Particles in a solid (packed in rows), a liquid (touching but jumbled) and a gas (far apart).', 'solid, liquid, gas'),
    'filtering-numbered': (art.filtering(), 'Filtering muddy water with a funnel and filter paper, parts numbered.', numbered(art.FILTER_PARTS)),
    'heat-transfer-lettered': (art23.heat_transfer(names=False), 'Three pictures lettered A, B, C: a spoon in a hot drink, a pot of water over a flame with arrows, and the Sun warming a hand.', lettered(art23.HEAT_WAYS)),
    'heat-transfer-labelled': (art23.heat_transfer(), 'Conduction, convection and radiation shown with examples.', 'labelled'),
    'vacuum-flask-numbered': (art.vacuum_flask(), 'A vacuum flask cut in half with parts numbered.', numbered(art.FLASK_PARTS)),
    'insulation-cups': (art.insulation_cups(), 'Four cups of hot water: one with no cover and others wrapped in newspaper, wool and foil.', 'no cover, newspaper, wool, foil'),
    'thermometers-abc': (art23.thermometers((5, 25, 40)), 'Three thermometers A, B and C.', 'A = 5 °C; B = 25 °C; C = 40 °C'),
    'thermometers-def': (art23.thermometers((12, 37, 48)), 'Three thermometers A, B and C.', 'A = 12 °C; B = 37 °C; C = 48 °C'),
    # forces and machines
    'lever-numbered': (art.lever(), 'A see-saw lever with three parts numbered.', numbered(art.LEVER_PARTS)),
    'simple-machines-lettered': (art.simple_machines(names=False), 'Six simple machines lettered A to F.', lettered(art.MACHINE_NAMES)),
    'pulley-gears': (art23.pulley_gears(), 'A pulley lifting a bucket from a well, and two gears turning.', 'pull down, bucket goes up; gears turn each other'),
    'ramp-lift': (art23.ramp_lift(), 'Lifting a box straight up needs 10 N; pulling it up a ramp needs 4 N.', 'ramp: longer path, less force'),
    'tubewell-numbered': (art.tubewell(), 'A hand tubewell with parts numbered.', numbered(art.TUBEWELL_PARTS)),
    'forcemeter-4n': (art4.forcemeter(4), 'A forcemeter reading 4 newtons.', '4 N'),
    'forcemeter-7n': (art4.forcemeter(7), 'A forcemeter reading 7 newtons.', '7 N'),
    'flight-forces': (art4.flight_forces(), 'An aeroplane with four force arrows: lift, weight, thrust and drag.', 'lift up, weight down, thrust forward, drag backward'),
    'force-arrows': (art4.force_arrows(), 'Force arrows on everyday objects.', 'pushes, pulls, friction, gravity, upthrust, air resistance'),
    # electricity and magnets
    'circuit-closed': (art4.circuit(('cell', 'lamp', 'switch'), closed=True), 'A circuit with a cell, a lamp and a closed switch.', 'complete circuit: lamp on'),
    'circuit-open': (art4.circuit(('cell', 'lamp', 'switch'), closed=False), 'A circuit with a cell, a lamp and an open switch.', 'gap in the circuit: lamp off'),
    'circuit-buzzer': (art4.circuit(('cell', 'buzzer', 'switch'), closed=True), 'A circuit with a cell, a buzzer and a closed switch.', 'complete circuit: buzzer sounds'),
    'circuit-motor': (art4.circuit(('cell', 'motor', 'switch'), closed=True), 'A circuit with a cell, a motor and a closed switch.', 'complete circuit: motor turns'),
    'circuit-two-lamps': (art4.circuit(('cell', 'lamp', 'lamp'), closed=True), 'A circuit with one cell and two lamps.', 'complete circuit: both lamps on (dimmer than one lamp)'),
    'circuit-symbols': (art4.circuit_symbols(), 'Circuit symbols with names.', 'labelled'),
    'current-model': (art23.current_model(), 'A model of current: tiny particles flow all the way round a circuit.', 'particles flow round the complete loop'),
    'bar-magnets': (art4.bar_magnets(), 'Bar magnets: N facing S attract; N facing N repel.', 'unlike poles attract, like poles repel'),
    # sound and light
    'sound-waves-lettered': (art.sound_waves(numbered=True), 'Four sound wave pictures lettered A to D.', 'A = loud, low pitch; B = quiet, low pitch; C = loud, high pitch; D = quiet, high pitch'),
    'decibel-scale': (art23.decibel_scale(), 'A loudness scale in decibels with everyday sounds; above 85 dB can damage hearing.', 'leaves 20 dB; birds 40; talking 60; traffic 80; loud music 100; plane 120'),
    'bottle-pitch-lettered': (art23.bottle_pitch(numbered=True), 'Four bottles A to D with more and more water, tapped with a spoon.', 'A least water = highest note; D most water = lowest note'),
    'instruments': (art.instruments(), 'A dhol (drum), an ektara (string) and a bansuri (flute).', 'drum skin, string, air vibrate'),
    'string-phone': (art.string_phone(), 'A string telephone: vibrations travel along a tight string.', 'sound travels through the string'),
    'shadow-setup': (art.shadow_setup(), 'A torch, an object and its shadow on a screen.', 'object blocks light, shadow forms behind it'),
    'reflection': (art.reflection(), 'Light reflecting off a mirror.', 'angle in = angle out'),
    'periscope': (art.periscope(), 'A periscope with two mirrors.', 'light reflects twice'),
    'optical-devices-lettered': (art.optical_devices(names=False), 'Five optical devices lettered A to E.', lettered(art.OPTICAL_DEVICES)),
}


def fname(name):
    return re.sub(r'[^a-z0-9]+', '-', name.lower()).strip('-')


def main():
    d = os.path.join(OUT, 'diagrams')
    os.makedirs(d, exist_ok=True)
    index = {'diagrams': {}, 'openmoji': {}}
    for name, (svg, alt, key) in DIAGRAMS.items():
        svg = svg.replace('style="width:100%;height:auto" ', '', 1)
        with open(os.path.join(d, name + '.svg'), 'w', encoding='utf-8') as f:
            f.write(svg)
        index['diagrams'][name] = {'src': f'diagrams/{name}.svg', 'alt': alt, 'key': key}
    o = os.path.join(OUT, 'openmoji')
    os.makedirs(o, exist_ok=True)
    for name, hexcode in sorted(openmoji.NAMES.items()):
        src = openmoji.path(hexcode)
        if os.path.exists(src):
            shutil.copy(src, os.path.join(o, fname(name) + '.svg'))
            index['openmoji'][name] = f'openmoji/{fname(name)}.svg'
    with open(os.path.join(OUT, 'index.json'), 'w', encoding='utf-8') as f:
        json.dump(index, f, indent=1, ensure_ascii=False)
    print(len(index['diagrams']), 'diagrams,', len(index['openmoji']), 'OpenMoji pictures')


if __name__ == '__main__':
    main()
