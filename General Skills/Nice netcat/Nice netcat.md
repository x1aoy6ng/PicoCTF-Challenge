# Nice netcat
# Description
There is a nice program that you can talk to by using this command in a shell: $ nc mercury.picoctf.net 43239, 
but it doesn't speak English...

# Solution
1. Open webshell terminal
2. Enter this command in the terminal prompt:$ nc mercury.picoctf.net 43239
3. You will see a list of numbers come out....
4. Using ASCII table to find the flag
5. Flag found

# Easiest way to find flag without using ASCII table
I wrote a Python script to make it easier for me to find the flag.
Find the [source](General Skills/Nice netcat/ASCII.py) here

# Flag
picoCTF{g00d_k1tty!_n1c3_k1tty!_7c0821f5}
