---
title: "select element that is created by insertAdjacentHTML for adding or remove class"
site: stackoverflow
question_id: 73873818
url: https://stackoverflow.com/q/73873818
asked: 2022-09-27T21:06:25Z
asked_by: "joyi61"
asked_by_url: https://stackoverflow.com/users/19601673
last_edited: never
tags: [javascript, insertadjacenthtml]
score: 2
views_at_snapshot: 879
answer_count: 2
accepted_answer_id: 73875491
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 2f41887300e5ff5b1ab9b52528464af6eb03021dd5c6eee2c94827c7302d0da2
---

# select element that is created by insertAdjacentHTML for adding or remove class

Asked by [joyi61](https://stackoverflow.com/users/19601673) on Stack Overflow, <https://stackoverflow.com/q/73873818>, 2022-09-27. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

guys i want to add one class to **li** Element aftet it is created through **insertAdjacentHTML** 
but i dont know how i can select it
in fact i replaced **insertAdjacentHTML**  way with **append** that i commented appen way;
my codes are:

    function todosGenerator(todosList) {
    todoListElem.innerHTML = ''
    
        // let newTodoLiElem, newTodoLabalElem, newTodoCompleteBtn, newTodoDeleteBtn
    
    
        todosList.forEach(function (todo) {
        //     console.log(todo);
        //     newTodoLiElem = $.createElement('li')
        //     newTodoLiElem.className = 'completed well'
    
        //     newTodoLabalElem = $.createElement('label')
        //     newTodoLabalElem.innerHTML = todo.title
    
        //     newTodoCompleteBtn = $.createElement('button')
        //     newTodoCompleteBtn.className = 'btn btn-success'
        //     newTodoCompleteBtn.innerHTML = 'Complete'
        //     newTodoCompleteBtn.setAttribute('onclick', 'editTodo(' + todo.id + ')')
    
        //     newTodoDeleteBtn = $.createElement('button')
        //     newTodoDeleteBtn.className = 'btn btn-danger'
        //     newTodoDeleteBtn.innerHTML = 'Delete'
        //     newTodoDeleteBtn.setAttribute('onclick', 'removeTodo(' + todo.id + ')')
    
            // if (todo.complete) {
            //     newTodoLiElem.className = 'uncompleted well'
            //     newTodoCompleteBtn.innerHTML = 'UnComplete'
            // } **/! ican not write these lines with insertAdjacentHTML**
    
            // newTodoLiElem.append(newTodoLabalElem, newTodoCompleteBtn, newTodoDeleteBtn)
    
            // todoListElem.append(newTodoLiElem)
    
    
    
            todoListElem.insertAdjacentHTML('beforeend','<li class="completed well is"><label>'+todo.title+'</label><button class="btn btn-success" onclick="editTodo('+todo.id+')">Complete</button><button class="btn btn-danger" onclick="removeTodo('+todo.id+')">Delete</button></li>')
    
        
    
        })
        
    }

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Emiel Zuurbier](https://stackoverflow.com/users/11619647)** (2022-09-27): Why did you decide to replace `append` with `insertAdjacentHTML`?
- **[joyi61](https://stackoverflow.com/users/19601673)** (2022-09-27): for Reducing the size of my codes
