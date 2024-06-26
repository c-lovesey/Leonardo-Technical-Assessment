# Use an official Ubuntu as a parent image
FROM ubuntu:latest

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive

# Install required packages
RUN apt-get update && \
    apt-get install -y build-essential g++ && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Create a directory for the Jenkins user
RUN mkdir -p /var/jenkins_home
RUN useradd -m -d /var/jenkins_home -s /bin/bash jenkins

# Set the working directory
WORKDIR /var/jenkins_home

# Switch to the Jenkins user
USER jenkins

# Default command to keep the container running
CMD ["sleep", "infinity"]
