# Enigma Machine

## Introduction
As part of COMP6841 (Extended Security Engineering and Cyber Security), students complete a 30-hour project on anything they think is awesome, yet relevant. For my project, I wanted to write a program that can encrypt and decrypt messages using the Enigma.

I wrote my program in Python, before I transpiled it into C++ to challenge myself with a language I hadn't used before (it was indeed challenging).

## Usage
To use the Python program, simply run it using `python enigma.py`.

To use the C++ program, first compile it using `gcc enigma.cpp -o enigma` before running the executable using `./enigma.exe`.

### Configuration
With the Python program, the available rotors are I, II and III and the available reflectors are B and C. The user can configure the rotor order, the reflector and the starting positions (A - Z) for the rotors.
* To use rotors II, I and III and in that order (left to right), enter `II I III` when prompted.
* To use reflector B, enter `B` when prompted.
* To start on A, B, C and in that order (left to right), enter `ABC` when prompted.

With the C++ program, the rotors in use are I, II and III (left to right) and the reflector in use is B. The user can however configure the starting positions (A - Z) for the rotors. To start on A, B, C and in that order (left to right), enter `ABC` when prompted.

### Encryption/ Decryption
Next, you will be prompted to enter your message. Please note the following -
* The Enigma Machine is a symmetric cipher. Whether you are encrypting or decrypting a message doesn't matter, as long as you have specified the correct configuration settings.
* Only alphabetical characters will be read - any punctuation or special characters will be ignored.
* The C++ implementation will only read the first word of your message so be sure to remove any spaces between words. This is not an issue with the Python implementation.

## Disclaimers
For the purposes of this project, the ring settings are hard-coded as '01-A' and there is no plugboard.

## Acknowledgements
I want to acknowledge the following resources -
* http://wiki.franklinheath.co.uk/index.php/Enigma/Paper_Enigma
* https://www.cs.cornell.edu/courses/cs3110/2019sp/a1/#step-6-rotors
* https://en.wikipedia.org/wiki/Enigma_rotor_details#Rotor_offset
* https://www.101computing.net/enigma/enigma-M3.html

## What's Next
As mentioned earlier, users cannot configure the ring settings or the plugboard. This will be coming soon!<br>
I want to continue working on this project to add these features, as well as more options for the rotors and reflectors. Eventually, I'll want to create a front-end user interface for the program too.
