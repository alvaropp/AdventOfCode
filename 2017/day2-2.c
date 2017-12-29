#include <stdio.h>
#include <stdlib.h>

// Compare function for sorting a numerical array in descending order
int compare( const void* a, const void* b)
{
  int int_a = * ( (int*) a );
  int int_b = * ( (int*) b );

  if ( int_a == int_b ) return 0;
  else if ( int_a < int_b ) return 1;
  else return -1;
}

// Main function
int main(void) {
  // Load data
  FILE *myFile;
  myFile = fopen("day2.txt", "r");

  // Cumulative sum
  int sum = 0;

  // Array of numbers in the line
  int lineNumbers[16];

  // Read each value and store
  char line[1024], *p, *e;
  int v, count=0;
  while (fgets(line, sizeof(line), myFile)) {
    count = 0;
    p = line;
    for (p = line; ; p = e) {
      v = strtol(p, &e, 10);
      if (p == e) {
        break;
      }
      lineNumbers[count] = v;
      count++;
    }
    // Now lineNumbers contains all numbers of the line, sort
    qsort(lineNumbers, 16, sizeof(int), compare);

    // Compare each value with only the next ones (as they are sorted)
    for (int i=0; i<16; i++) {
      for (int j=i+1; j<16; j++) {
        if (lineNumbers[i] % lineNumbers[j] == 0) {
          sum += lineNumbers[i]/lineNumbers[j];
          i = j = 16; break;
        }
      }
    }
  }
  
  printf("Solution = %d\n", sum);
  return 0;
}
