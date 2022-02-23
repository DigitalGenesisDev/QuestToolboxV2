const { apk_install } = require('./apk_install.js');
let count = 0
$('#click-counter').text(count.toString())
$('#countbtn').on('click', () => {
   $('#click-counter').text(count)
})
$('#install_qc').on('click', () => {
   console.log('clicked')
   apk_install()
})