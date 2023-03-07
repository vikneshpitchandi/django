/*var request = $.ajax({
    url: 'http://localhost:8000/Employee',
    type: "GET",
    dataType: "json",
    success: function (data) {
   data=JSON.parse(data)
    }
});*/
//alert("sds");
var html=""
var request
$.ajax({
        url: 'http://localhost:8000/Machine',
        contentType: "application/json",
        dataType: 'json',
        success: function(result){
              request=result;
             //result=JSON.parse(result);
             var count = Object.keys(result).length;
//            alert(count);
            for(var i=0;i<count;i++){
            //alert(result[i].Employee_Name);
            var obj= result[i];
             html = html+"<tr><td>"+obj.Machine+"</td>"+"<td>"+obj.OEF+"</td>"+"<td>"+obj.Work_Time+"</td>"+"<td>"+obj.Stop_Time+"</td>"+"<td>"+obj.EmpID+"</td>"+"<td>"+obj.Production_real+"</td></tr>"
              //alert(html)

             }
             $( ".Machine_body" ).append( html );


        }
    })

alert(request[0]);

;
for(var i=0;i<count;i++){
var obj= request[i];
html = html+"<tr>"+obj.EmpID+"</tr>"+"<tr>"+obj.Employee_Name+"</tr>"+"<tr>"+obj.DOB+"</tr>"+"<tr>"+obj.Sex+"</tr>"+"<tr>"+obj.CitizenDesc+"</tr>"
$( ".labour_body" ).append( html );
}


alert(request)


