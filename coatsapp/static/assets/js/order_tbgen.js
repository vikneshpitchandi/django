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
        url: 'http://localhost:8000/order',
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
             html = html+"<tr><td>"+obj.ORDER_NUMBER+"</td>"+"<td>"+obj.ORDER_STARTED+"</td>"+"<td>"+obj.ORDER_COMPLETED+"</td></tr>"
              //alert(html)

             }
             $( ".order_body" ).append( html );


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


