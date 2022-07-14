from ltypes import f64
from numpy import empty

def loop_vec():
    a: f64[9216] = empty(9216)
    b: f64[9216] = empty(9216)
    c: f64[9216] = empty(9216)
    i: i32

    for i in range(9216):
        c[i] = a[i] + b[i]

    for i in range(9216):
        assert c[i] == 0.0
