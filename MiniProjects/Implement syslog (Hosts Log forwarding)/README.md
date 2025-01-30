# Background

In its current state, the lab only monitors network traffic.

To add more visibility, we will use syslog to collect host events from:
- `**Ubuntu machine** (192.168.7.10)`
- `**Domain Controller**: Windows Server with User1 and User2 machines (192.168.2.x)`

The logs will be routed to Security Onion. 

# Security onion settings

Allows syslog traffic through the firewall by visiting:
`Administration –> Configuration –> firewall –> hostgroups –> syslog`

Then set the value of allowed IP block that can access the assigned syslog port `514`.

# Ubuntu machine settings

Ubuntu comes prepacked with rsyslog.

To enable sending logs to security onion, simply open `/etc/rsyslog.conf` and add the line:
`*.* @<security onion interface>:514`





