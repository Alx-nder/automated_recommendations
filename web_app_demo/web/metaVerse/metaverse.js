// collecting user id to deliver preference
var username=document.getElementById("user_id").innerHTML;
var logout=document.getElementById("logout");
if (username=="guest"){
    logout.style.display = "none";
}
var username_tag=document.getElementById("user_id");
username_tag.style.display="none";


var nft_uri="http://localhost/recommendalgo/web_app_demo/APIs/decentralandapi.py";

// creating a recommend card
function a_recommendation(){
    fetch(nft_uri,{
        method:"POST"
    })
    .then(function(response){
        return response.json();
    })
    .then((resp)=>{
        var outer_div = document.createElement("div");
        outer_div.setAttribute("class","col"); 

        var nex = document.createElement("div");
        nex.setAttribute("class","card h-100 bg-light"); 
        outer_div.appendChild(nex);
        
        var nex_nested = document.createElement("img");   
        nex_nested.setAttribute("src", resp[4]);
        nex_nested.setAttribute("class", "list_img my_img rounded my-2 mx-2");
        nex_nested.setAttribute("style", "max-width:100%; height:auto; object-fit:contain;");
        nex_nested.setAttribute("alt",resp[5]);
        nex.appendChild(nex_nested);

        var nex_nested_div = document.createElement("div");   
        nex_nested_div.setAttribute("class", "card-body");
        nex.appendChild(nex_nested_div);

        var nex_nested_div_title = document.createElement("h5");   
        nex_nested_div_title.setAttribute("class", " text-wrap card-title");
        nex_nested_div.appendChild(nex_nested_div_title);
        nex_nested_div_title.innerHTML=""+ resp[2] + "<br><br>"+resp[6]+" ETH";

        var nex_nested_div_text = document.createElement("p");   
        nex_nested_div_text.setAttribute("class", "card-text");
        nex_nested_div.appendChild(nex_nested_div_text);
        nex_nested_div_text.innerHTML ="X:"+resp[0]+"<br>"+"Y:"+resp[1]+"<br><br>Owner: "+resp[3];
        
        var nex_nested_footer = document.createElement("div");   
        nex_nested_footer.setAttribute("class", "card-footer");
        nex.appendChild(nex_nested_footer);
        
        var nex_nested_footer_text = document.createElement("small");   
        nex_nested_footer_text.setAttribute("class", "text-muted");
        nex_nested_footer.appendChild(nex_nested_footer_text);
        nex_nested_footer_text.innerHTML="Current Status: "+ resp[7];
        
        document.getElementById("csec").appendChild(outer_div);

        enter_tour();
    })
    .catch((err)=>{
        console.log('ERROR: ', err.message);
    });
}

// first few recommendations
a_recommendation();
a_recommendation();
a_recommendation();
a_recommendation();
a_recommendation();


 // // open new window for tour
 function enter_tour(){
    var list_img = document.getElementsByClassName('list_img');
    for (var i = 0, len = list_img.length; i < len; ++i) {
        list_img[i].onclick=function () {
            window.open(this.alt);
        }
    }}

// infinite scroll
$(window).scroll(function () {
    $("#loader_image").css("display", "block");
    if ($(document).height() <= $(window).scrollTop() + $(window).height()) {
        a_recommendation();
        a_recommendation();
        a_recommendation();
    }
    $("#loader_image").css("display", "none");
});
