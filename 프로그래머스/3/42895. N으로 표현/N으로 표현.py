def solution(N, number):
    memory = [[] for i in range(8)]
    def math_mixer(first_array: list, second_array: list):
        result = list()
        for a in first_array:
            for b in second_array:
                result.append(a*b)
                result.append(a+b)
                result.append(a-b)
                result.append(b-a)
                if a != 0:
                    result.append(b/a)
                if b != 0:
                    result.append(a/b)
        return result
    
    for i in range(8):
        memory[i].append(int(str(N)*(i+1)))
        if i == 1:
            memory[i].extend(math_mixer(memory[0], memory[0]))
        if i == 2:
            memory[i].extend(math_mixer(memory[0], memory[1]))
        if i == 3:
            memory[i].extend(math_mixer(memory[1], memory[1]))
            memory[i].extend(math_mixer(memory[2], memory[0]))
        if i == 4:
            memory[i].extend(math_mixer(memory[0], memory[3]))
            memory[i].extend(math_mixer(memory[1], memory[2]))
        if i == 5:
            memory[i].extend(math_mixer(memory[0], memory[4]))
            memory[i].extend(math_mixer(memory[1], memory[3]))
            memory[i].extend(math_mixer(memory[2], memory[2]))
        if i == 6:
            memory[i].extend(math_mixer(memory[0], memory[5]))
            memory[i].extend(math_mixer(memory[1], memory[4]))
            memory[i].extend(math_mixer(memory[2], memory[3]))
        if i == 7:
            memory[i].extend(math_mixer(memory[0], memory[6]))
            memory[i].extend(math_mixer(memory[1], memory[5]))
            memory[i].extend(math_mixer(memory[2], memory[4]))
            memory[i].extend(math_mixer(memory[3], memory[3]))
        
        if number in memory[i]:
            return i+1
        
    return -1
            