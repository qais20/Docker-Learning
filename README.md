# Docker Reference Guide

## Table of Contents
- [What is Docker?](#what-is-docker)
- [Containers](#containers)
- [Images](#images)
- [Difference Between Docker and VMs](#difference-between-docker-and-vms)
- [Layer-Based Approach](#layer-based-approach)
- [Docker Compose Files](#docker-compose-files)
- [Dockerfiles](#dockerfiles)
- [Docker Swarm vs Kubernetes](#docker-swarm-vs-kubernetes)
- [Purpose of Orchestration Tools](#purpose-of-orchestration-tools)
- [Namespaces](#namespaces)
- [Cgroups](#cgroups)
- [Common Docker Commands](#common-docker-commands)
- [Docker Learning](#docker-learning)
- [Additional Resources](#additional-resources)

---

## What is Docker?

Docker is an open-source platform that allows developers to automate the deployment of applications in lightweight, portable containers. Containers package an application with all its dependencies, ensuring it runs consistently across different environments.

### Key Benefits:
- **Portability**: Run the same container on any system that supports Docker.
- **Isolation**: Keep applications isolated from each other, reducing dependency conflicts.
- **Scalability**: Easily scale applications up or down by adding or removing containers.

---

## Containers

Containers are lightweight, standalone, executable packages that include everything needed to run a piece of software: code, runtime, libraries, and system tools.

### Features:
- **Lightweight**: Containers share the host system’s kernel and resources, making them much more efficient than traditional virtual machines (VMs).
- **Fast Startup**: Containers can start up in seconds, significantly reducing the time to deploy applications.

### Example:
To run a simple container using the official Ubuntu image:
```bash
docker run -it ubuntu /bin/bash
```

---

## Images

Images are the read-only templates used to create containers. An image is composed of multiple layers, each representing a filesystem change or addition.

### Features:
- **Version Control**: Images can be versioned and stored in registries like Docker Hub.
- **Reusability**: Layers in images can be reused across different images, saving space.

### Example:
To pull the latest Nginx image:
```bash
docker pull nginx:latest
```

---

## Difference Between Docker and VMs

### Docker
- Runs on the host OS kernel.
- Containers share the same OS and are more lightweight.
- Starts in seconds.

### Virtual Machines (VMs)
- Runs on hypervisors (like VMware, VirtualBox).
- Each VM includes a full copy of an OS, resulting in larger sizes.
- Takes minutes to start.

### Comparison Table:

| Feature                   | Docker                | Virtual Machines       |
|---------------------------|-----------------------|-------------------------|
| Overhead                  | Low                   | High                    |
| Boot Time                 | Seconds               | Minutes                 |
| OS Sharing                | Yes                   | No                      |
| Resource Allocation        | Efficient            | Less efficient          |

---

## Layer-Based Approach

Docker uses a layered filesystem to manage images. Each layer represents a change to the image. This approach allows for efficient storage and management.

### Features:
- **Copy-on-Write**: Only changes made to the previous layer are saved.
- **Layer Sharing**: Multiple images can share common layers, reducing disk space usage.

### Example:
```bash
# Create a new image with a Dockerfile
FROM ubuntu:20.04
RUN apt-get update && apt-get install -y python3
```
This Dockerfile creates an image with two layers: one for the base Ubuntu image and another for the installed packages.

---

## Docker Compose Files

Docker Compose is a tool for defining and running multi-container Docker applications. It uses a YAML file to configure the application’s services.

### Features:
- **Multi-container Setup**: Easily manage and orchestrate multiple containers.
- **Configuration**: Simplifies the configuration of services, networks, and volumes.

### Example `docker-compose.yml`:
```yaml
version: '3'
services:
  web:
    image: nginx
    ports:
      - "80:80"
  app:
    build: .
    ports:
      - "5000:5000"
```
In this example, we define a web service using Nginx and an application service that builds from the current directory.

---

## Dockerfiles

A Dockerfile is a script that contains a series of instructions to create a Docker image. Each instruction creates a new layer in the image.

### Common Instructions:
- `FROM`: Specifies the base image to use for the Docker image.
- `RUN`: Executes commands in the container.
- `COPY`: Copies files from the host machine into the container.
- `WORKDIR`: Sets the working directory for subsequent instructions.
- `CMD`: Specifies the command to run when the container starts.

### Example `Dockerfile`:
```dockerfile
# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Run app.py when the container launches
CMD ["python", "app.py"]
```

---

## Docker Swarm vs Kubernetes

### Docker Swarm
- Native clustering and orchestration for Docker.
- Simpler to set up and manage.
- Integrated with Docker CLI.

### Kubernetes
- A powerful orchestration tool for managing containers at scale.
- Supports complex workloads and has a steeper learning curve.
- Offers features like self-healing, horizontal scaling, and advanced networking.

### Summary Table:

| Feature                    | Docker Swarm        | Kubernetes           |
|----------------------------|---------------------|-----------------------|
| Complexity                  | Low                 | High                  |
| Setup Time                  | Quick               | Longer                |
| Scaling                     | Easy                | Very robust           |
| Load Balancing              | Built-in            | Advanced              |

---

## Purpose of Orchestration Tools

Orchestration tools like Docker Swarm and Kubernetes manage the deployment, scaling, and operations of application containers across clusters of hosts.

### Benefits:
- **Scaling**: Automatically scale applications based on demand.
- **High Availability**: Ensure applications remain available despite failures.
- **Resource Management**: Efficiently manage resources across multiple containers.

---

## Namespaces

Namespaces provide isolation for system resources, allowing containers to operate as if they have their own operating system. Docker uses several types of namespaces:

- **PID Namespace**: Isolates process IDs.
- **NET Namespace**: Isolates network interfaces.
- **IPC Namespace**: Isolates inter-process communication.

### Example:
To see the namespaces in action, you can check the PID namespace:
```bash
# Run a container and check its PID namespace
docker run --rm -it --pid=host ubuntu bash
```

---

## Cgroups

Control groups (cgroups) manage and limit the resources (CPU, memory, disk I/O, etc.) that a set of processes can use. Docker uses cgroups to ensure containers do not exceed their resource limits.

### Key Features:
- **Resource Limitation**: Set limits on CPU and memory usage.
- **Resource Accounting**: Track resource usage for individual containers.

### Example:
To limit memory usage for a container:
```bash
docker run -it --memory="512m" ubuntu /bin/bash
```

---

## Common Docker Commands

| Command                                | Description                                      |
|----------------------------------------|--------------------------------------------------|
| `docker run <image>`                  | Run a container from an image.                   |
| `docker ps`                            | List running containers.                          |
| `docker ps -a`                         | List all containers (running and stopped).      |
| `docker stop <container_id>`          | Stop a running container.                         |
| `docker start <container_id>`         | Start a stopped container.                        |
| `docker exec -it <container_id> bash` | Execute a command inside a running container.    |
| `docker images`                        | List all Docker images on the local machine.    |
| `docker rmi <image_id>`               | Remove a Docker image.                           |
| `docker build -t <name>:<tag> .`      | Build an image from a Dockerfile in the current directory. |
| `docker-compose up`                    | Start services defined in a `docker-compose.yml` file. |
| `docker-compose down`                  | Stop and remove containers defined in a `docker-compose.yml` file. |

---

## Docker Learning

### Docker Commands Explained:

- **`FROM`**: Specifies the base image to use for the Docker image.
- **`RUN`**: Executes commands in the container, commonly used for installing packages.
- **`COPY`**: Copies files from the host machine into the container.
- **`WORKDIR`**: Sets the working directory for subsequent instructions, making it easier to manage file paths.
- **`CMD`**: Specifies the command to run when the container starts, defining the default behaviour.

---

## Additional Resources
- [Official Docker Documentation](https://docs.docker.com/)
- [Docker Hub](https://hub.docker.com/)
- [Kubernetes Documentation](https://kubernetes.io/docs/home/)
- [Docker Compose Documentation](https://docs.docker.com/compose/)

---
