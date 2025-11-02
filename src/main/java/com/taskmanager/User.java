package com.taskmanager.models;

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
                ", username='" + username + '\'' +
                ", email='" + email + '\'' +
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
}