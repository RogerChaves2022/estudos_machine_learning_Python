import math

input = 0

output_desire = 0

input_weight = 0.1

learning_rate = 0.01

def activation(sum):
    if sum >= 0:
        return 1
    else:
        return 0

print("entrada:", input, "desejado:", output_desire)

erro = math.inf

i = 0

bias = 1

bias_weight = 0.5

while not erro == 0:
    i += 1
    
    print("Iteração:", i)
    
    print("Peso:", input_weight) 
    print("Peso:", bias_weight)
    
    sum = (input * input_weight) + (bias * bias_weight)

    output = activation(sum)

    print("saída:", output)

    erro = output_desire - output

    print("erro:", erro)

    if not erro == 0:
        input_weight = input_weight + (learning_rate * input * erro)
        bias_weight = bias_weight + (learning_rate * bias * erro)
    
print("Parabéns! A rede aprendeu.")