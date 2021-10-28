let urls = {
    'connexion': '/connexion/',
    'deconnexion': '/deconnexion/',
    'loadtodos': '/loadtodos/',
}

let csrf = {
    key: 'csrftoken',
    value: ''
};

let element ='';
$(document).ready(function () {
    console.log('Ma TODO');
    getcookie();
    get_todos();
})


function get_todos() {
     let data = {
        username: 'login',
        password: 'mot_de_passe'
    };
    $.ajax({
        type: "POST",
        url: urls.loadtodos,
        data: JSON.stringify(data),
        contentType: "application/json; charset=utf-8",
        headers: {"X-CSRFToken": csrf.value},
        success: function (msg) {
            // add elements in page
            $(".elements").empty().append(msg);
        },
        error: function (msg) {
            console.log('Failure loading elements');
        },
    });
}

function getcookie(){
    let csrf_response = document.cookie.split(';');
    csrf.value = search_key(" csrftoken", csrf_response);
}

function search_key(key, data) {
    for (let i = 0; i < data.length; i++) {
        let data_loop = data[i].split("=");
        if (data_loop[0] === key)
            return data_loop[1];
    }
    return false;
}