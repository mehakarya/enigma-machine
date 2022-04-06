# constants
ROTOR_I = [4, 10, 12, 5, 11, 6, 3, 16, 21, 25, 13, 19, 14, 22, 24, 7, 23, 20, 18, 15, 0, 8, 1, 17, 2, 9] 
TURNOVER_I = 16

ROTOR_II = [0, 9, 3, 10, 18, 8, 17, 20, 23, 1, 11, 7, 22, 19, 12, 2, 16, 6, 25, 13, 15, 24, 5, 21, 14, 4]
TURNOVER_II = 4

ROTOR_III = [1, 3, 5, 7, 9, 11, 2, 15, 17, 19, 23, 21, 25, 13, 24, 4, 8, 22, 6, 0, 10, 12, 20, 18, 16, 14]
TURNOVER_III = 21

REFLECTOR_B = [24, 17, 20, 7, 16, 18, 11, 3, 15, 23, 13, 6, 14, 10, 12, 8, 4, 1, 5, 25, 2, 22, 21, 9, 0, 19]
REFLECTOR_C = [5, 21, 15, 9, 8, 0, 14, 24, 4, 3, 17, 25, 23, 22, 6, 2, 19, 10, 20, 16, 18, 1, 13, 12, 7, 11]

RING = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

# encryption function
def encrypt(order, reflector, start, message):

    rotor1 = returnRotor(order[0])
    rotor2 = returnRotor(order[1])
    rotor3 = returnRotor(order[2])

    turnover2 = returnTurnover(order[1])
    turnover3 = returnTurnover(order[2])

    reflector = returnReflector(reflector)

    offset1 = getPosition(start[0])
    offset2 = getPosition(start[1])
    offset3 = getPosition(start[2])

    output = ""
    for l in message.upper():
        if (l >= "A" and l <= "Z"):

            # stepping
            if (offset2 == turnover2):
                offset1 = (offset1 + 1) % 26
                offset2 = (offset2 + 1) % 26
                offset3 = (offset3 + 1) % 26
            elif (offset3 == turnover3):
                offset2 = (offset2 + 1) % 26
                offset3 = (offset3 + 1) % 26
            else:
                offset3 = (offset3 + 1) % 26

            # encryption
            temp = rotorRtoL(rotor3, (getPosition(l) + offset3) % 26)
            temp = rotorRtoL(rotor2, (temp + offset2 - offset3) % 26)
            temp = rotorRtoL(rotor1, (temp + offset1 - offset2) % 26) 
            temp = (reflect(reflector, (temp - offset1) % 26) + offset1) % 26
            temp = (rotorLtoR(rotor1, temp) - offset1 + offset2) % 26
            temp = (rotorLtoR(rotor2, temp) - offset2 + offset3) % 26
            temp = (rotorLtoR(rotor3, temp) - offset3) % 26
            output = output + getLetter(RING, temp)
    
    return output

# helper functions
def getPosition(char):
    return ord(char) - 65

def getLetter(ring, pos):
    return ring[pos]

def returnRotor(rotor):
    if (rotor == "I"):
        return ROTOR_I
    elif (rotor == "II"):
        return ROTOR_II
    elif (rotor == "III"):
        return ROTOR_III

def returnTurnover(turnover):
    if (turnover == "I"):
        return TURNOVER_I
    elif (turnover == "II"):
        return TURNOVER_II
    elif (turnover == "III"):
        return TURNOVER_III

def returnReflector(reflector):
    if (reflector == "B"):
        return REFLECTOR_B
    elif (reflector == "C"):
        return REFLECTOR_C

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

    print("Rotor Order: ")
    order = input().split(" ")

    print("Reflector B or C: ")
    reflector = input()

    print("Starting Position: ")
    start = input()
    while (len(start) != 3 or isAlpha(start) == False):
        print("Try again. Make sure you're entering three letters with no spaces.")
        start = input()

    print("Nice! What's the secret message?")
    message = input()

    print(f"Output:\n{encrypt(order, reflector, start.upper(), message)}", end="")