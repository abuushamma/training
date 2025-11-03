
# Generate complete configuration and remaining backend files including pom.xml, schema.sql, etc.

# pom.xml
pom_xml = """<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0
         http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>com.taskmanager</groupId>
    <artifactId>smart-task-manager</artifactId>
    <version>1.0.0</version>
    <packaging>jar</packaging>

    <name>Smart Task Manager</name>
    <description>Full-stack task management system with Java backend and JavaScript frontend</description>

    <properties>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
        <maven.compiler.source>1.8</maven.compiler.source>
        <maven.compiler.target>1.8</maven.compiler.target>
        <dropwizard.version>2.0.28</dropwizard.version>
        <mysql.version>8.0.28</mysql.version>
    </properties>

    <dependencies>
        <!-- Dropwizard Core -->
        <dependency>
            <groupId>io.dropwizard</groupId>
            <artifactId>dropwizard-core</artifactId>
            <version>${dropwizard.version}</version>
        </dependency>

        <!-- Dropwizard JDBC -->
        <dependency>
            <groupId>io.dropwizard</groupId>
            <artifactId>dropwizard-jdbi3</artifactId>
            <version>${dropwizard.version}</version>
        </dependency>

        <!-- MySQL Connector -->
        <dependency>
            <groupId>mysql</groupId>
            <artifactId>mysql-connector-java</artifactId>
            <version>${mysql.version}</version>
        </dependency>

        <!-- CORS Support -->
        <dependency>
            <groupId>io.dropwizard</groupId>
            <artifactId>dropwizard-client</artifactId>
            <version>${dropwizard.version}</version>
        </dependency>

        <!-- Jackson for JSON -->
        <dependency>
            <groupId>com.fasterxml.jackson.core</groupId>
            <artifactId>jackson-annotations</artifactId>
            <version>2.12.3</version>
        </dependency>

        <!-- Testing -->
        <dependency>
            <groupId>junit</groupId>
            <artifactId>junit</artifactId>
            <version>4.13.2</version>
            <scope>test</scope>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <!-- Maven Compiler Plugin -->
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-compiler-plugin</artifactId>
                <version>3.8.1</version>
                <configuration>
                    <source>1.8</source>
                    <target>1.8</target>
                </configuration>
            </plugin>

            <!-- Maven Shade Plugin for creating fat JAR -->
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-shade-plugin</artifactId>
                <version>3.2.4</version>
                <configuration>
                    <createDependencyReducedPom>true</createDependencyReducedPom>
                    <transformers>
                        <transformer implementation="org.apache.maven.plugins.shade.resource.ServicesResourceTransformer"/>
                        <transformer implementation="org.apache.maven.plugins.shade.resource.ManifestResourceTransformer">
                            <mainClass>com.taskmanager.TaskManagerApplication</mainClass>
                        </transformer>
                    </transformers>
                    <filters>
                        <filter>
                            <artifact>*:*</artifact>
                            <excludes>
                                <exclude>META-INF/*.SF</exclude>
                                <exclude>META-INF/*.DSA</exclude>
                                <exclude>META-INF/*.RSA</exclude>
                            </excludes>
                        </filter>
                    </filters>
                </configuration>
                <executions>
                    <execution>
                        <phase>package</phase>
                        <goals>
                            <goal>shade</goal>
                        </goals>
                    </execution>
                </executions>
            </plugin>

            <!-- Maven JAR Plugin -->
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-jar-plugin</artifactId>
                <version>3.2.0</version>
                <configuration>
                    <archive>
                        <manifest>
                            <addDefaultImplementationEntries>true</addDefaultImplementationEntries>
                        </manifest>
                    </archive>
                </configuration>
            </plugin>
        </plugins>
    </build>
</project>"""

# schema.sql
schema_sql = """-- ============================================================
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
-- GROUP BY u.id, u.username;"""

# config.yml
config_yml = """# Smart Task Manager Configuration
# Day 11-12: Dropwizard Configuration

# Server configuration
server:
  applicationConnectors:
    - type: http
      port: 8080
  adminConnectors:
    - type: http
      port: 8081
  
  # CORS configuration
  rootPath: /*

# Logging configuration
logging:
  level: INFO
  appenders:
    - type: console
      threshold: ALL
      target: stdout
      logFormat: "%-5level [%date] %logger: %message%n"
    - type: file
      threshold: ALL
      currentLogFilename: ./logs/application.log
      archive: true
      archivedLogFilenamePattern: ./logs/application-%d.log
      archivedFileCount: 5
      timeZone: UTC

# Database configuration
database:
  driverClass: com.mysql.cj.jdbc.Driver
  url: jdbc:mysql://localhost:3306/task_manager?useSSL=false&serverTimezone=UTC&allowPublicKeyRetrieval=true
  user: root
  password: your_mysql_password
  
  # Connection pool settings
  properties:
    charSet: UTF-8
  maxWaitForConnection: 1s
  validationQuery: "SELECT 1"
  minSize: 8
  maxSize: 32
  checkConnectionWhileIdle: true
  checkConnectionOnBorrow: true"""

with open('pom.xml', 'w', encoding='utf-8') as f:
    f.write(pom_xml)
with open('schema.sql', 'w', encoding='utf-8') as f:
    f.write(schema_sql)
with open('config.yml', 'w', encoding='utf-8') as f:
    f.write(config_yml)

print("✓ Generated: pom.xml")
print("✓ Generated: schema.sql")
print("✓ Generated: config.yml")
