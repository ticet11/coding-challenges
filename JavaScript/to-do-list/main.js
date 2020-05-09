const items = document.querySelectorAll(".todoItem");
const incompletedItems = document.getElementById("incompleteTodoWrapper");
const completedItemsList = document.querySelector(".completeTodoWrapper");
const completedItems = completedItemsList.querySelectorAll("li").getE;
const pendingH2 = document.getElementById("pendingTodos");

items.forEach((item) => {
    item.addEventListener("click", function completedItem(e) {
        const target = e.target;
        completedItemsList.appendChild(target);
        item.classList.add("completedTodoItem");
        if (incompletedItems.querySelectorAll("li").length === 0) {
            pendingH2.classList.add('empty');
        }
    });
});
