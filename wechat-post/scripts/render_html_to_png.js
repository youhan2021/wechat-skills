#!/usr/bin/env node
/**
 * wechat-post — HTML to PNG renderer using Playwright
 * Renders a wide cover image for WeChat public account articles.
 *
 * Usage:
 *   node render_html_to_png.js <input.html> <output.png> [width] [height]
 *
 * Defaults: 900x383 (WeChat article cover size)
 */

const { chromium } = require('/home/ubuntu/.hermes/hermes-agent/node_modules/playwright-core');
const path = require('path');
const fs = require('fs');

const inputHtml = process.argv[2];
const outputPng = process.argv[3];
const width = parseInt(process.argv[4]) || 900;
const height = parseInt(process.argv[5]) || 383;

if (!inputHtml || !outputPng) {
  console.error('Usage: node render_html_to_png.js <input.html> <output.png> [width] [height]');
  process.exit(1);
}

const inputPath = path.resolve(inputHtml);
if (!fs.existsSync(inputPath)) {
  console.error(`File not found: ${inputPath}`);
  process.exit(1);
}

async function main() {
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage();
  // Output must end with .png so Telegram recognizes the file type
  const finalOutput = outputPng.endsWith('.png') ? outputPng : outputPng + '.png';
  await page.setViewportSize({ width, height });

  const fileUrl = `file://${inputPath}`;
  await page.goto(fileUrl, { waitUntil: 'networkidle', timeout: 30000 });
  await page.waitForTimeout(1000);

  const canvas = await page.$('canvas');
  if (canvas) {
    await canvas.screenshot({ path: finalOutput, type: 'png' });
  } else {
    await page.screenshot({ path: finalOutput, type: 'png' });
  }

  await browser.close();
  console.log(finalOutput);
}

main().catch(err => {
  console.error('Error:', err.message);
  process.exit(1);
});
