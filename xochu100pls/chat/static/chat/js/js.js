var amount_of_messages = 0;
var timefunc = 0;

function openChat(self) {
    loginfrom = document.getElementById('login').innerHTML;
    loginto = self.getAttribute('name');

    if (timefunc){
        clearInterval(timefunc);
    }
    timefunc = setInterval(openChat, 2000, self);

    var url = 'ajax/getmessages/?loginfrom=' + loginfrom + '&loginto=' + loginto;
    $.ajax({
        url:url,
        type:'get',
        data:'',
        success:function (data) {
            document.getElementById('opponentname').innerHTML = self.innerHTML;
            document.getElementById('opponentname').setAttribute('name', self.getAttribute('name'));

            var messages = document.querySelector("div.messages");
            messages.innerHTML = '';

            for (var k in data) {
                let mess = document.createElement("p");
                let message = document.createTextNode(data[k].slice(12));

                mess.classList.add('msg');

                if (data[k].slice(0, 12) == '<myyyyyyy..>'){
                    mess.classList.add('mymessage');
                } else {
                    mess.classList.add('opponentmessage');
                }

                mess.appendChild(message);
                messages.appendChild(mess);
            }

            var local_amount_of_messages = document.getElementById("msgs").childElementCount;
            if (local_amount_of_messages != amount_of_messages) {
                document.getElementById("msgs").scrollTop = document.getElementById("msgs").scrollHeight;
            }

            amount_of_messages = document.getElementById("msgs").childElementCount;
        },
        error:function (error) {
            alert('fail');
        }
    })

}

function sendMessage() {
    var msg = document.getElementById("inp").value;
    var loginto = document.getElementById("opponentname").getAttribute("name");
    var loginfrom = document.getElementById("login").innerHTML;

    document.querySelector("input.inpmessage").value = '';

    if (loginto){
        if (msg != null && msg.trim()) {

            var url = 'ajax/addmessage/?loginfrom=' + loginfrom + '&loginto=' + loginto + '&message=' + msg;
            $.ajax({
                url:url,
                type:'get',
                data:'',
                success:function (data) {
                    var messages = document.querySelector("div.messages");
                    let mess = document.createElement("p");
                    let message = document.createTextNode(msg);
                    mess.classList.add("msg");
                    mess.classList.add("mymessage");
                    mess.appendChild(message);
                    messages.appendChild(mess);

                    document.getElementById("msgs").scrollTop = document.getElementById("msgs").scrollHeight
                },
                error:function (error) {
                    alert('fail');
                }
            })
        }
    }

    document.getElementById("inp").focus();
}

function update() {
    var login = document.getElementById('login').innerHTML;

    var url = 'ajax/update/?login=' + login;
    $.ajax({
        url:url,
        type:'get',
        data:'',
        success:function (data) {
            var listDiv = document.querySelector("div.listofpeople");
            listDiv.innerHTML = '';

            for (var i = 0; i < data.size; i++) {

                if (data[String(i)] != document.getElementById('login').innerHTML){
                    let people = document.createElement("div");
                    let peoplename = document.createTextNode(data[String(i) + 'name']);

                    people.classList.add('people');
                    people.setAttribute("name", data[String(i)]);
                    people.appendChild(peoplename);

                    people.onclick = function() {
                        openChat(people);
                    }

                    listDiv.appendChild(people);

                } else {
                    document.getElementById('name').innerHTML = data[String(i) + 'name']
                }
            }

        },
        error:function (error) {
            alert('fail');
        }
    })
}

window.onload = update;
update();