package com.taskmanager;

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
        String password = "abuzada909";


        Class.forName("com.mysql.cj.jdbc.Driver");
        return DriverManager.getConnection(url, username, password);
    }
}