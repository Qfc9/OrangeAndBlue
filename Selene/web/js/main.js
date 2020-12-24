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

var config;
var update_data;
eel.py_get_config();

$("#update-btn").hide();
$("#update-spinner").hide();

$(document).ready(function () {

    setInterval(function () {

		$.getJSON( "https://eos.secretservice.app/update.php", function( data ) {
			console.log(data);

			console.log(config);

			update_data = data;

			if(data.version != config.version){
				$("#update-btn").show();
			}
			else{
				$("#update-btn").hide();
			}

		  });
    }, 3000);

});

eel.expose(start_up)
eel.expose(js_get_config)
eel.expose(finished_update)
eel.expose(close_app)

function js_get_config(conf){
	console.log(conf);
	config = jQuery.parseJSON( conf );
}

function close_app(){
	window.close();
}

function update_app(){
	$("#update-text").text("Updating...")
	$("#update-spinner").show();
	$("#update-btn").attr("disabled", true);
	eel.update_app(update_data.link, update_data.restart);
}

function finished_update(){
	$("#update-text").text("Update")
	$("#update-spinner").hide();
	$("#update-btn").attr("disabled", false);
	$("#update-btn").hide();
}

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

	if($("#on-off").prop('checked') == true){
		console.log("turned ON");
		eel.launch_worker(cpu, ram, server)
		$(".title-blue").css("color", "#20c997");
		$("#on-off").css("background-color", "#20c997");
		$("#on-off").css("border-color", "#20c997");
	}
	else{
		console.log("turned off");
		eel.close_worker()
		$(".title-blue").css("color", "#dc5c35");
		$("#on-off").css("background-color", "#dc5c35");
		$("#on-off").css("border-color", "#dc5c35");
	}
}

