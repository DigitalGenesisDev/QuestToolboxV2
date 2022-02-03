const {app, BrowserWindow} = require('electron')
const url = require('url')
const path = require('path')
const os = require('os')
const platform = os.platform()
const document = ('browserfy')
var unique = require('uniq');
const browserify = require('browserify')
//const sysInfoBtn = document.getElementById('sys-info')
var data = [1, 2, 2, 3, 4, 5, 5, 5, 6];

console.log(unique(data));

let win

function createWindow() {
   win = new BrowserWindow({width: 800, height: 600})
   win.loadURL(url.format ({
      pathname: path.join(__dirname, 'index.html'),
      protocol: 'file:',
      slashes: true
   }))
}

/*sysInfoBtn.addEventListener('click', function () {
      const message = 'Your system ADB platform is set to: ${platform}'
      document.getElementById('got-sys-info').innerHTML = message
   })*/

app.on('ready', createWindow)