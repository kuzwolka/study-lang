def solution(s):
    stack = []
    answer = ""
    reference = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }
    
    for x in s:
        if x.isdigit():
            answer += x
        else:
            stack.append(x)
            refer = reference.get(''.join(stack))
            if refer != None:
                answer += refer
                stack = []
    return int(answer)