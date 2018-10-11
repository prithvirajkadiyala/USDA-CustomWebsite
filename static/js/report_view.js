$(document).ready(function(){
	$.ajax({
		url : '/api/report/get/',
		type : 'POST',
		dataType : 'json',
		async: false,
		success : function(data) {
			$(data).each(function(i,elem){
				elem.start_date = StringToDate(elem.start_date);
				elem.end_date = StringToDate(elem.end_date);
				var value = JSON.parse(elem.parameters);
				var attributes = "";
				$(value).each(function(i,elem){
					attributes += elem;
					attributes += ", ";
				});
				elem.parameters = attributes.replace(/,\s*$/, "");
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
