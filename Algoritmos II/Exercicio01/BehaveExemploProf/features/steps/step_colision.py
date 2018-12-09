"""Testes de colisao de objetos."""

from behave import given, when, then

from retangulo import Retangulo


@given('um ponto com as coordenadas ({x}, {y})')
def given_um_ponto(context, x, y):
    """Define ponto dados as suas coordenadas."""
    context.ponto = (int(x), int(y))


@given('um retangulo nas coordenadas ({x:d}, {y:d}) e dimensao ({w:d}, {h:d})')
def given_um_retangulo(context, x, y, w, h):
    """Cria objeto retangulo com os parametros especificados."""
    context.retangulo = Retangulo(x, y, w, h)


@when('quero saber se o ponto esta dentro do retangulo')
def when_ponto_colide_retangulo(context):
    """Executa deteccao de colisao."""
    retangulo = context.retangulo
    ponto = context.ponto
    context.colisao = retangulo.colide(ponto)


@then('o resultado e "{esperado}".')
def then_colisao_ocorreu(context, esperado):
    """Testa se colisao realmente ocorreu."""
    expected = True if esperado == "verdadeiro" else False
    assert context.colisao == expected
