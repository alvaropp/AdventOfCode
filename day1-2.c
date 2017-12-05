#include <stdio.h>

int main(void) {
  // Load number
  int numbers[2042];
  // from file
  FILE *myFile;
  myFile = fopen("day1.txt", "r");
  for (int i=0; i<2042; i++)
  {
    fscanf(myFile, "%1d", &numbers[i]);
  }

  // Find half-way around distance
  int half = 2042/2;

  // Check for repeated values and sum
  int sum = 0;
  for (int i=0; i<2042; i++) {
    if (numbers[i] == numbers[(i+half) % 2042]) {
      sum += numbers[i];
    }
  }

  printf("Solution = %d\n", sum);
  return 0;
}
