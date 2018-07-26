$("#Inspection_Submit").click(function(){
	var data = {
		pasture_ID : $("#pasture_number").val(),
		general_appearance : $("#general_appearance option:selected").text(),
		live_stock : $("#livestock option:selected").text(),
		date : $("#date").val(),
		animal_condition : $("#animal_condition option:selected").text(),
		fencing : $("#fencing option:selected").text(),
		access_to_food : $("#access_to_feed option:selected").text(),
		access_to_water : $("#access_to_water option:selected").text(),
		cleaniness_of_water : $("#water_cleanliness option:selected").text(),
		access_to_shelter : $("#shed_access option:selected").text(),
		comments : $("#comments").val(),
		pasture_major_deficiencies : $("#major_deficiencies").val(),
		pasture_minor_deficiencies : $("#minor_deficiencies").val(),
		email_ID : "test",
		builinding_number : 0,
		lighting : 0,
		housekeeping : 0,
		head_catch_condition : 0,
		non_slip_surface_evidence : 0,
		Pen_condition : 0,
		container_disposal : 0,
		drug_storage : 0
	};
	var myJSON = JSON.stringify(data);
	$.ajax({
		url: '/api/inspection/report/',
		data: myJSON,
		type: 'POST',
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
});

$("#Inspection_Submit_Building").click(function(){
	var data = {
		pasture_ID : 0,
		live_stock : 0,
		animal_condition : 0,
		fencing : 0,
		access_to_food : 0,
		access_to_water : 0,
		cleaniness_of_water : $("#housekeeping_cleanliness option:selected").text(),
		access_to_shelter : 0,
		comments : $("#iacuc2_comments").val(),
		pasture_major_deficiencies : $("#iacuc_major2_deficiencies").val(),
		pasture_minor_deficiencies : $("#iacuc_minor2_deficiencies").val(),
		email_ID : "test",
		builinding_number : $("#building_number").val(),
		general_appearance : $("#general_appearance_building option:selected").text(),
		lighting : $("#electrical_lighting option:selected").text(),
		date : $("#date_building").val(),
		housekeeping : $("#housekeeping_cleanliness option:selected").text(),
		head_catch_condition : $("#squeezechute_headcatch option:selected").text(),
		non_slip_surface_evidence : $("#headcatch_exit option:selected").text(),
		Pen_condition : $("#pen_condition option:selected").text(),
		container_disposal : $("#sharp_disposal_containers option:selected").text(), 
		drug_storage : $("#drug_storage option:selected").text()
	};
	var myJSON = JSON.stringify(data);
	$.ajax({
		url: '/api/inspection/report/',
		data: myJSON,
		type: 'POST',
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
});