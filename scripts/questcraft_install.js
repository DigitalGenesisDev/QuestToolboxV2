import Bluebird from 'bluebird';
import Adb from '@devicefarmer/adbkit';

const client = Adb.createClient();
const apk = 'vendor/app.apk';
// curl https://api.github.com/repos/user/reponame/releases/latest | grep "browser_download_url" | grep -Eo 'https://[^\"]*' | xargs wget
const test = async () => {
    try {
        const devices = await client.listDevices();
        await Bluebird.map(devices, (device) => client.install(device.id, apk));
        console.log(`Installed ${apk} on all connected devices`);
    } catch (err) {
        console.error('Something went wrong:', err.stack);
    }
};