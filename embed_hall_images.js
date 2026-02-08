const fs = require('fs');
const path = require('path');

// Convert image to base64
function imageToBase64(imagePath) {
    const imageBuffer = fs.readFileSync(imagePath);
    const base64 = imageBuffer.toString('base64');
    const ext = path.extname(imagePath).toLowerCase();
    const mime = ['.jpg', '.jpeg'].includes(ext) ? 'image/jpeg' : 'image/png';
    return `data:${mime};base64,${base64}`;
}

// Image paths to embed
const images = {
    'before and after pictures/inside_hall_before.jpeg': null,
    'before and after pictures/inside_hall_after.png': null,
    'before and after pictures/outside_hall_before.jpeg': null,
    'before and after pictures/outside_hall_after.png': null
};

console.log('Embedding hall images in quotes.html...');

// Encode all images
for (const imgPath of Object.keys(images)) {
    if (fs.existsSync(imgPath)) {
        console.log(`  Encoding: ${imgPath}`);
        images[imgPath] = imageToBase64(imgPath);
    } else {
        console.log(`  ERROR: Not found: ${imgPath}`);
    }
}

// Read quotes.html
let content = fs.readFileSync('quotes.html', 'utf8');

// Replace image paths with base64
for (const [original, base64Data] of Object.entries(images)) {
    if (base64Data) {
        content = content.replace(`src="${original}"`, `src="${base64Data}"`);
    }
}

// Write updated quotes.html
fs.writeFileSync('quotes.html', content, 'utf8');

console.log('✓ Hall images embedded in quotes.html!');
console.log('  The file is now standalone and portable.');
