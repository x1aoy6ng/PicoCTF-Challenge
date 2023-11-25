# First grep
# Description
Can you find the flag in [file](https://jupiter.challenges.picoctf.org/static/315d3325dc668ab7f1af9194f2de7e7a/file)? This would be really tedious to look through manually, something tells me there is a better way.

# Solution
1. Download the [file](https://jupiter.challenges.picoctf.org/static/315d3325dc668ab7f1af9194f2de7e7a/file).
2. Enter these into the terminal prompt: `$ strings file | grep pico`

# Flag
picoCTF{grep_is_good_to_find_things_f77e0797}
