#include <stdio.h>
#define n 4
#define T 1000

int compareState(int a[n], int b[n]) {
  int equal = 1;
  for (int i=0; i<n; i++) {
    if (a[i] != b[i]) {
      equal = 0;
      break;
    }
  }
  return equal;
}

int saveState(int *state, int **states, int t) {
  for (int i=0; i<n; i++) {
    states[t][i] = state[i];
  }
}

void updateState(int *state) {
  // Find max
  int max = 0;
  int pos = 0;
  for (int i=0; i<n; i++) {
    if (state[i] > max) {
      max = state[i];
      pos = i;
    }
  } // This finds the maximum, and its position
  // Delete all blocks from maximum
  int blocks = state[pos];
  state[pos] = 0;
  printf("Max = %d, Pos = %d, Blocks = %d\n", max, pos, blocks);
  printf("\n");

  // Reallocate one by one
  for (int b=0; b<blocks; b++) {
    state[(pos+b+1) % n] ++;
  }

  for (int i=0; i<n; i++) {
    printf("Value = %d\n", state[i]);
  }
}

int main(void) {
  // Load number
  int state[n];
  // from file
  FILE *myFile;
  myFile = fopen("day6.txt", "r");
  for (int i=0; i<1024; i++)
  {
    fscanf(myFile, "%d", &state[i]);
  }

  // Store all historical states
  int states[T][n];
  // save the current one
  printf("State ");
  int t = 0;
  saveState(state, states, t);
  for (t=1; t<T; t++) {
    // Update state
    updateState(state);
    // Check for coincidence with historical states
    for (int i=0; i<t; i++) {
      if (compareState(state, states[i])) {
        t = T; break;
      }
    }
  }

  return 0;
}
