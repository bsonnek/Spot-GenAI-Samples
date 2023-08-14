# Spot by NetApp - Generative AI Repository for Generative AI and LLM learning

## Getting Started

This GitHub repo is meant to provide Spot Developers with a controlled development docker container for learning and testing Generative AI. Using this repo will provide Spot Develoeprs a quick and reliable way to gain access to a dedicated, secure, and audited Azure OpenAI service. 

### To Run Locally

This repo has only been tested on Windows using VSCode and Docker Desktop to run a docker dev container. We will need to consider using other options if this doesn't scale well.

* [VSCode](https://code.visualstudio.com/download) - Install VSCode if not already installed.
* [Git](https://git-scm.com/downloads) - Instal git
* [Docker VSCode Extension](https://code.visualstudio.com/docs/containers/overview) - Install Docker Extension in VSCode
* [Docker Desktop](https://docs.docker.com/desktop/) - Install Docker Desktop on local machine. The Docker Extension in VSCode will detect it automatically and use it to build a docker image for this project.

#### When Properly configured to run locally, You should expect the following:
 - When VSCode opens this repo it will automatically load the repo in a Docker conatiner python image.
 - Environmental variables will automatically be loaded for the Python Virtual Environment
 - Python will auto pip install everything in the "requirements.txt" file
 - Sample Notebooks will load .env variables and have a python virtual environment available to run sample code.
 - Running `streamlit run Streamlit-ChatBot-App.py` from a terminal. You can then access a local chatbot app app at `http://localhost:8501`. 

### Devcontainer

This project is designed to be used with VSCode and the Remote Containers extension.  Once you have the extension installed, open the project in VSCode and you will be prompted to open the project in a container.  This will build the container and install all the dependencies.

### Python Dependencies

The `requirements.txt` file contains all the python dependencies for this project.  The `devcontainer.json` file will automatically install these dependencies when the container is built.

### Configure to run locally in Docker Container Environment

To get started, you will need to create a `.env` file in the .devcontainer folder.  You will need to fill in the following values provided to you for the Azure API Management Service. Each Spot Gropu will have their own dedicated Endpoint for tracking and logging. Typically this Endpoint field would point to and OpenAI Instance:

```bash
AZURE_OPENAI_ENDPOINT =
AZURE_OPENAI_KEY =
```

### Running the App

To run the app, simply run the `streamlit run Streamlit-ChatBot-App.py`.  This will start the app on port 8501.  You can then access the app at `http://localhost:8501`. If running in a container, you will need to forward the port to your local machine if VSCode does not do it for you automatically.








## Credits

This project was forked from the [streamlit-chatgpt-ui](https://github.com/marshmellow77/streamlit-chatgpt-ui) under the MIT license and adapted to the Azure OpenAI Service.
This project was forked from the [az-oai-chatgpt-streamlit-harness](https://github.com/microsoft/az-oai-chatgpt-streamlit-harness/tree/main)

## Contributing
This project welcomes contributions and suggestions. Most contributions require you to agree to a Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us the rights to use your contribution. For details, visit https://cla.opensource.microsoft.com.

When you submit a pull request, a CLA bot will automatically determine whether you need to provide a CLA and decorate the PR appropriately (e.g., status check, comment). Simply follow the instructions provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the Microsoft Open Source Code of Conduct. For more information see the Code of Conduct FAQ or contact opencode@microsoft.com with any additional questions or comments.

## Trademarks
This project may contain trademarks or logos for projects, products, or services. Authorized use of Microsoft trademarks or logos is subject to and must follow Microsoft's Trademark & Brand Guidelines. Use of Microsoft trademarks or logos in modified versions of this project must not cause confusion or imply Microsoft sponsorship. Any use of third-party trademarks or logos are subject to those third-party's policies.
