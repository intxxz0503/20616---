inputs = [0.8, 0.5]
weights = [2.0, 3.0]
bias = -1.0

def simple_neuron(inputs, weights, bias):
    total = 0
    for i in range(len(inputs)):
        total += inputs[i] * weights[i]
    return total + bias

result = simple_neuron(inputs, weights, bias)
print("뉴런 계산 결과:", result)

if result > 0:
    print("판정: 합격! (신호를 전달합니다)")
else:
    print("판정: 불합격! (신호를 차단합니다)")
