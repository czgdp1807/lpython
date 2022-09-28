# from goto import with_goto #TODO: need to be supported for cpython integration_tests

@with_goto
def func() -> i16:
    i:i16
    for i in range(10):
        goto .end
        i = 10

    label .end
    assert i == 0
    return i

    