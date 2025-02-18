# Home Security Lab

This repository documents projects from my home security lab built with VMware. It is not intended to provide step-by-step instructions for reproducing the lab environment. The lab is used to simulate various attacks and test different defense measures. 

## Overview
The home security lab features:
- Virtualized network and system environment.
- Configurable firewall and security rules
- Tools for network monitoring and threat detection.

## Lab Architecture
![Lab Architecture](https://github.com/omarbinmuhisen/HomeLab/blob/main/Lab%20Diagram.png?raw=true)

### Components
- **Router/Firewall**: pfSense (192.168.1.1 to 192.168.7.1)
- **Attack Machine**: Kali Linux (192.168.1.129)
- **Domain Controller**: Windows Server with User1 and User2 machines (192.168.2.x)
- **Monitoring**: Security Onion (192.168.3.10)
- **Logging**: Splunk (192.168.4.10)
- **Other Systems**: Ubuntu machine (192.168.7.10)
