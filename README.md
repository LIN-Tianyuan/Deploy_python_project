# Deploy python project

Psl file to deploy python project to remote server and install and start services automatically.


## Usage

1. Prepare the project folder, add **pyproject.toml**, **read_toml.py** and **requirements.txt** files to the folder.
2. requirements.txt can be generated with this command: pip freeze > requirements.txt .
3. Fill in **pyproject.toml** file with relevant information (project name, python version, dependencies, remote server name), etc.
4. In the **DeployTemplate.psl** file, fill in the project name (projectName), root path (source_path), target path of the remote server (destination_path) and conda environment path of the remote server (env_path).
5. Copy the project folder to the root path(source_path).
6. Run the **DeployTemplate.psl** script.


## Implementation of automation steps

1. If the remote server has a service with the same name running, suspend and delete it.
2. Delete the folder with the same name as the project in the destination path of the remote server.
3. Copy the project files in the source path to the destination path of the remote server.
4. Delete the conda environment of the same name from the remote server, create a conda virtual environment with the same name as the project name, activate this virtual environment, enter the project and install the dependencies.
5. Install and start the service.
## Contributing

LIN Tianyuan

## License

[MIT](https://choosealicense.com/licenses/mit/)