#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <cstring>
using namespace std;

// constants
const int MAX_SIZE = 99999;
const int ROTOR_SIZE = 26;

const int ROTOR_I[ROTOR_SIZE] = {4, 10, 12, 5, 11, 6, 3, 16, 21, 25, 13, 19, 14, 22, 24, 7, 23, 20, 18, 15, 0, 8, 1, 17, 2, 9};
const int TURNOVER_I = 16;

const int ROTOR_II[ROTOR_SIZE] = {0, 9, 3, 10, 18, 8, 17, 20, 23, 1, 11, 7, 22, 19, 12, 2, 16, 6, 25, 13, 15, 24, 5, 21, 14, 4};
const int TURNOVER_II = 4;

const int ROTOR_III[ROTOR_SIZE] = {1, 3, 5, 7, 9, 11, 2, 15, 17, 19, 23, 21, 25, 13, 24, 4, 8, 22, 6, 0, 10, 12, 20, 18, 16, 14};
const int TURNOVER_III = 21;

const int REFLECTOR_B[ROTOR_SIZE] = {24, 17, 20, 7, 16, 18, 11, 3, 15, 23, 13, 6, 14, 10, 12, 8, 4, 1, 5, 25, 2, 22, 21, 9, 0, 19};
const char RING[ROTOR_SIZE] = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'};

// helper functions
int getPosition(char c) {
    return toupper(c) - 65;
}

char getLetter(const char *ring, int position) {
    return ring[position];
}

int rotorRtoL(const int *rotor, int position) {
    return rotor[position];
}

int rotorLtoR(const int *rotor, int position) {
    for (int i = 0; i < ROTOR_SIZE; i++) {
        if (rotor[i] == position) {
            return i;
        }
    }
}

int reflect(const int *reflector, int position) {
    return reflector[position];
}

bool isAlpha(char *str) {
    for (int i = 0; i < strlen(str); i++) {
        if (toupper(str[i]) < 65 || toupper(str[i]) > 90) {
            return false;
        }
    }
    return true;
}

// encryption function
char *encrypt(char *msg, char *startPosition) {

    int offset1 = getPosition(startPosition[0]);
    int offset2 = getPosition(startPosition[1]);
    int offset3 = getPosition(startPosition[2]);

    for (int i = 0; i < strlen(msg); i++) {

        if (toupper(msg[i]) >= 65 && toupper(msg[i] <= 90)) {
            
            // stepping
            if (offset2 == TURNOVER_II) {
                offset1 = (offset1 + 1) % 26;
                offset2 = (offset2 + 1) % 26;
                offset3 = (offset3 + 1) % 26;
            } else if (offset3 == TURNOVER_III) {
                offset2 = (offset2 + 1) % 26;
                offset3 = (offset3 + 1) % 26;
            } else {
                offset3 = (offset3 + 1) % 26;
            }

            // encryption
            int temp = rotorRtoL(ROTOR_III, (getPosition(toupper(msg[i])) + offset3) % 26);
            temp = rotorRtoL(ROTOR_II, (temp + offset2 - offset3) % 26);
            temp = rotorRtoL(ROTOR_I, (temp + offset1 - offset2) % 26);
            temp = (reflect(REFLECTOR_B, (temp - offset1) % 26) + offset1) % 26;
            temp = (rotorLtoR(ROTOR_I, temp) - offset1 + offset2) % 26;
            temp = (rotorLtoR(ROTOR_II, temp) - offset2 + offset3) % 26;
            temp = (rotorLtoR(ROTOR_III, temp) - offset3) % 26;

            // wrap around alphabet
            if (temp < 0) {
                temp += 26;
            }

            printf("%c", getLetter(RING, temp));
        }
    }

    return msg;
}

// main function
int main() {

    char startPosition[10];
    printf("Starting Position:\n");
    scanf("%s", startPosition);

    while (strlen(startPosition) != 3 || !isAlpha(startPosition)) {
        printf("Try again. Make sure you're entering three letters with no spaces.\n");
        scanf("%s", startPosition);
    }

    char message[MAX_SIZE];
    printf("Nice! What's the secret message?\n");
    scanf("%s", message);

    // call encryption
    printf("Output:\n");
    encrypt(message, startPosition);

    return 0;
}