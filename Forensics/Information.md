# Information
# Description
Files can always be changed in a secret way. Can you find the flag? [cat.jpg](https://mercury.picoctf.net/static/b4d62f6e431dc8e563309ea8c33a06b3/cat.jpg)

# Solution
1. open webshell
2. Enter these in the terminal prompt: wget https://mercury.picoctf.net/static/b4d62f6e431dc8e563309ea8c33a06b3/cat.jpg
3. Use exiftool to read cat.jpg: $ exiftool cat.jpg
4. Find the license of the cat.jpg (base64 encoded)
5. Enter these in the terminal prompt: $ echo cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9 | base64 -d

# Flag
picoCTF{the_m3tadata_1s_modified}

# Command
exiftool - read, write or create files <br>
echo - display lines of strings that are passed as arguments
