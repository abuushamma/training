@echo off
REM Smart Task Manager - Windows Installation Script

echo ================================================
echo Smart Task Manager - Windows Setup
echo ================================================
echo.

REM Check Java
echo [1/5] Checking Java installation...
java -version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Java not found! Please install JDK 8 or higher.
    echo Download from: https://www.oracle.com/java/technologies/javase-downloads.html
    pause
    exit /b 1
)
echo ✓ Java found

REM Check Maven
echo [2/5] Checking Maven installation...
mvn -version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Maven not found! Please install Maven 3.6+
    echo Download from: https://maven.apache.org/download.cgi
    pause
    exit /b 1
)
echo ✓ Maven found

REM Check MySQL
echo [3/5] Checking MySQL installation...
mysql --version >nul 2>&1
if %errorlevel% neq 0 (
    echo WARNING: MySQL command not found in PATH
    echo Please ensure MySQL is installed and running
    echo Download from: https://dev.mysql.com/downloads/mysql/
)
echo ✓ MySQL check complete

REM Build backend
echo [4/5] Building backend...
cd week2\backend
call mvn clean package -DskipTests
if %errorlevel% neq 0 (
    echo ERROR: Maven build failed!
    pause
    exit /b 1
)
echo ✓ Backend built successfully

REM Setup database
echo [5/5] Database setup...
echo Please run the following command in MySQL:
echo   mysql -u root -p ^< database/schema.sql
echo.

echo ================================================
echo Installation Complete!
echo ================================================
echo.
echo Next steps:
echo 1. Configure database password in:
echo    - src/main/resources/config.yml
echo    - src/main/java/com/taskmanager/TaskManagerApplication.java
echo 2. Run the database schema: mysql -u root -p ^< database/schema.sql
echo 3. Start the backend: java -jar target/smart-task-manager-1.0.0.jar server src/main/resources/config.yml
echo 4. Open frontend: week2/frontend/index.html in your browser
echo.
pause
