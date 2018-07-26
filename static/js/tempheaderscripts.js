function getQueryVariable(variable)
{
   var query = window.location.search.substring(1);
   var vars = query.split("&");
   for (var i=0;i<vars.length;i++) {
		   var pair = vars[i].split("=");
		   if(pair[0] == variable){return pair[1];}
   }
   return false;
};	

function alertbox(txt) {
	var r = confirm(txt);
	return r;
}
	
function StringToDate(string)
{
	
	if (string==null){return null;}
	else{
		var date = moment.utc(string).format('YYYY-MM-DD');
		// var dateString = string;
		// var dateObj = new Date(dateString);
		// var curr_date = dateObj.getDate() + 1; //Converting GMT to CDT causes datebacking so +1
		// var curr_month = dateObj.getMonth() + 1; //Months are zero based
		// var curr_year = dateObj.getFullYear();
		// var date = curr_year + "-" + curr_month + "-" + curr_date
	return date;
	}
};

function SubmitStringToDate(string)
{
	if (string==null){return null;}
	else{
		var date = moment.utc(string).format('YYYY-MM-DD');
		// var dateString = string;
		// var dateObj = new Date(dateString);
		// var curr_date = dateObj.getDate(); //Converted already from GMT to CDT to just need to change the format
		// var curr_month = dateObj.getMonth() + 1; //Months are zero based
		// var curr_year = dateObj.getFullYear();
		// var date = curr_year + "-" + curr_month + "-" + curr_date
		return date;
	}
};