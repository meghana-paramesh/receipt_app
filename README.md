# Receipt Processor

This application is designed to manage and process receipt data. It is containerized using Docker for easy setup and deployment.

## Prerequisites

Before running the application, ensure you have the following prerequisites installed:

1. **Docker Desktop**: The application runs in a Docker container, so Docker Desktop is required. If it's not already installed, follow the instructions on the [Docker Desktop Installation Guide](https://docs.docker.com/desktop/install/windows-install/).

2. **Git**: To clone the repository, you need Git installed. If you don't have Git, you can download it from [Git Downloads](https://git-scm.com/downloads).

## Running the Application

Follow these steps to get the application up and running:

### 1. Clone the Repository

First, clone the repository from GitHub to your local machine:

```bash
git clone https://github.com/meghana-paramesh/receipt_app.git
```

### 2. Navigate to the Project Directory
Change into the root directory of the project:
```
cd path/to/receipt_app
```
Replace path/to/receipt_app with the actual path to the cloned repository on your machine.

### 3. Build and Run the Application using Docker
With Docker Desktop running, execute the following command in the root directory of the project:
```
docker-compose up --build
```
This command builds the Docker image for the application and starts the containers as defined in the docker-compose.yml file.
### 4. Accessing the Application
Once the application is running, you can access it through your web browser. The default port and URL will be provided in the terminal output.

### 5. Accessing the application endpoints
This application utilizes Swagger for API documentation and testing. The Swagger UI can be accessed at the following URL: http://\<domain:port\>/receipts/swagger/ (Example: http://localhost:8000/receipts/swagger/). This interface provides a convenient way to view and interact with the application's API endpoints.
### 6. Additional Information
1. Docker Compose: This project uses Docker Compose for defining and running multi-container Docker applications.
2. Logs: You can view the logs in the terminal to monitor the application activity.

