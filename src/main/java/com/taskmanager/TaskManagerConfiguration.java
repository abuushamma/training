package com.taskmanager;

import io.dropwizard.Configuration;
import com.fasterxml.jackson.annotation.JsonProperty;

/**
 * Configuration Class
 * Day 11-12: Dropwizard Configuration
 */
public class TaskManagerConfiguration extends Configuration {

    @JsonProperty
    private String database;

    @JsonProperty
    private String username;

    @JsonProperty
    private String password;

    public String getDatabase() {
        return database;
    }

    public void setDatabase(String database) {
        this.database = database;
    }

    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
}