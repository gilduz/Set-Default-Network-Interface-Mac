# Set-Default-Network-Interface-Mac
A really simple python app for mac OSX to select default network interface by command line

This tool is useful when more than one connection is active at the same time and you need to select the default one.
The same behavior can be reproduced moving UP/DOWN the connections in "System Preferences" -> "Network"


## Usage
sudo privileges needed

1) toggle between the first two preferred network interfaces
```
python toggleNetworkInterface.py
```

2) select between all network interfaces
```
python switchNetworkInterface.py
```
