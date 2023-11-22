# Wave a Flag
# Description
Can you invoke help flags for a tool or binary? This [program](https://mercury.picoctf.net/static/a14be2648c73e3cda5fc8490a2f476af/warm) has extraordinarily helpful information...

# Solution
1. Open the webshell terminal
2. Enter this in the terminal prompt: $ wget https://mercury.picoctf.net/static/a14be2648c73e3cda5fc8490a2f476af/warm
3. Make terminal executable with: $ chmod +x warm
4. Enter this in terminal prompt: $ ./warm
5. Enter this in terminal prompt to get the flag: $ ./warm -h 
6. Flag found

# Flag
picoCTF{b1scu1ts_4nd_gr4vy_755f3544}

# Command
chmod - change the permissions of a file or directory to all types of users

