const items = document.querySelectorAll('.todoItem');
const completedItemsList = document.querySelector('.completeTodoWrapper');

items.forEach(item => {
    item.addEventListener('click', function completedItem(e) {
        const target = e.target;
        completedItemsList.appendChild(target);
        

    });
});
