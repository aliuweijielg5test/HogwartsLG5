#装饰器

def b(fun):
    def run(*args, **kwargs):
        print("before b")
        fun(*args, **kwargs)
        print("after b")
    return run

@b
def test_a():
    print("a")


