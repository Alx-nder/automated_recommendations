const cb_uri = "http://localhost/virtualtourwebsite/chatbot1/chatbot1.py";
const mic_url="http://localhost/virtualtourwebsite/chatbot1/speech_module.py";

var chat_controls=document.getElementById("chat_controls");
chat_controls.style.display="none";

var response_area=document.getElementById("response_area");
response_area.style.display="none";

$("#chat_trigger").click(function(){
    if(chat_controls.style.display == "block"){
        chat_controls.style.display="none";
        response_area.style.display="none";

    }else{
        chat_controls.style.display="block";
        response_area.style.display="block";

    }
})

$(".mic").click(function(){
    $.ajax({
        url:mic_url,
        method:"Get",
        success: function(mic_bot){
            alert(mic_bot);
        }
    })
})

$(".send").click(function(){
    var message = $('[name=chat]').val();
    if (message=="")
    {
    }
    else{
        $.ajax({
            url: cb_uri,
            method: "POST",
            data: {message_py:message},
            dataType: "text",
            success: function(data){
                response_area=document.getElementById("response_area");
                
                // user
                var user = document.createElement("p");   
                user.setAttribute("class", "text-end px-3");
                response_area.appendChild(user);
                user.innerHTML=message;

                // bot
                var bot = document.createElement("p");   
                bot.setAttribute("class", "text-start px-3");
                response_area.appendChild(bot);
                bot.innerHTML=data;
                var user_chat=document.getElementById("user_chat");
                user_chat.value="";
            }
        })
    }
})
