calls = 0


def count_calls():
    global calls
    calls += 1
    return calls


def string_info(string):
    a = (len(string), string.upper(), string.lower())
    count_calls()
    return a


def is_contains(string, list_to_search):
    count_calls()  # return string.lower() in [a.lower() for a in list_to_search]
    for i in range(len(list_to_search)):
        if string.lower() in list_to_search[i].lower() or list_to_search[i].lower() in string.lower():
            return True
        return False


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BeNaN', 'urBAN']))  # Urban - urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)
