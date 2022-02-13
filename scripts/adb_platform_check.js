const platform = os.platform()
const document = require('jquery')
const sysInfoBtn = document.getElementById('sys-info')

sysInfoBtn.addEventListener('click', function () {
    const message = 'Your system ADB platform is set to: ${platform}'
    document.getElementById('got-sys-info').innerHTML = message
    console.log(message)
 })
