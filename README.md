Jenkins solution which compiles the C++ program HelloWorld, archives the executable and includes a python script to get the status.

start docker and create a jenkins image, after setup is complete open up the command line and type this command: docker exec -u 0 -it CONTAINER_NAME /bin/bash
after you have access to the jenkins command line install g++ using these commands: 
apt-get update
apt-get install -y build-essential g++ to update current packages and install g++ from build-essentials.

create a new pipeline and link to this github repository
the setup should now be complete and you can build the pipeline.
