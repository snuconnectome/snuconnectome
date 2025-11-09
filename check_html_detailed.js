const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');

(async () => {
  const htmlFile = path.resolve(__dirname, '워크샵_제출_자료_final.html');
  const fileUrl = `file://${htmlFile}`;
  
  console.log('='.repeat(60));
  console.log('HTML 파일 상세 검증');
  console.log('='.repeat(60));
  console.log(`\n파일 경로: ${htmlFile}`);
  console.log(`URL: ${fileUrl}\n`);
  
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage();
  await page.goto(fileUrl);
  
  // 페이지 제목 확인
  const title = await page.title();
  console.log(`✓ 페이지 제목: ${title}`);
  
  // H1 헤더 확인
  const h1 = await page.$('h1');
  if (h1) {
    const h1Text = await h1.textContent();
    console.log(`✓ H1: ${h1Text.trim()}`);
  }
  
  // 표 개수 확인
  const tables = await page.$$('table');
  console.log(`\n✓ 발견된 표 개수: ${tables.length}`);
  
  // 첫 번째 표 (일정표) 확인
  if (tables.length > 0) {
    console.log('\n--- 일정표 확인 ---');
    const firstTable = tables[0];
    const firstTableRows = await firstTable.$$('tr');
    console.log(`  행 개수: ${firstTableRows.length}`);
    
    // 헤더 확인
    const headers = await firstTable.$$('th');
    if (headers.length > 0) {
      const headerTexts = await Promise.all(headers.map(h => h.textContent()));
      console.log(`  헤더: ${headerTexts.join(' | ')}`);
    }
    
    // 첫 번째 데이터 행 확인
    if (firstTableRows.length > 1) {
      const firstDataRow = firstTableRows[1];
      const cells = await firstDataRow.$$('td');
      const cellTexts = await Promise.all(cells.map(c => c.textContent()));
      console.log(`  첫 번째 행: ${cellTexts.join(' | ')}`);
    }
  }
  
  // 두 번째 표 (교수 명단) 확인
  if (tables.length > 1) {
    console.log('\n--- 참여 교수 명단 확인 ---');
    const secondTable = tables[1];
    const secondTableRows = await secondTable.$$('tr');
    console.log(`  행 개수: ${secondTableRows.length}`);
    
    // 헤더 확인
    const headers = await secondTable.$$('th');
    if (headers.length > 0) {
      const headerTexts = await Promise.all(headers.map(h => h.textContent()));
      console.log(`  헤더: ${headerTexts.join(' | ')}`);
    }
    
    // 첫 번째 교수 정보 확인
    if (secondTableRows.length > 1) {
      const firstDataRow = secondTableRows[1];
      const cells = await firstDataRow.$$('td');
      const cellTexts = await Promise.all(cells.map(c => c.textContent()));
      console.log(`  첫 번째 교수: ${cellTexts.join(' | ')}`);
    }
  }
  
  // 마크다운 문법 확인 (**, ### 등이 남아있는지)
  const bodyText = await page.textContent('body');
  const hasMarkdown = bodyText.includes('**') || bodyText.includes('###') || bodyText.includes('```');
  console.log(`\n✓ 마크다운 문법 남아있음: ${hasMarkdown ? '❌ 있음' : '✓ 없음'}`);
  
  // 섹션 확인
  const h2Elements = await page.$$('h2');
  console.log(`\n✓ H2 섹션 개수: ${h2Elements.length}`);
  if (h2Elements.length > 0) {
    const h2Texts = await Promise.all(h2Elements.slice(0, 5).map(h => h.textContent()));
    console.log(`  주요 섹션: ${h2Texts.join(', ')}`);
  }
  
  // 스크린샷 저장
  await page.screenshot({ 
    path: 'html_preview.png',
    fullPage: true 
  });
  console.log('\n✓ 전체 페이지 스크린샷 저장: html_preview.png');
  
  // PDF 생성
  await page.pdf({ 
    path: '워크샵_제출_자료_playwright.pdf',
    format: 'A4',
    printBackground: true,
    margin: { top: '20mm', right: '15mm', bottom: '20mm', left: '15mm' }
  });
  console.log('✓ PDF 생성 완료: 워크샵_제출_자료_playwright.pdf');
  
  await browser.close();
  
  console.log('\n' + '='.repeat(60));
  console.log('검증 완료!');
  console.log('='.repeat(60));
})();
