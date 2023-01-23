#include "nbody_util.h"
#include <time.h>
#include <stdlib.h>

void init_positions_weights(float* positions, float* weights, int32_t n) {
    srand(time(NULL));
    for( int32_t i = 0; i < n; i++ ) {
        positions[i] = ((float) rand() / (float)RAND_MAX);
        positions[i + 1] = ((float) rand() / (float)RAND_MAX);
        weights[i] = ((float) rand() / (float)RAND_MAX);
    }
}
