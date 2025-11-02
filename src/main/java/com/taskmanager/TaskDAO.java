package com.taskmanager.dao;

import com.taskmanager.models.Task;
import com.taskmanager.models.Task.Priority;
import com.taskmanager.models.Task.Status;
import java.sql.*;
import java.util.ArrayList;
import java.util.List;

/**
 * Task Data Access Object
 * Implements CRUD operations using JDBC
 * Day 10: JDBC + MySQL
 */
public class TaskDAO {

    private Connection connection;

    public TaskDAO(Connection connection) {
        this.connection = connection;
    }

    /**
     * Create a new task
     * @param task Task object to create
     * @return Created task with generated ID
     * @throws SQLException
     */
    public Task createTask(Task task) throws SQLException {
        String sql = "INSERT INTO tasks (title, description, user_id, priority, status, due_date, created_at, updated_at) " +
                     "VALUES (?, ?, ?, ?, ?, ?, ?, ?)";

        try (PreparedStatement stmt = connection.prepareStatement(sql, Statement.RETURN_GENERATED_KEYS)) {
            stmt.setString(1, task.getTitle());
            stmt.setString(2, task.getDescription());
            stmt.setInt(3, task.getUserId());
            stmt.setString(4, task.getPriority().name());
            stmt.setString(5, task.getStatus().name());
            stmt.setTimestamp(6, task.getDueDate() != null ? new Timestamp(task.getDueDate().getTime()) : null);
            stmt.setTimestamp(7, new Timestamp(task.getCreatedAt().getTime()));
            stmt.setTimestamp(8, new Timestamp(task.getUpdatedAt().getTime()));

            int affectedRows = stmt.executeUpdate();

            if (affectedRows == 0) {
                throw new SQLException("Creating task failed, no rows affected.");
            }

            try (ResultSet generatedKeys = stmt.getGeneratedKeys()) {
                if (generatedKeys.next()) {
                    task.setId(generatedKeys.getInt(1));
                } else {
                    throw new SQLException("Creating task failed, no ID obtained.");
                }
            }
        }

        return task;
    }

    /**
     * Get task by ID
     * @param id Task ID
     * @return Task object or null if not found
     * @throws SQLException
     */
    public Task getTaskById(int id) throws SQLException {
        String sql = "SELECT * FROM tasks WHERE id = ?";

        try (PreparedStatement stmt = connection.prepareStatement(sql)) {
            stmt.setInt(1, id);

            try (ResultSet rs = stmt.executeQuery()) {
                if (rs.next()) {
                    return extractTaskFromResultSet(rs);
                }
            }
        }

        return null;
    }

    /**
     * Get all tasks for a specific user
     * @param userId User ID
     * @return List of tasks
     * @throws SQLException
     */
    public List<Task> getTasksByUserId(int userId) throws SQLException {
        List<Task> tasks = new ArrayList<>();
        String sql = "SELECT * FROM tasks WHERE user_id = ? ORDER BY created_at DESC";

        try (PreparedStatement stmt = connection.prepareStatement(sql)) {
            stmt.setInt(1, userId);

            try (ResultSet rs = stmt.executeQuery()) {
                while (rs.next()) {
                    tasks.add(extractTaskFromResultSet(rs));
                }
            }
        }

        return tasks;
    }

    /**
     * Get all tasks
     * @return List of all tasks
     * @throws SQLException
     */
    public List<Task> getAllTasks() throws SQLException {
        List<Task> tasks = new ArrayList<>();
        String sql = "SELECT * FROM tasks ORDER BY created_at DESC";

        try (Statement stmt = connection.createStatement();
             ResultSet rs = stmt.executeQuery(sql)) {

            while (rs.next()) {
                tasks.add(extractTaskFromResultSet(rs));
            }
        }

        return tasks;
    }

    /**
     * Get tasks by status
     * @param status Task status
     * @return List of tasks with given status
     * @throws SQLException
     */
    public List<Task> getTasksByStatus(Status status) throws SQLException {
        List<Task> tasks = new ArrayList<>();
        String sql = "SELECT * FROM tasks WHERE status = ? ORDER BY created_at DESC";

        try (PreparedStatement stmt = connection.prepareStatement(sql)) {
            stmt.setString(1, status.name());

            try (ResultSet rs = stmt.executeQuery()) {
                while (rs.next()) {
                    tasks.add(extractTaskFromResultSet(rs));
                }
            }
        }

        return tasks;
    }

    /**
     * Get tasks by priority
     * @param priority Task priority
     * @return List of tasks with given priority
     * @throws SQLException
     */
    public List<Task> getTasksByPriority(Priority priority) throws SQLException {
        List<Task> tasks = new ArrayList<>();
        String sql = "SELECT * FROM tasks WHERE priority = ? ORDER BY created_at DESC";

        try (PreparedStatement stmt = connection.prepareStatement(sql)) {
            stmt.setString(1, priority.name());

            try (ResultSet rs = stmt.executeQuery()) {
                while (rs.next()) {
                    tasks.add(extractTaskFromResultSet(rs));
                }
            }
        }

        return tasks;
    }

    /**
     * Update task
     * @param task Task object with updated information
     * @return Updated task
     * @throws SQLException
     */
    public Task updateTask(Task task) throws SQLException {
        String sql = "UPDATE tasks SET title = ?, description = ?, priority = ?, status = ?, " +
                     "due_date = ?, updated_at = ? WHERE id = ?";

        try (PreparedStatement stmt = connection.prepareStatement(sql)) {
            stmt.setString(1, task.getTitle());
            stmt.setString(2, task.getDescription());
            stmt.setString(3, task.getPriority().name());
            stmt.setString(4, task.getStatus().name());
            stmt.setTimestamp(5, task.getDueDate() != null ? new Timestamp(task.getDueDate().getTime()) : null);
            stmt.setTimestamp(6, new Timestamp(new java.util.Date().getTime()));
            stmt.setInt(7, task.getId());

            int affectedRows = stmt.executeUpdate();

            if (affectedRows == 0) {
                throw new SQLException("Updating task failed, no rows affected.");
            }
        }

        return getTaskById(task.getId());
    }

    /**
     * Delete task by ID
     * @param id Task ID
     * @return true if deleted successfully
     * @throws SQLException
     */
    public boolean deleteTask(int id) throws SQLException {
        String sql = "DELETE FROM tasks WHERE id = ?";

        try (PreparedStatement stmt = connection.prepareStatement(sql)) {
            stmt.setInt(1, id);

            int affectedRows = stmt.executeUpdate();
            return affectedRows > 0;
        }
    }

    /**
     * Helper method to extract Task from ResultSet
     */
    private Task extractTaskFromResultSet(ResultSet rs) throws SQLException {
        Task task = new Task();
        task.setId(rs.getInt("id"));
        task.setTitle(rs.getString("title"));
        task.setDescription(rs.getString("description"));
        task.setUserId(rs.getInt("user_id"));
        task.setPriority(Priority.valueOf(rs.getString("priority")));
        task.setStatus(Status.valueOf(rs.getString("status")));

        Timestamp dueDate = rs.getTimestamp("due_date");
        if (dueDate != null) {
            task.setDueDate(new java.util.Date(dueDate.getTime()));
        }

        task.setCreatedAt(rs.getTimestamp("created_at"));
        task.setUpdatedAt(rs.getTimestamp("updated_at"));
        return task;
    }
}