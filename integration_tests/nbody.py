from ltypes import f32, i32, f64, ccall, TypeVar
from numpy import zeros_like, empty, float32
from math import sqrt

n: i32
n = TypeVar("n")

def lpython_nbody(positions: f32[:, :], weights: f32[:], n: i32) -> f32[n, 2]:
    # TODO: replace the following loop with np.zeros_like
    # accelerations = zeros_like(positions)
    accelerations: f32[n, 2] = empty((n, 2), dtype=float32)
    # TODO: support getting n from .shape attribue of array.
    # For now it is passed as an argument
    # n = weights.shape[0]
    ax: f32; ay: f32; rx: f32; ry: f32;
    sqr_dist: f32; sixth_dist: f32; inv_dist_cube: f32
    s: f32
    i: i32; j: i32
    eps_2: f32 = f32(1e-6)
    for i in range(n):
        ax = f32(0.0)
        ay = f32(0.0)
        for j in range(n):
            rx = positions[j, 0] - positions[i, 0]
            ry = positions[j, 1] - positions[i, 1]
            sqr_dist = rx * rx + ry * ry + eps_2
            sixth_dist = sqr_dist * sqr_dist * sqr_dist
            # QUESTION: Should we define sqrt for f32 types?
            inv_dist_cube = f32(1.0) / f32(sqrt(f64(sixth_dist)))
            s = weights[j] * inv_dist_cube
            ax += s * rx
            ay += s * ry
        accelerations[i, 0] = ax
        accelerations[i, 1] = ay
    return accelerations

@ccall
def init_positions_weights(positions: f32[:, :], weights: f32[:], n: i32):
    pass

def run_lpython_nbody(n: i32):
    i: i32
    positions: f32[n, 2] = empty((n, 2), dtype=float32)
    weights: f32[n] = empty(n, dtype=float32)
    accelerations: f32[n] = empty((n, 2), dtype=float32)
    # replace the following function call with
    # np.random.RandomState(0).uniform for
    # both positions and weights vectors
    init_positions_weights(positions, weights, n)
    accelerations = lpython_nbody(positions, weights, n)
    for i in range(n):
        print(accelerations[i, 0], accelerations[i, 1])

run_lpython_nbody(10)
