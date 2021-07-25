# Here we install python3 with all packages and updates (you can choose any version from dockerhub).
FROM ubuntu:20.04
RUN apt-get update && apt-get -y update
RUN apt-get install -y build-essential python3.6 python3-pip python3-dev
RUN pip3 -q install pip --upgrade
# Here we create new directory and copy all files to it.
RUN mkdir /app
WORKDIR /app
COPY . .
# Now we install needed packages for project to work (db,jupyter and scripts)
RUN pip3 install -r requirements.txt
RUN pip3 install jupyter
# Now we run the automation shell inside the isolated container
RUN chmod +x esc.sh
RUN ./esc.sh
# Ensures that docker container starts at the notebook i have saved
WORKDIR /src/notebooks
# Start the notebook in the end
CMD ["jupyter", "lab", "--port=8888", "--no-browser", "--ip=0.0.0.0", "--allow-root"]
