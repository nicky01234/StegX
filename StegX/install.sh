#!/bin/bash

clear
echo "Installing StegX..."
sleep 1

pip3 install -r requirements.txt

chmod +x stegx.py
sudo ln -sf $(pwd)/stegx.py /usr/local/bin/stegx

echo "Installation complete!"
echo "Run the tool using: stegx"
