import Bluebird from 'bluebird';
import Adb from '@devicefarmer/adbkit';
function apk_install(){
const client = Adb.createClient();
// create folder inside compiled app
const fs = require('fs');
const path = require('path');
const os = require('os');
const appPath = path.join("./"/*os.tmpdir()*/, 'app');
fs.mkdirSync(appPath);
//download apk from latest release on github
var downloadReleases = require('dl-github-releases');
var options = {
    repo: 'QuestCraft',
    user: 'QuestCraftPlusPlus',
    outputdir: appPath};

downloadReleases(options)
    .then(function () {
        console.log('Downloaded latest release');
    })
    .catch(function (err) {
        console.error('Something went wrong:', err.stack);
    });
// fs.writeFileSync(path.join(appPath, 'index.html'), '<h1>Hello World</h1>');
// const apk = os.join(appPath, 'app-debug.apk');
// const test = async () => {
//     try {
//         const devices = await client.listDevices();
//         await Bluebird.map(devices, (device) => client.install(device.id, apk));
//         console.log(`Installed ${apk} on all connected devices`);
//     } catch (err) {
//         console.error('Something went wrong:', err.stack);
//     }
// };
}