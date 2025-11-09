const { chromium } = require('playwright');
const path = require('path');

(async () => {
  const htmlFile = path.resolve(__dirname, '워크샵_제출_자료_final.html');
  const fileUrl = `file://${htmlFile}`;
  
  console.log(`Opening: ${fileUrl}`);
  
  const browser = await chromium.launch({ headless: false });
  const page = await browser.newPage();
  await page.goto(fileUrl);
  
  console.log('브라우저가 열렸습니다. 창을 닫으면 종료됩니다.');
  
  // 브라우저가 닫힐 때까지 대기
  await new Promise(() => {});
})();
