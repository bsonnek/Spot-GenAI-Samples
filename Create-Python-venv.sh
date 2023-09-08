 #!/bin/sh
## Building a Virtual Environment is not necessary if running inside a docker container.
## To Run: Open Terminal - Paste:  ./Create-Python-venv.sh


echo ""
echo "Building Python Environment for testing API Keys"
echo ""


echo 'Creating python virtual environment ".venv"'
python3 -m venv .venv

echo 'Installing PIP Requirments"'
./.venv/bin/python -m pip install -r requirements.txt