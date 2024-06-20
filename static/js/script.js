document.addEventListener('DOMContentLoaded', function() {
    loadTasks();

    document.getElementById('task-form').addEventListener('submit', function(e) {
        e.preventDefault();
        const taskId = document.getElementById('task-id').value;
        const taskName = document.getElementById('task-name').value;
        const taskTitle = document.getElementById('task-title').value;
        const taskDescription = document.getElementById('task-description').value;

        const taskData = {
            name: taskName,
            title: taskTitle,
            description: taskDescription
        };

        if (taskId) {
            // Update task
            axios.put(`/tasks/${taskId}`, taskData)
                .then(response => {
                    $('#taskModal').modal('hide');
                    loadTasks();
                });
        } else {
            // Create new task
            axios.post('/tasks', taskData)
                .then(response => {
                    $('#taskModal').modal('hide');
                    loadTasks();
                });
        }
    });
});

function loadTasks() {
    axios.get('/tasks')
        .then(response => {
            const taskList = document.getElementById('task-list');
            taskList.innerHTML = '';

            response.data.forEach(task => {
                const taskElement = document.createElement('div');
                taskElement.className = 'task';
                taskElement.innerHTML = `
                    <div class="task-actions">
                        <h5>${task.title}</h5>
                        <div>
                            <button class="btn btn-sm btn-info" onclick="editTask(${task.id})">Edit</button>
                            <button class="btn btn-sm btn-danger" onclick="deleteTask(${task.id})">Delete</button>
                        </div>
                    </div>
                    <p><strong>Name:</strong> ${task.name}</p>
                    <p><strong>Description:</strong> ${task.description}</p>
                `;
                taskList.appendChild(taskElement);
            });
        });
}

function editTask(id) {
    axios.get(`/tasks/${id}`)
        .then(response => {
            const task = response.data;
            document.getElementById('task-id').value = task.id;
            document.getElementById('task-name').value = task.name;
            document.getElementById('task-title').value = task.title;
            document.getElementById('task-description').value = task.description;
            $('#taskModal').modal('show');
        });
}

function deleteTask(id) {
    axios.delete(`/tasks/${id}`)
        .then(response => {
            loadTasks();
        });
}
