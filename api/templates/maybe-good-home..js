function printSimilarity(sent_1, sent_2, method, use_lem, use_pos, use_stop) {
    // if(method == 'korpusová metóda') {
    // 	alert(sent_1)
    //     // return sent_1;       
    // }
    // if(method == 'znalostná metóda') {
    // 	alert(sent_2)
    //     // return sent_2;       
    // }

    var xhr = new XMLHttpRequest();
	xhr.open('GET', "http://localhost:5000/api", false);
	xhr.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
	xhr.send()
	alert(xhr)
}