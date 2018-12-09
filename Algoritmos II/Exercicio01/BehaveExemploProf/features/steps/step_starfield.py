"""Testa starfield."""

from behave import given, then, when

from starfield import cria_estrela, move_estrela


@given('dois valores inteiros e positivos, 0 e 600')
def given_dois_valores_inteiros(context):
    """Cria tupla com dois numeros."""
    context.range_int = (0, 600)


@given('uma lista com os valores 1, 2 e 3')
def given_lista_com_valores(context):
    """Cria lista com os valores dados."""
    context.lista = [1, 2, 3]


@when('eu crio um objeto que representa uma estrela')
def when_crio_uma_estrela(context):
    """Executa criacao de uma estrela."""
    tupla = context.range_int
    lista = context.lista
    context.resultado = cria_estrela(tupla, lista)


@then('a coordenada X da estrela é 800')
def then_avalia_coordenada_X_estrela(context):
    """Testa se a coordenada X da estrela é 800."""
    esperado = 800
    observado = context.resultado[0]
    assert esperado == observado


@then('a coordenada Y da estrela esta entre 0 e 600')
def then_avalia_coordenada_Y_estrela(context):
    """Testa se a coordenada Y esta na faixa valida."""
    observado = context.resultado[1]
    assert (0 <= observado <= 600) is True


@then('a velocidade da estrela é 1, 2 ou 3')
def then_avalia_velocidade_estrela(context):
    """Testa se a velocidade tem um valor valido."""
    observado = context.resultado[2]
    assert observado in [1, 2, 3]


@given('um objeto representando uma estrela')
def given_objeto_representando_estrela(context):
    """Cria uma estrela."""
    context.estrela = cria_estrela((0, 600), [1, 2, 3])


@when('eu movo a estrela')
def when_move_estrela(context):
    """Move a estrela."""
    estrela = context.estrela
    context.resultado = move_estrela(estrela)


@then('a coordenada X varia de acordo com a velocidade da estrela')
def then_X_varia_com_velocidade(context):
    """Avalia movimentacao da estrela."""
    e_orig = context.estrela
    e_move = context.resultado
    spd = e_orig[2]
    x_esperado = e_orig[0] - spd
    assert e_move[0] == x_esperado


@then('a coordenada Y da estrela não varia')
def then_Y_nao_varia(context):
    """Testa se Y nao variou."""
    e_orig = context.estrela
    e_move = context.resultado
    assert e_orig[1] == e_move[1]


@then('a velocidade da estrela não varia')
def then_velocidade_nao_varia(context):
    """Testa se a velocidade nao variou."""
    e_orig = context.estrela
    e_move = context.resultado
    assert e_orig[2] == e_move[2]
