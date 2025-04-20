"""
Cuarta tarea de APA - generación de números aleatorios 
Nombre y apellidos: Alex Segura Medina

Este fichero implementa un generador de números pseudoaleatorios usando
el algoritmo de Generación Lineal Congruente (LGC), tanto en forma de clase como de función generadora.

Incluye las pruebas unitarias de ambos métodos usando la biblioteca doctest.ç

"""

# CLASE Aleat
class Aleat:
    '''
    Descripción: Generador de números pseudoaleatorios usando el método LGC (Linear Congruential Generator).

    Atributos:
    - m: Módulo (entero positivo).
    - a: Multiplicador (entero, 0 < a < m).
    - c: Incremento (entero, 0 ≤ c < m).
    - x: Semilla actual.
    - initial_seed: Guarda la semilla inicial para posibles reinicios.

    Métodos:
    - __next__(): Genera el siguiente número pseudoaleatorio.
    - __iter__(): Retorna el propio objeto.
    - __call__(x0): Reinicia la secuencia con una nueva semilla.

    Pruebas unitarias:
    >>> rand = Aleat(m=32, a=9, c=13, x0=11)
    >>> for _ in range(4):
    ...     print(next(rand))
    ...
    16
    29
    18
    15

    >>> rand(29)
    >>> for _ in range(4):
    ...     print(next(rand))
    ...
    18
    15
    20
    1
    '''

    def __init__(self, *, m=2**48, a=25214903917, c=11, x0=1212121):
        self.m = m
        self.a = a
        self.c = c

        self.x = x0 

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
    '''
    Descripción: Generador de números pseudoaleatorios con el método LGC.

    Argumentos:
    - m: Módulo (entero positivo).
    - a: Multiplicador.
    - c: Incremento.
    - x0: Semilla inicial.

    Devuelve:
    Un generador infinito que produce números pseudoaleatorios.

    Pruebas unitarias:
    >>> rand = aleat(m=64, a=5, c=46, x0=36)
    >>> for _ in range(4):
    ...     print(next(rand))
    ...
    34
    24
    38
    44

    >>> rand.send(24)
    38
    >>> for _ in range(4):
    ...     print(next(rand))
    ...
    44
    10
    32
    14
    '''

    x = x0
    while True:
        x = (a * x + c) % m
        new_seed = (yield x)
        if new_seed is not None:
            x = new_seed


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)


