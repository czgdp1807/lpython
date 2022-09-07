from ltypes import i16, i32

@ccall
def f(lower: i32, upper: i32) -> i32:
    pass

def run():
    lower: i32; upper: i32
    lower = 0
    upper = 100
    print(f(lower, upper))

run()
