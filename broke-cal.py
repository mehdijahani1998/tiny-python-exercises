from numpy import number


def find_max_ending(string_a, string_b):

    n = min(len(string_a), len(string_b))

    if string_b == '':
        return ['', string_a, 0]
    elif string_a == '':
        return ['', string_a, 0]

    common_substring = ""

    for i in range(n):
        end_a = string_a[i-n:]
        begin_b = string_b[:n-i]
        if end_a == begin_b:
            common_substring = end_a
            break
    
    if (common_substring == ""):
        return['', string_a, 0]
    else:
        len_common = len(common_substring)
        remaining_string = string_a[:-len_common]
        return [common_substring, remaining_string, 1 + len(string_b) - len_common]

def number_of_clicks (number_to_make, list_of_numbers, dp):
    length = len(number_to_make)
    if length == 0:
        dp[0] = 0
        return 0

    elif length == 1:
        stage_answers = []
        for sd in list_of_numbers:
            com_str, rem_str, clicks = find_max_ending(number_to_make, sd)
            dp[1] = min(stage_answers)
            return dp[1]

    elif dp[length] is not None:
            return dp[length]
    else:
        stage_answers = []
        for sd in list_of_numbers:

        dp[length] = min(
            find_max_ending(number_to_make, sd[0])[2] + number_of_clicks(find_max_ending(number_to_make, sd[0])[1], list_of_numbers, dp),
            find_max_ending(number_to_make, sd[1])[2] + number_of_clicks(find_max_ending(number_to_make, sd[1])[1], list_of_numbers, dp),
            find_max_ending(number_to_make, sd[2])[2] + number_of_clicks(find_max_ending(number_to_make, sd[2])[1], list_of_numbers, dp),
            
        )
        return dp[length]

list_of_keys = ['0','1','2','3','4','5','6','7','8','9']

#str_1 = input()
#str_2 = input()

#print(find_max_ending(str_1, str_2))

in_string = input()
dp = [None for _ in range(len(in_string)+1)]

number_of_clicks(in_string, list_of_keys, dp)

print(dp)

    
    


