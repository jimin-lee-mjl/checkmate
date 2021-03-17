get_profile();

$(document).ready(function() {
    $("#edit_email_btn").click(function() { 
        $(".div_new_email").toggle();
    });

    $("#change_password_btn").click(function() { 
        $(".div_change_password").toggle();
    });
});

//get profile
function get_profile(){
    var url = "/profile/email";
    console.log(url);
    fetch(url)
        .then(function (type){
            return type.json();
        })
        .then(function (result){
            console.log(result.result);
            var result = result.result;
            var username = result.username;
            var email = result.email;

            console.log(username);
            $("#div_username").text(username);

            console.log(email);
            $("#original_email").text(email);
        });
    }

function edit_email(){
    var new_email = $("#input_new_email").val();
    console.log(new_email);
    var url = "/profile/email";
    fetch(url, {
            method: "PUT",
            body: JSON.stringify({
              email: new_email
            }),
            headers: {
              "Content-Type": "application/json"
            }
        })
        .then(function (type){
                return type.json();
        })
        .then(function (result){
            console.log(result);
            if (result.status == 'success') {
                var success_msg = "이메일이 변경되었습니다.";
                var email = result.result.email;
                console.log(email);
                //alert(success_msg);

                //Sweetalert2
                Swal.fire({
                    position: 'center',
                    icon: 'success',
                    title: success_msg,
                    showConfirmButton: false,
                    timer: 1000
                })
            } else {
                var error_msg = "이메일 형식이 유효하지 않습니다.";
                //alert(error_msg);

                //Sweetalert2
                Swal.fire({
                    position: 'center',
                    icon: 'warning',
                    title: error_msg,
                    showConfirmButton: false,
                    timer: 1000
                })
            }   
        });
}

function change_password(){
    var cur_password = $("#input_cur_password").val(); 
    var new_password = $("#input_new_password").val(); 
    console.log(cur_password);
    console.log(new_password);
    if (new_password.length < 8) {
        var error_msg = "비밀번호는 8자 이상이어야 합니다.";
        
        //Sweetalert2
        Swal.fire({
            position: 'center',
            icon: 'warning',
            title: error_msg,
            showConfirmButton: false,
            timer: 1000
        })

        return;
    } else {
        var url = "/profile/password";
        fetch(url, {
                method: "PUT",
                body: JSON.stringify({
                    cur_password: cur_password,
                    new_password :new_password
                }),
                headers: {
                "Content-Type": "application/json",
                },
            })
            .then(function (type){
                return type.json();
            })
            .then(function (result){
                console.log(result);
                if (result.status == 'success') {
                    var success_msg = result.result.success_msg;
                    //alert(success_msg);

                    //Sweetalert2
                    Swal.fire({
                        position: 'center',
                        icon: 'success',
                        title: success_msg,
                        showConfirmButton: false,
                        timer: 1000
                    })
                } else {
                    var error_msg = result.result.error_msg;
                    //alert(error_msg);

                    //Sweetalert2
                    Swal.fire({
                        position: 'center',
                        icon: 'warning',
                        title: error_msg,
                        showConfirmButton: false,
                        timer: 1000
                    })
                }   
            });
    }
}