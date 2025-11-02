
# Create all complete code files and save them as CSV

# Day 3: Algorithms
algorithms_js = """// ============================================================
// Algorithms & Big O Analysis - Smart Task Manager Training
// Day 3: Problem Solving & Complexity Analysis
// ============================================================

console.log("=== Algorithms & Big O Analysis ===\\n");

// ============================================================
// 1. FIBONACCI SEQUENCE
// ============================================================
console.log("1. Fibonacci Sequence:\\n");

// Recursive approach - O(2^n) time, O(n) space
function fibonacciRecursive(n) {
    if (n <= 1) return n;
    return fibonacciRecursive(n - 1) + fibonacciRecursive(n - 2);
}

// Iterative approach - O(n) time, O(1) space
function fibonacciIterative(n) {
    if (n <= 1) return n;
    
    let prev = 0, curr = 1;
    for (let i = 2; i <= n; i++) {
        let next = prev + curr;
        prev = curr;
        curr = next;
    }
    return curr;
}

// Dynamic Programming approach - O(n) time, O(n) space
function fibonacciDP(n, memo = {}) {
    if (n in memo) return memo[n];
    if (n <= 1) return n;
    
    memo[n] = fibonacciDP(n - 1, memo) + fibonacciDP(n - 2, memo);
    return memo[n];
}

console.log("Fibonacci sequence (first 10 numbers):");
for (let i = 0; i < 10; i++) {
    console.log(`  F(${i}) = ${fibonacciIterative(i)}`);
}

console.log("\\nTime Complexity:");
console.log("  Recursive: O(2^n) - Exponential");
console.log("  Iterative: O(n) - Linear");
console.log("  DP: O(n) - Linear with memoization\\n");

// ============================================================
// 2. PALINDROME CHECKER
// ============================================================
console.log("2. Palindrome Checker:\\n");

// Two-pointer approach - O(n) time, O(1) space
function isPalindrome(str) {
    // Remove non-alphanumeric and convert to lowercase
    const cleaned = str.toLowerCase().replace(/[^a-z0-9]/g, '');
    
    let left = 0;
    let right = cleaned.length - 1;
    
    while (left < right) {
        if (cleaned[left] !== cleaned[right]) {
            return false;
        }
        left++;
        right--;
    }
    return true;
}

// Recursive approach - O(n) time, O(n) space
function isPalindromeRecursive(str) {
    const cleaned = str.toLowerCase().replace(/[^a-z0-9]/g, '');
    
    function checkPalindrome(s, left, right) {
        if (left >= right) return true;
        if (s[left] !== s[right]) return false;
        return checkPalindrome(s, left + 1, right - 1);
    }
    
    return checkPalindrome(cleaned, 0, cleaned.length - 1);
}

const testStrings = [
    "racecar",
    "A man a plan a canal Panama",
    "hello",
    "Madam",
    "12321"
];

console.log("Testing palindromes:");
testStrings.forEach(str => {
    console.log(`  "${str}" -> ${isPalindrome(str)}`);
});

console.log("\\nTime Complexity: O(n) - Linear");
console.log("Space Complexity: O(1) for iterative, O(n) for recursive\\n");

// ============================================================
// 3. LINEAR SEARCH
// ============================================================
console.log("3. Linear Search:\\n");

// O(n) time, O(1) space
function linearSearch(arr, target) {
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] === target) {
            return i;
        }
    }
    return -1;
}

const numbers = [64, 34, 25, 12, 22, 11, 90, 88, 45, 50];
console.log("Array:", numbers);
console.log(`Search for 22: index = ${linearSearch(numbers, 22)}`);
console.log(`Search for 99: index = ${linearSearch(numbers, 99)}`);

console.log("\\nTime Complexity: O(n) - Linear");
console.log("Space Complexity: O(1) - Constant");
console.log("Best Case: O(1) - element at first position");
console.log("Worst Case: O(n) - element at last position or not found\\n");

// ============================================================
// 4. BINARY SEARCH
// ============================================================
console.log("4. Binary Search:\\n");

// Iterative - O(log n) time, O(1) space
function binarySearch(arr, target) {
    let left = 0;
    let right = arr.length - 1;
    
    while (left <= right) {
        const mid = Math.floor((left + right) / 2);
        
        if (arr[mid] === target) {
            return mid;
        } else if (arr[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    return -1;
}

// Recursive - O(log n) time, O(log n) space
function binarySearchRecursive(arr, target, left = 0, right = arr.length - 1) {
    if (left > right) return -1;
    
    const mid = Math.floor((left + right) / 2);
    
    if (arr[mid] === target) {
        return mid;
    } else if (arr[mid] < target) {
        return binarySearchRecursive(arr, target, mid + 1, right);
    } else {
        return binarySearchRecursive(arr, target, left, mid - 1);
    }
}

const sortedNumbers = [11, 12, 22, 25, 34, 45, 50, 64, 88, 90];
console.log("Sorted Array:", sortedNumbers);
console.log(`Binary search for 45: index = ${binarySearch(sortedNumbers, 45)}`);
console.log(`Binary search for 99: index = ${binarySearch(sortedNumbers, 99)}`);

console.log("\\nTime Complexity: O(log n) - Logarithmic");
console.log("Space Complexity: O(1) iterative, O(log n) recursive");
console.log("Note: Requires sorted array\\n");

// ============================================================
// 5. MERGE SORT
// ============================================================
console.log("5. Merge Sort:\\n");

// O(n log n) time, O(n) space
function mergeSort(arr) {
    if (arr.length <= 1) return arr;
    
    const mid = Math.floor(arr.length / 2);
    const left = mergeSort(arr.slice(0, mid));
    const right = mergeSort(arr.slice(mid));
    
    return merge(left, right);
}

function merge(left, right) {
    const result = [];
    let leftIndex = 0;
    let rightIndex = 0;
    
    while (leftIndex < left.length && rightIndex < right.length) {
        if (left[leftIndex] < right[rightIndex]) {
            result.push(left[leftIndex]);
            leftIndex++;
        } else {
            result.push(right[rightIndex]);
            rightIndex++;
        }
    }
    
    return result
        .concat(left.slice(leftIndex))
        .concat(right.slice(rightIndex));
}

const unsorted = [64, 34, 25, 12, 22, 11, 90, 88, 45, 50];
console.log("Unsorted:", unsorted);
console.log("Sorted:  ", mergeSort(unsorted));

console.log("\\nTime Complexity: O(n log n) - Linearithmic");
console.log("Space Complexity: O(n) - Linear");
console.log("Stable: Yes");
console.log("Best for: Large datasets, linked lists\\n");

// ============================================================
// 6. PERFORMANCE BENCHMARKING
// ============================================================
console.log("6. Performance Benchmarking:\\n");

function benchmark(fn, ...args) {
    const start = performance.now();
    const result = fn(...args);
    const end = performance.now();
    return { result, time: end - start };
}

// Fibonacci comparison
console.log("Fibonacci(30) comparison:");
const fibIter = benchmark(fibonacciIterative, 30);
const fibDP = benchmark(fibonacciDP, 30);
console.log(`  Iterative: ${fibIter.time.toFixed(4)}ms`);
console.log(`  DP: ${fibDP.time.toFixed(4)}ms`);

// Search comparison
const largeArray = Array.from({ length: 10000 }, (_, i) => i);
console.log("\\nSearch in 10,000 elements:");
const linear = benchmark(linearSearch, largeArray, 9999);
const binary = benchmark(binarySearch, largeArray, 9999);
console.log(`  Linear Search: ${linear.time.toFixed(4)}ms`);
console.log(`  Binary Search: ${binary.time.toFixed(4)}ms`);

console.log("\\n=== End of Algorithms Demo ===");
"""

# Save algorithms
with open('algorithms.js', 'w', encoding='utf-8') as f:
    f.write(algorithms_js)

print("✓ Generated: algorithms.js")
print()
