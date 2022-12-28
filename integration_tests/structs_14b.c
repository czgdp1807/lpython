#include "structs_14b.h"

int16_t sum_buffer_i16(int16_t data[], int32_t size) {
    int16_t sum_buffer = 0;
    for( int32_t i = 0; i < size; i++ ) {
        sum_buffer += data[i];
    }
    return sum_buffer;
}
