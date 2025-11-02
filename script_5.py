
# Generate Week 2 Java Backend Files

# User.java
user_java = """package com.taskmanager.models;

import com.fasterxml.jackson.annotation.JsonProperty;
import java.util.Date;

/**
 * User Model Class
 * Demonstrates OOP principles: Encapsulation, Data Modeling
 * Day 8-9: Java Fundamentals + OOP
 */
public class User {
    
    @JsonProperty
    private int id;
    
    @JsonProperty
    private String username;
    
    @JsonProperty
    private String email;
    
    @JsonProperty
    private String password;
    
    @JsonProperty
    private Date createdAt;
    
    @JsonProperty
    private Date updatedAt;

    // Default constructor
    public User() {
        this.createdAt = new Date();
        this.updatedAt = new Date();
    }

    // Parameterized constructor
    public User(int id, String username, String email, String password) {
        this.id = id;
        this.username = username;
        this.email = email;
        this.password = password;
        this.createdAt = new Date();
        this.updatedAt = new Date();
    }

    // Constructor without ID (for new users)
    public User(String username, String email, String password) {
        this.username = username;
        this.email = email;
        this.password = password;
        this.createdAt = new Date();
        this.updatedAt = new Date();
    }

    // Getters and Setters (Encapsulation)
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
        this.updatedAt = new Date();
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
        this.updatedAt = new Date();
    }

    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
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

    // Override toString() for better debugging
    @Override
    public String toString() {
        return "User{" +
                "id=" + id +
                ", username='" + username + '\\'' +
                ", email='" + email + '\\'' +
                ", createdAt=" + createdAt +
                '}';
    }

    // Override equals() for object comparison
    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (obj == null || getClass() != obj.getClass()) return false;
        
        User user = (User) obj;
        return id == user.id && 
               username.equals(user.username) && 
               email.equals(user.email);
    }

    // Override hashCode() (required when equals is overridden)
    @Override
    public int hashCode() {
        int result = id;
        result = 31 * result + username.hashCode();
        result = 31 * result + email.hashCode();
        return result;
    }

    // Business method: Validate user data
    public boolean isValid() {
        return username != null && !username.isEmpty() &&
               email != null && email.contains("@") &&
               password != null && password.length() >= 6;
    }

    // Business method: Sanitize user data before display
    public User getSafeUser() {
        User safeUser = new User();
        safeUser.setId(this.id);
        safeUser.setUsername(this.username);
        safeUser.setEmail(this.email);
        safeUser.setCreatedAt(this.createdAt);
        safeUser.setUpdatedAt(this.updatedAt);
        // Note: password is intentionally not included for security
        return safeUser;
    }
}"""

# Task.java
task_java = """package com.taskmanager.models;

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
                ", title='" + title + '\\'' +
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
}"""

with open('User.java', 'w', encoding='utf-8') as f:
    f.write(user_java)
with open('Task.java', 'w', encoding='utf-8') as f:
    f.write(task_java)

print("✓ Generated: User.java")
print("✓ Generated: Task.java")
