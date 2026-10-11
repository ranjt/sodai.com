// Screenshot an HTML file (dev helper): node shot.js in.html out.png [width]
const { chromium } = require('playwright-core');
(async () => {
  const [inp, out, w] = process.argv.slice(2);
  const b = await chromium.launch(process.env.CHROME_PATH ? { executablePath: process.env.CHROME_PATH } : {});
  const p = await b.newPage({ viewport: { width: +(w || 900), height: 600 } });
  const errs = []; p.on('pageerror', e => errs.push(e.message)); p.on('console', m => m.type() === 'error' && errs.push(m.text()));
  await p.goto('file://' + require('path').resolve(inp));
  await p.waitForTimeout(500);
  await p.screenshot({ path: out, fullPage: true });
  if (errs.length) console.log('ERRORS', errs);
  await b.close();
})();
