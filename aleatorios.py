"""
    Cuarta tarea de APA - generación de números aleatorios

    Nombre y apellidos: Alex Segura Medina
"""

class Aleat:
    def __init__(self, *, m=2**48, a=25214903917, c=11, x0=1212121):
        self.m = m
        self.a = a
        self.c = c
        self.x = x0  # semilla inicial
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
