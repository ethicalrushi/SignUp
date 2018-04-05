



$(document).ready(function(){
  $.getJSON("http://127.0.0.1:8000/api/images/?format=json",function(data){
    var tr;
    console.log(data)
    for(var i=0;i<data.length;i++)
    {
      tr = $('<tr/>');

      tr.append("<td>"+data[i].fullname+"</td>");
      tr.append("<td>"+data[i].username+"</td>");
      //tr.append("<td>"+data[i].email+"</td>");
      //tr.append("<td>"+data[i].address.city+"</td>");
     
      $('table').append(tr);
    }
  });
});
