package com.taskmanager.models;

import com.fasterxml.jackson.annotation.JsonProperty;
import java.util.Date;

/**
 * Task Model Class
 * Demonstrates OOP principles: Encapsulation, Enums, Data Modeling
 * Day 8-9: Java Fundamentals + OOP
 */
public class Task {

    // Enum for task priority
    public enum Priority {
        LOW(1),
        MEDIUM(2),
        HIGH(3),
        URGENT(4);

        private final int value;

        Priority(int value) {
            this.value = value;
        }

        public int getValue() {
            return value;
        }
    }

    // Enum for task status
    public enum Status {
        TODO("To Do"),
        IN_PROGRESS("In Progress"),
        COMPLETED("Completed"),
        CANCELLED("Cancelled");

        private final String displayName;

        Status(String displayName) {
            this.displayName = displayName;
        }

        public String getDisplayName() {
            return displayName;
        }
    }

    @JsonProperty
    private int id;

    @JsonProperty
    private String title;

    @JsonProperty
    private String description;

    @JsonProperty
    private int userId;

    @JsonProperty
    private Priority priority;

    @JsonProperty
    private Status status;

    @JsonProperty
    private Date dueDate;

    @JsonProperty
    private Date createdAt;

    @JsonProperty
    private Date updatedAt;

    // Default constructor
    public Task() {
        this.priority = Priority.MEDIUM;
        this.status = Status.TODO;
        this.createdAt = new Date();
        this.updatedAt = new Date();
    }

    // Parameterized constructor
    public Task(int id, String title, String description, int userId, Priority priority) {
        this.id = id;
        this.title = title;
        this.description = description;
        this.userId = userId;
        this.priority = priority;
        this.status = Status.TODO;
        this.createdAt = new Date();
        this.updatedAt = new Date();
    }

    // Constructor without ID (for new tasks)
    public Task(String title, String description, int userId, Priority priority) {
        this.title = title;
        this.description = description;
        this.userId = userId;
        this.priority = priority != null ? priority : Priority.MEDIUM;
        this.status = Status.TODO;
        this.createdAt = new Date();
        this.updatedAt = new Date();
    }

    // Getters and Setters
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
        this.updatedAt = new Date();
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
        this.updatedAt = new Date();
    }

    public int getUserId() {
        return userId;
    }

    public void setUserId(int userId) {
        this.userId = userId;
    }

    public Priority getPriority() {
        return priority;
    }

    public void setPriority(Priority priority) {
        this.priority = priority;
        this.updatedAt = new Date();
    }

    public Status getStatus() {
        return status;
    }

    public void setStatus(Status status) {
        this.status = status;
        this.updatedAt = new Date();
    }

    public Date getDueDate() {
        return dueDate;
    }

    public void setDueDate(Date dueDate) {
        this.dueDate = dueDate;
        this.updatedAt = new Date();
    }

    public Date getCreatedAt() {
        return createdAt;
    }

    public void setCreatedAt(Date createdAt) {
        this.createdAt = createdAt;
    }

    public Date getUpdatedAt() {
        return updatedAt;
    }

    public void setUpdatedAt(Date updatedAt) {
        this.updatedAt = updatedAt;
    }

    // Override toString()
    @Override
    public String toString() {
        return "Task{" +
                "id=" + id +
                ", title='" + title + '\'' +
                ", userId=" + userId +
                ", priority=" + priority +
                ", status=" + status +
                ", dueDate=" + dueDate +
                '}';
    }

    // Override equals()
    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (obj == null || getClass() != obj.getClass()) return false;

        Task task = (Task) obj;
        return id == task.id && 
               userId == task.userId && 
               title.equals(task.title);
    }

    // Override hashCode()
    @Override
    public int hashCode() {
        int result = id;
        result = 31 * result + title.hashCode();
        result = 31 * result + userId;
        return result;
    }

    // Business methods
    public boolean isValid() {
        return title != null && !title.isEmpty() && userId > 0;
    }

    public boolean isOverdue() {
        if (dueDate == null || status == Status.COMPLETED) {
            return false;
        }
        return dueDate.before(new Date());
    }

    public void complete() {
        this.status = Status.COMPLETED;
        this.updatedAt = new Date();
    }

    public void cancel() {
        this.status = Status.CANCELLED;
        this.updatedAt = new Date();
    }

    public int getDaysUntilDue() {
        if (dueDate == null) return -1;
        long diffInMillis = dueDate.getTime() - new Date().getTime();
        return (int) (diffInMillis / (1000 * 60 * 60 * 24));
    }
}