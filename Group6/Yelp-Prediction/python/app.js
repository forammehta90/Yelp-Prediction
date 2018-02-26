function a() {
var wifi = document.getElementById('sel1');
var meal = document.getElementById('sel2');
var ambience = document.getElementById('sel3');
var bikeparking = document.getElementById('sel4');
var wheelchair = document.getElementById('sel5');
var price = document.getElementById('sel6');
var alcohol = document.getElementById('sel7');
var noiselevel = document.getElementById('sel8');
var caters = document.getElementById('sel9');
var businessparking = document.getElementById('sel10');

request[58] = wifi.options[wifi.selectedIndex].value;
for (var i=0,j=0;i<meal.options.length;i++) {
    if(meal.options[i].selected == true && meal.options[i].value != "0") {
        request[meal.options[i].value] = "1";
    }
}
for (var i=0,j=0;i<ambience.options.length;i++) {
    if(ambience.options[i].selected == true && ambience.options[i].value != "0") {
        request[ambience.options[i].value] = "1";
    }
}
request[18] = bikeparking.options[bikeparking.selectedIndex].value;
request[57] = wheelchair.options[wheelchair.selectedIndex].value;
request[52] = price.options[price.selectedIndex].value;
request[0] = alcohol.options[alcohol.selectedIndex].value;
for (var i=0,j=0;i<noiselevel.options.length;i++) {
    if(noiselevel.options[i].selected == true && noiselevel.options[i].value != "0") {
        request[noiselevel.options[i].value] = "1";
    }
}
request[26] = caters.options[caters.selectedIndex].value;
for (var i=0,j=0;i<businessparking.options.length;i++) {
    if(businessparking.options[i].selected == true && businessparking.options[i].value != "0") {
        request[businessparking.options[i].value] = "1";
    }
}

    request[7] = "1";
    /*request[43] = "1";
    request[46] = "1";
    request[12] = "1";
    request[16] = "1";
    request[13] = "1";
    request[41] = "1";
    request[25] = "1";
    request[6] = "1";
    request[24] = "1";*/

console.log(request)
        $.ajax({
            url: 'http://127.0.0.1:8000/app/'+request,
            type: 'POST',
            success: function(response) {
                console.log(response);
                document.getElementById('result').innerHTML = '<b>Linear Regression : '+ response.lr + '<br/> Binary Classification : '+ response.bin + '</b>';
                $("result").show();
            },
            error: function(error) {
                console.log(error);
            }
        });

return false;
}
$("result").hide();
var request = new Array(60).fill("0");