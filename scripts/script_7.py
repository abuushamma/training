
# Generate REST API Resources and configuration files

# UserResource.java
user_resource_java = """package com.taskmanager.resources;

import com.taskmanager.dao.UserDAO;
import com.taskmanager.models.User;
import javax.ws.rs.*;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;
import java.sql.Connection;
import java.sql.SQLException;
import java.util.List;

/**
 * User REST API Resource
 * Implements RESTful endpoints for user management
 * Day 11-12: REST API with Dropwizard
 */
@Path("/api/users")
@Produces(MediaType.APPLICATION_JSON)
@Consumes(MediaType.APPLICATION_JSON)
public class UserResource {
    
    private final Connection connection;
    
    public UserResource(Connection connection) {
        this.connection = connection;
    }
    
    /**
     * GET /api/users
     * Get all users
     * @return List of all users
     */
    @GET
    public Response getAllUsers() {
        try {
            UserDAO userDAO = new UserDAO(connection);
            List<User> users = userDAO.getAllUsers();
            
            // Return safe user objects without passwords
            List<User> safeUsers = users.stream()
                .map(User::getSafeUser)
                .collect(java.util.stream.Collectors.toList());
            
            return Response.ok(safeUsers).build();
        } catch (SQLException e) {
            return Response.status(Response.Status.INTERNAL_SERVER_ERROR)
                    .entity(new ErrorResponse("Database error: " + e.getMessage()))
                    .build();
        }
    }
    
    /**
     * GET /api/users/{id}
     * Get user by ID
     * @param id User ID
     * @return User object
     */
    @GET
    @Path("/{id}")
    public Response getUserById(@PathParam("id") int id) {
        try {
            UserDAO userDAO = new UserDAO(connection);
            User user = userDAO.getUserById(id);
            
            if (user == null) {
                return Response.status(Response.Status.NOT_FOUND)
                        .entity(new ErrorResponse("User not found with ID: " + id))
                        .build();
            }
            
            return Response.ok(user.getSafeUser()).build();
        } catch (SQLException e) {
            return Response.status(Response.Status.INTERNAL_SERVER_ERROR)
                    .entity(new ErrorResponse("Database error: " + e.getMessage()))
                    .build();
        }
    }
    
    /**
     * POST /api/users
     * Create a new user
     * @param user User object from request body
     * @return Created user
     */
    @POST
    public Response createUser(User user) {
        try {
            // Validate user data
            if (!user.isValid()) {
                return Response.status(Response.Status.BAD_REQUEST)
                        .entity(new ErrorResponse("Invalid user data. Check username, email, and password."))
                        .build();
            }
            
            UserDAO userDAO = new UserDAO(connection);
            
            // Check if email already exists
            if (userDAO.emailExists(user.getEmail())) {
                return Response.status(Response.Status.CONFLICT)
                        .entity(new ErrorResponse("Email already exists: " + user.getEmail()))
                        .build();
            }
            
            User createdUser = userDAO.createUser(user);
            
            return Response.status(Response.Status.CREATED)
                    .entity(createdUser.getSafeUser())
                    .build();
        } catch (SQLException e) {
            return Response.status(Response.Status.INTERNAL_SERVER_ERROR)
                    .entity(new ErrorResponse("Database error: " + e.getMessage()))
                    .build();
        }
    }
    
    /**
     * PUT /api/users/{id}
     * Update existing user
     * @param id User ID
     * @param user Updated user data
     * @return Updated user
     */
    @PUT
    @Path("/{id}")
    public Response updateUser(@PathParam("id") int id, User user) {
        try {
            UserDAO userDAO = new UserDAO(connection);
            
            // Check if user exists
            User existingUser = userDAO.getUserById(id);
            if (existingUser == null) {
                return Response.status(Response.Status.NOT_FOUND)
                        .entity(new ErrorResponse("User not found with ID: " + id))
                        .build();
            }
            
            // Set ID and update
            user.setId(id);
            
            if (!user.isValid()) {
                return Response.status(Response.Status.BAD_REQUEST)
                        .entity(new ErrorResponse("Invalid user data"))
                        .build();
            }
            
            User updatedUser = userDAO.updateUser(user);
            
            return Response.ok(updatedUser.getSafeUser()).build();
        } catch (SQLException e) {
            return Response.status(Response.Status.INTERNAL_SERVER_ERROR)
                    .entity(new ErrorResponse("Database error: " + e.getMessage()))
                    .build();
        }
    }
    
    /**
     * DELETE /api/users/{id}
     * Delete user
     * @param id User ID
     * @return Success message
     */
    @DELETE
    @Path("/{id}")
    public Response deleteUser(@PathParam("id") int id) {
        try {
            UserDAO userDAO = new UserDAO(connection);
            
            // Check if user exists
            User user = userDAO.getUserById(id);
            if (user == null) {
                return Response.status(Response.Status.NOT_FOUND)
                        .entity(new ErrorResponse("User not found with ID: " + id))
                        .build();
            }
            
            boolean deleted = userDAO.deleteUser(id);
            
            if (deleted) {
                return Response.ok(new SuccessResponse("User deleted successfully")).build();
            } else {
                return Response.status(Response.Status.INTERNAL_SERVER_ERROR)
                        .entity(new ErrorResponse("Failed to delete user"))
                        .build();
            }
        } catch (SQLException e) {
            return Response.status(Response.Status.INTERNAL_SERVER_ERROR)
                    .entity(new ErrorResponse("Database error: " + e.getMessage()))
                    .build();
        }
    }
    
    // Helper classes for responses
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

with open('UserResource.java', 'w', encoding='utf-8') as f:
    f.write(user_resource_java)

print("✓ Generated: UserResource.java")
print("\nContinuing with TaskResource and configuration files...")
