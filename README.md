# Enigma Machine

## Introduction
As part of COMP6841 (Extended Security Engineering and Cyber Security), students complete a 30-hour project on anything they think is awesome, yet relevant. For my project, I wanted to write a program that can encrypt and decrypt messages using the Enigma.

## Usage
To use the program, simply run it using `python enigma.py`.

### Configuration
First, you will be prompted to enter your configuration settings i.e. the starting positions for the rotors. From left to right, the rotors in use are rotors I, II and III from the Enigma I.<br><br>
Each rotor can be configured to start on a different letter (A - Z). To start on A, B, C and in that order (left to right), enter `ABC`.

### Encryption/ Decryption
Next, you will be prompted to enter your message. Please note the following -
* The Enigma Machine is a symmetric cipher. Whether you are encrypting or decrypting a message doesn't matter, as long as you have specified the correct configuration settings.
* Only alphabetical characters will be read - any punctuation, spaces or special characters will be ignored.

## Disclaimers
For the purposes of this project, users can only select the starting positions of the rotors. The rotor order is 'I, II, III', the reflector in use is Reflector B, the ring settings are hard-coded as '01-A' and there is no plugboard.

## Acknowledgements
I want to acknowledge the following resources -
* http://wiki.franklinheath.co.uk/index.php/Enigma/Paper_Enigma
* https://www.cs.cornell.edu/courses/cs3110/2019sp/a1/#step-6-rotors
* https://en.wikipedia.org/wiki/Enigma_rotor_details#Rotor_offset
* https://www.101computing.net/enigma/enigma-M3.html

## What's Next
As mentioned earlier, users cannot configure the rotors, the reflector, the ring settings or the plugboard. This will be coming soon!<br>
I want to continue working on this project to add these features and eventually create a front-end user interface for the program.
