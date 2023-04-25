# Technical_Test_Worldsensing
This is an API that can be used to change the order of the characters of a string, using sortmaps.
I have not used any database, so the program is not persistent. 

# Instructions to build and run the program:
## Building the Docker Image
1. Make sure you have Docker installed on your machine.
2. Open a terminal window and navigate to the directory where the Dockerfile and main.py files are located.
3. Run the following command to build the Docker image:
```bash
docker build -t sortmap .
```
This command will build a Docker image with the name sortmap and the latest tag.

## Running the Docker Container
Run the following command to start a Docker container:
```bash
docker run -p 80:80 sortmap
```
This command will start a Docker container with the sortmap image and expose port 80 to the host machine.

## Accessing the API
Once the Docker container is running, you can access the API at http://localhost/api/.
