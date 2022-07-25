# 문제
# 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.
#
# 입력
# 첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 주어지는 단어의 길이는 1,000,000을 넘지 않는다.
#
# 출력
# 첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.



def find_most_frequency_alpha():
    frequency_list = [0 for _ in range(26)]

    word = input("input word : ")
    # word = "Mississipi"

    for char in word:
        num = ord(char)
        if 65 <= num < 65 + 26:
            num -= 65
        else:
            num -= 97
        frequency_list[num] += 1

    most_frequency = max(frequency_list)
    most_alpha = []
    for i, frequency in enumerate(frequency_list):
        if frequency == most_frequency:
            most_alpha.append(chr(i+65))

    if len(most_alpha) == 1:
        return most_alpha[0]
    else:
        return "?"


print(find_most_frequency_alpha())