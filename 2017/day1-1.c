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

  // Check for repeated values and sum
  int sum = 0;
  for (int i=0; i<2041; i++) {
    if (numbers[i] == numbers[i+1]) {
      sum += numbers[i];
    }
  }
  // last digit with first digit
  if (numbers[2041] == numbers[0]) {
    sum += numbers[0];
  }

  printf("Solution = %d\n", sum);
  return 0;
}
