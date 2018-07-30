$(document).ready(function(){
	$.ajax({
		url : '/api/inspection/report/',
		type : 'GET',
		dataType : 'json',
		async: false,
		success : function(data) {
			console.log(data);
			$(data).each(function(i,elem){
				elem.date = StringToDate(elem.date);
			});
			tablecall(data);
		},
		error: function(response){
			console.log(response);
		}
	});
});

function tablecall(data) {
    $('#table').bootstrapTable({
		filterControl: true,
		disableUnusedSelectOptions: true,
		singleSelect: true,
        data: data
    });
};