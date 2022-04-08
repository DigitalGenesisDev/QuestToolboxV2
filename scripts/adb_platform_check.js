const os = require('os');
const platform = os.platform()
const sysInfoBtn = document.getElementById('got-sys-info')

sysInfoBtn.addEventListener('click', function () {
    const message = `Your system ADB platform is set to: ${platform}`
    document.getElementById('got-sys-info').innerText = message
    console.log(message)
 })
