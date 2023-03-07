  google.charts.load('current', {'packages':['corechart']});
function fetch_task()
{
//alert("sds");
$.get( "/api/fetch_task", function( data ) {
  //data=JSON.stringify(data);
//  alert(data[0].task_id);
  create_graph(data);
});
}
function create_graph(r_data)
{

          for(var i = 0; i <=r_data.length; i++) {


                    google.charts.setOnLoadCallback(drawChart(r_data[i]));

                    // Draw the chart and set the chart values
                    function drawChart(r_data) {
                      //alert(r_data.coding)
                      var data = google.visualization.arrayToDataTable([
                      ['Task', 'per Day'],
                      ['coding', parseInt(r_data.coding)],
                      ['internet', parseInt(r_data.net)],
                      ['testing', parseInt(r_data.testing)],
                      ['designing', parseInt(r_data.designing)]
                    ]);
                      var a=i+1;
                      // Optional; add a title and set the width and height of the chart
                      var options = {'title':'Time spent by an Employee-'+a+' in a day', 'width':550, 'height':400};

                      // Display the chart inside the <div> element with id="piechart"
                      $(".monitor").append("<div id=task"+i+" class ='col s4 m4 l4' ></div>");

                      var chart = new google.visualization.PieChart(document.getElementById('task'+i));
                      chart.draw(data, options);
                    //  alert("sdsvk");
                    }
            }

}

function add_admin(admin_ids,admin_names,admin_designations,admin_mailids,admin_passwords)
{

   //alert({ admin_id: admin_ids.value,admin_name: admin_names.value,admin_designation:admin_designations.value,admin_mailid:admin_mailids.value,admin_password:admin_passwords.value });
   //alert(admin_ids.value+","+admin_names.value);
   alert(JSON.stringify({ admin_id: admin_ids.value,admin_name: admin_names.value,admin_designation:admin_designations.value,admin_mailid:admin_mailids.value,admin_password:admin_passwords.value }));
        /*$.post( '/api/add_admin', { admin_id: admin_ids.value,admin_name: admin_names.value,admin_designation:admin_designations.value,admin_mailid:admin_mailids.value,admin_password:admin_passwords.value })
            .done(function(data) {
            alert( "Data Loaded:");
            });*/

}


