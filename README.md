# Spot - Repository for Generative AI and LLM learning

## Design
![image](https://github.com/bsonnek/Spot-GenAI-Samples/assets/10324197/a8417dc2-dd9c-4e4b-af79-d090cee3e973)


## Getting Started

This GitHub repo is meant to provide Spot developers with a controlled development docker container for learning and testing Generative AI. Using this repo will provide Spot developers a quick and reliable way to gain access to a dedicated, secure, and audited Azure OpenAI service. 

### To Run Locally

This repo has only been tested on Windows using VSCode and Docker Desktop to run a docker dev container. We will need to consider using other options if this doesn't scale well.

* [VSCode](https://code.visualstudio.com/download) - Install VSCode - if not already installed.
* [Git](https://git-scm.com/downloads) - Install git
* [Docker VSCode Extension](https://code.visualstudio.com/docs/containers/overview) - Install Docker Extension while in VSCode
* [Docker Desktop](https://docs.docker.com/desktop/) - Install Docker Desktop on local machine. The Docker Extension in VSCode will detect Docker Desktop automatically and use it to build a docker image for this project.
* [Clone Repo in VSCode](https://learn.microsoft.com/en-us/azure/developer/javascript/how-to/with-visual-studio-code/clone-github-repository?tabs=create-repo-command-palette%2Cinitialize-repo-activity-bar%2Ccreate-branch-command-palette%2Ccommit-changes-command-palette%2Cpush-command-palette) - Clone this repo to VSCode.
* **DO Not Build Docker Container after Closing Repo** Follow steps below to create the .env file first before building docker. 
* After Cloning the repo, VSCode should then prompt to open the repo in a container. This will build the container and install all the dependencies.
* VSCode Can then build a Docker Container for this project locally. Once, VSCode builds the docker it will then Remotely connect to the container. 

# ** Do Not Builder Docker Until You Create the .env File **
### Create .env File  - 

To get started, you will need to create a `.env` file in the root.  Use the existing .envEXAMPLE as a template for the new .env file.

You will need to fill in the following values provided to you for the Azure API Management Service. 
Each Spot Group will have their own dedicated Endpoint and API Key for tracking and logging purposes.

```bash
AZURE_OPENAI_ENDPOINT=
AZURE_OPENAI_API_KEY=
```

When Changing Variables - You will need to rebuild the docker container to update variables in the Python virtual environment:
    - run Dev Containers: Rebuild Container from the Command Palette (F1) to pick up the change.

### Python Dependencies

The `requirements.txt` file contains all the python dependencies for this project.  The `devcontainer.json` file will automatically install these dependencies when the container is built.

#### When Properly configured to run locally, You should expect the following:
 - When VSCode opens this repo it will automatically load the repo in a Docker conatiner python image.
 - Environmental variables will automatically be loaded for the Python Virtual Environment
 - Python will auto pip install everything in the "requirements.txt" file
 - Sample Notebooks will load .env variables and have a python virtual environment available to run sample code.
 - Running `streamlit run Streamlit-ChatBot-App.py` from a terminal. You will have access a local chatbot app from your local browser `http://localhost:8501`. 

### Running the App

To run the app, simply run the `streamlit run Streamlit-ChatBot-App.py`.  This will start the app on port 8501.  You can then access the app at `http://localhost:8501`. If running in a container, you will need to forward the port to your local machine if VSCode does not do it for you automatically.

## Credits

This project was forked from the [streamlit-chatgpt-ui](https://github.com/marshmellow77/streamlit-chatgpt-ui) under the MIT license and adapted to the Azure OpenAI Service.
This project was forked from the [az-oai-chatgpt-streamlit-harness](https://github.com/microsoft/az-oai-chatgpt-streamlit-harness/tree/main)
This project refrences examples from [openai-cookbook](https://github.com/openai/openai-cookbook)
This repository contains references to LLM, as well as prompt engineering libraries, focused on Azure-related libraries. [azure-openai-llm-vector-langchain](https://github.com/kimtth/azure-openai-llm-vector-langchain/blob/main/README.md)
