let msg = document.getElementById('user_text');
let msg2 = document.getElementById('user_text2');

msg.addEventListener('keydown', (e) => {
    if(event.keyCode == 13) {
        queryAnswer(msg.value);
    }
    })

msg2.addEventListener('keydown', (e) => {
    if(event.keyCode == 13) {
        queryAnswer(msg2.value);
    }
    })

function queryAnswer(msg) {
    let request = new XMLHttpRequest;
    request.open('GET', "results");
    request.send();
}