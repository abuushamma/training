
# Generate the final integrated JavaScript frontend with full backend integration

final_app_js = """// ============================================================
// Smart Task Manager - Frontend Application
// Day 13: Frontend-Backend Integration
// ============================================================

// Configuration
const API_BASE_URL = 'http://localhost:8080/api';
const CURRENT_USER_ID = 1; // Default user for demo

// DOM Elements
const taskForm = document.getElementById('taskForm');
const tasksList = document.getElementById('tasksList');
const loadingState = document.getElementById('loadingState');
const errorState = document.getElementById('errorState');
const errorMessage = document.getElementById('errorMessage');
const taskCountElement = document.getElementById('taskCount');
const filterButtons = document.querySelectorAll('.filter-btn');

// State
let currentFilter = 'all';
let allTasks = [];

// ============================================================
// API FUNCTIONS
// ============================================================

/**
 * Fetch all tasks from the backend
 */
async function fetchTasks() {
    try {
        showLoading();
        hideError();

        const response = await fetch(`${API_BASE_URL}/tasks?userId=${CURRENT_USER_ID}`);
        
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }

        const tasks = await response.json();
        allTasks = tasks;
        
        hideLoading();
        displayTasks(tasks);
        updateTaskCount(tasks.length);

    } catch (error) {
        hideLoading();
        showError(`Failed to load tasks: ${error.message}. Make sure the backend server is running on port 8080.`);
        console.error('Fetch tasks error:', error);
    }
}

/**
 * Create a new task
 */
async function createTask(taskData) {
    try {
        showLoading();
        hideError();

        const response = await fetch(`${API_BASE_URL}/tasks`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(taskData)
        });

        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(errorData.error || 'Failed to create task');
        }

        const createdTask = await response.json();
        
        hideLoading();
        
        // Refresh tasks list
        await fetchTasks();
        
        // Reset form
        taskForm.reset();
        
        console.log('Task created successfully:', createdTask);

    } catch (error) {
        hideLoading();
        showError(`Failed to create task: ${error.message}`);
        console.error('Create task error:', error);
    }
}

/**
 * Update task status
 */
async function updateTaskStatus(taskId, newStatus) {
    try {
        // Get current task data
        const task = allTasks.find(t => t.id === taskId);
        if (!task) return;

        const updatedTask = {
            ...task,
            status: newStatus
        };

        const response = await fetch(`${API_BASE_URL}/tasks/${taskId}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(updatedTask)
        });

        if (!response.ok) {
            throw new Error('Failed to update task');
        }

        // Refresh tasks list
        await fetchTasks();

    } catch (error) {
        showError(`Failed to update task: ${error.message}`);
        console.error('Update task error:', error);
    }
}

/**
 * Delete a task
 */
async function deleteTask(taskId) {
    try {
        const response = await fetch(`${API_BASE_URL}/tasks/${taskId}`, {
            method: 'DELETE'
        });

        if (!response.ok) {
            throw new Error('Failed to delete task');
        }

        // Refresh tasks list
        await fetchTasks();

    } catch (error) {
        showError(`Failed to delete task: ${error.message}`);
        console.error('Delete task error:', error);
    }
}

// ============================================================
// UI FUNCTIONS
// ============================================================

/**
 * Display tasks in the UI
 */
function displayTasks(tasks) {
    // Filter tasks based on current filter
    let filteredTasks = tasks;
    if (currentFilter !== 'all') {
        filteredTasks = tasks.filter(task => task.status === currentFilter);
    }

    if (filteredTasks.length === 0) {
        tasksList.innerHTML = `
            <div class="empty-state">
                <h3>No tasks found</h3>
                <p>Create your first task using the form above!</p>
            </div>
        `;
        return;
    }

    tasksList.innerHTML = filteredTasks.map(task => createTaskCard(task)).join('');
}

/**
 * Create HTML for a task card
 */
function createTaskCard(task) {
    const completedClass = task.status === 'COMPLETED' ? 'completed' : '';
    const dueDate = task.dueDate ? new Date(task.dueDate).toLocaleString() : 'No due date';
    const createdDate = new Date(task.createdAt).toLocaleString();

    return `
        <div class="task-card priority-${task.priority} ${completedClass}" data-task-id="${task.id}">
            <div class="task-header">
                <h3 class="task-title">${escapeHtml(task.title)}</h3>
                <div class="task-badges">
                    <span class="badge badge-priority ${task.priority}">${task.priority}</span>
                    <span class="badge badge-status ${task.status}">${formatStatus(task.status)}</span>
                </div>
            </div>
            
            ${task.description ? `<p class="task-description">${escapeHtml(task.description)}</p>` : ''}
            
            <div class="task-meta">
                <span>📅 Due: ${dueDate}</span>
                <span>🕒 Created: ${createdDate}</span>
            </div>
            
            <div class="task-actions">
                ${task.status !== 'COMPLETED' ? 
                    `<button class="btn btn-success" onclick="completeTask(${task.id})">✓ Complete</button>` : 
                    `<button class="btn btn-success" onclick="updateTaskStatus(${task.id}, 'TODO')">↺ Reopen</button>`
                }
                ${task.status === 'TODO' ? 
                    `<button class="btn btn-primary" onclick="updateTaskStatus(${task.id}, 'IN_PROGRESS')">▶ Start</button>` : ''
                }
                <button class="btn btn-danger" onclick="confirmDelete(${task.id})">🗑 Delete</button>
            </div>
        </div>
    `;
}

/**
 * Complete a task
 */
async function completeTask(taskId) {
    await updateTaskStatus(taskId, 'COMPLETED');
}

/**
 * Confirm delete action
 */
function confirmDelete(taskId) {
    if (confirm('Are you sure you want to delete this task?')) {
        deleteTask(taskId);
    }
}

/**
 * Format status for display
 */
function formatStatus(status) {
    return status.replace('_', ' ');
}

/**
 * Escape HTML to prevent XSS
 */
function escapeHtml(text) {
    const map = {
        '&': '&amp;',
        '<': '&lt;',
        '>': '&gt;',
        '"': '&quot;',
        "'": '&#039;'
    };
    return text.replace(/[&<>"']/g, m => map[m]);
}

/**
 * Update task count display
 */
function updateTaskCount(count) {
    taskCountElement.textContent = `Tasks: ${count}`;
}

/**
 * Show loading state
 */
function showLoading() {
    loadingState.classList.remove('hidden');
    tasksList.classList.add('hidden');
}

/**
 * Hide loading state
 */
function hideLoading() {
    loadingState.classList.add('hidden');
    tasksList.classList.remove('hidden');
}

/**
 * Show error message
 */
function showError(message) {
    errorMessage.textContent = message;
    errorState.classList.remove('hidden');
}

/**
 * Hide error message
 */
function hideError() {
    errorState.classList.add('hidden');
}

// ============================================================
// EVENT LISTENERS
// ============================================================

/**
 * Handle task form submission
 */
taskForm.addEventListener('submit', async (e) => {
    e.preventDefault();

    const title = document.getElementById('taskTitle').value.trim();
    const description = document.getElementById('taskDescription').value.trim();
    const priority = document.getElementById('taskPriority').value;
    const dueDateInput = document.getElementById('taskDueDate').value;

    if (!title) {
        showError('Please enter a task title');
        return;
    }

    const taskData = {
        title: title,
        description: description,
        userId: CURRENT_USER_ID,
        priority: priority,
        status: 'TODO'
    };

    // Add due date if provided
    if (dueDateInput) {
        taskData.dueDate = new Date(dueDateInput).toISOString();
    }

    await createTask(taskData);
});

/**
 * Handle filter button clicks
 */
filterButtons.forEach(button => {
    button.addEventListener('click', () => {
        // Update active state
        filterButtons.forEach(btn => btn.classList.remove('active'));
        button.classList.add('active');

        // Update current filter
        currentFilter = button.dataset.filter;

        // Re-display tasks with new filter
        displayTasks(allTasks);
    });
});

// ============================================================
// INITIALIZATION
// ============================================================

/**
 * Initialize the application
 */
async function init() {
    console.log('Smart Task Manager - Initializing...');
    console.log('API URL:', API_BASE_URL);
    console.log('Current User ID:', CURRENT_USER_ID);

    // Load tasks on startup
    await fetchTasks();

    console.log('Smart Task Manager - Ready!');
    console.log('\\nMake sure your backend is running:');
    console.log('1. Start MySQL server');
    console.log('2. Run: java -jar target/smart-task-manager-1.0.0.jar server config.yml');
    console.log('3. Backend should be available at http://localhost:8080');
}

// Start the application when DOM is ready
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
} else {
    init();
}

// Make functions globally available for onclick handlers
window.completeTask = completeTask;
window.updateTaskStatus = updateTaskStatus;
window.confirmDelete = confirmDelete;"""

with open('final-app.js', 'w', encoding='utf-8') as f:
    f.write(final_app_js)

print("✓ Generated: final-app.js")
print("\nAll code files generated successfully!")
print("="*80)
