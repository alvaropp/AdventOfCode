#include <stdio.h>
#include <stdlib.h>

int main(void) {
  // Load data
  FILE *myFile;
  myFile = fopen("day2.txt", "r");

  // Max and min values from each line, cumulative sum
  int sum = 0;
  int min = 999999;
  int max = 0;

  // Read each value and update min, max appropriately
  char line[1024], *p, *e;
  int v;
  while (fgets(line, sizeof(line), myFile)) {
    p = line;
    for (p = line; ; p = e) {
      v = strtol(p, &e, 10);
      if (p == e)
        break;
      if (v > max) {
        max = v;
      }
      if (v < min) {
        min = v;
      }
    }
    sum += (max - min);
    min = 999999;
    max = 0;
  }
  
  printf("Solution = %d\n", sum);
  return 0;
}
