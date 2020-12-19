var toastElList = [].slice.call(document.querySelectorAll('.toast'))
var toastList = toastElList.map(function (toastEl) {
  return new bootstrap.Toast(toastEl).show()
})

var myToastEl = document.getElementById('myToast')
myToastEl.addEventListener('hidden.bs.toast', function () {
	$('#myToast').remove();
})

eel.expose(update_cpu)
eel.expose(update_ram)
function update_cpu(cpu_count){
	$('#cpu').text(cpu_count)
}

function update_ram(ram_count){
	$('#ram').text(ram_count)
}

// $('.toast').toast.show();
// toast.show();

function sendIt() {
	// var data = document.getElementById("data").value
	// eel.generate_qr(data)(setImage)
	eel.sendit()
}

function setImage(base64) {
	document.getElementById("qr").src = base64
}