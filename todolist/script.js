// Seleciona elementos do DOM
const newTaskInput = document.getElementById('newTask');
const taskDateInput = document.getElementById('taskDate'); // Novo campo para data
const taskTimeInput = document.getElementById('taskTime'); // Novo campo para hora
const addTaskButton = document.getElementById('addTaskButton');
const taskList = document.getElementById('taskList');

// Carrega tarefas salvas no Local Storage
document.addEventListener('DOMContentLoaded', loadTasks);

// Define um valor padrão de data para 2024
taskDateInput.addEventListener('focus', () => {
    if (!taskDateInput.value) {
        taskDateInput.value = '2024-01-01'; // Define a data padrão para 1º de janeiro de 2024
    }
});

// Adiciona um ouvinte de evento ao botão de adicionar tarefa
addTaskButton.addEventListener('click', addTask);

// Função para adicionar uma nova tarefa
function addTask() {
    const taskText = newTaskInput.value.trim();
    const taskDate = taskDateInput.value; // Obtém a data da tarefa
    const taskTime = taskTimeInput.value; // Obtém a hora da tarefa

    if (taskText === '') {
        alert('Por favor, insira uma tarefa.');
        return;
    }

    // Cria um elemento de lista para a nova tarefa
    const li = document.createElement('li');
    li.textContent = `${taskText} - ${taskDate} ${taskTime}`; // Inclui data e hora

    // Adiciona um botão de remover a cada tarefa
    const removeButton = document.createElement('button');
    removeButton.textContent = 'Remover';
    removeButton.className = 'remove-button';
    removeButton.addEventListener('click', () => {
        li.remove();
        saveTasks();
    });

    li.appendChild(removeButton);
    li.addEventListener('click', () => {
        li.classList.toggle('completed');
        saveTasks();
    });
    taskList.appendChild(li);

    // Limpa os campos de entrada
    newTaskInput.value = '';
    taskDateInput.value = '';
    taskTimeInput.value = '';

    saveTasks();
}

// Função para salvar tarefas no Local Storage
function saveTasks() {
    const tasks = [];
    taskList.querySelectorAll('li').forEach(task => {
        const [taskText, taskDate, taskTime] = task.textContent.replace('Remover', '').split(' - ').map(item => item.trim());
        tasks.push({
            text: taskText,
            date: taskDate,
            time: taskTime,
            completed: task.classList.contains('completed')
        });
    });
    localStorage.setItem('tasks', JSON.stringify(tasks));
}

// Função para carregar tarefas do Local Storage
function loadTasks() {
    const savedTasks = JSON.parse(localStorage.getItem('tasks'));
    if (savedTasks) {
        savedTasks.forEach(task => {
            const li = document.createElement('li');
            li.textContent = `${task.text} - ${task.date} ${task.time}`;

            if (task.completed) {
                li.classList.add('completed');
            }

            const removeButton = document.createElement('button');
            removeButton.textContent = 'Remover';
            removeButton.className = 'remove-button';
            removeButton.addEventListener('click', () => {
                li.remove();
                saveTasks();
            });

            li.appendChild(removeButton);
            li.addEventListener('click', () => {
                li.classList.toggle('completed');
                saveTasks();
            });
            taskList.appendChild(li);
        });
    }
}
