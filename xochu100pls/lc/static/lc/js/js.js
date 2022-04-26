setInterval(showrequestlist, 5000);
setInterval(showfriendlist, 5000);
showrequestlist();
showfriendlist();

function infoChangeClick(idd) {
    if ($('#' + idd)[0].disabled == false) {
        $('#' + idd)[0].disabled = true;

        var url = 'ajax/updatelc/?login=' + $('#login')[0].name + '&p=' + idd + '&val=' + $('#' + idd).val();
        $.ajax({
            url:url,
            type:'get',
            data:'',
            success:function (data) {
            },
            error:function (error) {
                alert('fail');
            }
        })

    } else {
        $('#' + idd)[0].disabled = false;
    }
}

function myProfile() {
    login = $('#login')[0].name;

    var url = 'ajax/fillinfobylogin/?login=' + login;
    $.ajax({
        url:url,
        type:'get',
        data:'',
        success:function (data) {
            $('#login').val(data.login);
            $('#name').val(data.name);
            $('#lastname').val(data.lastname);
            //$('#photo').val(data.photo);
            $('#status').val(data.status);
            $('#education').val(data.education);
            $('#foodpreferences').val(data.foodpreferences);
            $('#attitudetoalcohol').val(data.attitudetoalcohol);
            $('#attitudetosmoking').val(data.attitudetosmoking);
        },
        error:function (error) {
            alert('fail');
        }
    })

}

function addFriend() {
    loginfrom = $('#login')[0].name;
    loginto = prompt('enter login of friend');

    var url = 'ajax/sendfriendrequest/?loginfrom=' + loginfrom + '&loginto=' + loginto;
    $.ajax({
        url:url,
        type:'get',
        data:'',
        success:function (data) {
            if (data.res){
                alert('request sent');
            } else {
                alert('error');
            }
        },
        error:function (error) {
            alert('fail');
        }
    })
}

function getfriendinfo(login) {
    var url = 'ajax/fillinfobylogin/?login=' + login;
    $.ajax({
        url:url,
        type:'get',
        data:'',
        success:function (data) {
            $('#login').val(data.login);
            $('#name').val(data.name);
            $('#lastname').val(data.lastname);
            //$('#photo').val(data.photo);
            $('#status').val(data.status);
            $('#education').val(data.education);
            $('#foodpreferences').val(data.foodpreferences);
            $('#attitudetoalcohol').val(data.attitudetoalcohol);
            $('#attitudetosmoking').val(data.attitudetosmoking);
        },
        error:function (error) {
            alert('fail');
        }
    })
}

function showfriendlist() {
    login = $('#login')[0].name;

    var url = 'ajax/getfriendlist/?login=' + login;
    $.ajax({
        url:url,
        type:'get',
        data:'',
        success:function (data) {
            $('.friendslist').html('');
            for (var k in data) {
                $('.friendslist').append($('<p class="people" onclick="getfriendinfo(\'' + data[k] + '\')">' + data[k] + '</p>'));
            }
        },
        error:function (error) {
            alert('fail');
        }
    })
}

function showrequestlist() {
    login = $('#login')[0].name;

    var url = 'ajax/getrequestlist/?login=' + login;
    $.ajax({
        url:url,
        type:'get',
        data:'',
        success:function (data) {
            $('.friendsrequests').html('');
            for (var k in data) {
                $('.friendsrequests').append($('<div class="request"><p>' + data[k] + '</p><button class="btnanim" onclick="acceptfriend(\'' + data[k] + '\')">+</button><button class="btnanim" onclick="denyfriend(\'' + data[k] + '\')">-</button></div>'));
            }
        },
        error:function (error) {
            alert('fail');
        }
    })
}

function acceptfriend(login1) {
    login2 = $('#login')[0].name;

    var url = 'ajax/acceptfriend/?login1=' + login1 + '&login2=' + login2;
    $.ajax({
        url:url,
        type:'get',
        data:'',
        success:function (data) {
        showrequestlist();
        },
        error:function (error) {
            alert('fail');
        }
    })
}

function denyfriend(login1) {
    login2 = $('#login')[0].name;

    var url = 'ajax/denyfriend/?login1=' + login1 + '&login2=' + login2;
    $.ajax({
        url:url,
        type:'get',
        data:'',
        success:function (data) {
            showrequestlist();
        },
        error:function (error) {
            alert('fail');
        }
    })
}

function goChat() {
    login = $('#login')[0].name;
    name = $('#name').val();

    var url = '../chat/?login=' + login + '&name=' + name;
    document.location.href = url;
}
