function sendIt() {
	// var data = document.getElementById("data").value
	// eel.generate_qr(data)(setImage)
	eel.sendit()
}

function setImage(base64) {
	document.getElementById("qr").src = base64
}