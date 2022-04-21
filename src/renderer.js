// Import Modules
const { execSync } = require('child_process');

// Declare DOM elements
const listDevicesBtn = document.querySelector('#list-devices-btn');

// Event listeners
listDevicesBtn.addEventListener('click', () => {
    printDevices()
})

// Button functions
function printDevices() {
    const connectedDevices = execSync('./resources/adb devices', { encoding: 'utf-8' });
    console.log(connectedDevices);
}
