#include <math.h>
#include <stdint.h>
#include <stdlib.h>
int rightmost_unset_bit(int i) {
  return log2(~i & -~i) + 1; // rightmost unset bit
}
void sobol(double *points, int N) {
  int L = (unsigned)ceil(log2((double)N));
  uint64_t V[64];
  for (int j = 0; j < 2; j++) {
    for (int i = 0; i < L; i++) {
      uint64_t m = 0;
      for (int k = 0; k < 64; k += 30) {
        m = m * (RAND_MAX + 1Lu) + rand(); // 64 bit random integer
      }
      V[i] = m << (uint64_t) (63-i);
    }
    uint64_t X = 0;
    for (int i = 0; i < N; i++) {
      X = X ^ V[rightmost_unset_bit(i)];
      points[2*i+j] = X / 0x1.0p64; /* floating-point hexadecimal literal 2**64 */
    }
  }
}
