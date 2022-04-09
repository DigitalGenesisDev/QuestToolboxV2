// Import Modules
import Bluebird from 'bluebird';
import Adb from '@devicefarmer/adbkit';
const client = Adb.createClient();
// Declare DOM elements
const testButton = document.querySelector('#testButton');

// Create Adb Client and List Devices
const devices = client.listDevices();

// Button Functions

function test() {
    console.log('Test');
}