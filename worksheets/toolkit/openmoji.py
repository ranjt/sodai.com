"""OpenMoji pictures (https://openmoji.org, CC BY-SA 4.0): black line-art emoji used as illustrations.

The pictures listed in NAMES are kept in toolkit/openmoji/<HEX>.svg (black outline versions, about 1 MB).
Add a picture: put its name and hex code in NAMES (codes: https://openmoji.org/library/), then run
    python3 worksheets/toolkit/openmoji.py fetch
which downloads any missing files from the pinned OpenMoji release on GitHub.
Credit (printed on every pack cover that uses them): "Pictures from OpenMoji (openmoji.org), CC BY-SA 4.0".
"""
import os
import re
import sys
import urllib.request

RELEASE = '17.0.0'
HERE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'openmoji')
URL = 'https://raw.githubusercontent.com/hfg-gmuend/openmoji/{release}/black/svg/{hex}.svg'

NAMES = {
    # mammals
    'tiger': '1F405', 'tiger face': '1F42F', 'leopard': '1F406', 'monkey': '1F412', 'elephant': '1F418', 'deer': '1F98C',
    'water buffalo': '1F403', 'cow': '1F404', 'goat': '1F410', 'dog': '1F415', 'cat': '1F408', 'rabbit': '1F407',
    'rat': '1F400', 'mouse': '1F401', 'bat': '1F987', 'otter': '1F9A6', 'dolphin': '1F42C', 'whale': '1F40B',
    'hedgehog': '1F994', 'chipmunk': '1F43F', 'fox': '1F98A', 'bear': '1F43B', 'horse': '1F40E', 'camel': '1F42A',
    'polar bear': '1F43B-200D-2744-FE0F', 'giraffe': '1F992', 'rhinoceros': '1F98F', 'mammoth': '1F9A3',
    # birds
    'bird': '1F426', 'eagle': '1F985', 'owl': '1F989', 'duck': '1F986', 'swan': '1F9A2', 'chicken': '1F414',
    'rooster': '1F413', 'hatching chick': '1F423', 'baby chick': '1F424', 'peacock': '1F99A', 'parrot': '1F99C',
    'penguin': '1F427', 'dove': '1F54A', 'pigeon': 'E009', 'flamingo': '1F9A9', 'feather': '1FAB6', 'nest with eggs': '1FABA',
    'dodo': '1F9A4', 'goose': '1FABF', 'wing': '1FABD',
    # reptiles, amphibians, fish
    'crocodile': '1F40A', 'turtle': '1F422', 'lizard': '1F98E', 'snake': '1F40D', 'frog': '1F438', 'fish': '1F41F',
    'tropical fish': '1F420', 'shark': '1F988', 'blowfish': '1F421', 'goldfish': 'E000', 'T-Rex': '1F996',
    # invertebrates
    'octopus': '1F419', 'crab': '1F980', 'shrimp': '1F990', 'snail': '1F40C', 'butterfly': '1F98B', 'caterpillar': '1F41B',
    'ant': '1F41C', 'honeybee': '1F41D', 'beetle': '1FAB2', 'lady beetle': '1F41E', 'cricket': '1F997', 'spider': '1F577',
    'spider web': '1F578', 'scorpion': '1F982', 'mosquito': '1F99F', 'fly': '1FAB0', 'worm': '1FAB1', 'jellyfish': '1FABC',
    'spiral shell': '1F41A', 'coral': '1FAB8', 'microbe': '1F9A0', 'cockroach': '1FAB3',
    # plants and fungi
    'lotus': '1FAB7', 'sunflower': '1F33B', 'hibiscus': '1F33A', 'rose': '1F339', 'tulip': '1F337', 'blossom': '1F33C',
    'seedling': '1F331', 'potted plant': '1FAB4', 'evergreen tree': '1F332', 'deciduous tree': '1F333', 'palm tree': '1F334',
    'cactus': '1F335', 'rice plant': '1F33E', 'herb': '1F33F', 'shamrock': '2618', 'four leaf clover': '1F340',
    'maple leaf': '1F341', 'fallen leaf': '1F342', 'leaves in wind': '1F343', 'mushroom': '1F344', 'wilted flower': '1F940',
    'leafless tree': '1FABE', 'wood': '1FAB5', 'rock': '1FAA8',
    # food
    'mango': '1F96D', 'banana': '1F34C', 'coconut': '1F965', 'apple': '1F34E', 'carrot': '1F955', 'potato': '1F954',
    'cooked rice': '1F35A', 'egg': '1F95A', 'bread': '1F35E', 'milk': '1F95B', 'honey pot': '1F36F', 'salt': '1F9C2',
    'ice cube': '1F9CA', 'cup of tea': '2615', 'water glass': '1F95B', 'peanuts': '1F95C',
    # weather and Earth
    'sun': '2600', 'cloud': '2601', 'sun behind cloud': '26C5', 'rain cloud': '1F327', 'thunder cloud': '26C8',
    'lightning': '26A1', 'snowflake': '2744', 'tornado': '1F32A', 'fog': '1F32B', 'wind face': '1F32C', 'cyclone': '1F300',
    'rainbow': '1F308', 'umbrella with rain': '2614', 'droplet': '1F4A7', 'water wave': '1F30A', 'thermometer': '1F321',
    'globe asia': '1F30F', 'mountain': '26F0', 'volcano': '1F30B', 'desert': '1F3DC', 'island': '1F3DD', 'national park': '1F3DE',
    'flood': 'E09F', 'earthquake': 'E09C', 'shelter': 'E098', 'fire': '1F525', 'moon': '1F319', 'star': '2B50', 'comet': '2604',
    'iceberg': 'E2C0', 'sea level rise': 'E2D0', 'oil spill': 'E2CB', 'factory smoke': 'E2CC', 'car exhaust': 'E2CF',
    'solar energy': 'E2CD', 'wind energy': 'E2D1', 'reusable bag': 'E2D2', 'nuclear power plant': 'E2D4',
    # people, places and things
    'house': '1F3E0', 'factory': '1F3ED', 'school': '1F3EB', 'hospital': '1F3E5', 'farmer': '1F9D1-200D-1F33E',
    'scientist': '1F9D1-200D-1F52C', 'teacher': '1F9D1-200D-1F3EB', 'student': '1F9D1-200D-1F393', 'person running': '1F3C3',
    'person cycling': '1F6B4', 'person swimming': '1F3CA', 'bone': '1F9B4', 'leg': '1F9B5', 'flexed biceps': '1F4AA',
    'brain': '1F9E0', 'ear': '1F442', 'eye': '1F441', 'nose': '1F443', 'tooth': '1F9B7', 'footprints': '1F463',
    'pill': '1F48A', 'syringe': '1F489', 'recycling': '267B', 'wastebasket': '1F5D1',
    'plastic bottle': 'E0CC', 'glass bottle': 'E0CB', 'newspaper': '1F4F0', 'package': '1F4E6', 'tin can': '1F96B',
    'axe': 'E347', 'saw': 'E348', 'spade': 'E345', 'wheelbarrow': 'E344', 'watering can': '1FAA3',
    # transport and flight
    'bicycle': '1F6B2', 'auto rickshaw': '1F6FA', 'bus': '1F68C', 'car': '1F697', 'ship': '1F6A2', 'sailboat': '26F5',
    'canoe': '1F6F6', 'speedboat': '1F6A4', 'airplane': '2708', 'helicopter': '1F681', 'parachute': '1FA82', 'kite': '1FA81',
    'rocket': '1F680', 'hot air balloon': '1F388', 'balloon': '1F388', 'flying disc': '1F94F', 'skateboard': '1F6F9',
    # science, energy, electricity, sound and light
    'light bulb': '1F4A1', 'battery': '1F50B', 'low battery': '1FAAB', 'electric plug': '1F50C', 'outlet': 'E144',
    'magnet': '1F9F2', 'compass': '1F9ED', 'high voltage': '26A1', 'gear': '2699', 'balance scale': '2696',
    'test tube': '1F9EA', 'microscope': '1F52C', 'telescope': '1F52D', 'magnifying glass': '1F50D', 'stopwatch': '23F1',
    'ruler': '1F4CF', 'abacus': '1F9EE', 'candle': '1F56F', 'flashlight': '1F526', 'mirror': '1FA9E',
    'bell': '1F514', 'drum': '1F941', 'guitar': '1F3B8', 'violin': '1F3BB', 'trumpet': '1F3BA', 'flute': '1FA88',
    'loudspeaker': '1F50A', 'speaker muted': '1F507', 'headphone': '1F3A7', 'microphone': '1F3A4', 'radio': '1F4FB',
    'mobile phone': '1F4F1', 'television': '1F4FA', 'laptop': '1F4BB', 'fan': '1FAAD', 'satellite': '1F6F0',
    'satellite antenna': '1F4E1', 'clipboard': '1F4CB', 'bar chart': '1F4CA', 'chart increasing': '1F4C8', 'notebook': '1F4D3',
    'pencil': '270F', 'atom': '269B', 'dna': '1F9EC', 'petri dish': '1F9EB', 'alembic': '2697', 'hammer': '1F528',
    'wrench': '1F527', 'nut and bolt': '1F529', 'scissors': '2702', 'paperclip': '1F4CE', 'key': '1F511', 'coin': '1FA99',
    'soap': '1F9FC', 'sponge': '1F9FD', 'basket': '1F9FA', 'thread': '1F9F5', 'yarn': '1F9F6', 'teddy bear': '1F9F8',
    'umbrella': '2602', 'shirt': '1F455', 'glasses': '1F453', 'warning': '26A0', 'no entry': '26D4', 'check mark': '2714',
    # added for Grades 2 and 3
    'baby': '1F476', 'child': '1F9D2', 'adult': '1F9D1', 'older person': '1F9D3', 'person standing': '1F9CD', 'tongue': '1F445',
    'hand': '270B', 'mouth': '1F444', 'shopping cart': '1F6D2', 'football': '26BD', 'playground slide': '1F6DD', 'teapot': '1FAD6',
    'ice cream': '1F366', 'chocolate': '1F36B', 'sandwich': '1F96A', 'broccoli': '1F966', 'cake': '1F370', 'lollipop': '1F36D',
    'french fries': '1F35F', 'burger': '1F354', 'bed': '1F6CF', 'toothbrush': '1FAA5', 'snowman': '2603', 'camping': '1F3D5',
    'beach': '1F3D6', 'city': '1F3D9', 'full moon': '1F315', 'new moon': '1F311', 'first quarter moon': '1F313',
    'last quarter moon': '1F317', 'waxing gibbous moon': '1F314', 'waning gibbous moon': '1F316', 'waxing crescent moon': '1F312',
    'waning crescent moon': '1F318', 'ringed planet': '1FA90', 'shooting star': '1F320', 'milky way': '1F30C', 'hook': '1FA9D',
    'ladder': '1FA9C', 'frying egg': '1F373', 'pot of food': '1F372', 'fire extinguisher': '1F9EF', 'hot drink': '2615',
    'lifting weights': '1F3CB', 'sleeping face': '1F634', 'medical mask face': '1F637', 'sunrise': '1F305', 'night with stars': '1F303',
    'spoon': '1F944', 'fork and knife': '1F374', 'lemon': '1F34B', 'grapes': '1F347', 'watermelon': '1F349', 'tomato': '1F345',
    'leafy green': '1F96C', 'bucket': '1FAA3', 'rowing boat': '1F6A3', 'wheel': '1F6DE', 'family': '1F46A', 'sweat droplets': '1F4A6',
    'musical notes': '1F3B6', 'long drum': '1FA98', 'harp': '1FA89', 'tractor': '1F69C', 'construction': '1F6A7',
    'building construction': '1F3D7', 'hut': '1F6D6', 'tent': '26FA', 'snow-capped mountain': '1F3D4', 'gem stone': '1F48E',
    'ring': '1F48D', 'chair': '1FA91', 'broom': '1F9F9', 'sun behind small cloud': '1F324', 'pig': '1F416', 'collision': '1F4A5',
    'mechanical arm': '1F9BE', 'pinching hand': '1F90F',
    'gloves': '1F9E4', 'scarf': '1F9E3', 'coat': '1F9E5', 'socks': '1F9E6', 'brick': '1F9F1', 'window': '1FA9F', 'door': '1F6AA',
    'screwdriver': '1FA9B', 'firefighter': '1F9D1-200D-1F692', 'telephone': '260E', 'saxophone': '1F3B7', 'maracas': '1FA87',
    'ear with hearing aid': '1F9BB', 'bowl with spoon': '1F963', 'kitchen knife': '1F52A', 'safety pin': '1F9F7',
    'manual wheelchair': '1F9BD', 'motorway': '1F6E3', 'flag': '1F3F3', 'clock': '1F570', 'sewing needle': '1FAA1',
}

_cache = {}


def path(hexcode):
    return os.path.join(HERE, f'{hexcode}.svg')


def inner(name):
    """The drawing (without the outer <svg>) for a NAMES key or hex code, in a 72 x 72 box."""
    hexcode = NAMES.get(name, name)
    if hexcode not in _cache:
        p = path(hexcode)
        if not os.path.exists(p):
            raise FileNotFoundError(f'OpenMoji {name!r} ({hexcode}) missing: run python3 worksheets/toolkit/openmoji.py fetch')
        s = open(p, encoding='utf-8').read()
        s = re.sub(r'<\?xml.*?\?>|<!--.*?-->', '', s, flags=re.S)
        s = re.sub(r'^.*?<svg[^>]*>|</svg>\s*$', '', s.strip(), flags=re.S)
        s = re.sub(r'\sid="[^"]*"', '', s)
        _cache[hexcode] = re.sub(r'\s+', ' ', s).strip()
    return _cache[hexcode]


def fetch(names=None):
    os.makedirs(HERE, exist_ok=True)
    wanted = sorted({NAMES.get(n, n) for n in (names or NAMES)})
    got = 0
    for h in wanted:
        if os.path.exists(path(h)):
            continue
        try:
            data = urllib.request.urlopen(URL.format(release=RELEASE, hex=h), timeout=30).read()
        except Exception as e:  # noqa: BLE001
            print('missing', h, e)
            continue
        open(path(h), 'wb').write(data)
        got += 1
    print(f'fetched {got}; {len(os.listdir(HERE))} pictures in {HERE}')


if __name__ == '__main__':
    if sys.argv[1:2] == ['fetch']:
        fetch(sys.argv[2:] or None)
    else:
        print(__doc__)
