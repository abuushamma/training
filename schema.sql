-- ============================================================
-- Smart Task Manager Database Schema
-- Day 10: JDBC + MySQL
-- ============================================================

-- Create database
CREATE DATABASE IF NOT EXISTS task_manager;
USE task_manager;

-- ============================================================
-- Users Table
-- ============================================================
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_email (email),
    INDEX idx_username (username)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ============================================================
-- Tasks Table
-- ============================================================
CREATE TABLE IF NOT EXISTS tasks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    description TEXT,
    user_id INT NOT NULL,
    priority ENUM('LOW', 'MEDIUM', 'HIGH', 'URGENT') DEFAULT 'MEDIUM',
    status ENUM('TODO', 'IN_PROGRESS', 'COMPLETED', 'CANCELLED') DEFAULT 'TODO',
    due_date TIMESTAMP NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    INDEX idx_user_id (user_id),
    INDEX idx_status (status),
    INDEX idx_priority (priority),
    INDEX idx_due_date (due_date)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ============================================================
-- Sample Data (for testing)
-- ============================================================

-- Insert sample users
INSERT INTO users (username, email, password) VALUES
('ahmad', 'ahmad@example.com', 'password123'),
('sarah', 'sarah@example.com', 'password123'),
('john', 'john@example.com', 'password123');

-- Insert sample tasks
INSERT INTO tasks (title, description, user_id, priority, status, due_date) VALUES
('Setup development environment', 'Install Java, Maven, MySQL, and IntelliJ IDEA', 1, 'HIGH', 'COMPLETED', '2025-11-01 10:00:00'),
('Learn JavaScript fundamentals', 'Study variables, functions, and control flow', 1, 'HIGH', 'COMPLETED', '2025-11-02 15:00:00'),
('Implement algorithms', 'Create Fibonacci, palindrome, and search algorithms', 1, 'MEDIUM', 'COMPLETED', '2025-11-03 12:00:00'),
('Build data structures', 'Implement Stack, Queue, and Binary Search Tree', 1, 'MEDIUM', 'IN_PROGRESS', '2025-11-04 14:00:00'),
('Create Weather Dashboard', 'Build async API integration with fetch()', 1, 'MEDIUM', 'TODO', '2025-11-05 16:00:00'),
('Setup Git repository', 'Initialize repo and create branches', 1, 'HIGH', 'TODO', '2025-11-06 10:00:00'),
('Build Java backend', 'Create REST API with Dropwizard', 1, 'URGENT', 'TODO', '2025-11-08 18:00:00'),
('Connect frontend to backend', 'Integrate JavaScript frontend with Java API', 1, 'URGENT', 'TODO', '2025-11-13 20:00:00'),
('Write documentation', 'Create comprehensive README with setup instructions', 1, 'MEDIUM', 'TODO', '2025-11-14 17:00:00'),
('Prepare presentation', 'Demo project functionality', 1, 'HIGH', 'TODO', '2025-11-14 19:00:00');

-- ============================================================
-- Useful Queries
-- ============================================================

-- Get all tasks for a specific user
-- SELECT * FROM tasks WHERE user_id = 1 ORDER BY created_at DESC;

-- Get high priority tasks
-- SELECT * FROM tasks WHERE priority IN ('HIGH', 'URGENT') ORDER BY due_date;

-- Get completed tasks
-- SELECT * FROM tasks WHERE status = 'COMPLETED';

-- Get tasks due soon (next 7 days)
-- SELECT * FROM tasks WHERE due_date BETWEEN NOW() AND DATE_ADD(NOW(), INTERVAL 7 DAY);

-- Get user task statistics
-- SELECT 
--     u.username,
--     COUNT(t.id) as total_tasks,
--     SUM(CASE WHEN t.status = 'COMPLETED' THEN 1 ELSE 0 END) as completed_tasks,
--     SUM(CASE WHEN t.status = 'TODO' THEN 1 ELSE 0 END) as pending_tasks
-- FROM users u
-- LEFT JOIN tasks t ON u.id = t.user_id
-- GROUP BY u.id, u.username;