# pbctf_writeup
[PBCTF Write Up](https://github.com/tbart27/pbctf_writeup)

# Dragon_CTF_WriteUp
### Team: 466 Crew
Taylor Bart<br>
Kamal Nadesan<br>
Matt Evans<br>
John Tiffany<br>

### Crypto: Ainissesthai
This challenge involved analyzing the output of an enigma machine algorithm implemented in Python. After researching the enigma machine, I came across this flaw in the enigma machine.<br>
<br>
![](https://github.com/tbart27/pbctf_writeup/blob/main/crypto1.png)<br>
<br>
Specifically, it was important to note that the cipher was involutionary therefore, when we recieve enough output then all we need to do is check for a letter that never shows up for that index in the string. Running `nc ainissesthai.chal.perfect.blue 1 >> enigma_output` manually a couple times gave me enough output to test my theory with this [code](https://github.com/tbart27/pbctf_writeup/blob/main/basicEnigmaBreaker.py).<br>
<br>
`import string`<br>
`enigma_file = open("enigma_output", 'r')`<br>
`results = list(enigma_file.readlines())`<br>
`enigma_file.close()`<br>
`message = ""`<br>
`for i in range(17):`<br>
&nbsp;&nbsp;&nbsp;&nbsp;`letter = string.ascii_uppercase`<br>
&nbsp;&nbsp;&nbsp;&nbsp;`count = [0] * 26`<br>
&nbsp;&nbsp;&nbsp;&nbsp;`for result in results:`<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`reading = result[i]`<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`readingNumber = ord(reading) - 65`<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`count[readingNumber] += 1`<br>
&nbsp;&nbsp;&nbsp;&nbsp;`report = list(zip(letter, count))`<br>
&nbsp;&nbsp;&nbsp;&nbsp;`for result in report:`<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`if result[1] == 0:`<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`message += result[0]`<br>
`print(message)`<br>
<br>
### Web: Sploosh
This seemed like a basic SSRF attack where we needed to redirect a request back to the server machine. At first I was looking for a SQL injection attack but the useless coordinates were throwing me for a loop. If I had more time, my next strategy would be to see if I could inject a reference to the flag on the server via the html objects.<br>
### Misc: Not-Stego
In terms of the challenge, I was unable to make any progress or leads for finding the flag. Howver, while attempting this challenge I installed and learned many tools for steganography (binwalk and stegsolv were a couple new ones for me alongside old methods like xxd).<br>
### Conclusion
As a team we were able to solve one flag but more importantly, I learned a lot about steganography tools and the enigma cipher.
