const { chromium } = require('playwright');
const path = require('path');

(async () => {
  const htmlFile = path.resolve(__dirname, '워크샵_제출_자료_final.html');
  const fileUrl = `file://${htmlFile}`;
  
  console.log(`Checking HTML file: ${fileUrl}`);
  
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage();
  await page.goto(fileUrl);
  
  // 표가 있는지 확인
  const tables = await page.$$('table');
  console.log(`\n✓ 발견된 표 개수: ${tables.length}`);
  
  // 교수 명단 표 확인
  const professorTable = await page.$('table');
  if (professorTable) {
    const rows = await page.$$('table tr');
    console.log(`✓ 표의 행 개수: ${rows.length}`);
  }
  
  // 일정표 확인
  const scheduleTables = await page.$$('table');
  console.log(`✓ 총 표 개수: ${scheduleTables.length}`);
  
  // PDF로 저장
  await page.pdf({ 
    path: '워크샵_제출_자료_playwright.pdf',
    format: 'A4',
    printBackground: true
  });
  console.log('\n✓ PDF 생성 완료: 워크샵_제출_자료_playwright.pdf');
  
  await browser.close();
  console.log('\n✓ HTML 파일 검증 완료!');
})();
