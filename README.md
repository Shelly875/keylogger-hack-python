<img src="./images/keylogger-guide.jpg">

<h1> keylogger-hack-python <h1>
<h4> This project contains keyloger program, with encryption and peer to peer comunication. <h4>
  
# Authors
  * Shelly Miron
  * Liat Gobler
  * Beni Segal
# Getting Started:
  * Install <code>pycharm</code> and <code>python3.6</code> or above.
  * Packages required: <code> socket, Listener, pynput, logging </code>
  * Environemnt to run: <code> Windows 10 </code>.
  * Firewall - disabled.
# Steps to run:
  * Run first the <code>py</code> file that sends the hacked keys to the reciver - <code>client2.py</code>
  * Run the <code>py</code> file that recived the hacked data from the sender - <code>client.py</code>
  * Behind the Scenes - the hacked keys are encoded with base64 and send to the reciver
    whome decode the keys back. all the procedure happed without the attacked client (client2) knows about his keys recorded.
