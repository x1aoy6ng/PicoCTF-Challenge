# Matryoshka doll
# Description
Matryoshka dolls are a set of wooden dolls of decreasing size placed one inside another. What's the final one? Image: [this](https://mercury.picoctf.net/static/5ef2e9103d55972d975437f68175b9ab/dolls.jpg)
# Solution
xiaoyangishere-picoctf@webshell:~`$ wget https://mercury.picoctf.net/static/5ef2e9103d55972d975437f68175b9ab/dolls.jpg`<br>
xiaoyangishere-picoctf@webshell:~$ `binwalk -e dolls.jpg` <br> 


| DECIMAL | HEXADECIMAL | DESCRIPTION |
| :-----: | :-----:     | :-----:     |
|0        |     0x0     | PNG image, 594 x 1104, 8-bit/color RGBA, non-interlaced |
|3226     |     0xC9A   | TIFF image data, big-endian, offset of first image directory: 8 |
|272492   |    0x4286C  | Zip archive data, at least v2.0 to extract, compressed size: 378954, uncompressed size: 383940, name: **base_images/2_c.jpg** |
|651612   |   0x9F15C   | End of Zip archive, footer length: 22|
<br>

xiaoyangishere-picoctf@webshell:~$ `ls` <br>
**README.txt  _dolls.jpg.extracted  dolls.jpg** <br>
xiaoyangishere-picoctf@webshell:~$ `cd _dolls.jpg.extracted/base_images/` <br>
xiaoyangishere-picoctf@webshell:~/_dolls.jpg.extracted/base_images$ `ls` <br>
**2_c.jpg** <br>
xiaoyangishere-picoctf@webshell:~/_dolls.jpg.extracted/base_images$ `binwalk -e 2_c.jpg`
<br>

| DECIMAL | HEXADECIMAL | DESCRIPTION |
| :-----: | :-----:     | :-----:     |
|0        |    0x0      | PNG image, 526 x 1106, 8-bit/color RGBA, non-interlaced |
|3226     |     0xC9A   | TIFF image data, big-endian, offset of first image directory: 8 |
|187707   |     0x2DD3B | Zip archive data, at least v2.0 to extract, compressed size: 196045, uncompressed size: 201447, name: **base_images/3_c.jpg** |
|383807   |     0x5DB3F | End of Zip archive, footer length: 22 |
|383918   |     0x5DBAE | End of Zip archive, footer length: 22 |
<br>

xiaoyangishere-picoctf@webshell:~/_dolls.jpg.extracted/base_images$ `ls` <br>
**2_c.jpg  _2_c.jpg.extracted**
xiaoyangishere-picoctf@webshell:~/_dolls.jpg.extracted/base_images$ `cd _2_c.jpg.extracted/base_images/` <br>
xiaoyangishere-picoctf@webshell:~/_dolls.jpg.extracted/base_images/_2_c.jpg.extracted/base_images$ `ls` <br>
**3_c.jpg** <br>
xiaoyangishere-picoctf@webshell:~/_dolls.jpg.extracted/base_images/_2_c.jpg.extracted/base_images$ `binwalk -e 3_c.jpg`
<br>

| DECIMAL | HEXADECIMAL | DESCRIPTION |
| :-----: | :-----:     | :-----:     |
|  0      |   0x0       | PNG image, 428 x 1104, 8-bit/color RGBA, non-interlaced |
|  3226   |   0xC9A     | TIFF image data, big-endian, offset of first image directory: 8 |
|  123606 |   0x1E2D6   | Zip archive data, at least v2.0 to extract, compressed size: 77653, uncompressed size: 79808, name: **base_images/4_c.jpg** |
|  201425 |   0x312D1   | End of Zip archive, footer length: 22 |
<br>

xiaoyangishere-picoctf@webshell:~/_dolls.jpg.extracted/base_images/_2_c.jpg.extracted/base_images$ `ls` <br>
**3_c.jpg  _3_c.jpg.extracted** <br>
xiaoyangishere-picoctf@webshell:~/_dolls.jpg.extracted/base_images/_2_c.jpg.extracted/base_images$ `cd _3_c.jpg.extracted/base_images/` <br>
xiaoyangishere-picoctf@webshell:~/_dolls.jpg.extracted/base_images/_2_c.jpg.extracted/
base_images/_3_c.jpg.extracted/base_images$ `binwalk -e 4_c.jpg` <br> 

| DECIMAL | HEXADECIMAL | DESCRIPTION |
| :-----: | :-----:     | :-----:     |
|  0      |  0x0        |  PNG image, 320 x 768, 8-bit/color RGBA, non-interlaced |
|  3226   |  0xC9A      |  TIFF image data, big-endian, offset of first image directory: 8 |
|  79578  |  0x136DA    |  Zip archive data, at least v2.0 to extract, compressed size: 64, uncompressed size: 81, name: **flag.txt** |
|  79786  |  0x137AA    |  End of Zip archive, footer length: 22 |
<br>

xiaoyangishere-picoctf@webshell:~/_dolls.jpg.extracted/base_images/_2_c.jpg.extracted/base_images/
_3_c.jpg.extracted/base_images$ `ls`<br>
**4_c.jpg   _4_c.jpg.extracted** <br>
xiaoyangishere-picoctf@webshell:~/_dolls.jpg.extracted/base_images/_2_c.jpg.extracted/base_images/
_3_c.jpg.extracted/base_images$ `cd _4_c.jpg.extracted/`<br>  
xiaoyangishere-picoctf@webshell:~/_dolls.jpg.extracted/base_images/_2_c.jpg.extracted/base_images/
_3_c.jpg.extracted/base_images/_4_c.jpg.extracted$ `ls`<br>
**136DA.zip   flag.txt** <br>
xiaoyangishere-picoctf@webshell:~/_dolls.jpg.extracted/base_images/_2_c.jpg.extracted/base_images/
_3_c.jpg.extracted/base_images/_4_c.jpg.extracted$ `cat flag.txt`<br> 
**picoCTF{e3f378fe6c1ea7f6bc5ac2c3d6801c1f}**

# Flag
picoCTF{e3f378fe6c1ea7f6bc5ac2c3d6801c1f}

# Command
binwalk - a tool for searching given binary image for embedded files and executable code
