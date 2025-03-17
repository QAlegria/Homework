def statistics_avg(param_list: list) -> int:
    avg = sum(param_list)/(len(param_list))
    print(f'Среднее арифметическое = {avg}')
    return avg

def statistics_med(param_list: list) -> int:
    list.sort(param_list)
    len_list = len(param_list)
    if len_list % 2 == 0:
        med = (param_list[(len_list//2)-1] + param_list[len_list//2]) / 2
    else:
        med = param_list[len_list//2]
    print(f'Медиана = {med}')
    return med