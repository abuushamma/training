# Smart Task Manager - Full-Stack Training Project

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![Java](https://img.shields.io/badge/Java-8-orange)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6-yellow)
![MySQL](https://img.shields.io/badge/MySQL-8.0-blue)

A complete full-stack web application built as a 2-week developer training project, featuring a Java backend with Dropwizard REST API and a vanilla JavaScript frontend.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation & Setup](#installation--setup)
- [Running the Application](#running-the-application)
- [API Documentation](#api-documentation)
- [Week-by-Week Progress](#week-by-week-progress)
- [Learning Outcomes](#learning-outcomes)
- [Troubleshooting](#troubleshooting)

## 🎯 Overview

This project demonstrates a complete full-stack development workflow, covering:
- **Week 1**: JavaScript fundamentals, algorithms, data structures, and async programming
- **Week 2**: Java backend development, REST APIs, database integration, and frontend-backend communication

## ✨ Features

- ✅ Full CRUD operations for tasks
- ✅ User management system
- ✅ Task prioritization (Low, Medium, High, Urgent)
- ✅ Task status tracking (To Do, In Progress, Completed, Cancelled)
- ✅ RESTful API with proper HTTP methods
- ✅ Async JavaScript with fetch API
- ✅ Responsive UI design
- ✅ Real-time task filtering
- ✅ MySQL database integration
- ✅ Error handling and loading states

## 🛠️ Technology Stack

### Backend
- **Java 8**: Core programming language
- **Dropwizard 2.0.28**: REST API framework
- **MySQL 8.0**: Database
- **JDBC**: Database connectivity
- **Maven**: Build tool

### Frontend
- **HTML5**: Structure
- **CSS3**: Styling with modern features
- **JavaScript ES6**: Logic and API integration
- **Fetch API**: HTTP requests

## 📁 Project Structure

\`\`\`
smart-task-manager/
├── README.md
├── .gitignore
│
├── week1/                              # Week 1: JavaScript Mastery
│   ├── day1-2-js-fundamentals/
│   │   └── fundamentals.js            # Variables, functions, objects, arrays
│   ├── day3-algorithms/
│   │   ├── algorithms.js              # Fibonacci, palindrome, search, sort
│   │   └── performance-report.md
│   ├── day4-data-structures/
│   │   └── data-structures.js         # Stack, Queue, Binary Search Tree
│   ├── day5-async-api/
│   │   ├── weather-dashboard.html
│   │   ├── weather-dashboard.css
│   │   └── weather-dashboard.js       # Async/await, fetch API
│   └── day7-task-manager-ui/
│       ├── index.html
│       ├── style.css
│       └── app.js
│
└── week2/                              # Week 2: Java Backend
    ├── backend/
    │   ├── pom.xml                    # Maven configuration
    │   ├── src/
    │   │   └── main/
    │   │       ├── java/
    │   │       │   └── com/
    │   │       │       └── taskmanager/
    │   │       │           ├── TaskManagerApplication.java
    │   │       │           ├── TaskManagerConfiguration.java
    │   │       │           ├── models/
    │   │       │           │   ├── User.java
    │   │       │           │   └── Task.java
    │   │       │           ├── dao/
    │   │       │           │   ├── UserDAO.java
    │   │       │           │   └── TaskDAO.java
    │   │       │           └── resources/
    │   │       │               ├── UserResource.java
    │   │       │               └── TaskResource.java
    │   │       └── resources/
    │   │           └── config.yml
    │   └── database/
    │       └── schema.sql             # Database schema
    │
    └── frontend/
        ├── index.html                 # Main application
        ├── style.css                  # Application styles
        └── app.js                     # Frontend logic
\`\`\`

## 📋 Prerequisites

Before starting, ensure you have the following installed:

1. **Java Development Kit (JDK) 8 or higher**
   - Download: https://www.oracle.com/java/technologies/javase-downloads.html
   - Verify: \`java -version\`

2. **Apache Maven 3.6+**
   - Download: https://maven.apache.org/download.cgi
   - Verify: \`mvn -version\`

3. **MySQL 8.0+**
   - Download: https://dev.mysql.com/downloads/mysql/
   - Verify: \`mysql --version\`

4. **IntelliJ IDEA** (recommended) or any Java IDE
   - Download: https://www.jetbrains.com/idea/download/

5. **Git**
   - Download: https://git-scm.com/downloads
   - Verify: \`git --version\`

6. **Web Browser** (Chrome, Firefox, or Edge recommended)

## 🚀 Installation & Setup

### Step 1: Clone or Create the Project

\`\`\`bash
# Create project directory
mkdir smart-task-manager
cd smart-task-manager

# Initialize Git repository
git init
\`\`\`

### Step 2: Set Up the Database

1. **Start MySQL Server**
   \`\`\`bash
   # Windows
   net start MySQL80

   # macOS/Linux
   sudo systemctl start mysql
   # or
   sudo service mysql start
   \`\`\`

2. **Create Database and Tables**
   \`\`\`bash
   # Login to MySQL
   mysql -u root -p
   \`\`\`

   Then run the schema:
   \`\`\`sql
   source week2/backend/database/schema.sql;
   \`\`\`

   Or copy and paste the contents of \`schema.sql\` into the MySQL console.

3. **Verify Database Setup**
   \`\`\`sql
   USE task_manager;
   SHOW TABLES;
   SELECT * FROM users;
   SELECT * FROM tasks;
   \`\`\`

### Step 3: Configure the Backend

1. **Update Database Credentials**

   Edit \`week2/backend/src/main/resources/config.yml\`:
   \`\`\`yaml
   database:
     url: jdbc:mysql://localhost:3306/task_manager?useSSL=false&serverTimezone=UTC
     user: root
     password: YOUR_MYSQL_PASSWORD  # Change this!
   \`\`\`

   Also update \`TaskManagerApplication.java\` line 53:
   \`\`\`java
   String password = "YOUR_MYSQL_PASSWORD"; // Change this!
   \`\`\`

2. **Navigate to Backend Directory**
   \`\`\`bash
   cd week2/backend
   \`\`\`

### Step 4: Build the Backend

\`\`\`bash
# Clean and compile the project
mvn clean compile

# Package the application (creates JAR file)
mvn package

# This creates: target/smart-task-manager-1.0.0.jar
\`\`\`

**Note**: The first build may take several minutes as Maven downloads all dependencies.

### Step 5: Open in IntelliJ IDEA (Optional)

1. Open IntelliJ IDEA
2. Click "Open" and select \`week2/backend\` directory
3. IntelliJ will detect the Maven project and import it
4. Wait for dependencies to download
5. Set up Run Configuration:
   - Go to Run → Edit Configurations
   - Click "+" → Application
   - Name: "TaskManagerApp"
   - Main class: \`com.taskmanager.TaskManagerApplication\`
   - Program arguments: \`server src/main/resources/config.yml\`
   - Click OK

## ▶️ Running the Application

### Option 1: Using Maven (Recommended)

\`\`\`bash
# From week2/backend directory
mvn exec:java -Dexec.mainClass="com.taskmanager.TaskManagerApplication" -Dexec.args="server src/main/resources/config.yml"
\`\`\`

### Option 2: Using JAR File

\`\`\`bash
# From week2/backend directory
java -jar target/smart-task-manager-1.0.0.jar server src/main/resources/config.yml
\`\`\`

### Option 3: Using IntelliJ IDEA

1. Open the project in IntelliJ
2. Click the green "Run" button
3. Or press Shift+F10 (Windows/Linux) or Control+R (macOS)

### Verify Backend is Running

You should see:
\`\`\`
===========================================
Smart Task Manager API Started!
===========================================
API Base URL: http://localhost:8080/api
Admin URL: http://localhost:8081
===========================================
\`\`\`

Test the API:
\`\`\`bash
# Test users endpoint
curl http://localhost:8080/api/users

# Test tasks endpoint
curl http://localhost:8080/api/tasks
\`\`\`

### Running the Frontend

1. Navigate to \`week2/frontend\` directory
2. Open \`index.html\` in a web browser
3. Or use a local web server:
   \`\`\`bash
   # Using Python
   python -m http.server 3000
   # Then open: http://localhost:3000

   # Using Node.js
   npx http-server -p 3000
   # Then open: http://localhost:3000
   \`\`\`

## 📚 API Documentation

### Base URL
\`\`\`
http://localhost:8080/api
\`\`\`

### User Endpoints

#### Get All Users
\`\`\`
GET /api/users
Response: 200 OK
[
  {
    "id": 1,
    "username": "ahmad",
    "email": "ahmad@example.com",
    "createdAt": "2025-11-01T12:00:00",
    "updatedAt": "2025-11-01T12:00:00"
  }
]
\`\`\`

#### Get User by ID
\`\`\`
GET /api/users/{id}
Response: 200 OK
{
  "id": 1,
  "username": "ahmad",
  "email": "ahmad@example.com"
}
\`\`\`

#### Create User
\`\`\`
POST /api/users
Content-Type: application/json

{
  "username": "newuser",
  "email": "newuser@example.com",
  "password": "password123"
}

Response: 201 Created
{
  "id": 4,
  "username": "newuser",
  "email": "newuser@example.com"
}
\`\`\`

#### Update User
\`\`\`
PUT /api/users/{id}
Content-Type: application/json

{
  "username": "updated",
  "email": "updated@example.com",
  "password": "newpass123"
}

Response: 200 OK
\`\`\`

#### Delete User
\`\`\`
DELETE /api/users/{id}
Response: 200 OK
{
  "message": "User deleted successfully"
}
\`\`\`

### Task Endpoints

#### Get All Tasks
\`\`\`
GET /api/tasks
Query Parameters:
  - userId: Filter by user ID
  - status: Filter by status (TODO, IN_PROGRESS, COMPLETED, CANCELLED)
  - priority: Filter by priority (LOW, MEDIUM, HIGH, URGENT)

Response: 200 OK
[
  {
    "id": 1,
    "title": "Setup development environment",
    "description": "Install Java, Maven, MySQL",
    "userId": 1,
    "priority": "HIGH",
    "status": "COMPLETED",
    "dueDate": "2025-11-01T10:00:00",
    "createdAt": "2025-10-30T15:00:00",
    "updatedAt": "2025-11-01T10:30:00"
  }
]
\`\`\`

#### Get Task by ID
\`\`\`
GET /api/tasks/{id}
Response: 200 OK
\`\`\`

#### Create Task
\`\`\`
POST /api/tasks
Content-Type: application/json

{
  "title": "New Task",
  "description": "Task description",
  "userId": 1,
  "priority": "MEDIUM",
  "status": "TODO",
  "dueDate": "2025-11-10T15:00:00"
}

Response: 201 Created
\`\`\`

#### Update Task
\`\`\`
PUT /api/tasks/{id}
Content-Type: application/json

{
  "title": "Updated Task",
  "description": "Updated description",
  "userId": 1,
  "priority": "HIGH",
  "status": "IN_PROGRESS",
  "dueDate": "2025-11-12T15:00:00"
}

Response: 200 OK
\`\`\`

#### Delete Task
\`\`\`
DELETE /api/tasks/{id}
Response: 200 OK
{
  "message": "Task deleted successfully"
}
\`\`\`

## 📅 Week-by-Week Progress

### Week 1: JavaScript Mastery + Git Setup

- **Day 1-2**: JavaScript Fundamentals ✅
  - Variables (let, const)
  - Arrow functions
  - Template literals
  - Objects and arrays
  - Higher-order functions

- **Day 3**: Algorithms & Big O ✅
  - Fibonacci sequence
  - Palindrome checker
  - Linear and binary search
  - Merge sort
  - Time complexity analysis

- **Day 4**: Data Structures ✅
  - Stack implementation
  - Queue implementation
  - Binary Search Tree
  - Recursive algorithms

- **Day 5**: Async JS + APIs ✅
  - Weather Dashboard
  - fetch() API
  - async/await
  - Error handling

- **Day 6**: Git & Dev Tools ✅
  - Repository setup
  - Branching strategy
  - README documentation

- **Day 7**: Task Manager UI ✅
  - HTML structure
  - CSS styling
  - Dynamic JavaScript

### Week 2: Java Backend + Integration

- **Day 8-9**: Java Fundamentals + OOP ✅
  - Maven project setup
  - User and Task models
  - OOP principles
  - Annotations

- **Day 10**: JDBC + MySQL ✅
  - Database schema
  - UserDAO and TaskDAO
  - CRUD operations
  - PreparedStatements

- **Day 11-12**: REST API ✅
  - Dropwizard setup
  - RESTful endpoints
  - JSON serialization
  - CORS configuration

- **Day 13**: Frontend-Backend Integration ✅
  - Connect JavaScript to Java API
  - Async task operations
  - Error handling

- **Day 14**: Final Polish ✅
  - Code optimization
  - Documentation
  - Testing
  - Deployment preparation

## 🎓 Learning Outcomes

After completing this project, you will have learned:

### JavaScript
- ES6+ syntax and features
- Asynchronous programming
- DOM manipulation
- API integration
- Algorithm implementation
- Data structures

### Java
- Object-Oriented Programming
- JDBC and database connectivity
- REST API development
- Maven build tool
- Dropwizard framework

### Database
- SQL and MySQL
- Database design
- CRUD operations
- Data relationships

### Full-Stack Development
- Client-server architecture
- HTTP protocols
- JSON data format
- API design
- Error handling
- Version control with Git

## 🔧 Troubleshooting

### Backend Issues

**Problem**: \`Port 8080 already in use\`
\`\`\`
Solution: Stop the process using port 8080 or change the port in config.yml
\`\`\`

**Problem**: \`Cannot connect to MySQL\`
\`\`\`
Solution: 
1. Verify MySQL is running: sudo systemctl status mysql
2. Check credentials in config.yml and TaskManagerApplication.java
3. Test connection: mysql -u root -p
\`\`\`

**Problem**: \`ClassNotFoundException: com.mysql.cj.jdbc.Driver\`
\`\`\`
Solution: Run mvn clean install to download dependencies
\`\`\`

**Problem**: \`BUILD FAILURE in Maven\`
\`\`\`
Solution:
1. Check Java version: java -version (must be 8+)
2. Check Maven version: mvn -version
3. Clean and rebuild: mvn clean compile package
\`\`\`

### Frontend Issues

**Problem**: \`CORS error in browser console\`
\`\`\`
Solution: Backend includes CORS configuration. Ensure backend is running.
\`\`\`

**Problem**: \`Failed to fetch\`
\`\`\`
Solution: 
1. Verify backend is running on port 8080
2. Check API_BASE_URL in app.js
3. Open browser console for detailed errors
\`\`\`

**Problem**: \`Tasks not loading\`
\`\`\`
Solution:
1. Check browser console for errors
2. Verify database has data: SELECT * FROM tasks;
3. Test API directly: curl http://localhost:8080/api/tasks
\`\`\`

### Database Issues

**Problem**: \`Table doesn't exist\`
\`\`\`
Solution: Run schema.sql again: source week2/backend/database/schema.sql;
\`\`\`

**Problem**: \`Access denied for user\`
\`\`\`
Solution: 
1. Reset MySQL password
2. Update credentials in config.yml and TaskManagerApplication.java
\`\`\`

## 🤝 Contributing

This is a training project, but suggestions for improvements are welcome!

## 📄 License

This project is created for educational purposes.

## 👤 Author

**Training Project**
- 2-Week Full-Stack Developer Training
- Smart Task Manager Application

## 🙏 Acknowledgments

- Dropwizard Documentation
- MySQL Documentation
- MDN Web Docs
- Java Documentation

---

**Happy Coding! 🚀**

For questions or issues, please check the troubleshooting section above.
