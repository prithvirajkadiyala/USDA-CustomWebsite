$(document).ready(function () {
	$.ajax({
		url : '/api/health/record/',
		type : 'GET',
		dataType : 'json',
		async: false,
		success : function(data) {
			console.log(data);
			$(data).each(function(i,elem){
				elem.create_date = StringToDate(elem.create_date);
				$.ajax({
					url: '/api/animal/add/'+elem.Animal_id,
					data: $('form').serialize(),
					type: 'GET',
					async: false,
					success : function(response) {
						elem.animalname = response[0].animalname;
						
					},
					error: function(response){
						console.log(response);
					}
				});	
			});
			tablecall(data);
		},
		error: function(response){
			console.log(response);
		}
	});
});
function nameFormatter(value) {
	var values = String(value);
	var pair = values.split("-");
	if(pair[0]=="pdf"){
		return '<a target="_blank" href=/static/pdf_files/'+ pair[1] + '>'+pair[1]+'</a>';
	}
	else{
		return value
	}
}
function tablecall(data) {
    $('#table').bootstrapTable({
		filterControl: true,
		disableUnusedSelectOptions: true,
		singleSelect: true,
        data: data
    });
};

$('#Edit').click(function() {
  var log= $('#table').bootstrapTable('getSelections');
  console.log(log);
  $("#create_date").val(log[0].create_date);
  $("#animalname").val(log[0].animalname);
  $("#location").val(log[0].location);
  $("#Amt_given").val(log[0].Amt_given);
  $("#medical_notes").val(log[0].medical_notes);
  $("#route").val(log[0].route);
  $("#water_feed").val(log[0].water_feed);
  $("#withdraw_time").val(log[0].withdraw_time);
  $("#Record_ID").val(log[0].Record_ID);
  $.ajax({
		url : '/api/inventory/formulary/',
		type : 'GET',
		dataType : 'json',
		async: false,
		success : function(data) {
			console.log(data);
			$(data).each(function(j,elem){
				if($('select#Medical_ID option[value="'+elem.Medicine_ID+'"]').length >0){
					if(elem.drug == log[0].drug){
						document.getElementById('Medical_ID').value =elem.Medicine_ID;
					}
				}
				else{
					$("<option value='"+elem.Medicine_ID+"'>"+ elem.drug +" </option>").appendTo("#Medical_ID");
					if(elem.drug == log[0].drug){
						document.getElementById('Medical_ID').value =elem.Medicine_ID;
					}
				}
			});
		},
		error: function(response){
			console.log(response);
		}
	});
  $("#HealthEditModal").modal("show");
});
// $('#HealthEditModal').on('shown.bs.modal', function () {
    // $(this).find('.modal-dialog').css({height:'auto', 
                              // 'max-height':'100%'});
// });
$('#Health_Edit_Modal_Yes').click(function() {
	var animalname = $("#animalname").val();
	var Animal_ID;
	$.ajax({
		url : '/api/health/add/'+animalname,
		type : 'GET',
		dataType : 'json',
		async: false,
		success : function(data) {
			console.log(data);
			Animal_ID = data[0].Animal_ID;
		},
		error: function(response){
			console.log(response);
		}
	});
	var log= $('#table').bootstrapTable('getSelections');
	console.log(log);
	var amount = $("#Amt_given").val() - log[0].Amt_given;
	var data = {
		Record_ID : $("#Record_ID").val(),
		create_date : $("#create_date").val(),
		Animal_id : Animal_ID,
		Medicine_ID : $("#Medical_ID").val(),
		location : $("#location").val(),
		Amt_given : $("#Amt_given").val(),
		difference : amount,
		medical_notes : $("#medical_notes").val(),
		result : $("#result").val(),
		route : $("#route").val(),
		water_feed : $("#water_feed").val(),
		withdraw_time : $("#withdraw_time").val(),
		email_ID : "test"
	}
	var dataJson = JSON.stringify(data);
	console.log(dataJson);

	$.ajax({
		url: '/api/health/record/',
		data: dataJson,
		type: 'PATCH',
		dataType: 'json',
		success: function(response) {
			console.log(response);
			$.notify("Data Saved", "info");
		},
		error: function(response) {
			console.log(response);
			$.notify("Data Not saved", "error");					
		}
	});
	console.log(data);
	setTimeout(function() {location.reload();}, 2000); 
});

$('#Delete').click(function() {
  var log= $('#table').bootstrapTable('getSelections');
  console.log(log);
  var result = alertbox("Please click 'OK' if you want to delete the following animal\n'"+log[0].animalname +"' on this date '"+ log[0].create_date +"'\nClick 'Cancel' if not");
  if (r = 1){
	$.ajax({
		url: '/api/health/record/'+log[0].Record_ID,
		type: 'DELETE',
		dataType: 'json',
		success: function(response) {
			console.log(response);
			$.notify("Data Saved", "info");
			setTimeout(function() {location.reload();}, 2000); 
		},
		error: function(response) {
			console.log(response);
			$.notify("Data Not saved", "error");					
		}
	});  
  }
  else{
	alert("Not deleted");
  }
});
$('#Delete_Yes').click(function() {
	var log= $('#table').bootstrapTable('getSelections');
	var animalname= $('#Delete_Animal')[0].textContent;
	var number = animalname.replace(/['"]+/g, '')
	alert(number);
	$.ajax({
		url: '/api/animal/update/'+animalname,
		type : 'DELETE',
		async: false,
		success : function(data) {
			location.reload();
			$.notify("Animal Data Deleted.")
		},
		error: function(response){
			$.notify("Not Deleted. Please contact IT")
		}
	});
});
