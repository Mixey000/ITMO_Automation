a: int = 5
b: str = 'строка'
c: list = [1, 2]

def indent(s: str, width: int) -> str:
    return '' * (max(0, width - len (s))) + s

print(indent('123', 123))

def uno(s: str = '') -> int:
    return len(s)


def dos(a: list, b: list) -> int:
    return max(len(a), len(b))


def tres(l=[1, 2]):
    l.append(3)
    return l


def quatro(l) ->int:
    x=0
    for elem in l:
        result = result + elem
        return result