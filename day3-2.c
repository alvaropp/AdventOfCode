#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define N 101

int checkNeighbours(int coords[2], int array[N][N], int maskX[2], int maskY[2]) {
  // Sum and return all the values of the neighbours
  int value = 0;
  for (int i=0; i<8; i++) {
    value += array[coords[0]+maskX[i]][coords[1]+maskY[i]];
  }
  return value;
}

int main(void) {
  // Initialise grid with zeros and the initial one in the middle
  int array[N][N];
  memset(array, 0, sizeof(array));
  array[50][50] = 1;

  // Initialise the neighbouring coordinates mask
  int maskX[] = {0,-1,-1,-1,0,1,1,1};
  int maskY[] = {1,1,0,-1,-1,-1,0,1};

  // Puzzle input
  int input = 277678;

  // Initialise coordinates and temp value
  int coords[] = {50, 50};
  int value = 0;

  // Loop around the outwards spiral
  int counter = 0;
  while (1) {
    counter++;

    // One step to the right
    for (int i=0; i<1; i++) {
      coords[1]++;
      value = checkNeighbours(coords, array, maskX, maskY);
      array[coords[0]][coords[1]] = value;
      printf("Coords = [%d ,%d], value = %d, counter = %d\n", coords[0], coords[1], value, counter);
      if (value >= input) {
        break;
      }
    }
    if (value >= input) {
      break;
    }

    // Steps up
    for (int i=0; i<2*counter-1; i++) {
      coords[0]--;
      value = checkNeighbours(coords, array, maskX, maskY);
      array[coords[0]][coords[1]] = value;
      printf("Coords = [%d, %d], value = %d, counter = %d\n", coords[0], coords[1], value, counter);
      if (value >= input) {
        break;
      }
    }
    if (value >= input) {
      break;
    }

    // Steps to the left
    for (int i=0; i<2*counter; i++) {
      coords[1]--;
      value = checkNeighbours(coords, array, maskX, maskY);
      array[coords[0]][coords[1]] = value;
      printf("Coords = [%d, %d], value = %d, counter = %d\n", coords[0], coords[1], value, counter);
      if (value >= input) {
        break;
      }
    }
    if (value >= input) {
      break;
    }

    // Steps down
    for (int i=0; i<2*counter; i++) {
      coords[0]++;
      value = checkNeighbours(coords, array, maskX, maskY);
      array[coords[0]][coords[1]] = value;
      printf("Coords = [%d, %d], value = %d, counter = %d\n", coords[0], coords[1], value, counter);
      if (value >= input) {
        break;
      }
    }
    if (value >= input) {
      break;
    }

    // Steps to the right
    for (int i=0; i<2*counter; i++) {
      coords[1]++;
      value = checkNeighbours(coords, array, maskX, maskY);
      array[coords[0]][coords[1]] = value;
      printf("Coords = [%d, %d], value = %d, counter = %d\n", coords[0], coords[1], value, counter);
      if (value >= input) {
        break;
      }
    }
  }

  printf("value = %d\n", value);
  return 0;
}
