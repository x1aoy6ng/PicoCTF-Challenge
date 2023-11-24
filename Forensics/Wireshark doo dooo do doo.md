# Wireshark doo dooo do doo...
# Description
Can you find the flag? [shark1.pcapng](https://mercury.picoctf.net/static/ea41c400c3c7b4a63406e5e607d362ab/shark1.pcapng).
# Solution
1. Open this [file](https://mercury.picoctf.net/static/ea41c400c3c7b4a63406e5e607d362ab/shark1.pcapng) with wireshark, click Statistics --> Endpoints --> TCP --> first line with port 80 (searching for http) <br>
2. In line 827, line-based text data consists of **`Gur synt vf cvpbPGS{c33xno00_1_f33_h_qrnqorrs}`** <br>
3. Use [online tool](https://www.cryptool.org/en/cto/caesar) to decrypt it using _**ROT13**_
# Flag
pICocTf{p33KAB00_1_s33_u_DEADBEEF}
