from pilha import then

pushBack(valor)
Cenário: Inserindo um valor no início Deque.
  Dado que eu tenho um deque
  Quando não há início da estrutura, o valor 8
  Entao a estrutura nao esta vazia
    E o elemento não final da estrutura tem o valor 8


    @given('que eu tenho uma pilha')
    def _given_uma_pilha(context):
        context.pilha=pilha(10)

    @when('qunado verifico a estrutura da pilha')
    def _when_verifico_pilha(context,valor):
        if valor is not None:
            print('Estrutura com valor')
        else
            print('Estrutura com valor')


    @then('o valor inicial e 8')
    def _then_valor_pilha(context,valor):
        
