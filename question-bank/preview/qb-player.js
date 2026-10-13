/* InquiryMind question-bank player: renders and marks one question of any type. No libraries.
 *
 *   const c = QBPlayer.render(question, element, {imageBase: '../images/', simBase: '/science-simulations/sims/',
 *                                                  teacher: false, onResult: r => ...});
 *   c.check()      -> marks the learner's answer, shows feedback, returns the result (also sent to onResult)
 *   c.reveal()     -> shows the right answer (teacher view)
 *   QBPlayer.score(question, response) -> {correct, score (0..1), needsReview, parts}
 *
 * Response formats (what score() expects):
 *   mcq: option index · multi: list of option indexes · truefalse: true/false · fill: list of strings (one per ___)
 *   match: list, for each pair i the index of the right-hand item the learner joined to left i (-1 = none)
 *   sort: list, for each item i the category name chosen (null = none) · order: list of original step indexes in
 *   the learner's order · short: the learner's text
 */
(function () {
  'use strict';

  const ENDINGS = ['', 's', 'es', 'ed', 'd', 'ing', 'er', 'ers', 'ly', 'y', 'ies'];

  function normalise(s) {
    return String(s == null ? '' : s).normalize('NFKD').replace(/[̀-ͯ]/g, '').toLowerCase()
      .replace(/[‘’]/g, "'").replace(/[^a-z0-9°%'\s.-]/g, ' ').replace(/[.'-]+(\s|$)/g, ' ')
      .replace(/\s+/g, ' ').trim().replace(/^(a|an|the) /, '');
  }

  function choiceText(c) {
    if (c == null) return '';
    if (typeof c === 'string') return c;
    return c.text || (c.image || '').replace(/^.*\//, '').replace(/\.svg$/, '').replace(/-/g, ' ');
  }

  /* keyword found if a word starts with it and only a common ending follows ("ear" matches "ears", not "earth") */
  function hasKeyword(text, kw) {
    const words = normalise(text).split(' ');
    const k = normalise(kw).split(' ');
    for (let i = 0; i + k.length <= words.length; i++) {
      let ok = true;
      for (let j = 0; j < k.length && ok; j++) {
        const w = words[i + j], p = k[j];
        ok = w.startsWith(p) && ENDINGS.includes(w.slice(p.length));
      }
      if (ok) return true;
    }
    return false;
  }

  function score(q, r) {
    const res = { correct: false, score: 0, needsReview: false, parts: [] };
    const sameSet = (a, b) => a.length === b.length && a.every(x => b.includes(x));
    switch (q.type) {
      case 'mcq':
      case 'truefalse':
        res.correct = r === q.answer;
        break;
      case 'multi': {
        const picked = Array.isArray(r) ? r : [];
        res.parts = q.options.map((_, i) => picked.includes(i) === q.answer.includes(i));
        res.correct = sameSet(picked, q.answer);
        const hits = picked.filter(i => q.answer.includes(i)).length;
        res.score = Math.max(0, (hits - (picked.length - hits)) / q.answer.length);
        break;
      }
      case 'fill':
        res.parts = q.blanks.map((acc, i) => acc.some(a => normalise(a) === normalise((r || [])[i])));
        break;
      case 'match':
        res.parts = q.pairs.map((_, i) => (r || [])[i] === i);
        break;
      case 'sort':
        res.parts = q.items.map((it, i) => (r || [])[i] === it[1]);
        break;
      case 'order':
        res.parts = q.sequence.map((_, i) => (r || [])[i] === i);
        break;
      case 'short': {
        const found = q.keywords.map(group => group.some(k => hasKeyword(r || '', k)));
        const need = q.min_keywords || 1;
        const n = found.filter(Boolean).length;
        res.parts = found;
        res.correct = n >= need;
        res.score = Math.min(1, n / need);
        res.needsReview = true;
        return res;
      }
    }
    if (res.parts.length && q.type !== 'multi') {
      res.score = res.parts.filter(Boolean).length / res.parts.length;
      res.correct = res.parts.every(Boolean);
    }
    if (q.type === 'mcq' || q.type === 'truefalse') res.score = res.correct ? 1 : 0;
    return res;
  }

  /* the right answer in words (feedback and teacher view) */
  function answerText(q) {
    switch (q.type) {
      case 'mcq': return choiceText(q.options[q.answer]);
      case 'multi': return q.answer.map(i => choiceText(q.options[i])).join(' · ');
      case 'truefalse': return q.answer ? 'True' : 'False';
      case 'fill': return q.blanks.map(b => b[0]).join(' · ');
      case 'match': return q.pairs.map(p => choiceText(p[0]) + ' → ' + choiceText(p[1])).join(' · ');
      case 'sort': return q.categories.map(c => c + ': ' + q.items.filter(it => it[1] === c).map(it => choiceText(it[0])).join(', ')).join(' | ');
      case 'order': return q.sequence.map((s, i) => (i + 1) + '. ' + choiceText(s)).join('  ');
      case 'short': return q.model_answer;
    }
    return '';
  }

  /* ---------- small helpers ---------- */
  function esc(s) {
    return String(s).replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
  }
  function rich(s) { return esc(s).replace(/\*\*(.+?)\*\*/g, '<b>$1</b>'); }
  function el(tag, cls, html) {
    const e = document.createElement(tag);
    if (cls) e.className = cls;
    if (html != null) e.innerHTML = html;
    return e;
  }
  function seeded(id) {
    let h = 2166136261;
    for (const ch of id) h = Math.imul(h ^ ch.charCodeAt(0), 16777619);
    return function () {
      h += 0x6D2B79F5;
      let t = h;
      t = Math.imul(t ^ (t >>> 15), t | 1);
      t ^= t + Math.imul(t ^ (t >>> 7), t | 61);
      return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
    };
  }
  /* a shuffled list of 0..n-1 that is never the original order (n > 1) */
  function shuffled(n, id) {
    const rnd = seeded(id), a = [...Array(n).keys()];
    for (let tries = 0; tries < 6; tries++) {
      for (let i = n - 1; i > 0; i--) {
        const j = Math.floor(rnd() * (i + 1));
        [a[i], a[j]] = [a[j], a[i]];
      }
      if (n < 2 || a.some((x, i) => x !== i)) break;
    }
    if (n > 1 && a.every((x, i) => x === i)) a.push(a.shift());
    return a;
  }

  function choiceHTML(c, base) {
    if (typeof c === 'string') return '<span>' + rich(c) + '</span>';
    let h = '';
    if (c.image) h += '<img src="' + esc(base + c.image) + '" alt="' + esc(c.text || choiceText(c)) + '" loading="lazy">';
    if (c.text) h += '<span>' + rich(c.text) + '</span>';
    return h;
  }

  function speak(q) {
    if (!('speechSynthesis' in window)) return;
    const parts = [q.stem.replace(/\*\*/g, '').replace(/___/g, ' blank ')];
    if (q.options) parts.push(q.options.map(choiceText).join('. '));
    if (q.type === 'truefalse') parts.push('True, or false?');
    speechSynthesis.cancel();
    const u = new SpeechSynthesisUtterance(parts.join('. '));
    u.lang = 'en-GB';
    u.rate = 0.9;
    speechSynthesis.speak(u);
  }

  /* ---------- render ---------- */
  function render(q, root, opts) {
    opts = Object.assign({ imageBase: '../images/', simBase: '../../science-simulations/sims/', teacher: false }, opts || {});
    const B = opts.imageBase;
    root.innerHTML = '';
    root.classList.add('qbp', 'qbp-type-' + q.type);
    const state = { done: false };
    let getResponse = () => null, mark = () => {}, showAnswer = () => {};

    const head = el('div', 'qbp-stem');
    if (q.read_aloud) {
      const b = el('button', 'qbp-speak', '🔊');
      b.type = 'button';
      b.title = 'Read aloud';
      b.setAttribute('aria-label', 'Read the question aloud');
      b.onclick = () => speak(q);
      head.appendChild(b);
    }
    if (q.type !== 'fill') head.insertAdjacentHTML('beforeend', rich(q.stem));
    root.appendChild(head);
    if (q.sim) {
      const s = el('div', 'qbp-sim');
      s.innerHTML = '<b>Simulation:</b> ' + rich(q.sim.task) +
        ' <a target="_blank" rel="noopener" href="' + esc(opts.simBase + q.sim.id + '.html') + '">Open the simulation ↗</a>';
      root.appendChild(s);
    }
    if (q.image) {
      const f = el('figure', 'qbp-figure');
      f.innerHTML = '<img src="' + esc(B + q.image) + '" alt="' + esc(q.image_alt || '') + '">';
      root.appendChild(f);
    }
    const body = el('div', 'qbp-body');
    root.appendChild(body);

    if (q.type === 'mcq' || q.type === 'multi' || q.type === 'truefalse') {
      const opts2 = q.type === 'truefalse' ? ['True', 'False'] : q.options;
      const pics = opts2.some(o => o && o.image);
      const box = el('div', 'qbp-options' + (pics ? ' qbp-pics' : ''));
      const picked = new Set();
      const btns = opts2.map((o, i) => {
        const b = el('button', 'qbp-opt', choiceHTML(o, B));
        b.type = 'button';
        b.setAttribute('aria-pressed', 'false');
        b.onclick = () => {
          if (state.done) return;
          if (q.type !== 'multi') picked.clear();
          picked.has(i) ? picked.delete(i) : picked.add(i);
          btns.forEach((x, j) => x.setAttribute('aria-pressed', String(picked.has(j))));
        };
        box.appendChild(b);
        return b;
      });
      body.appendChild(box);
      if (q.type === 'multi' && !/choose all/i.test(q.stem)) body.appendChild(el('p', 'qbp-note', 'Choose all that are right.'));
      const right = i => q.type === 'truefalse' ? (i === 0) === q.answer : q.type === 'multi' ? q.answer.includes(i) : i === q.answer;
      getResponse = () => q.type === 'multi' ? [...picked].sort() : q.type === 'truefalse' ? (picked.size ? picked.has(0) : null) : (picked.size ? [...picked][0] : null);
      mark = () => btns.forEach((b, i) => {
        if (right(i)) b.classList.add('ok');
        else if (picked.has(i)) b.classList.add('bad');
      });
      showAnswer = () => btns.forEach((b, i) => right(i) && b.classList.add('ok'));
    } else if (q.type === 'fill') {
      const parts = q.stem.split('___');
      const inputs = [];
      parts.forEach((p, i) => {
        head.insertAdjacentHTML('beforeend', rich(p));
        if (i < parts.length - 1) {
          const inp = el('input', 'qbp-blank');
          inp.setAttribute('aria-label', 'blank ' + (i + 1));
          inp.size = Math.max(6, Math.min(18, (q.blanks[i][0] || '').length + 2));
          inputs.push(inp);
          head.appendChild(inp);
        }
      });
      let focus = 0;
      inputs.forEach((inp, i) => inp.addEventListener('focus', () => { focus = i; }));
      if (q.bank) {
        const bank = el('div', 'qbp-bank');
        shuffled(q.bank.length, q.id).forEach(k => {
          const b = el('button', 'qbp-chip', esc(q.bank[k]));
          b.type = 'button';
          b.onclick = () => {
            if (state.done) return;
            const target = inputs[focus] && !inputs[focus].value ? inputs[focus] : inputs.find(x => !x.value) || inputs[focus];
            target.value = q.bank[k];
            focus = Math.min(inputs.indexOf(target) + 1, inputs.length - 1);
          };
          bank.appendChild(b);
        });
        body.appendChild(el('p', 'qbp-note', 'Tap a word, or type it.'));
        body.appendChild(bank);
      }
      getResponse = () => inputs.map(x => x.value);
      mark = r => inputs.forEach((x, i) => { x.classList.add(r.parts[i] ? 'ok' : 'bad'); x.readOnly = true; });
      showAnswer = () => inputs.forEach((x, i) => { x.value = q.blanks[i][0]; x.classList.add('ok'); });
    } else if (q.type === 'match') {
      const order = shuffled(q.pairs.length, q.id);
      const link = q.pairs.map(() => -1);
      let sel = -1;
      const grid = el('div', 'qbp-match');
      const L = el('div', 'qbp-col'), R = el('div', 'qbp-col');
      grid.append(L, R);
      body.appendChild(el('p', 'qbp-note', 'Tap an item on the left, then its partner on the right.'));
      body.appendChild(grid);
      const lb = q.pairs.map((p, i) => {
        const b = el('button', 'qbp-item', choiceHTML(p[0], B));
        b.type = 'button';
        b.onclick = () => { if (!state.done) { sel = i; paint(); } };
        L.appendChild(b);
        return b;
      });
      const rb = order.map(k => {
        const b = el('button', 'qbp-item', choiceHTML(q.pairs[k][1], B));
        b.type = 'button';
        b.onclick = () => {
          if (state.done || sel < 0) return;
          for (let i = 0; i < link.length; i++) if (link[i] === k) link[i] = -1;
          link[sel] = k;
          sel = link.indexOf(-1);
          paint();
        };
        R.appendChild(b);
        return b;
      });
      const paint = () => {
        lb.forEach((b, i) => {
          b.classList.toggle('sel', i === sel);
          b.dataset.tag = link[i] >= 0 ? String(i + 1) : '';
        });
        rb.forEach((b, j) => {
          const i = link.indexOf(order[j]);
          b.dataset.tag = i >= 0 ? String(i + 1) : '';
        });
      };
      getResponse = () => link.slice();
      mark = r => lb.forEach((b, i) => b.classList.add(r.parts[i] ? 'ok' : 'bad'));
      showAnswer = () => { q.pairs.forEach((_, i) => { link[i] = i; }); sel = -1; paint(); lb.forEach(b => b.classList.add('ok')); };
      paint();
    } else if (q.type === 'sort') {
      const place = q.items.map(() => null);
      let sel = -1;
      const tray = el('div', 'qbp-tray');
      const bins = el('div', 'qbp-bins');
      body.appendChild(el('p', 'qbp-note', 'Tap an item, then tap the group it belongs to.'));
      body.append(tray, bins);
      const order = shuffled(q.items.length, q.id);
      const items = q.items.map((it, i) => {
        const b = el('button', 'qbp-item', choiceHTML(it[0], B));
        b.type = 'button';
        b.onclick = () => { if (!state.done) { sel = sel === i ? -1 : i; paint(); } };
        return b;
      });
      const binEls = q.categories.map(c => {
        const d = el('div', 'qbp-bin');
        const h = el('button', 'qbp-binhead', esc(c));
        h.type = 'button';
        h.onclick = () => { if (!state.done && sel >= 0) { place[sel] = c; sel = -1; paint(); } };
        d.append(h, el('div', 'qbp-binbody'));
        bins.appendChild(d);
        return d;
      });
      const paint = () => {
        order.forEach(i => {
          const target = place[i] == null ? tray : binEls[q.categories.indexOf(place[i])].lastChild;
          target.appendChild(items[i]);
          items[i].classList.toggle('sel', i === sel);
        });
        tray.classList.toggle('empty', place.every(p => p != null));
      };
      getResponse = () => place.slice();
      mark = r => items.forEach((b, i) => b.classList.add(r.parts[i] ? 'ok' : 'bad'));
      showAnswer = () => { q.items.forEach((it, i) => { place[i] = it[1]; }); sel = -1; paint(); items.forEach(b => b.classList.add('ok')); };
      paint();
    } else if (q.type === 'order') {
      const seq = shuffled(q.sequence.length, q.id);
      const list = el('ol', 'qbp-order');
      body.appendChild(el('p', 'qbp-note', 'Use the arrows to put the steps in the right order.'));
      body.appendChild(list);
      const paint = () => {
        list.innerHTML = '';
        seq.forEach((k, pos) => {
          const li = el('li', 'qbp-step');
          li.innerHTML = '<span class="qbp-steptext">' + choiceHTML(q.sequence[k], B) + '</span>';
          const up = el('button', 'qbp-move', '↑'), down = el('button', 'qbp-move', '↓');
          up.type = down.type = 'button';
          up.setAttribute('aria-label', 'move up');
          down.setAttribute('aria-label', 'move down');
          up.disabled = pos === 0 || state.done;
          down.disabled = pos === seq.length - 1 || state.done;
          up.onclick = () => { [seq[pos - 1], seq[pos]] = [seq[pos], seq[pos - 1]]; paint(); };
          down.onclick = () => { [seq[pos + 1], seq[pos]] = [seq[pos], seq[pos + 1]]; paint(); };
          li.append(up, down);
          list.appendChild(li);
        });
      };
      getResponse = () => seq.slice();
      mark = () => { paint(); [...list.children].forEach((li, pos) => li.classList.add(seq[pos] === pos ? 'ok' : 'bad')); };
      showAnswer = () => { seq.sort((a, b) => a - b); paint(); [...list.children].forEach(li => li.classList.add('ok')); };
      paint();
    } else if (q.type === 'short') {
      const ta = el('textarea', 'qbp-text');
      ta.rows = 3;
      ta.placeholder = 'Write your answer in a sentence.';
      body.appendChild(ta);
      getResponse = () => ta.value;
      mark = () => { ta.readOnly = true; };
      showAnswer = () => {};
    }

    if (q.hint) {
      const h = el('details', 'qbp-hint', '<summary>Hint</summary>' + rich(q.hint));
      body.appendChild(h);
    }
    const bar = el('div', 'qbp-bar');
    const btn = el('button', 'qbp-check', 'Check');
    btn.type = 'button';
    bar.appendChild(btn);
    root.appendChild(bar);
    const fb = el('div', 'qbp-feedback');
    root.appendChild(fb);

    function feedback(r, teacher) {
      fb.className = 'qbp-feedback show ' + (teacher ? 'key' : r.correct ? 'right' : 'wrong');
      let h = teacher ? '<b>Answer:</b> ' + rich(answerText(q)) : r.correct ? '<b>✓ Well done!</b>' :
        '<b>Not quite.</b> The answer: ' + rich(answerText(q));
      if (q.type === 'short') {
        h = teacher ? '<b>Model answer:</b> ' + rich(q.model_answer) :
          '<b>' + (r.correct ? '✓ Your answer has the key ideas.' : 'Compare with the model answer.') + '</b> ' + rich(q.model_answer);
        if (teacher) h += '<br><small>Auto-marking looks for ' + (q.min_keywords || 1) + ' of: ' +
          q.keywords.map(g => esc(g.join(' / '))).join(' · ') + '</small>';
      }
      h += '<p>' + rich(q.explanation) + '</p>';
      fb.innerHTML = h;
    }

    const api = {
      getResponse: () => getResponse(),
      check() {
        if (state.done) return null;
        const resp = getResponse();
        const empty = resp == null || resp === '' || (Array.isArray(resp) && (resp.length === 0 || resp.every(x => x == null || x === '' || x === -1)));
        if (empty) {
          fb.className = 'qbp-feedback show wrong';
          fb.innerHTML = 'Answer first, then press Check.';
          return null;
        }
        const r = score(q, resp);
        state.done = true;
        mark(r);
        feedback(r, false);
        btn.disabled = true;
        if (opts.onResult) opts.onResult(r, q, resp);
        return r;
      },
      reveal() {
        state.done = true;
        showAnswer();
        feedback(null, true);
        btn.disabled = true;
      },
    };
    btn.onclick = () => api.check();
    if (opts.teacher) api.reveal();
    return api;
  }

  window.QBPlayer = { render, score, answerText, normalise, hasKeyword, choiceText };
})();
