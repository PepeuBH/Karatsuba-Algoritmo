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