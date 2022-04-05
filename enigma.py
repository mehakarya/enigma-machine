# constants
ROTOR_I = [4, 10, 12, 5, 11, 6, 3, 16, 21, 25, 13, 19, 14, 22, 24, 7, 23, 20, 18, 15, 0, 8, 1, 17, 2, 9] 
TURNOVER_I = 16

ROTOR_II = [0, 9, 3, 10, 18, 8, 17, 20, 23, 1, 11, 7, 22, 19, 12, 2, 16, 6, 25, 13, 15, 24, 5, 21, 14, 4]
TURNOVER_II = 4

ROTOR_III = [1, 3, 5, 7, 9, 11, 2, 15, 17, 19, 23, 21, 25, 13, 24, 4, 8, 22, 6, 0, 10, 12, 20, 18, 16, 14]
TURNOVER_III = 21

REFLECTOR_B = [24, 17, 20, 7, 16, 18, 11, 3, 15, 23, 13, 6, 14, 10, 12, 8, 4, 1, 5, 25, 2, 22, 21, 9, 0, 19]
RING = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

# encryption function
def encrypt(message, startPosition):

    offset1 = getPosition(startPosition[0])
    offset2 = getPosition(startPosition[1])
    offset3 = getPosition(startPosition[2])

    output = ""
    for l in message.upper():
        if (l >= "A" and l <= "Z"):

            # stepping
            if (offset2 == TURNOVER_II):
                offset1 = (offset1 + 1) % 26
                offset2 = (offset2 + 1) % 26
                offset3 = (offset3 + 1) % 26
            elif (offset3 == TURNOVER_III):
                offset2 = (offset2 + 1) % 26
                offset3 = (offset3 + 1) % 26
            else:
                offset3 = (offset3 + 1) % 26

            # encryption
            temp = rotorRtoL(ROTOR_III, (getPosition(l) + offset3) % 26)
            temp = rotorRtoL(ROTOR_II, (temp + offset2 - offset3) % 26)
            temp = rotorRtoL(ROTOR_I, (temp + offset1 - offset2) % 26) 
            temp = (reflect(REFLECTOR_B, (temp - offset1) % 26) + offset1) % 26  
            temp = (rotorLtoR(ROTOR_I, temp) - offset1 + offset2) % 26
            temp = (rotorLtoR(ROTOR_II, temp) - offset2 + offset3) % 26
            temp = (rotorLtoR(ROTOR_III, temp) - offset3) % 26
            output = output + getLetter(RING, temp)

        elif (l == " "):
            output = output + l
    
    return output

# helper functions
def getPosition(char):
    return ord(char) - 65

def getLetter(ring, pos):
    return ring[pos]

def rotorRtoL(rotor, position):
    return rotor[position]

def rotorLtoR(rotor, position):
    for each in rotor:
        if (rotor[each] == position):
            return each

def reflect(reflector, position):
    return reflector[position]

def isAlpha(string):
    for c in string.upper():
        if (c < "A" or c > "Z"):
            return False
    return True

# main function
if __name__ == "__main__":

    print("Starting Position: ")
    startPosition = input()

    while (len(startPosition) != 3 or isAlpha(startPosition) == False):
        print("Try again. Make sure you're entering three letters with no spaces.")
        startPosition = input()

    print("Nice! What's the secret message?")
    message = input()

    print(f"Output:\n{encrypt(message, startPosition.upper())}", end="")