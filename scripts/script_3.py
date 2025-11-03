
# Create Data Structures file

data_structures_js = """// ============================================================
// Data Structures & Recursion - Smart Task Manager Training
// Day 4: Stack, Queue, Binary Search Tree
// ============================================================

console.log("=== Data Structures & Recursion ===\\n");

// ============================================================
// 1. STACK IMPLEMENTATION
// ============================================================
console.log("1. Stack (LIFO - Last In First Out):\\n");

class Stack {
    constructor() {
        this.items = [];
    }

    // Push element to top - O(1)
    push(element) {
        this.items.push(element);
    }

    // Remove and return top element - O(1)
    pop() {
        if (this.isEmpty()) {
            return "Stack is empty";
        }
        return this.items.pop();
    }

    // View top element without removing - O(1)
    peek() {
        if (this.isEmpty()) {
            return "Stack is empty";
        }
        return this.items[this.items.length - 1];
    }

    // Check if stack is empty - O(1)
    isEmpty() {
        return this.items.length === 0;
    }

    // Get stack size - O(1)
    size() {
        return this.items.length;
    }

    // Clear stack - O(1)
    clear() {
        this.items = [];
    }

    // Print stack
    print() {
        console.log("  Stack:", this.items.join(" -> "));
    }
}

// Stack demonstration
const stack = new Stack();
console.log("Stack operations:");
stack.push(10);
stack.push(20);
stack.push(30);
stack.print();
console.log(`  Pop: ${stack.pop()}`);
console.log(`  Peek: ${stack.peek()}`);
stack.print();
console.log(`  Size: ${stack.size()}`);
console.log(`  Is empty: ${stack.isEmpty()}\\n`);

// Real-world example: Undo functionality
console.log("Stack use case - Undo functionality:");
class UndoManager {
    constructor() {
        this.actions = new Stack();
    }

    doAction(action) {
        this.actions.push(action);
        console.log(`  Action performed: ${action}`);
    }

    undo() {
        const action = this.actions.pop();
        if (action !== "Stack is empty") {
            console.log(`  Undoing: ${action}`);
        } else {
            console.log("  Nothing to undo");
        }
    }
}

const undoManager = new UndoManager();
undoManager.doAction("Type 'Hello'");
undoManager.doAction("Type ' World'");
undoManager.doAction("Add bold formatting");
undoManager.undo();
undoManager.undo();
console.log();

// ============================================================
// 2. QUEUE IMPLEMENTATION
// ============================================================
console.log("2. Queue (FIFO - First In First Out):\\n");

class Queue {
    constructor() {
        this.items = [];
    }

    // Add element to rear - O(1)
    enqueue(element) {
        this.items.push(element);
    }

    // Remove and return front element - O(n) for array, O(1) for linked list
    dequeue() {
        if (this.isEmpty()) {
            return "Queue is empty";
        }
        return this.items.shift();
    }

    // View front element - O(1)
    front() {
        if (this.isEmpty()) {
            return "Queue is empty";
        }
        return this.items[0];
    }

    // Check if queue is empty - O(1)
    isEmpty() {
        return this.items.length === 0;
    }

    // Get queue size - O(1)
    size() {
        return this.items.length;
    }

    // Clear queue - O(1)
    clear() {
        this.items = [];
    }

    // Print queue
    print() {
        console.log("  Queue:", this.items.join(" <- "));
    }
}

// Queue demonstration
const queue = new Queue();
console.log("Queue operations:");
queue.enqueue("Task 1");
queue.enqueue("Task 2");
queue.enqueue("Task 3");
queue.print();
console.log(`  Dequeue: ${queue.dequeue()}`);
console.log(`  Front: ${queue.front()}`);
queue.print();
console.log(`  Size: ${queue.size()}\\n`);

// Real-world example: Print job queue
console.log("Queue use case - Print job queue:");
class PrintQueue {
    constructor() {
        this.jobs = new Queue();
    }

    addJob(job) {
        this.jobs.enqueue(job);
        console.log(`  Added to queue: ${job}`);
    }

    processNext() {
        const job = this.jobs.dequeue();
        if (job !== "Queue is empty") {
            console.log(`  Processing: ${job}`);
        } else {
            console.log("  No jobs to process");
        }
    }
}

const printer = new PrintQueue();
printer.addJob("Document1.pdf");
printer.addJob("Report.docx");
printer.addJob("Photo.jpg");
printer.processNext();
printer.processNext();
console.log();

// ============================================================
// 3. BINARY SEARCH TREE (BST)
// ============================================================
console.log("3. Binary Search Tree:\\n");

class TreeNode {
    constructor(value) {
        this.value = value;
        this.left = null;
        this.right = null;
    }
}

class BinarySearchTree {
    constructor() {
        this.root = null;
    }

    // Insert value - O(log n) average, O(n) worst
    insert(value) {
        const newNode = new TreeNode(value);

        if (this.root === null) {
            this.root = newNode;
            return this;
        }

        let current = this.root;
        while (true) {
            if (value === current.value) return undefined; // No duplicates
            
            if (value < current.value) {
                if (current.left === null) {
                    current.left = newNode;
                    return this;
                }
                current = current.left;
            } else {
                if (current.right === null) {
                    current.right = newNode;
                    return this;
                }
                current = current.right;
            }
        }
    }

    // Search for value - O(log n) average, O(n) worst
    search(value) {
        let current = this.root;

        while (current !== null) {
            if (value === current.value) {
                return true;
            } else if (value < current.value) {
                current = current.left;
            } else {
                current = current.right;
            }
        }
        return false;
    }

    // In-order traversal (sorted order) - O(n)
    inOrderTraversal(node = this.root, result = []) {
        if (node !== null) {
            this.inOrderTraversal(node.left, result);
            result.push(node.value);
            this.inOrderTraversal(node.right, result);
        }
        return result;
    }

    // Pre-order traversal - O(n)
    preOrderTraversal(node = this.root, result = []) {
        if (node !== null) {
            result.push(node.value);
            this.preOrderTraversal(node.left, result);
            this.preOrderTraversal(node.right, result);
        }
        return result;
    }

    // Post-order traversal - O(n)
    postOrderTraversal(node = this.root, result = []) {
        if (node !== null) {
            this.postOrderTraversal(node.left, result);
            this.postOrderTraversal(node.right, result);
            result.push(node.value);
        }
        return result;
    }

    // Level-order traversal (BFS) - O(n)
    levelOrderTraversal() {
        if (this.root === null) return [];

        const result = [];
        const queue = [this.root];

        while (queue.length > 0) {
            const node = queue.shift();
            result.push(node.value);

            if (node.left !== null) queue.push(node.left);
            if (node.right !== null) queue.push(node.right);
        }

        return result;
    }

    // Find minimum value - O(log n)
    findMin(node = this.root) {
        if (node === null) return null;
        while (node.left !== null) {
            node = node.left;
        }
        return node.value;
    }

    // Find maximum value - O(log n)
    findMax(node = this.root) {
        if (node === null) return null;
        while (node.right !== null) {
            node = node.right;
        }
        return node.value;
    }

    // Get tree height - O(n)
    getHeight(node = this.root) {
        if (node === null) return -1;
        return 1 + Math.max(
            this.getHeight(node.left),
            this.getHeight(node.right)
        );
    }

    // Count nodes - O(n)
    countNodes(node = this.root) {
        if (node === null) return 0;
        return 1 + this.countNodes(node.left) + this.countNodes(node.right);
    }
}

// BST demonstration
const bst = new BinarySearchTree();
console.log("Building BST with values: 50, 30, 70, 20, 40, 60, 80");
[50, 30, 70, 20, 40, 60, 80].forEach(val => bst.insert(val));

console.log("\\nTree Traversals:");
console.log("  In-order (sorted):", bst.inOrderTraversal());
console.log("  Pre-order:", bst.preOrderTraversal());
console.log("  Post-order:", bst.postOrderTraversal());
console.log("  Level-order (BFS):", bst.levelOrderTraversal());

console.log("\\nTree Properties:");
console.log(`  Min value: ${bst.findMin()}`);
console.log(`  Max value: ${bst.findMax()}`);
console.log(`  Height: ${bst.getHeight()}`);
console.log(`  Total nodes: ${bst.countNodes()}`);

console.log("\\nSearch operations:");
console.log(`  Search 40: ${bst.search(40)}`);
console.log(`  Search 100: ${bst.search(100)}`);

// ============================================================
// 4. RECURSION EXAMPLES
// ============================================================
console.log("\\n4. Recursion Examples:\\n");

// Factorial - O(n) time, O(n) space
function factorial(n) {
    if (n <= 1) return 1;
    return n * factorial(n - 1);
}

console.log("Factorial:");
for (let i = 0; i <= 5; i++) {
    console.log(`  ${i}! = ${factorial(i)}`);
}

// Sum of array - O(n) time, O(n) space
function sumArray(arr, index = 0) {
    if (index >= arr.length) return 0;
    return arr[index] + sumArray(arr, index + 1);
}

const numbers = [1, 2, 3, 4, 5];
console.log(`\\nSum of ${numbers}: ${sumArray(numbers)}`);

// Power function - O(log n) time with optimization
function power(base, exponent) {
    if (exponent === 0) return 1;
    if (exponent === 1) return base;
    
    if (exponent % 2 === 0) {
        const half = power(base, exponent / 2);
        return half * half;
    } else {
        return base * power(base, exponent - 1);
    }
}

console.log(`\\nPower function:`);
console.log(`  2^10 = ${power(2, 10)}`);
console.log(`  3^5 = ${power(3, 5)}`);

console.log("\\n=== End of Data Structures Demo ===");
"""

with open('data-structures.js', 'w', encoding='utf-8') as f:
    f.write(data_structures_js)

print("✓ Generated: data-structures.js")
