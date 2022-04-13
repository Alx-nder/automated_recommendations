var username=document.getElementById("user_id").innerHTML;

$(".submit").click(function(){

$.ajax({
    url: "http://localhost/recommendalgo/web_app_demo/web/seller/estimation.py",
    method: "POST",
    data: {message_py:""},
    dataType: "text",
    success: function(data){
        data=JSON.parse(data);
            var living_space= $("[name=living_space]").val();
            var land=$("[name=land]").val();
            var age=$('[name=age]').val();
            var bedrooms= $("[name=bedrooms]").val();
            var building_class=$("[name=building_class]").val();
            var bathrooms=$("[name=bathrooms]").val();
            var the_estimate=((living_space*data[0])+(bathrooms*data[1])+(bedrooms*data[2])+(building_class*data[3])+(land*data[4])+(age*data[5])); 
            $('#the_estimate').attr('placeholder',the_estimate);    
    }
})
})