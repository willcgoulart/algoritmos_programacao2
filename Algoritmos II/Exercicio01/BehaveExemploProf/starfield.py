"""Implementa uma simulacao de campo de estrelas em movimento."""

from random import randint, choice


def cria_estrela(limites_verticais, velocidades):
    """Cria uma estrela com os parametros fornecidos."""
    x = 800
    y = randint(*limites_verticais)
    speed = choice(velocidades)
    return (x, y, speed)


def move_estrela(estrela):
    """Move uma estrela."""
    x, y, speed = estrela
    return (x - speed, y, speed)
