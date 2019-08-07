# Download python
if(!(Test-Path "python-3.6.8-embed-amd64.zip")){
    wget "https://www.python.org/ftp/python/3.6.8/python-3.6.8-embed-amd64.zip" `
        -O "python-3.6.8-embed-amd64.zip"
}
Expand-Archive -Path python-3.6.8-embed-amd64.zip -DestinationPath python-3.6.8-embed-amd64

# Download get-pip
cd python-3.6.8-embed-amd64
[System.Net.ServicePointManager]::SecurityProtocol = [System.Net.SecurityProtocolType]::Tls12;
wget "https://bootstrap.pypa.io/get-pip.py" -O "get-pip.py"
Add-Content -Path ./python36._pth -Value "import site" -Encoding UTF8
./python get-pip.py

# Install video_to_picture_intervals
cd ../
./python-3.6.8-embed-amd64/python -m pip install -r requirements.txt
./python-3.6.8-embed-amd64/python -m pip install opencv-python
