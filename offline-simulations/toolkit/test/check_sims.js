// Test built simulations in headless Chromium and (optionally) make catalog thumbnails.
//
// Usage (from the repository root):
//   npm install --prefix offline-simulations/toolkit/test playwright-core
//   node offline-simulations/toolkit/test/check_sims.js [--thumbnails] [--fuzz=15] FOLDER [FOLDER ...]
//   e.g. node offline-simulations/toolkit/test/check_sims.js --thumbnails simulations science-simulations
//
// For each FOLDER/sims/<id>.html:
//   1. opens the first screen (?screens=1) and checks for JavaScript errors
//      (with --thumbnails, saves a 600x394 screenshot to FOLDER/thumbnails/<id>.png)
//   2. runs PhET's ?fuzz mode (random clicks/drags on every screen) for N seconds (default 15; --fuzz=0 skips)
// Browser: set CHROME_PATH to a Chromium/Chrome executable, or run `npx playwright install chromium` once.
// Prints OK/ERR per sim and exits with code 1 if any sim had errors.

const { chromium } = require('playwright-core');
const fs = require('fs');
const path = require('path');

const args = process.argv.slice(2);
const thumbnails = args.includes('--thumbnails');
const fuzzArg = args.find(a => a.startsWith('--fuzz='));
const fuzzSeconds = fuzzArg ? Number(fuzzArg.split('=')[1]) : 15;
const folders = args.filter(a => !a.startsWith('--'));
if (!folders.length) {
  console.log('usage: node check_sims.js [--thumbnails] [--fuzz=15] FOLDER [FOLDER ...]');
  process.exit(2);
}

(async () => {
  const browser = await chromium.launch(process.env.CHROME_PATH ? { executablePath: process.env.CHROME_PATH } : {});
  const jobs = folders.flatMap(folder => fs.readdirSync(path.join(folder, 'sims'))
    .filter(f => f.endsWith('.html')).sort()
    .map(f => ({ folder, id: f.replace(/\.html$/, ''), url: 'file://' + path.resolve(folder, 'sims', f) })));
  let failures = 0;

  async function check(job) {
    const errors = [];
    // 1200x788 layout rendered at half resolution gives a sharp 600x394 thumbnail
    const page = await browser.newPage({ viewport: { width: 1200, height: 788 }, deviceScaleFactor: 0.5 });
    page.on('pageerror', e => errors.push('screen 1: ' + e.message.slice(0, 160)));
    await page.goto(job.url + '?screens=1');
    await page.waitForTimeout(6000);
    if (thumbnails) {
      fs.mkdirSync(path.join(job.folder, 'thumbnails'), { recursive: true });
      await page.screenshot({ path: path.join(job.folder, 'thumbnails', job.id + '.png') });
    }
    await page.close();
    if (fuzzSeconds > 0) {
      const fuzz = await browser.newPage({ viewport: { width: 1024, height: 640 } });
      fuzz.on('pageerror', e => errors.push('fuzz: ' + e.message.slice(0, 160)));
      await fuzz.goto(job.url + '?fuzz');
      await fuzz.waitForTimeout(fuzzSeconds * 1000);
      await fuzz.close();
    }
    if (errors.length) failures++;
    console.log((errors.length ? 'ERR ' : 'OK  ') + path.join(job.folder, job.id) +
                (errors.length ? '  ' + JSON.stringify([...new Set(errors)].slice(0, 3)) : ''));
  }

  const queue = [...jobs];
  await Promise.all([1, 2, 3].map(async () => { while (queue.length) await check(queue.shift()); }));
  await browser.close();
  console.log(`${jobs.length - failures}/${jobs.length} OK`);
  process.exit(failures ? 1 : 0);
})();
