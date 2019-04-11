function printSimilarity(sent_1, sent_2, method, use_lem, use_pos, use_stop) {
//     if(method == 'korpusová metóda') {
//     	alert(sent_1)
//         // return sent_1;
//     }
//     if(method == 'znalostná metóda') {
//     	alert(sent_2)
//         // return sent_2;
//     }

    var httpRequest = new XMLHttpRequest();
    var json = 'NaN';
    httpRequest.open('GET', "http://localhost:5000/api", true);
    httpRequest.setRequestHeader("Content-Type", "application/json");
//    var data = JSON.stringify("{}");
    httpRequest.send();

//    httpRequest.onreadystatechange = function () {
//         if (httpRequest.readyState == 4 && (httpRequest.status == 200)) {
//            console.log("ready")
//            var Data = JSON.parse(httpRequest.responseText);
//            console.log(Data);
//            console.log(Data.first);
//        } else {
//            console.log("not ready yet")
//        }
//    }


//    json = JSON.parse(httpRequest.responseText);
    alert(json);
    console.log(httpRequest);
    console.log(json);
    return json;
}