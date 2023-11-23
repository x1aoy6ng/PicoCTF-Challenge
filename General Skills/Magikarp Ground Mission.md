# Magikarp Ground Mission
# Description
Do you know how to move between directories and read files in the shell? Start the container, `ssh` to it, and then `ls` once connected to begin. Login via `ssh` as `ctf-player` with the password, `6d448c9c`
Additional details will be available after launching your challenge instance.

# Solution
1. Open webshell
2. Enter these into terminal prompt:`$ ssh ctf-player@venus.picoctf.net -p 54934`
3. Enter: `yes`
4. password: **6d448c9c**
5. Enter these into terminal prompt: `$ ls`
6. Enter these into terminal prompt to get first part of flag: `$ cat 1of3.flag.txt instructions-to-2of3.txt` to get first part of flag
7. Enter these into terminal prompt: `$ cd /`
8. Enter these into terminal prompt: `$ ls`
9. Enter these into terminal prompt to get middle part of flag: `$ cat 2of3.flag.txt instructions-to-3of3.txt`
10. Enter these into terminal prompt: `$ cd ~`
11. Enter these into terminal prompt to get last part of flag: `$ cat 3of3.flag.txt`

# Flag
picoCTF{xxsh_0ut_0f_\/\/4t3r_5190b070}

# Command
ls - list out directory contents <br>
cd - change directory
