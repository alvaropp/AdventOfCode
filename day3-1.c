#include <stdio.h>
#include <stdlib.h>

int squareNumber(int input) {
  // Compute which square the input belongs to: square n has 8n numbers
  int Sn, n = 1;
  while (1) {
    Sn = 4*n*(n+1) + 1;
    if (input <= Sn) {
      break;
    }
    n++;
  }
  return n;
}

int manhattanDistance(int input, int n) {
  int squareSize, pos, groupSize, posGroup, start, mh;
  squareSize = 8*n;
  pos = input - 4*n*(n-1) - 2;
  groupSize = 2*n;
  posGroup = pos%groupSize;
  start = 2*n-1;
  // Compute solution distance
  if (posGroup < groupSize/2) {
    mh = start - posGroup;
  } else {
    mh = start - groupSize/2 + 1 + (posGroup - groupSize/2 + 1);
  }
  return mh;
}

int main(void) {
  int n, mh, input = 277678;
  n = squareNumber(input);
  mh = manhattanDistance(input, n);

  printf("mh=%d", mh);
  return 0;
}
