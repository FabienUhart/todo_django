let urls = {
    'connexion': '/connexion/',
    'deconnexion': '/deconnexion/',
    'loadtodos': '/loadtodos/',
    'addtodo': '/addtodo/',
    'updatetodo': '/updatetodo/',
}
let csrf = {
    key: 'csrftoken',
    value: ''
};
let valNewTodo = '';
let idClass = {
    'inputAddTodo': '#addTodo input',
    'getValNewTodo': '#addval',
}
let element = '';
$(document).ready(function () {
    $(idClass.inputAddTodo).change(function () {
        let $this = $(this);
        if ($this.val() !== '') {
            valNewTodo = $this.val();
        }
    });
    $(idClass.getValNewTodo).click(function () {
        addNewTodo();
    });
    $('.redirect').click(function () {
        redirection($(this).attr('data-url'));
    });
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

function getcookie() {
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

function addNewTodo() {
    let data = {
        details: valNewTodo
    };
    $.ajax({
        type: "POST",
        url: urls.addtodo,
        data: JSON.stringify(data),
        contentType: "application/json; charset=utf-8",
        headers: {"X-CSRFToken": csrf.value},
        success: function (msg) {
            get_todos();
        },
        error: function (msg) {
            console.log('msg');
        },
    });
}

function redirection(url) {
    document.location.href = url;
}