const ExcelJS = require('exceljs');
const { createCanvas } = require('canvas');
const fs = require('fs');
const path = require('path');

async function convertExcelToJpg(directoryPath, outputFilePath) {
  try {
    const files = fs.readdirSync(directoryPath);

    let targetFilePath;
    for (const file of files) {
      if (file.endsWith('Results.xlsx')) {
        targetFilePath = path.join(directoryPath, file);
        break;
      }
    }

    if (!targetFilePath) {
      console.error('Excel file ending with "Result.xlsx" not found in the directory.');
      return;
    }

    const workbook = new ExcelJS.Workbook();
    await workbook.xlsx.readFile(targetFilePath);

    const worksheet = workbook.getWorksheet(1); // Assuming the first sheet in the workbook

    const rowCount = worksheet.rowCount;
    const columnCount = worksheet.columnCount;

    const cellWidth = 250; // Adjust the cell width as needed
    const cellHeight = 30; // Adjust the cell height as needed
    const canvasWidth = columnCount * cellWidth;
    const canvasHeight = rowCount * cellHeight;

    const canvas = createCanvas(canvasWidth, canvasHeight);
    const context = canvas.getContext('2d');

    // Set font properties for cell text
    const font = '12px Arial';
    context.font = font;
    context.textBaseline = 'middle';

    // Iterate over the rows and columns of the worksheet
    worksheet.eachRow((row, rowIndex) => {
      row.eachCell((cell, colIndex) => {
        const x = (colIndex - 1) * cellWidth;
        const y = (rowIndex - 1) * cellHeight;

        // Draw the cell background
        context.fillStyle = '#ffffff'; // Set the cell background color
        context.fillRect(x, y, cellWidth, cellHeight);

        // Draw the cell border
        context.strokeStyle = '#000000'; // Set the cell border color
        context.strokeRect(x, y, cellWidth, cellHeight);

        // Draw the cell text
        context.fillStyle = '#000000'; // Set the cell text color
        context.fillText(cell.value, x + cellWidth / 2, y + cellHeight / 2);
      });
    });

    // Convert the canvas to a JPG image
    const jpgStream = canvas.createJPEGStream({ quality: 0.8 });

    // Pipe the JPG image stream to a file
    const writeStream = fs.createWriteStream(outputFilePath);
    jpgStream.pipe(writeStream);

    console.log('Conversion completed successfully!');
  } catch (error) {
    console.error('Error occurred during conversion:', error);
  }
}

// Usage example
const directoryPath = 'C:\\assignment\\PageObjectModelWithCucumber\\PageObjectModel';
const outputFilePath = 'output.jpg';

convertExcelToJpg(directoryPath, outputFilePath);
