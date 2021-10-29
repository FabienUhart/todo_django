let todo = '';
let different = '';
let elements = {
    'updateTodoButton': '.updateButton',
}
state_choices = {
    'RUN': 0,
    'DONE': 1,
    'INTER': 2,
}

$(document).ready(function () {
    updateButton('hide');
    $('.inputTodo').change(function () {
        $this = $(this);
        let value = $this.val();
        let name = $(this).attr('name');
        if (todo[name] !== value) {
            changeTodo(name, value);
            updateButton('show');
        }
    });
    $('.selectState').change(function () {
        let val = $(this).val()[0];
        if (todo['state'] !== val) {
            changeTodo('state', val);
            changeTodo('state_order', state_choices[val]);
            updateButton('show');
        }
    });
    $(elements.updateTodoButton).click(function () {
        updateTodo();
    })
})

function loadTodoElements(id, title, details, state) {
    console.log(id, "Title " + title, details, state);
    let state_order = state_choices[state];
    todo = {
        'id': id,
        'title': title,
        'details': details,
        'state': state,
        'state_order': state_order
    }
}

function changeTodo(name, value) {
    todo[name] = value;
}

function updateButton(display) {
    if (display === 'show')
        $(elements.updateTodoButton).show();
    else
        $(elements.updateTodoButton).hide();
}

function updateTodo() {
    $.ajax({
        type: "POST",
        url: urls.updatetodo,
        data: JSON.stringify(todo),
        contentType: "application/json; charset=utf-8",
        headers: {"X-CSRFToken": csrf.value},
        success: function (msg) {
            redirection('/home');
        },
        error: function (msg) {
            console.log('failure updateTodo')
        },
    });
}