
# Create comprehensive code files for Week 1 - Day 1-2: JavaScript Fundamentals

fundamentals_js = """// ============================================================
// JavaScript Fundamentals - Smart Task Manager Training
// Day 1-2: Syntax, Functions, and Logic
// ============================================================

console.log("=== JavaScript Fundamentals Demo ===\\n");

// ============================================================
// 1. VARIABLE DECLARATIONS (let, const, var)
// ============================================================
console.log("1. Variable Declarations:");

// let - block-scoped, can be reassigned
let userName = "Ahmad";
console.log(`Using let: userName = ${userName}`);
userName = "Ali";
console.log(`After reassignment: userName = ${userName}`);

// const - block-scoped, cannot be reassigned
const MAX_TASKS = 100;
console.log(`Using const: MAX_TASKS = ${MAX_TASKS}`);

// var - function-scoped (old way, avoid in modern code)
var legacyVariable = "old style";
console.log(`Using var: legacyVariable = ${legacyVariable}\\n`);

// ============================================================
// 2. ARROW FUNCTIONS
// ============================================================
console.log("2. Arrow Functions:");

// Traditional function
function traditionalAdd(a, b) {
    return a + b;
}

// Arrow function - concise syntax
const arrowAdd = (a, b) => a + b;

// Arrow function with body
const arrowMultiply = (a, b) => {
    const result = a * b;
    return result;
};

console.log(`Traditional function: 5 + 3 = ${traditionalAdd(5, 3)}`);
console.log(`Arrow function: 5 + 3 = ${arrowAdd(5, 3)}`);
console.log(`Arrow function with body: 5 * 3 = ${arrowMultiply(5, 3)}\\n`);

// ============================================================
// 3. TEMPLATE LITERALS
// ============================================================
console.log("3. Template Literals:");

const taskName = "Complete training project";
const priority = "High";
const dueDate = "November 15, 2025";

// Old way with concatenation
console.log("Old way: Task: " + taskName + ", Priority: " + priority);

// Modern way with template literals
console.log(`Modern way: Task: ${taskName}, Priority: ${priority}`);
console.log(`Full details: "${taskName}" is due on ${dueDate} with ${priority} priority\\n`);

// Multi-line template literals
const taskSummary = `
Task Summary:
-------------
Name: ${taskName}
Priority: ${priority}
Due: ${dueDate}
Status: In Progress
`;
console.log(taskSummary);

// ============================================================
// 4. OBJECTS AND OBJECT DESTRUCTURING
// ============================================================
console.log("4. Objects and Destructuring:");

const task = {
    id: 1,
    title: "Build REST API",
    description: "Create Java backend with Dropwizard",
    priority: "High",
    completed: false,
    assignee: {
        name: "Ahmad",
        email: "ahmad@example.com"
    }
};

console.log("Task object:", task);

// Object destructuring
const { title, priority: taskPriority, assignee } = task;
console.log(`Destructured - Title: ${title}, Priority: ${taskPriority}`);
console.log(`Assignee: ${assignee.name} (${assignee.email})\\n`);

// ============================================================
// 5. ARRAYS AND ARRAY METHODS
// ============================================================
console.log("5. Arrays and Array Methods:");

const tasks = [
    { id: 1, title: "Setup project", priority: 3 },
    { id: 2, title: "Write code", priority: 1 },
    { id: 3, title: "Test application", priority: 2 },
    { id: 4, title: "Deploy", priority: 1 }
];

console.log("Original tasks:", tasks);

// map - transform array elements
const taskTitles = tasks.map(t => t.title);
console.log("Task titles (map):", taskTitles);

// filter - select elements matching condition
const highPriorityTasks = tasks.filter(t => t.priority === 1);
console.log("High priority tasks (filter):", highPriorityTasks);

// find - get first matching element
const testTask = tasks.find(t => t.title.includes("Test"));
console.log("Test task (find):", testTask);

// reduce - aggregate values
const totalPriority = tasks.reduce((sum, t) => sum + t.priority, 0);
console.log(`Total priority sum (reduce): ${totalPriority}\\n`);

// ============================================================
// 6. CONTROL FLOW AND LOGIC
// ============================================================
console.log("6. Control Flow:");

function getTaskStatus(task) {
    if (task.priority === 1) {
        return "URGENT";
    } else if (task.priority === 2) {
        return "IMPORTANT";
    } else {
        return "NORMAL";
    }
}

// Ternary operator
const getStatusShort = (priority) => priority === 1 ? "URGENT" : "NORMAL";

console.log("Task statuses:");
tasks.forEach(t => {
    console.log(`  ${t.title}: ${getTaskStatus(t)}`);
});

// Switch statement
function getDayActivity(day) {
    switch(day) {
        case 1:
        case 2:
            return "JavaScript Fundamentals";
        case 3:
            return "Algorithms & Big O";
        case 4:
            return "Data Structures";
        case 5:
            return "Async JS & APIs";
        default:
            return "Project work";
    }
}

console.log(`\\nDay 3 activity: ${getDayActivity(3)}\\n`);

// ============================================================
// 7. HIGHER-ORDER FUNCTIONS
// ============================================================
console.log("7. Higher-Order Functions:");

// Function that returns a function
const createMultiplier = (factor) => {
    return (number) => number * factor;
};

const double = createMultiplier(2);
const triple = createMultiplier(3);

console.log(`Double 5: ${double(5)}`);
console.log(`Triple 5: ${triple(5)}`);

// Function that accepts a function as parameter
const processTask = (task, processor) => {
    return processor(task);
};

const formatTask = (t) => `[${t.id}] ${t.title}`;
console.log("\\nFormatted tasks:");
tasks.forEach(t => console.log(`  ${processTask(t, formatTask)}`));

// ============================================================
// 8. CLASSES AND OOP
// ============================================================
console.log("\\n8. Classes and Object-Oriented Programming:");

class Task {
    constructor(id, title, priority = 3) {
        this.id = id;
        this.title = title;
        this.priority = priority;
        this.completed = false;
        this.createdAt = new Date();
    }

    complete() {
        this.completed = true;
        console.log(`Task "${this.title}" marked as complete!`);
    }

    updatePriority(newPriority) {
        this.priority = newPriority;
        console.log(`Task "${this.title}" priority updated to ${newPriority}`);
    }

    getInfo() {
        return `Task #${this.id}: ${this.title} [Priority: ${this.priority}, Completed: ${this.completed}]`;
    }
}

const newTask = new Task(5, "Review code");
console.log(newTask.getInfo());
newTask.updatePriority(1);
newTask.complete();
console.log(newTask.getInfo());

// ============================================================
// 9. SPREAD AND REST OPERATORS
// ============================================================
console.log("\\n9. Spread and Rest Operators:");

// Spread operator - expand array
const moreTasks = [
    { id: 5, title: "Documentation" },
    { id: 6, title: "Code review" }
];

const allTasks = [...tasks, ...moreTasks];
console.log(`Original tasks count: ${tasks.length}`);
console.log(`All tasks count: ${allTasks.length}`);

// Rest parameter - collect arguments
const createTask = (id, title, ...tags) => {
    return {
        id,
        title,
        tags: tags
    };
};

const taggedTask = createTask(7, "New feature", "frontend", "ui", "javascript");
console.log("Task with tags:", taggedTask);

// ============================================================
// 10. ERROR HANDLING
// ============================================================
console.log("\\n10. Error Handling:");

function divideNumbers(a, b) {
    try {
        if (b === 0) {
            throw new Error("Cannot divide by zero!");
        }
        return a / b;
    } catch (error) {
        console.error(`Error: ${error.message}`);
        return null;
    } finally {
        console.log("Division operation completed");
    }
}

console.log(`10 / 2 = ${divideNumbers(10, 2)}`);
console.log(`10 / 0 = ${divideNumbers(10, 0)}`);

console.log("\\n=== End of JavaScript Fundamentals Demo ===");
"""

print("Generated: fundamentals.js")
print("=" * 80)
print(fundamentals_js[:500] + "...\n")
