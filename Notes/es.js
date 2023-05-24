const ExcelJS = require('exceljs');
const { toPng } = require('html-to-image');
const fs = require('fs');
const { chromium } = require('playwright');

async function convertExcelToJpg(inputFilePath, outputFilePath) {
  try {
    const workbook = new ExcelJS.Workbook();
    await workbook.xlsx.readFile(inputFilePath);

    const sheet = workbook.getWorksheet(1); // Assuming the first sheet in the workbook

    const rowCount = sheet.rowCount;
    const columnCount = sheet.columnCount;

    const cellWidth = 250; // Adjust the cell width as needed
    const cellHeight = 30; // Adjust the cell height as needed

    const html = `
      <table>
        ${Array.from({ length: rowCount }, (_, rowIndex) => `
          <tr>
            ${Array.from({ length: columnCount }, (_, colIndex) => `
              <td style="width: ${cellWidth}px; height: ${cellHeight}px; border: 1px solid #000;">
                ${sheet.getCell(rowIndex + 1, colIndex + 1).value}
              </td>
            `).join('')}
          </tr>
        `).join('')}
      </table>
    `;
    const browser = await chromium.launch({ headless: true });
    const context = await browser.newContext();
    const page = await context.newPage();

    await page.setContent(html);

    const screenshotOptions = {
      type: 'jpeg',
      quality: 80,
      fullPage: true
    };

    await page.screenshot({ path: outputFilePath, ...screenshotOptions });

    await browser.close();

    console.log('Conversion completed successfully!');
  } catch (error) {
    console.error('Error occurred during conversion:', error);
  }
}



// Usage example
const inputFilePath = 'failed_scenarios_results.xlsx';
const outputFilePath = 'output.jpg';

convertExcelToJpg(inputFilePath, outputFilePath);
