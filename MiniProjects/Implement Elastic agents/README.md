# Background

In its current state, the lab only monitors network traffic.

To add more visibility, we will deploy Elastic agents to collect host events and allow for real time data collection:
- `Ubuntu machine** (192.168.7.10)`
- `Domain Controller: Windows Server with User1 and User2 machines (192.168.2.x)`


# Security onion settings

Allow Elastic agent traffic through the firewall by visiting:
`Administration –> Configuration –> firewall –> hostgroups –> elastic_agent_endpoint`

Then, set the value of allowed IP blocks that can access the Elastic fleet via port `8220`.

# Agent deployment

Simply download the agent installer from the `Downloads` tab and run it on each host.

Finally, each host should show up in the `Elastic fleet` interface and host logs should start showing up.






