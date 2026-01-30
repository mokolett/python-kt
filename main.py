def get_sum(a: int, b: int) -> int:
    return a + b

def count_capital_letters(text: str) -> int:
    count = 0
    for char in text:
        if ('A' <= char <= 'Z'):
            count += 1
    return count

print(count_capital_letters('avffDRhh'))

def decode_string(text: str):
    result = ''
    for char in text:
        count = text.lower().count(char.lower())
        if count == 1:
            result += '('
        else:
            result += ')'
    return result

print(decode_string('ffvgdvcbj'))

def get_odd_count(text: str) -> int:
    count = 0
    i = 0
    while i < len(text):
        num = int(text[i])
        if num % 2 == 0 and num != 0:
            count += 1
        i += 1
    return count
print(get_odd_count('7465746580'))

def check_access(has_keycard: bool, has_fingerprint: bool, is_alarm: bool, is_daylight: bool) -> bool:
    if is_alarm == True:
        return False
    
    elif has_fingerprint == True:
        return True
    
    elif has_keycard == True and is_daylight == True:
        return True
    
    else:
        return False
print("Тест 1 (Ключ, день, нет тревоги):", check_access(True, False, False, True))
print("Тест 3 (Палец, ночь, нет тревоги):", check_access(False, True, False, False))   
print("Тест 6 (Ничего нет):", check_access(False, False, False, True))       