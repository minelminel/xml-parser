# Installation script for local deployment

# [1] Prepare the environment
pip3 install virtualenv

# [2] Source the environment
source venv/bin/activate

# [3] Install requirements
pip3 install -r requirements.txt

# [4] Run the server
python3 src/app.py
