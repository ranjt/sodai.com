"""
Build the InquiryMind Visible Thinking Routine (VTR) organisers: one simple, printable A4 landscape page per thinking
routine, for teachers to download and use with any picture, object, story or topic, plus the download page.

Usage (from the repository root):
  python3 worksheets/toolkit/routines.py           # every routine: HTML + PDF + previews + zip + download page
  python3 worksheets/toolkit/routines.py R01 R09   # only these routines (the download page still lists all)
  python3 worksheets/toolkit/routines.py --no-pdf  # HTML only (fast preview)
Output: worksheets/thinking-routines/ (index.html, pdf/, print/, previews/, downloads/, assets/)

The routines were developed by Project Zero (Harvard Graduate School of Education). Every organiser here is an original
InquiryMind design (layout, wording, icons) and credits Project Zero in its footer.
"""
import os
import shutil
import subprocess
import sys
import zipfile

TOOLKIT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, TOOLKIT)
import ws  # noqa: E402
from build import WS, IM_WS, REPO, TAGLINE, MISSION, copy_assets, render_pdfs  # noqa: E402
import rt_icons  # noqa: E402

OUT = os.path.join(WS, 'thinking-routines')
GROUPS = {
    'explore': ('Look closely and get curious', 'zoom-in', 'Start a unit or a lesson: notice details, share what you already know and ask questions.'),
    'deeper': ('Dig deeper', 'search', 'Reason with evidence, look from different points of view and explore how things work.'),
    'reflect': ('Sum up and reflect', 'bulb', 'Pull ideas together, capture the big idea and notice how your thinking has changed.'),
}


class Part:
    """One section of an organiser.
    icon: rt_icons name; word: big heading; prompt: short question; body: None (blank space), ('lines', n),
    ('numbered', n), ('sub', [(big, label), ...]) or ('draw', caption); key: a letter or label shown in the badge."""
    def __init__(self, icon, word, prompt='', body=None, key=None):
        self.icon, self.word, self.prompt, self.body, self.key = icon, word, prompt, body, key


class Routine:
    def __init__(self, code, name, group, about, parts, layout='columns', focus='Our picture, object or topic:',
                 title=None, widths=None, arrows=False, bottom=None, steps=None, center=None, young=False):
        self.code, self.name, self.group, self.about, self.parts, self.layout = code, name, group, about, parts, layout
        self.focus, self.widths, self.arrows, self.bottom, self.steps, self.center = focus, widths, arrows, bottom, steps, center
        self.young = young
        self.title = title or name.replace(', ', ' · ')
        self.slug = f'{code.lower()}-' + ''.join(c if c.isalnum() else '-' for c in name.lower()).strip('-')
        while '--' in self.slug:
            self.slug = self.slug.replace('--', '-')


P = Part
SUB_321 = ('sub', [('3', 'words or ideas'), ('2', 'questions'), ('1', 'comparison: "It is like…"')])
ROUTINES = [
    # ------------------------------------------------------------------ look closely and get curious
    Routine('R01', 'See, Think, Wonder', 'explore', 'Look closely, explain what might be going on, then ask questions.', [
        P('see', 'I see', 'What do I notice? Only what I can really see.'),
        P('think', 'I think', 'What might be going on? What makes me say that?'),
        P('wonder', 'I wonder', 'What questions do I have now?')], young=True),
    Routine('R02', 'See, Feel, Think, Wonder', 'explore', 'Notice details, name feelings, explain and wonder.', [
        P('see', 'I see', 'What do I notice?'),
        P('heart', 'I feel', 'How does it make me feel?'),
        P('think', 'I think', 'What might be going on?'),
        P('wonder', 'I wonder', 'What questions do I have?')], young=True),
    Routine('R03', 'Think, Puzzle, Explore', 'explore', 'Share what you already know, what puzzles you and how to find out.', [
        P('think', 'I think I know…', 'What do I already know about this?'),
        P('puzzle', 'It puzzles me…', 'What questions or puzzles do I have?'),
        P('compass', 'I can explore…', 'How could I find out more?')], focus='Our topic:', young=True),
    Routine('R04', 'Zoom In', 'explore', 'Look at a picture revealed bit by bit and update your ideas each time.', [
        P('zoom1', 'Look 1', 'What do I see? What do I think it is?'),
        P('zoom2', 'Look 2', 'What new things do I see? Has my idea changed?'),
        P('zoom3', 'Look 3', 'What else do I see? What do I think now?'),
        P('zoom4', 'The whole picture', 'What is it? What surprised me?')], focus='Our hidden picture:', arrows=True, young=True),
    Routine('R05', 'Looking: Ten Times Two', 'explore', 'Look for 30 seconds and list 10 things, then look again and list 10 more.', [
        P('see', 'First look', 'Look for 30 seconds. Write 10 words or phrases about what I see.', ('numbered', 10)),
        P('zoom-in', 'Look again', 'Look once more. Add 10 new words or phrases.', ('numbered', 10))], young=True),
    Routine('R06', 'Chalk Talk', 'explore', 'A silent conversation on paper around a big question.', [
        P('pencil', 'Write', 'Write an idea or a question.'),
        P('messages', 'Reply', 'Read others\' ideas and add a comment.'),
        P('help', 'Ask', 'Ask a question about an idea.'),
        P('link', 'Connect', 'Draw lines to join ideas that go together.')],
        layout='map', focus='', center='Our big question:', title='Chalk Talk'),
    Routine('R07', 'Creative Question Starts', 'explore', 'Use question starters to ask many interesting questions.', [
        P(None, 'Why…?'), P(None, 'What if…?'), P(None, 'How would it be different if…?'), P(None, 'What would happen if…?'),
        P(None, 'Suppose that…'), P(None, 'What is the purpose of…?'), P(None, 'How might…?'), P(None, 'What would change if…?')],
        layout='nine', focus='', center='Our topic:'),
    Routine('R08', 'Question Sorts', 'explore', 'Sort your questions to choose the best ones to investigate.', [
        P('book-2', 'Find out more', 'Questions I really want to answer, but need books, experts or the internet.'),
        P('rocket', 'Start here!', 'Questions I really want to answer and can investigate myself.'),
        P('hourglass', 'Save for later', 'Questions I am less curious about and are hard to test.'),
        P('list-check', 'Quick check', 'Questions I am less curious about but can check easily.')],
        layout='quad', focus='Our topic:', center=('I really want to know', 'We can investigate it ourselves')),
    Routine('R09', 'Compass Points', 'explore', 'Look at an idea or plan from four directions before deciding.', [
        P('search', 'Need to know', 'What else do I need to know or find out?', key='N'),
        P('mood-happy', 'Excited', 'What excites me about this idea? What is good about it?', key='E'),
        P('flag', 'Stance or suggestion', 'What do I think now? What do I suggest?', key='S'),
        P('alert-triangle', 'Worrisome', 'What worries me about it? What could go wrong?', key='W')],
        layout='compass', focus='The idea, plan or proposal:'),
    Routine('R10', '3-2-1 Bridge', 'explore', 'Capture your first ideas, learn more, then build a bridge to your new ideas.', [
        P('brain', 'Before', 'My first ideas about the topic.', SUB_321),
        P('building-bridge', 'Bridge', 'How has my thinking changed? What new ideas did I get?'),
        P('think', 'After', 'My ideas after learning more.', SUB_321)], focus='Our topic:', widths=['1fr', '.8fr', '1fr'], arrows=True),
    Routine('R11', 'Think, Pair, Share', 'explore', 'Think on your own, talk with a partner, then share with the class.', [
        P('think', 'Think', 'What do I think? Note my idea here.'),
        P('users', 'Pair', 'What did my partner think? Where do we agree?'),
        P('speakerphone', 'Share', 'What will we share with the class?')], focus='Our question:', arrows=True, young=True),
    # ------------------------------------------------------------------ dig deeper
    Routine('R12', 'What Makes You Say That?', 'deeper', 'Give an idea and back it up with evidence.', [
        P('think', 'What\'s going on?', 'What do I think is happening here?'),
        P('see', 'What makes me say that?', 'What do I see or know that makes me think so?')], arrows=True, young=True),
    Routine('R13', 'Claim, Support, Question', 'deeper', 'Make a claim, support it with evidence and question it.', [
        P('flag', 'Claim', 'What do I think is true?'),
        P('list-check', 'Support', 'What evidence or reasons back up my claim?'),
        P('wonder', 'Question', 'What makes me unsure? What could I still ask?')], focus='Our topic or question:'),
    Routine('R14', 'Explanation Game', 'deeper', 'Name it, explain it, give reasons and think of other explanations.', [
        P('tag', 'Name it', 'What is it? What is it called?'),
        P('message-circle', 'Explain it', 'What is it doing? What is it for?'),
        P('list-check', 'Give reasons', 'Why do I think so? What is my evidence?'),
        P('arrows-split', 'Other ideas', 'What else could it be or do?')], focus='Our object, picture or event:'),
    Routine('R15', 'Circle of Viewpoints', 'deeper', 'Step into different points of view about a topic or event.', [
        P(None, 'Viewpoint') for _ in range(6)], layout='around', focus='', center='Our topic or event:',
        steps=[('users', 'List people or things that might see it differently.'), ('user', 'Choose one and step into its viewpoint.'),
               ('message-circle', '"From this viewpoint, I think… because…"'), ('help', '"A question I have from this viewpoint is…"')]),
    Routine('R16', 'Step Inside', 'deeper', 'Imagine what a person, animal or thing perceives, knows and cares about.', [
        P('see', 'Perceive', 'What can they see, hear and notice?'),
        P('brain', 'Know and believe', 'What might they know, understand or believe?'),
        P('heart', 'Care about', 'What might they care about or want?')], focus='I am stepping inside:'),
    Routine('R17', 'Tug of War', 'deeper', 'Pull reasons for both sides of a dilemma and decide where you stand.', [
        P('thumb-up', 'Pull for YES', 'Reasons that pull towards yes'), P('thumb-down', 'Pull for NO', 'Reasons that pull towards no')],
        layout='tug', focus='The dilemma: Should…', bottom=('help', 'What if…?', 'What new facts or questions could change my mind?')),
    Routine('R18', 'Red Light, Yellow Light', 'deeper', 'Spot ideas to stop and question, and ideas to slow down and check.', [
        P('red', 'Red light: stop!', 'Which ideas or claims might not be true? Why?'),
        P('yellow', 'Yellow light: slow down', 'Which ideas need checking? How could we check them?')],
        focus='What we are reading, watching or listening to:'),
    Routine('R19', 'Parts, Purposes, Complexities', 'deeper', 'Take an object or system apart: its parts, their jobs and what makes it tricky.', [
        P('settings', 'Parts', 'What are its parts or pieces?'),
        P('target-arrow', 'Purposes', 'What does each part do? What is it for?'),
        P('topology-star-3', 'Complexities', 'How do the parts work together? What is tricky about it?')], focus='Our object or system:'),
    Routine('R20', 'Parts, People, Interactions', 'deeper', 'Explore a system: its parts, the people involved and how they affect each other.', [
        P('settings', 'Parts', 'What are the parts of this system?'),
        P('users', 'People', 'Who is involved? Who makes it work, uses it or is affected?'),
        P('arrows-exchange', 'Interactions', 'How do the people and parts affect each other?')], focus='Our system:', arrows=True),
    Routine('R21', 'Think, Feel, Care', 'deeper', 'Take the perspective of someone in a situation.', [
        P('think', 'Think', 'What might this person think?'),
        P('heart', 'Feel', 'How might they feel?'),
        P('heart-handshake', 'Care', 'What might they care about most?')], focus='The person in the situation:', young=True),
    Routine('R22', 'See, Think, Me, We', 'deeper', 'Look closely, then connect the topic to yourself and to others.', [
        P('see', 'See', 'What do I notice?'),
        P('think', 'Think', 'What might be going on?'),
        P('user', 'Me', 'How does this connect to me and my life?'),
        P('users-group', 'We', 'How does it connect to other people and the world?')]),
    Routine('R23', 'The 3 Y\'s', 'deeper', 'Think about why a topic matters to me, to people around me and to the world.', [
        P('user', 'Why me?', 'Why might this matter to me?'),
        P('home', 'Why us?', 'Why might it matter to my family, class and community?'),
        P('world', 'Why the world?', 'Why might it matter to the world?')], focus='Our topic or question:', title='The 3 Y\'s'),
    Routine('R24', 'Beauty and Truth', 'deeper', 'Find what is beautiful and what is true in a story, picture or event.', [
        P('flower', 'Beauty', 'What is beautiful, inspiring or moving here?'),
        P('shield-check', 'Truth', 'What is true here? How do I know?')], focus='Our story, picture or event:',
        bottom=('sparkles', 'Beauty and truth', 'Can beauty help us see the truth? Can it ever hide the truth?')),
    Routine('R25', 'Peel the Fruit', 'deeper', 'Build understanding layer by layer, from the surface to the core.', [
        P('see', 'Skin: the surface', 'What do I notice first? What do I already know?', key='1'),
        P('puzzle', 'Flesh: going deeper', 'What puzzles me? What patterns, connections and explanations can I find? What do others think?', key='2'),
        P('heart', 'Core: the heart of it', 'What is the most important idea at the centre of it all?', key='3')],
        layout='fruit', focus='Our topic:'),
    Routine('R26', 'Unveiling Stories', 'deeper', 'Find the many stories inside a picture, object or event.', [
        P('book', 'The story', 'What is the story here?'),
        P('users', 'The human story', 'What is the story of the people involved?'),
        P('world', 'The world story', 'What does it tell us about the world?'),
        P('sparkles', 'The new story', 'What new ideas or questions does it give us?'),
        P('eye-off', 'The untold story', 'What is missing? What is not being told?')], layout='rows', focus='Our picture, object or event:'),
    # ------------------------------------------------------------------ sum up and reflect
    Routine('R27', 'I Used to Think, Now I Think', 'reflect', 'Notice how your thinking has changed.', [
        P('history', 'I used to think…', 'What did I think at the start?'),
        P('think', 'Now I think…', 'What do I think now? What changed my mind?')], focus='Our topic:', arrows=True,
        title='I used to think… Now I think…', young=True),
    Routine('R28', 'Connect, Extend, Challenge', 'reflect', 'Link new ideas to what you know, notice what stretched you and what is still hard.', [
        P('link', 'Connect', 'How does this connect to what I already know?'),
        P('arrows-maximize', 'Extend', 'What new ideas stretched my thinking?'),
        P('bolt', 'Challenge', 'What is still hard or confusing for me?')]),
    Routine('R29', 'Headlines', 'reflect', 'Capture the big idea of a lesson or topic in a newspaper headline.', [
        P('article', 'Headline', 'Sum up the most important idea in a few words.'),
        P('photo', 'Picture', 'Draw a picture for the front page.'),
        P('message-circle', 'Why this headline?', 'What makes it the most important idea?'),
        P('refresh', 'Changes', 'How has my headline changed since we started?')], layout='headline', focus='Our topic:'),
    Routine('R30', 'Colour, Symbol, Image', 'reflect', 'Show the big idea with a colour, a symbol and a picture.', [
        P('palette', 'Colour', 'Choose a colour for the big idea. Why?', ('draw', 'Colour or shade here')),
        P('star', 'Symbol', 'Draw a symbol that stands for it. Why?', ('draw', 'Draw a symbol')),
        P('photo', 'Image', 'Draw a picture that shows it. Why?', ('draw', 'Draw a picture'))], focus='Our big idea:', young=True),
    Routine('R31', 'Generate, Sort, Connect, Elaborate', 'reflect', 'Build a concept map of everything you know about a topic.', [
        P('pencil', 'Generate', 'Write words and ideas about the topic.'),
        P('category', 'Sort', 'Put the most important ideas near the centre.'),
        P('link', 'Connect', 'Draw lines between ideas and write how they connect.'),
        P('circle-plus', 'Elaborate', 'Add new ideas that build on the others.')],
        layout='map', focus='', center='Our topic:', title='Generate · Sort · Connect · Elaborate'),
    Routine('R32', 'Sentence, Phrase, Word', 'reflect', 'Pick out the sentence, phrase and word that matter most in a text.', [
        P('article', 'Sentence', 'A sentence that matters most to me.'),
        P('quote', 'Phrase', 'A phrase that caught my attention.'),
        P('letter-case', 'Word', 'A word that stood out for me.')], focus='Our text:',
        bottom=('users-group', 'Our group', 'What do our choices show? What big ideas do we notice?')),
    Routine('R33', 'The 4 C\'s', 'reflect', 'Find connections, a challenge, key concepts and changes in a text or topic.', [
        P('link', 'Connections', 'How does it connect to my life or other learning?'),
        P('bolt', 'Challenge', 'Which ideas do I want to question or argue with?'),
        P('think', 'Concepts', 'Which key ideas are worth remembering?'),
        P('refresh', 'Changes', 'What changes in thinking or actions does it suggest?')], layout='quad', focus='Our text or topic:', title='The 4 C\'s'),
    Routine('R34', 'Imagine If', 'reflect', 'Imagine ways to make an object, system or place better.', [
        P('rocket', '…it worked better', 'How could it do its job better?'),
        P('tool', '…it was easier', 'How could it be simpler or easier to use?'),
        P('heart-handshake', '…it was kinder', 'How could it be fairer or better for people and nature?'),
        P('flower', '…it was more beautiful', 'How could it look, sound or feel better?')],
        focus='Our object, system or place:', title='Imagine if…'),
]


# ---------------------------------------------------------------- pieces
def icon(name):
    return rt_icons.get(name) if name else ''


def body(b):
    if not b:
        return ''
    kind, arg = b
    if kind == 'lines':
        return '<div class="rt-lines">' + '<div class="rt-ln"></div>' * arg + '</div>'
    if kind == 'numbered':
        return '<ol class="rt-numbered">' + ''.join(f'<li><span>{i}</span></li>' for i in range(1, arg + 1)) + '</ol>'
    if kind == 'sub':
        return '<div class="rt-sub">' + ''.join(f'<div><b>{ws.esc(big)}</b><span>{ws.esc(label)}</span></div>' for big, label in arg) + '</div>'
    if kind == 'draw':
        return f'<div class="rt-draw"><span>{ws.esc(arg)}</span></div><div class="rt-because">because…</div><div class="rt-ln"></div>'
    raise ValueError(kind)


def col(p, i, arrow=False):
    return (f'<div class="rt-col"><div class="rt-col-head"><span class="rt-num">{p.key or i}</span>{icon(p.icon)}'
            f'<div class="rt-word">{ws.esc(p.word)}</div><div class="rt-prompt">{ws.esc(p.prompt)}</div></div>'
            f'<div class="rt-space">{body(p.body)}</div>{arrow_badge() if arrow else ""}</div>')


def box(p, i, cls=''):
    """A part with a compact horizontal heading (icon beside the words)."""
    return (f'<div class="rt-box {cls}"><div class="rt-box-head"><span class="rt-num">{p.key or i}</span>{icon(p.icon)}'
            f'<div><div class="rt-word">{ws.esc(p.word)}</div><div class="rt-prompt">{ws.esc(p.prompt)}</div></div></div>'
            f'<div class="rt-space">{body(p.body)}</div></div>')


def arrow_badge():
    return ('<span class="rt-arrow"><svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round" '
            'stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg></span>')


def bottom(r):
    if not r.bottom:
        return ''
    ic, word, prompt = r.bottom
    return box(P(ic, word, prompt), '★', 'rt-bottom')


def steps(items):
    return '<div class="rt-steps">' + ''.join(f'<div><span class="rt-num">{i}</span>{icon(ic)}<span>{ws.esc(t)}</span></div>'
                                              for i, (ic, t) in enumerate(items, 1)) + '</div>'


def center_bubble(label, ic, cls='rt-bubble'):
    return f'<div class="{cls}">{icon(ic)}<b>{ws.esc(label)}</b><span></span><span></span></div>'


# ---------------------------------------------------------------- layouts
def lay_columns(r):
    n = len(r.parts)
    widths = ' '.join(r.widths) if r.widths else f'repeat({n}, 1fr)'
    cols = ''.join(col(p, i, r.arrows and i < n) for i, p in enumerate(r.parts, 1))
    return f'<div class="rt-cols n{n}" style="grid-template-columns:{widths}">{cols}</div>{bottom(r)}'


def lay_rows(r):
    rows = ''.join(f'<div class="rt-row"><div class="rt-row-head"><span class="rt-num">{p.key or i}</span>{icon(p.icon)}'
                   f'<div><div class="rt-word">{ws.esc(p.word)}</div><div class="rt-prompt">{ws.esc(p.prompt)}</div></div></div>'
                   f'<div class="rt-space"></div></div>' for i, p in enumerate(r.parts, 1))
    return f'<div class="rt-rows">{rows}</div>'


def lay_compass(r):
    n, e, s, w = r.parts
    return (f'<div class="rt-compass">{box(n, "N", "c-n")}{box(w, "W", "c-w")}'
            f'<div class="c-c">{rt_icons.compass_rose()}</div>{box(e, "E", "c-e")}{box(s, "S", "c-s")}</div>')


def lay_quad(r):
    boxes = ''.join(box(p, i) for i, p in enumerate(r.parts, 1))
    if not isinstance(r.center, tuple):
        return f'<div class="rt-quad">{boxes}</div>'
    up, right = r.center
    return (f'<div class="rt-axes"><div class="ax-y"><span>{ws.esc(up)} →</span></div><div class="rt-quad">{boxes}</div>'
            f'<div></div><div class="ax-x">{ws.esc(right)} →</div></div>')


def lay_nine(r):
    cells = [f'<div class="rt-q9"><div class="rt-word">{ws.esc(p.word)}</div><div class="rt-space"></div></div>' for p in r.parts]
    cells.insert(4, center_bubble(r.center, 'wonder', 'rt-q9 rt-q9c'))
    return f'<div class="rt-nine">{"".join(cells)}</div>'


def lay_around(r):
    def vp(i):
        return (f'<div class="rt-box rt-vp"><div class="rt-vp-head"><span class="rt-num">{i}</span><b>Viewpoint:</b><span class="rt-fill"></span></div>'
                f'<div class="rt-vp-body"><div><i>I think… because…</i></div><div><i>I wonder…</i></div></div></div>')
    left = ''.join(vp(i) for i in (1, 2, 3))
    right = ''.join(vp(i) for i in (4, 5, 6))
    return (f'{steps(r.steps)}<div class="rt-around"><div class="rt-side">{left}</div>'
            f'<div class="rt-hubc">{center_bubble(r.center, "users-group", "rt-circle")}</div><div class="rt-side">{right}</div></div>')


def lay_tug(r):
    yes, no = r.parts

    def side(p, cls):
        tags = ''.join('<div class="rt-tag"><span class="rt-hole"></span></div>' for _ in range(3))
        return (f'<div class="rt-tug-side {cls}"><div class="rt-tug-head">{icon(p.icon)}<div><div class="rt-word">{ws.esc(p.word)}</div>'
                f'<div class="rt-prompt">{ws.esc(p.prompt)}</div></div></div><div class="rt-tags">{tags}</div></div>')
    return (f'<div class="rt-tug">{side(yes, "yes")}{side(no, "no")}</div>'
            f'<div class="rt-rope-wrap">{rt_icons.rope()}<div class="rt-rope-labels"><span>Strongly yes</span><span>Not sure</span>'
            f'<span>Strongly no</span></div><div class="rt-rope-note">Mark an <b>X</b> on the rope to show where you stand.</div></div>{bottom(r)}')


def lay_fruit(r):
    return (f'<div class="rt-fruit"><div class="rt-fruit-fig">{rt_icons.fruit()}<div class="rt-fruit-keys">'
            f'<span><b>1</b> skin</span><span><b>2</b> flesh</span><span><b>3</b> core</span></div></div>{lay_rows(r)}</div>')


def lay_headline(r):
    hl, pic, why, change = r.parts
    return (f'<div class="rt-news"><div class="rt-mast"><span>Edition no. ______</span><b>The Big Idea Times</b><span>Date: __________</span></div>'
            f'<div class="rt-hl"><div class="rt-hl-label">{icon(hl.icon)}<div><div class="rt-word">{ws.esc(hl.word)}</div>'
            f'<div class="rt-prompt">{ws.esc(hl.prompt)}</div></div></div><div class="rt-hl-space"></div></div>'
            f'<div class="rt-news-cols">{box(pic, 2)}<div class="rt-news-right">{box(why, 3)}{box(change, 4)}</div></div></div>')


def lay_map(r):
    chips = ''.join(f'<div class="rt-chip"><span class="rt-num">{i}</span>{icon(p.icon)}<div><b>{ws.esc(p.word)}</b>'
                    f'<span>{ws.esc(p.prompt)}</span></div></div>' for i, p in enumerate(r.parts, 1))
    return (f'<div class="rt-chips" style="--n:{len(r.parts)}">{chips}</div>'
            f'<div class="rt-mapspace">{center_bubble(r.center, "wonder" if r.code == "R06" else "topology-star-3")}</div>')


LAYOUTS = {'columns': lay_columns, 'rows': lay_rows, 'compass': lay_compass, 'quad': lay_quad, 'nine': lay_nine,
           'around': lay_around, 'tug': lay_tug, 'fruit': lay_fruit, 'headline': lay_headline, 'map': lay_map}


def page(r):
    focus = f'<div class="rt-focus">{ws.esc(r.focus)}<span></span></div>' if r.focus else '<div class="rt-gap"></div>'
    return (f'<section class="rt-page rt-{r.layout}-page"><header class="rt-top"><img class="rt-logo" src="../assets/inquirymind-logo-bw.png" alt="InquiryMind">'
            f'<h1 class="rt-title">{ws.esc(r.title)}</h1><div class="rt-name"><span>Name</span><span>Date</span></div></header>'
            f'{focus}<div class="rt-main">{LAYOUTS[r.layout](r)}</div>'
            f'<footer class="rt-foot"><span><b>InquiryMind</b> · {TAGLINE} · {MISSION}.</span>'
            f'<span>Thinking routine: Project Zero, Harvard Graduate School of Education</span></footer></section>')


def document(r):
    return (f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">'
            f'<title>{ws.esc(r.title)} | InquiryMind Visible Thinking Routines</title><link rel="stylesheet" href="../assets/styles.css">'
            f'<style>@page {{ size: A4 landscape; margin: 9mm; @bottom-left {{ content: none; }} @bottom-right {{ content: none; }} }}</style>'
            f'</head><body class="routine"><div class="doc rt-doc">{page(r)}</div></body></html>')


def previews(routines):
    """Small PNG pictures of each organiser for the download page (needs pdftoppm; skipped if missing)."""
    if not shutil.which('pdftoppm'):
        print('pdftoppm not found: previews skipped')
        return
    d = os.path.join(OUT, 'previews')
    os.makedirs(d, exist_ok=True)
    for r in routines:
        pdf = os.path.join(OUT, 'pdf', r.slug + '.pdf')
        if os.path.exists(pdf):
            subprocess.run(['pdftoppm', '-png', '-singlefile', '-scale-to', '560', pdf, os.path.join(d, r.slug)], check=True)


def make_zip(routines):
    d = os.path.join(OUT, 'downloads')
    os.makedirs(d, exist_ok=True)
    z = os.path.join(d, 'inquirymind-visible-thinking-routines.zip')
    with zipfile.ZipFile(z, 'w', zipfile.ZIP_DEFLATED) as f:
        for r in routines:
            p = os.path.join(OUT, 'pdf', r.slug + '.pdf')
            if os.path.exists(p):
                f.write(p, f'inquirymind-visible-thinking-routines/{r.slug}.pdf')
    print('zip', os.path.relpath(z, REPO), round(os.path.getsize(z) / 1e6, 1), 'MB')


def main(argv):
    only = [a.upper() for a in argv if not a.startswith('--')]
    make_pdf = '--no-pdf' not in argv
    for d in ('print', 'pdf'):
        os.makedirs(os.path.join(OUT, d), exist_ok=True)
    copy_assets(OUT)
    jobs, chosen = [], []
    for r in ROUTINES:
        if only and r.code not in only:
            continue
        p = os.path.join(OUT, 'print', r.slug + '.html')
        with open(p, 'w', encoding='utf-8') as f:
            f.write(document(r))
        jobs.append({'html': p, 'pdf': os.path.join(OUT, 'pdf', r.slug + '.pdf')})
        chosen.append(r)
        print('built', r.code, r.name)
    if make_pdf and jobs:
        render_pdfs(jobs)
        previews(chosen)
        if not only:
            make_zip(ROUTINES)
    import hub
    hub.write_routines(OUT, ROUTINES, GROUPS)
    import inventory
    inventory.write()
    if os.path.isdir(os.path.dirname(IM_WS)):
        shutil.rmtree(os.path.join(IM_WS, 'thinking-routines'), ignore_errors=True)
        shutil.copytree(OUT, os.path.join(IM_WS, 'thinking-routines'))
        print('copied to', os.path.relpath(os.path.join(IM_WS, 'thinking-routines'), REPO))


if __name__ == '__main__':
    main(sys.argv[1:])
