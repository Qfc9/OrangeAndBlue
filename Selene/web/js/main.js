var toastElList = [].slice.call(document.querySelectorAll('.toast'))
var toastList = toastElList.map(function (toastEl) {
  return new bootstrap.Toast(toastEl).show()
})

var myToastEl = document.getElementById('myToast')
myToastEl.addEventListener('hidden.bs.toast', function () {
	$('#myToast').remove();
})

cpu_slider(1);
ram_slider(1);

eel.expose(start_up)


function start_up(cpu_count, ram_count){

	$("#cpu-slider").attr({
		"max" : cpu_count,
		"min" : 1,
		"value": 1
	 });

	 $("#ram-slider").attr({
		"max" : ram_count,
		"min" : 1,
		"value": 1
	 });
}


function cpu_slider(count){
	$('#cpu').text("CPU: " + count)
}

function ram_slider(count){
	$('#ram').text("RAM: " + count + "gb")
}

function launch() {
	cpu = $('#cpu-slider').val()
	ram = $('#ram-slider').val()
	server = $('#server').val()
	// console.log(cpu, ram, server);
	eel.launch_worker(cpu, ram, server)
}