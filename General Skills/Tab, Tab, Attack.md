# Tab, Tab, Attack
# Description
Using tabcomplete in the Terminal will add years to your life, esp. when dealing with long rambling directory structures and filenames: [Addadshashanammu.zip](https://mercury.picoctf.net/static/659efd595171e4c40378be6a2e9b7298/Addadshashanammu.zip)

# Solution
1. Open webshell
2. Enter these into terminal prompt: $ wget https://mercury.picoctf.net/static/659efd595171e4c40378be6a2e9b7298/Addadshashanammu.zip
3. Enter these to unzip the file: $ unzip Addadshashanammu.zip
4. Enter these to change directory: $ cd /Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/Maelkashishi/Onnissiralis/Ularradallaku
5. Enter these: $ strings fang-of-haynekhtnamet | grep pico

# Flag
picoCTF{l3v3l_up!_t4k3_4_r35t!_524e3dc4}
