$(document).ready(function(){
	$.ajax({
		url : '/api/experiment/list/',
		type : 'GET',
		dataType : 'json',
		async: false,
		success : function(data) {
			$(data).each(function(i,elem){
				elem.customheightdate = StringToDate(elem.customheightdate);
				elem.customweightdate = StringToDate(elem.customweightdate);
				elem.expt_date = StringToDate(elem.expt_date);
				elem.weanweightdate = StringToDate(elem.weanweightdate);
				elem.yearlingdate = StringToDate(elem.yearlingdate);
			});
			tablecall(data);
		},
		error: function(response){
			console.log(response);
		}
	});
	function tablecall(data) {
		$('#table').bootstrapTable({
			filterControl: true,
			disableUnusedSelectOptions: true,
			singleSelect: true,
			data: data
		});
	};
});

$('#Edit').click(function() {
  var log= $('#table').bootstrapTable('getSelections');
  console.log(log);
  $("#name").val(log[0].name);
  $("#ExperimentEditModal").modal("show");
});
$('#Edit_Experiment_Yes').click(function() {
	var name= $('#name').val();
		setTimeout(function() {
		window.location.href = '/experiment/edit?herdname=' +name
	}, 2000); 
});

$('#Delete').click(function() {
  var log= $('#table').bootstrapTable('getSelections');
  console.log(log);
  var result = alertbox("Please click 'OK' if you want to delete the following Herd\n'"+log[0].name +"' created on this date '"+ log[0].create_date +"'\nClick 'Cancel' if not");
  if (r = 1){
	  var data = {
		  name : log[0].name,
		  create_date : log[0].create_date
	  }
	  myJSON = JSON.stringify(data)
	$.ajax({
		url: '/api/herd/create/',
		type: 'DELETE',
		data : myJSON,
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

$('#button_Done').click(function() {
  setTimeout(location.reload(), 2000);
});

$('#UploadCSV').click(function() {
  $("#UploadCSVModal").modal("show");
});
$('#Upload_Done').click(function() {
	location.reload();
});


$(function () {
    $("#upload").bind("click", function () {
        var regex = /^([a-zA-Z0-9\s_\\.\-:])+(.csv|.txt)$/;
        if (regex.test($("#fileUpload").val().toLowerCase())) {
            if (typeof (FileReader) != "undefined") {
                var reader = new FileReader();
                reader.onload = function (e) {
					var data=$.csv.toObjects(e.target.result);
					console.log(data);
					$(data).each(function(i, elem){
							var dataJson = JSON.stringify(elem);
							console.log(dataJson);
							$.ajax({
								url: '/api/animal/add/',
								data: dataJson,
								type: 'post',
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
					
                    var table = $("<table />");
                    var rows = e.target.result.split("\n");
                    for (var i = 0; i < rows.length; i++) {
                        var row = $("<tr />");
                        var cells = rows[i].split(",");
                        for (var j = 0; j < cells.length; j++) {
                            var cell = $("<td />");
                            cell.html(cells[j]);
                            row.append(cell);
                        }
                        table.append(row);
                    }
                    $("#dvCSV").html('');
                    $("#dvCSV").append(table);
                }
                reader.readAsText($("#fileUpload")[0].files[0]);
            } else {
                alert("This browser does not support HTML5.");
            }
        } else {
            alert("Please upload a valid CSV file.");
        }
    });
});
	