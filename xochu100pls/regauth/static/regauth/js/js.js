$('#signup').click(function() {
    var login = $('#rlogin').val();
    var pass1 = $('#rpass1').val();
    var pass2 = $('#rpass2').val();

    if (pass1 != pass2 || pass1.length < 4 || login.length < 4) {
        if (pass1 != pass2){
            alert('password and repeat password are different');
        }
        if (pass1.length < 4){
            alert('password must be longer than 3');
        }
        if (login.length < 4) {
            alert('login must be longer than 3');
        }
        return;
    }

    var url = 'ajax/signup/?login=' + login + '&pass=' + pass1;
    $.ajax({
        url:url,
        type:'get',
        data:'',
        success:function (data) {
            if (data.is){
                alert('success');
            } else {
                alert('error');
            }
        },
        error:function (error) {
            alert('fail');
        }
    })
})


$('#signin').click(function() {
    login = $('#alogin').val();
    pass1 = $('#apass1').val();

    var url = 'ajax/signin/?login=' + login + '&pass=' + pass1;
    $.ajax({
            url:url,
            type:'get',
            data:'',
            success:function (data) {
                if (data.is){
                    document.location.href = '../lc/?login=' + data.login;
                } else {
                    alert('Wrong login or password');
                }
            },
            error:function (error) {
                alert('fail');
            }
        }
    )
})