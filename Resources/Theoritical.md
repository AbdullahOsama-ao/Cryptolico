## Pre-intro

__Computer Systems have a huge critical value for their owners. So, it became so important to Computer Experts to find some manners to provide good protection for Systems & Data for setting them to be fit according to a concept called (CIA-Triad)...__

> Q1: Protection for/from what?

- __vulnerabilities__ :  A weakness in the system that could be exploited to cause a harm.

- __threat__ :  Set of conditions that could use a vulnerability to cause loss or harm in a system.

  => __human-initiated__ : A human has ability to exploit a vulnerability.

  => __computer-initiated__ : A program deny another from working correctly.

- __incident__ : Occurs when a threat exploits the vulnerability and causing harm.

- __control__ : Prevent threats from exercising vulnerabilities.

> Q2: What's CIA-Triad?

__(A system in CIA-Triad means that it achieves 3 rules...)__

1. __confidentiality__ : Assets are viewed only by authorized users.
2. __integrity__ : Assets are modified only by authorized users.
3. __availability__ : Assets can be used/reached any time only by authorized users.

__(2 Rules are added if our system we protect is dealing with Networks...)__

4. __authentication__ : Confirm ID of a sender.
5. __nonrepudiation(accountability)__ : Confirm that the sender can't deny having sent something.

> Q3: What's major security tools used?

- __identification__ : Verifying (who) person uses the system.
- __access-control__  : Verifying (how) he uses the system.
- __encryption__ : Obstacle for (what) unauthorized access.

---



## About Encryption/Cryptography

__Cryptography is a technique or tool used against unauthorized people to hide the real data from them. There are a lot of kinds of Encryption techniques used...__

> no-key-required algorithms...

- Reverse
- Rot13
- Hash functions

> key-required algorithms...

- Caesar
- Mono-alphabetic
- Poly-alphabetic
- Hill
- DES (Data Encryption Standard)
- AES (Advanced Encryption Standard)
- RSA (Rivest-Shamir-Adleman)

---



## Highlight on the Poly-alphabetic  Technique

__The main idea of it is to encrypt text using multiple substitution alphabets to increase security by making the frequency analysis of letters more difficult for cryptanalysts...__

> properties...

- average-strength algorithm.
- more powerful than (mono-alphabetic algorithm) that's susceptible to frequency analysis by cryptanalysts.
- manipulating of algorithm is more flexible.
- easy to implement.

> poly-alphabetic types ... 

- Vigenère cipher
- Autokey cipher
- Beaufort cipher
- Playfair cipher
- Alberti cipher
- Trithemius cipher

---



## About Vigenère cipher

__An algorithm is used to encrypt text by shifting letters using a keyword(key), creating a polyalphabetic substitution cipher that varies the shift for each letter based on the keyword...__

> encryption mechanism...

- repeating (key)  that user enters along the text that user want to encrypt(plain-text).
- converting (key) & (plain-text) to numerical equivalent numbers according to (a=0 ~ z=25), in case of just dealing with lowercase.
- shifting each letter of (plain-text) using a specific arithmetic equation corresponding to the (key's) value.
- by combining each shifted letter of (plain-text), it gives you shifted-letters text called (cipher-text)

> decryption mechanism...

- literally, the same encryption's steps, except that we will apply the reversed or contrary arithmetic equation that leads us to return the original text(plain-text)

> Considerations...

- using unpredictable & long key will less from potential that your data Vulnerable to frequency analysis and vice versa.
- Performing (frequency analysis) on your data may lead to your data being Hacked after several attempts if you didn't choose the key well.
