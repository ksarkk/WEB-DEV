const todoList = [];
const todoListElement = document.querySelector("#ul-task");
const addBtn = document.querySelector("#add_button");
const inputField = document.querySelector("#myInput");

addBtn.addEventListener("click", addTodo);
inputField.addEventListener("keydown", function(e) {
    if (e.keyCode === 13) {
        addTodo();
    }
});

function addTodo() {
    const todoText = inputField.value.trim();
    if (todoText) {
        todoList.unshift({
            id: todoList.length,
            todoText,
            isDone: false,
        });
        displayTodos();
    } else {
        alert("You didn't enter any tasks");
    }
}

function doneTodo(todoId) {
    const todo= todoList.findIndex((item) => item.id == todoId);
    todoList[todo].isDone
        ? (todoList[todo].isDone = false)
        : (todoList[todo].isDone = true);
    displayTodos();
}

function deleteItem(x) {
    todoList.splice(todoList.findIndex(item => item.id === x), 1);
    displayTodos();
}

function displayTodos() {
    todoListElement.innerHTML = "";
    inputField.value = "";
    todoList.forEach(item => {
        const listElement = document.createElement("li");
        const delBtn = document.createElement("i");

        listElement.textContent = item.todoText;
        listElement.setAttribute("item", item.id);

        delBtn.setAttribute("item", item.id);
        delBtn.classList.add("far", "fa-trash-alt");

        if (item.isDone) {
            listElement.classList.add("checked");
        }

        listElement.addEventListener("click", function(e) {
            doneTodo(e.target.getAttribute("item"));
        });

        delBtn.addEventListener("click", function(e) {
            deleteItem(e.target.getAttribute("item"));
        });

        listElement.appendChild(delBtn);
        todoListElement.appendChild(listElement);
    });
}
