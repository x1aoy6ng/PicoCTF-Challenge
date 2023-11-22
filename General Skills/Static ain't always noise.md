# Static ain't always noise
# Description
Can you look at the data in this binary: [static](https://mercury.picoctf.net/static/bc72945175d643626d6ea9a689672dbd/static)? This [BASH script](https://mercury.picoctf.net/static/bc72945175d643626d6ea9a689672dbd/ltdis.sh) might help!

# Solution
1. Open webshell
2. Enter these into terminal prompt: $ wget https://mercury.picoctf.net/static/bc72945175d643626d6ea9a689672dbd/static && wget https://mercury.picoctf.net/static/bc72945175d643626d6ea9a689672dbd/ltdis.sh
3. Enter these into terminal prompt: $ strings static | grep pico

# Command
strings - return the string characters into files <br>
grep - search text and strings in a given file

# Flag
picoCTF{d15a5m_t34s3r_1e6a7731}
