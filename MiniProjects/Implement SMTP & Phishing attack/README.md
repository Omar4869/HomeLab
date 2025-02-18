# Background

One of the most successful avenues for initial access is phishing. Thus, i decided to implement a mail server on the DC host to allow for sending and receiving email.

# Mail server setup (DC)
Large organizations usually use Microsoft Exchange, however i opted for [hMailServer](https://www.hmailserver.com) since it offers a more lightweight solution. 

The installer is pretty standard and we choose `mail.homelab.local` as our domain. 

After the setup, we can add a user using the hMailServer GUI.

Finally, we can use Thunderbird to connect to our user account and view any emails

Note: make sure to allow port 25 to use SMTP

# pfSense setup (DC)

Not a lot of changes are needed on pfSense. I did have to do 2 things:
- Make sure to add a rule that allows SMTP (port 25) traffic
- If you are using pfSense as a DNS resolver, make sure the domain used for hMailServer resolves to the ip of DC.

# Hosting a simple credentials harvester 
There are more sophisticated open-source tools that harvest credentials such as Gophish. However, for simplicity, we opted for a simple python script to host a credentials harvester.

The script `phish_server.py` hosts a login page that directs to an error page. The script stores the collected credentials in the same folder.

![login](MiniProjects\Implement SMTP server\Images\Login_page.jpg)

![login_error](MiniProjects\Implement SMTP server\Images\login_error.jpg)


# Sending The phishing email

On our kali VM, we will use "swaks" to send emails.

we will use the following command to send the email:
```
swaks --to user1@homelab.local \
      --from attacker@mykali.com \
      --server mail.homelab.local \
      --header "Subject: Urgent: Account Verification Required" \
      --header "Content-Type: text/html" \
      --body '<html>
<head>
    <style>
        body { font-family: Arial, sans-serif; color: #333; }
        .container { padding: 20px; background-color: #f9f9f9; border: 1px solid #ddd; }
        .button { display: inline-block; padding: 10px 20px; color: white; background-color: #007bff; text-decoration: none; border-radius: 5px; }
        .footer { font-size: 12px; color: #777; margin-top: 20px; }
    </style>
</head>
<body>
    <div class="container">
        <h2>Important: Immediate Action Required</h2>
        <p>Hello,</p>
        <p>We detected unusual activity on your account. Please verify your information to prevent access restrictions.</p>
        <p><a href="http://192.168.1.129" class="button">Verify Account</a></p>
        <p class="footer">If you did not request this, please ignore this email.</p>
    </div>
</body>
</html>'

```

The email should look like this:
![email](MiniProjects\Implement SMTP server\Images\email.jpg)

Finally, we should see the stored password:
![password](MiniProjects\Implement SMTP server\Images\password.jpg)

# Final thoughts

- Real-life phishing requires more social engineering and understanding of the context of the email
- Other tools offer capabilities such as campaign management and link-clicks tracking
- Email solutions such as Microsoft Exchange and security solutions such as Zscaler offer countermeasures for phishing. 
