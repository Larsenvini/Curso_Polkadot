// Seleciona elementos do DOM

// Seleciona elementos do DOM
const newTaskInput = document.getElementById('newTask'); // Seleciona o campo de entrada de texto onde o usuário digita uma nova tarefa.
const addTaskButton = document.getElementById('addTaskButton'); // Seleciona o botão "Adicionar Tarefa" que o usuário clica para adicionar uma nova tarefa à lista.
const taskList = document.getElementById('taskList'); // Seleciona o elemento de lista (<ul>) onde as tarefas serão exibidas.

// Carrega tarefas salvas no Local Storage
document.addEventListener('DOMContentLoaded', loadTasks); // Adiciona um ouvinte de evento que chama a função 'loadTasks' quando o documento HTML é totalmente carregado. Isso garante que as tarefas armazenadas no Local Storage sejam carregadas e exibidas na tela quando a página é aberta.

// Adiciona um ouvinte de evento ao botão de adicionar tarefa
addTaskButton.addEventListener('click', addTask); // Adiciona um ouvinte de evento 'click' ao botão "Adicionar Tarefa". Quando o botão é clicado, a função 'addTask' é chamada para adicionar uma nova tarefa à lista.

// Função para adicionar uma nova tarefa
function addTask() {
    const taskText = newTaskInput.value.trim(); // Captura o texto digitado no campo de entrada de texto, removendo quaisquer espaços extras no início e no final.

    if (taskText === '') { // Verifica se o campo de entrada está vazio.
        alert('Por favor, insira uma tarefa.'); // Se estiver vazio, exibe um alerta para o usuário pedindo para inserir uma tarefa.
        return; // Interrompe a execução da função se o campo de entrada estiver vazio.
    }

    // Cria um elemento de lista para a nova tarefa
    const li = document.createElement('li'); // Cria um novo elemento de lista (<li>) para representar a nova tarefa.
    li.textContent = taskText; // Define o texto do novo elemento de lista como o texto digitado pelo usuário.

    // Adiciona um botão de remover a cada tarefa
    const removeButton = document.createElement('button'); // Cria um novo botão que será usado para remover a tarefa.
    removeButton.textContent = 'Remover'; // Define o texto do botão como "Remover".
    removeButton.className = 'remove-button'; // Adiciona uma classe CSS ao botão para estilização.
    removeButton.addEventListener('click', () => { // Adiciona um ouvinte de evento 'click' ao botão de remover.
        li.remove(); // Remove o elemento de lista correspondente ao botão clicado.
        saveTasks(); // Salva a lista atualizada de tarefas no Local Storage após a remoção.
    });

    // Adiciona a tarefa à lista e ao DOM
    li.appendChild(removeButton); // Adiciona o botão de remover como filho do elemento de lista (<li>).
    li.addEventListener('click', () => { // Adiciona um ouvinte de evento 'click' ao elemento de lista para marcar a tarefa como concluída.
        li.classList.toggle('completed'); // Alterna a classe 'completed' para o elemento de lista. Se a classe estiver presente, ela é removida; se não estiver presente, ela é adicionada.
        saveTasks(); // Salva o estado atualizado da tarefa no Local Storage (se está concluída ou não).
    });
    taskList.appendChild(li); // Adiciona o elemento de lista (<li>) ao elemento de lista não ordenada (<ul>), exibindo a nova tarefa na tela.

    // Limpa o campo de entrada de texto
    newTaskInput.value = ''; // Limpa o campo de entrada de texto após adicionar a tarefa para que o usuário possa digitar uma nova tarefa.

    saveTasks(); // Salva a lista atualizada de tarefas no Local Storage.
}

// Função para salvar tarefas no Local Storage
function saveTasks() {
    const tasks = []; // Cria um array vazio para armazenar as tarefas.
    taskList.querySelectorAll('li').forEach(task => { // Seleciona todos os elementos de lista (<li>) e itera sobre eles.
        tasks.push({
            text: task.textContent.replace('Remover', '').trim(), // Adiciona um objeto ao array de tarefas contendo o texto da tarefa (removendo o texto do botão 'Remover') e removendo espaços extras.
            completed: task.classList.contains('completed') // Verifica se a tarefa está marcada como concluída (contém a classe 'completed') e armazena o estado como booleano.
        });
    });
    localStorage.setItem('tasks', JSON.stringify(tasks)); // Converte o array de tarefas para uma string JSON e salva no Local Storage com a chave 'tasks'.
}

// Função para carregar tarefas do Local Storage
function loadTasks() {
    const savedTasks = JSON.parse(localStorage.getItem('tasks')); // Recupera as tarefas armazenadas no Local Storage e as converte de uma string JSON para um array de objetos.
    if (savedTasks) { // Verifica se existem tarefas salvas.
        savedTasks.forEach(task => { // Itera sobre cada tarefa salva e a recria na lista.
            const li = document.createElement('li'); // Cria um novo elemento de lista (<li>) para cada tarefa salva.
            li.textContent = task.text; // Define o texto do elemento de lista como o texto da tarefa salva.

            if (task.completed) { // Verifica se a tarefa estava marcada como concluída.
                li.classList.add('completed'); // Adiciona a classe 'completed' ao elemento de lista, marcando-o como concluído.
            }

            const removeButton = document.createElement('button'); // Cria um botão "Remover" para cada tarefa carregada.
            removeButton.textContent = 'Remover'; // Define o texto do botão como "Remover".
            removeButton.className = 'remove-button'; // Adiciona uma classe CSS ao botão para estilização.
            removeButton.addEventListener('click', () => { // Adiciona um ouvinte de evento 'click' ao botão de remover.
                li.remove(); // Remove o elemento de lista correspondente ao botão clicado.
                saveTasks(); // Salva a lista atualizada de tarefas no Local Storage após a remoção.
            });

            li.appendChild(removeButton); // Adiciona o botão de remover ao elemento de lista (<li>).
            li.addEventListener('click', () => { // Adiciona um ouvinte de evento 'click' ao elemento de lista para marcar a tarefa como concluída.
                li.classList.toggle('completed'); // Alterna a classe 'completed' para o elemento de lista. Se a classe estiver presente, ela é removida; se não estiver presente, ela é adicionada.
                saveTasks(); // Salva o estado atualizado da tarefa no Local Storage.
            });
            taskList.appendChild(li); // Adiciona o elemento de lista (<li>) ao elemento de lista não ordenada (<ul>), exibindo a tarefa carregada na tela.
        });
    }
}
