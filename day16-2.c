#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define N 16
#define M 10000
#define TIMES 100000

int main(void) {
  // Load data into arrays
  FILE *typeFile;
  FILE *dataFile1;
  FILE *dataFile2;
  typeFile = fopen("day16_type.txt", "r");
  dataFile1 = fopen("day16_data1.txt", "r");
  dataFile2 = fopen("day16_data2.txt", "r");
  char *line = NULL;
  int read, len = 0;
  int type, value1, value2, i;
  int types[M], value1s[M], value2s[M];

  // Type
  printf("Loading types...\n");
  i = 0;
  while ((read = getline(&line, &len, typeFile)) != -1) {
    type = line[0] - '0';
    types[i] = type;
    i++;
  }
  // Value 1
  printf("Loading value 1s...\n");
  i = 0;
  while ((read = getline(&line, &len, dataFile1)) != -1) {
    value1 = atoi(line);
    value1s[i] = value1;
    i++;
  }
  // Value 2
  printf("Loading value 2s...\n");
  i = 0;
  while ((read = getline(&line, &len, dataFile2)) != -1) {
    value2 = atoi(line);
    value2s[i] = value2;
    i++;
  }
  fclose(typeFile);
  fclose(dataFile1);
  fclose(dataFile2);

  // Initialise game
  char programs[N] = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
                      'j', 'k', 'l', 'm', 'n', 'o', 'p'};
  char copy[N];
  char temp;
  char A, B;
  int posA, posB;

  // Do the dance a billion times
  for (int t=0; t<TIMES; t++) {
    printf("Iteration t = %d\n", t);
    // Loop over the instructions
    for (int j=0; j<M; j++){
      // Get the instruction type
      if (types[j] == 0) {
        // Dance
        for (int i=0; i<N-value1s[j]; i++) {
          copy[i+value1s[j]] = programs[i];
        }
        for (int i=0; i<value1s[j]; i++) {
          copy[i] = programs[N-value1s[j]+i];
        }
        // Copy back
        strncpy(programs, copy, N);
      }

      if (types[j] == 1) {
        //Dance
        temp = programs[value1s[j]];
        programs[value1s[j]] = programs[value2s[j]];
        programs[value2s[j]] = temp;
      }

      if (types[j] == 2) {
        // Get the instruction values
        A = value1s[j];
        B = value2s[j];
        // Find them
        posA = 0;
        for (int i=0; i<N; i++) {
          if (programs[i] == A) {
            posA = i;
            break;
          }
        }
        posB = 0;
        for (int i=0; i<N; i++) {
          if (programs[i] == B) {
            posB = i;
            break;
          }
        }
        // Dance
        temp = programs[posA];
        programs[posA] = programs[posB];
        programs[posB] = temp;
      }
    }
  }

  printf("Result is %s\n", programs);
  return 0;
}
