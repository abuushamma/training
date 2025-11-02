
# Generate main application files and comprehensive README

# TaskManagerApplication.java
app_java = """package com.taskmanager;

import com.taskmanager.resources.TaskResource;
import com.taskmanager.resources.UserResource;
import io.dropwizard.Application;
import io.dropwizard.setup.Bootstrap;
import io.dropwizard.setup.Environment;
import org.eclipse.jetty.servlets.CrossOriginFilter;

import javax.servlet.DispatcherType;
import javax.servlet.FilterRegistration;
import java.sql.Connection;
import java.sql.DriverManager;
import java.util.EnumSet;

/**
 * Main Application Class
 * Day 11-12: REST API with Dropwizard
 */
public class TaskManagerApplication extends Application<TaskManagerConfiguration> {
    
    public static void main(String[] args) throws Exception {
        new TaskManagerApplication().run(args);
    }

    @Override
    public String getName() {
        return "smart-task-manager";
    }

    @Override
    public void initialize(Bootstrap<TaskManagerConfiguration> bootstrap) {
        // Initialization code here
    }

    @Override
    public void run(TaskManagerConfiguration configuration, Environment environment) throws Exception {
        // Setup CORS (Cross-Origin Resource Sharing)
        final FilterRegistration.Dynamic cors = environment.servlets()
                .addFilter("CORS", CrossOriginFilter.class);
        
        cors.setInitParameter(CrossOriginFilter.ALLOWED_ORIGINS_PARAM, "*");
        cors.setInitParameter(CrossOriginFilter.ALLOWED_HEADERS_PARAM, "X-Requested-With,Content-Type,Accept,Origin");
        cors.setInitParameter(CrossOriginFilter.ALLOWED_METHODS_PARAM, "OPTIONS,GET,PUT,POST,DELETE,HEAD");
        cors.addMappingForUrlPatterns(EnumSet.allOf(DispatcherType.class), true, "/*");

        // Setup database connection
        Connection connection = getConnection(configuration);

        // Register resources
        final UserResource userResource = new UserResource(connection);
        environment.jersey().register(userResource);

        final TaskResource taskResource = new TaskResource(connection);
        environment.jersey().register(taskResource);

        System.out.println("===========================================");
        System.out.println("Smart Task Manager API Started!");
        System.out.println("===========================================");
        System.out.println("API Base URL: http://localhost:8080/api");
        System.out.println("Admin URL: http://localhost:8081");
        System.out.println("===========================================");
    }

    private Connection getConnection(TaskManagerConfiguration configuration) throws Exception {
        String url = "jdbc:mysql://localhost:3306/task_manager?useSSL=false&serverTimezone=UTC&allowPublicKeyRetrieval=true";
        String username = "root";
        String password = "your_mysql_password"; // Change this to your MySQL password
        
        Class.forName("com.mysql.cj.jdbc.Driver");
        return DriverManager.getConnection(url, username, password);
    }
}"""

# TaskManagerConfiguration.java
config_java = """package com.taskmanager;

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
}"""

# TaskResource.java (the REST resource we need)
task_resource_java = """package com.taskmanager.resources;

import com.taskmanager.dao.TaskDAO;
import com.taskmanager.models.Task;
import javax.ws.rs.*;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;
import java.sql.Connection;
import java.sql.SQLException;
import java.util.List;

/**
 * Task REST API Resource
 * Day 11-12: REST API with Dropwizard
 */
@Path("/api/tasks")
@Produces(MediaType.APPLICATION_JSON)
@Consumes(MediaType.APPLICATION_JSON)
public class TaskResource {
    
    private final Connection connection;
    
    public TaskResource(Connection connection) {
        this.connection = connection;
    }
    
    @GET
    public Response getAllTasks(@QueryParam("userId") Integer userId,
                                 @QueryParam("status") String status,
                                 @QueryParam("priority") String priority) {
        try {
            TaskDAO taskDAO = new TaskDAO(connection);
            List<Task> tasks;
            
            if (userId != null) {
                tasks = taskDAO.getTasksByUserId(userId);
            } else if (status != null) {
                tasks = taskDAO.getTasksByStatus(Task.Status.valueOf(status));
            } else if (priority != null) {
                tasks = taskDAO.getTasksByPriority(Task.Priority.valueOf(priority));
            } else {
                tasks = taskDAO.getAllTasks();
            }
            
            return Response.ok(tasks).build();
        } catch (SQLException e) {
            return Response.status(Response.Status.INTERNAL_SERVER_ERROR)
                    .entity(new ErrorResponse("Database error: " + e.getMessage()))
                    .build();
        } catch (IllegalArgumentException e) {
            return Response.status(Response.Status.BAD_REQUEST)
                    .entity(new ErrorResponse("Invalid status or priority value"))
                    .build();
        }
    }
    
    @GET
    @Path("/{id}")
    public Response getTaskById(@PathParam("id") int id) {
        try {
            TaskDAO taskDAO = new TaskDAO(connection);
            Task task = taskDAO.getTaskById(id);
            
            if (task == null) {
                return Response.status(Response.Status.NOT_FOUND)
                        .entity(new ErrorResponse("Task not found with ID: " + id))
                        .build();
            }
            
            return Response.ok(task).build();
        } catch (SQLException e) {
            return Response.status(Response.Status.INTERNAL_SERVER_ERROR)
                    .entity(new ErrorResponse("Database error: " + e.getMessage()))
                    .build();
        }
    }
    
    @POST
    public Response createTask(Task task) {
        try {
            if (!task.isValid()) {
                return Response.status(Response.Status.BAD_REQUEST)
                        .entity(new ErrorResponse("Invalid task data. Title and user ID are required."))
                        .build();
            }
            
            TaskDAO taskDAO = new TaskDAO(connection);
            Task createdTask = taskDAO.createTask(task);
            
            return Response.status(Response.Status.CREATED)
                    .entity(createdTask)
                    .build();
        } catch (SQLException e) {
            return Response.status(Response.Status.INTERNAL_SERVER_ERROR)
                    .entity(new ErrorResponse("Database error: " + e.getMessage()))
                    .build();
        }
    }
    
    @PUT
    @Path("/{id}")
    public Response updateTask(@PathParam("id") int id, Task task) {
        try {
            TaskDAO taskDAO = new TaskDAO(connection);
            
            Task existingTask = taskDAO.getTaskById(id);
            if (existingTask == null) {
                return Response.status(Response.Status.NOT_FOUND)
                        .entity(new ErrorResponse("Task not found with ID: " + id))
                        .build();
            }
            
            task.setId(id);
            
            if (!task.isValid()) {
                return Response.status(Response.Status.BAD_REQUEST)
                        .entity(new ErrorResponse("Invalid task data"))
                        .build();
            }
            
            Task updatedTask = taskDAO.updateTask(task);
            
            return Response.ok(updatedTask).build();
        } catch (SQLException e) {
            return Response.status(Response.Status.INTERNAL_SERVER_ERROR)
                    .entity(new ErrorResponse("Database error: " + e.getMessage()))
                    .build();
        }
    }
    
    @DELETE
    @Path("/{id}")
    public Response deleteTask(@PathParam("id") int id) {
        try {
            TaskDAO taskDAO = new TaskDAO(connection);
            
            Task task = taskDAO.getTaskById(id);
            if (task == null) {
                return Response.status(Response.Status.NOT_FOUND)
                        .entity(new ErrorResponse("Task not found with ID: " + id))
                        .build();
            }
            
            boolean deleted = taskDAO.deleteTask(id);
            
            if (deleted) {
                return Response.ok(new SuccessResponse("Task deleted successfully")).build();
            } else {
                return Response.status(Response.Status.INTERNAL_SERVER_ERROR)
                        .entity(new ErrorResponse("Failed to delete task"))
                        .build();
            }
        } catch (SQLException e) {
            return Response.status(Response.Status.INTERNAL_SERVER_ERROR)
                    .entity(new ErrorResponse("Database error: " + e.getMessage()))
                    .build();
        }
    }
    
    public static class ErrorResponse {
        public String error;
        public long timestamp;
        
        public ErrorResponse(String error) {
            this.error = error;
            this.timestamp = System.currentTimeMillis();
        }
    }
    
    public static class SuccessResponse {
        public String message;
        public long timestamp;
        
        public SuccessResponse(String message) {
            this.message = message;
            this.timestamp = System.currentTimeMillis();
        }
    }
}"""

with open('TaskManagerApplication.java', 'w', encoding='utf-8') as f:
    f.write(app_java)
with open('TaskManagerConfiguration.java', 'w', encoding='utf-8') as f:
    f.write(config_java)
with open('TaskResource.java', 'w', encoding='utf-8') as f:
    f.write(task_resource_java)

print("✓ Generated: TaskManagerApplication.java")
print("✓ Generated: TaskManagerConfiguration.java")
print("✓ Generated: TaskResource.java")
