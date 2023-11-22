# Transformation
# Description
I wonder what this really is... [enc](https://mercury.picoctf.net/static/2b4cea9b07db22bf4f933fddd1b8caa9/enc) <br>''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])

# Solution
1. Open webshell
2. Enter these into terminal prompt: $ wget https://mercury.picoctf.net/static/2b4cea9b07db22bf4f933fddd1b8caa9/enc
3. Copy these 灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸弰㑣〷㘰摽 into [CyberChef](https://gchq.github.io/CyberChef/) using _**Magic**_ recipe
4. Recipe used is : **UTF-16BE**
   
# Flag
picoCTF{16_bits_inst34d_of_8_04c0760d}
