"""
    Cuarta tarea de APA - generación de números aleatorios 
    Nombre y apellidos: Alex Segura Medina

    
TESTS UNITARIOS:

Comprobación de funcionamiento de Aleat
>>> rand = Aleat(m=32, a=9, c=13, x0=11)
>>> for _ in range(4):
...     print(next(rand))
...
16
29
18
15

Comprobación de reinicio de Aleat
>>> rand(29)
>>> for _ in range(4):
...     print(next(rand))
...
18
15
20
1

Comprobación de funcionamiento de aleat()
>>> rand = aleat(m=64, a=5, c=46, x0=36)
>>> for _ in range(4):
...     print(next(rand))
...
34
24
38
44

Comprobación de reinicio de aleat()
>>> rand.send(24)
38
>>> for _ in range(4):
...     print(next(rand))
...
44
10
32
14
"""

# CLASE Aleat
class Aleat:
    def __init__(self, *, m=2**48, a=25214903917, c=11, x0=1212121):
        self.m = m
        self.a = a
        self.c = c
        self.x = x0 
        self.initial_seed = x0  # para poder reiniciar con __call__

    def __iter__(self):
        return self

    def __next__(self):
        self.x = (self.a * self.x + self.c) % self.m
        return self.x

    def __call__(self, x0):
        """Permite reiniciar la secuencia con una nueva semilla."""
        self.x = x0
        self.initial_seed = x0


# FUNCION aleat()
def aleat(*, m=2**48, a=25214903917, c=11, x0=1212121):
    x = x0
    while True:
        x = (a * x + c) % m
        new_seed = (yield x)
        if new_seed is not None:
            x = new_seed


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
