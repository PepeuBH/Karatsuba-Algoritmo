# Algoritmo de Karatsuba

O algoritmo de Karatsuba é uma técnica eficiente para multiplicação de números inteiros grandes, introduzida por Anatolii Karatsuba em 1960. Ele melhora a complexidade da multiplicação em comparação ao método tradicional de multiplicação direta.

## Descrição do Projeto

Este projeto implementa o **Algoritmo de Karatsuba**, um método eficiente para multiplicação de números grandes. Diferente da multiplicação tradicional, que possui complexidade , o algoritmo de Karatsuba reduz a complexidade para aproximadamente  utilizando a técnica de divisão e conquista.

A implementação segue os seguintes passos:

1. **Caso Base**: Se os números são pequenos (menores que 10), multiplica-se diretamente.
2. **Divisão**: O número é dividido em duas partes: parte alta e parte baixa.
3. **Recursão**: Três multiplicações menores são realizadas.
4. **Combinação**: Os resultados das multiplicações recursivas são combinados para obter o produto final.

### Explicação do Código (Linha a Linha)

````
def karatsuba(x, y):


    if x < 10 or y < 10: # multiplicação normal caso os números sejam pequenos
        return x * y


    n = max(len(str(x)), len(str(y))) # n = lenght dos números
    m = n // 2  # divide os numeros ao meio 1234 -> 12 34



    # separa o número ordenando por unidades (unidade, dezena, centena...) de acordo com o tamanho da variável "m"
    high_x, low_x = divmod(x, 10 ** m)
    high_y, low_y = divmod(y, 10 ** m)

    # chama o alg recursivo 😭😭😭
    z0 = karatsuba(low_x, low_y)
    z1 = karatsuba((low_x + high_x), (low_y + high_y))
    z2 = karatsuba(high_x, high_y)

    # junta os resultados usando a fórmula do moço
    return (z2 * 10 ** (2 * m)) + ((z1 - z2 - z0) * 10 ** m) + z0


# exemplo de multiplicação
a = 1717
b = 5656
resultado = karatsuba(a, b)
print(f"{a} * {b} = {resultado}")
````

* Caso base, retorna a multiplicação direta se os números forem pequenos.
* Calcula o tamanho de `X` e `Y` e divide pela metade (`M`).
* Usa `divmod` para separar os números em parte alta e parte baixa.
* Calcula três multiplicações recursivas.
* Combina os resultados para obter o produto final.

---

## Como Executar o Projeto

### Requisitos:

* Python 3.x instalado.

### Execução:

1. Clone ou baixe o repositório.
2. Execute o código com:
   ```
   python main.py
   ```
3. O resultado da multiplicação será impresso no terminal.

---

## Relatório Técnico

### Análise da Complexidade Ciclomática

O fluxo de controle da função `karatsuba(x, y)` pode ser representado como um grafo onde:

* Cada **bloco de código** (como if, chamadas recursivas) representa um **nó**.
* Cada **transição entre blocos** representa uma **aresta**.

### Grafo de Fluxo:

1. Início → Verificação do caso base → Retorno direto OU
2. Cálculo de `N` e `M` → Divisão de `X` e `Y` → Chamadas recursivas → Combinação de resultados → Retorno final

**Cálculo da Complexidade Ciclomática (M)**:  Onde:

* `E = 8` (arestas) -> transição entre cada nó (atribuições nulas/vazias não são arestas)
* `N = 7` (nós) -> cada instrução é um nó
* `P = 1` (componente conexo único)

  Fórmula: **M** = **8** − **7** + **2**(**1**) = 3
* **3** caminhos possíveis

### Análise da Complexidade Assintótica


| Caso        | Complexidade                |
| ----------- | --------------------------- |
| Melhor Caso | O(n) -> (números pequenos) |
| Caso Médio | O(n^log2^3)                 |
| Pior Caso   | O(n^log2^3)                 |

**Complexidade Espacial**: O(n), devido à profundidade da recursão.

---

## Conclusão

O algoritmo de Karatsuba é uma abordagem eficiente para multiplicação de números grandes, reduzindo a complexidade em comparação à multiplicação tradicional. Ele utiliza recursão e divide os números em partes menores para acelerar os cálculos. Apesar de sua vantagem teórica, para números pequenos a multiplicação direta pode ser mais rápida devido à sobrecarga da recursão.
