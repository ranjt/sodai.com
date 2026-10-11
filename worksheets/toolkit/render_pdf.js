// Print HTML worksheet packs to A4 PDF with headless Chromium.
// Usage: node render_pdf.js jobs.json   where jobs.json = [{ "html": "...", "pdf": "..." }, ...]
const { chromium } = require('playwright-core');
const fs = require('fs');

(async () => {
  const jobs = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
  const browser = await chromium.launch(process.env.CHROME_PATH ? { executablePath: process.env.CHROME_PATH } : {});
  const queue = [...jobs];
  let failed = 0;
  await Promise.all([1, 2, 3].map(async () => {
    while (queue.length) {
      const job = queue.shift();
      const page = await browser.newPage();
      const errors = [];
      page.on('pageerror', e => errors.push(e.message));
      page.on('requestfailed', r => errors.push('missing ' + r.url()));
      await page.goto('file://' + job.html, { waitUntil: 'load' });
      await page.evaluate(() => document.fonts.ready);
      await page.emulateMedia({ media: 'print' });
      await page.pdf({ path: job.pdf, format: 'A4', printBackground: true, preferCSSPageSize: true });
      await page.close();
      if (errors.length) { failed++; console.log('PROBLEM', job.html, errors.slice(0, 3)); }
      else console.log('pdf', job.pdf.split('/').slice(-1)[0]);
    }
  }));
  await browser.close();
  process.exit(failed ? 1 : 0);
})();
