def calcular_fibonacci(n):
    fib_sequence = [0, 1]  # Inicia a sequência com 0 e 1
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])  # Adiciona o próximo número
    return fib_sequence

def pertence_fibonacci(num):
    fib_sequence = calcular_fibonacci(20)  # Calcula os primeiros 20 números de Fibonacci
    return num in fib_sequence  # Verifica se o número está na sequência

# Exemplo de uso
numero = int(input("Informe um número: "))
if pertence_fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")