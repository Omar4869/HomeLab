# Background

During a bug hunting session a while ago, I discovered a misconfiguration that allowed external access to `/xmlrpc.php` on WordPress websites. This misconfiguration can be exploited to trigger outgoing requests from the server to a targeted destination.

More importantly, it can be used to determine the real IP address of a website that is behind a CDN such as Cloudflare.

More information here: [https://github.com/rm-onata/xmlrpc-attack](https://github.com/rm-onata/xmlrpc-attack).

I decided to create a detection rule to identify such access attempts.

# Environment Setup

The initial step was to configure the WordPress instance on an Ubuntu machine (192.168.7.10). The docker container was made using docker-compose.yml. It also ensures that the Docker container is only exposed to our internal network.

This set up allows us to interact with the Docker container from the Kali Linux host (192.168.1.129).

# Security Onion Detection Rule

Starting with Security Onion 2.4, it's possible to write Suricata rules directly from the Detection tab. In earlier versions, writing rules had to be done within Kibana.

So the rule i added is:

```suricata
alert http $EXTERNAL_NET any -> $HOME_NET any 
(msg:"POST to xmlrpc.php with 200 Response"; 
http.method; content:"POST"; 
http.uri; content:"/xmlrpc.php"; 
http.stat_code; content:"200"; 
!sameip; sid:1068526; rev:1;)
```

This rule looks for characteristics of access to /xmlrpc.php and generates an alert for security analysts.

Note: The rule's effect typically takes around 15-20 minutes after enabling it to start generating alerts.

# Testing

We can test the rule by using test_rule.py. After running the script we should see the following alert in Security Onion.

![results](https://github.com/omarbinmuhisen/HomeLab/blob/main/images/021649.png?raw=true)
