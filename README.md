## Overview
This project is in a very early stage of development, but will be continuously improved over time.

## Tech Stack
- FastAPI Python backend with Selenium for Firefox browser automation
- Svelte web remote to control the system
  - Vite compiles Svelte files into the build folder, where they are served as static files by FastAPI
 
This project is not ready for use, and will likely require significant debugging to get set up (this will change with time)
My setup for this project is a Raspberry Pi 5 8GB, but any modern-ish Pi should work

Currently working on configuration scripts to set up the Raspberry Pi from a clean install

## Getting Started
#### Install Node.js with NVM
```bash
sudo apt update
# Install Node.js with NVM
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.3/install.sh | bash
source ~/.bashrc
nvm install --lts --latest-npm
```

#### Install the Firefox Geckodriver
```bash
cd /tmp
curl -L -o geckodriver.tar.gz https://github.com/mozilla/geckodriver/releases/download/v0.36.0/geckodriver-v0.36.0-linux-aarch64.tar.gz
tar -xzf geckodriver.tar.gz
sudo mv geckodriver /usr/local/bin/
sudo chmod +x /usr/local/bin/geckodriver
rm geckodriver.tar.gz && cd ~
```

#### Clone the Repo & Setup Python Virtual Environment
```bash
git clone https://github.com/shsiena/ytbox
cd ytbox && python -m venv venv
source venv/bin/activate && pip install requirements.txt
```

#### Build the Web Remote
```bash
npm run build
```

## Usage
#### Make sure the venv is activated
```bash
source venv/bin/activate
```

#### Start the Server
```bash
python server.py
```


## Advanced Configuration
Two flags are currently supported:
- `--dev`: Launches Firefox in windowed mode
- `--vnc`: Sets the display output to the primary VNC display

*Note: using VNC is not recommended, I've had a lot of issues with it and this project*




## Contributions
Contributions are not only appreciated but actively welcomed. 
This is something I've wanted to exist for a long time, so I figured I'd build it myself. 
If you have any ideas for improvements, feel free to make a PR :)
