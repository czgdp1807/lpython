from ltypes import with_goto, goto, label, i32

@with_goto
def f() -> i32:
    i:i32
    for i in range(10):
        if i == 5:
            goto .end

    label .end
    assert i == 5
    return i

def test_goto():
    print(f())

test_goto()
