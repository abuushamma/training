#!/bin/bash

# Smart Task Manager - Unix/Linux/Mac Installation Script

echo "================================================"
echo "Smart Task Manager - Setup Script"
echo "================================================"
echo ""

# Check Java
echo "[1/5] Checking Java installation..."
if ! command -v java &> /dev/null; then
    echo "ERROR: Java not found! Please install JDK 8 or higher."
    echo "macOS: brew install openjdk@8"
    echo "Ubuntu: sudo apt install openjdk-8-jdk"
    exit 1
fi
echo "✓ Java found: $(java -version 2>&1 | head -n 1)"

# Check Maven
echo "[2/5] Checking Maven installation..."
if ! command -v mvn &> /dev/null; then
    echo "ERROR: Maven not found! Please install Maven 3.6+"
    echo "macOS: brew install maven"
    echo "Ubuntu: sudo apt install maven"
    exit 1
fi
echo "✓ Maven found: $(mvn -version | head -n 1)"

# Check MySQL
echo "[3/5] Checking MySQL installation..."
if ! command -v mysql &> /dev/null; then
    echo "WARNING: MySQL command not found"
    echo "macOS: brew install mysql"
    echo "Ubuntu: sudo apt install mysql-server"
else
    echo "✓ MySQL found: $(mysql --version)"
fi

# Build backend
echo "[4/5] Building backend..."
cd week2/backend
mvn clean package -DskipTests
if [ $? -ne 0 ]; then
    echo "ERROR: Maven build failed!"
    exit 1
fi
echo "✓ Backend built successfully"

# Setup instructions
echo "[5/5] Database setup..."
echo "Please run the following command:"
echo "  mysql -u root -p < database/schema.sql"
echo ""

echo "================================================"
echo "Installation Complete!"
echo "================================================"
echo ""
echo "Next steps:"
echo "1. Configure database password in:"
echo "   - src/main/resources/config.yml"
echo "   - src/main/java/com/taskmanager/TaskManagerApplication.java"
echo "2. Run the database schema: mysql -u root -p < database/schema.sql"
echo "3. Start the backend: java -jar target/smart-task-manager-1.0.0.jar server src/main/resources/config.yml"
echo "4. Open frontend: week2/frontend/index.html in your browser"
echo ""
