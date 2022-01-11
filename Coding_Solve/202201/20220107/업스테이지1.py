def solution(start_date, end_date, login_dates):
    month_day_dict = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
                      7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12:31}

    login_dates = sorted(login_dates)
    start_month = start_date.split()[0].split('/')[0]
    start_day = start_date.split()[0].split('/')[1]
    start_weekday = start_date.split()[1]

    weekday_list = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']

    max_cnt = 0
    cnt = 0
    flag = False  # 연속되는 로그인 시 주말인지 아닌지
    flag2 = True  # 저번주 주말에서 연결되는지 아닌지
    for i, login_date in enumerate(login_dates, 1):
        month = login_date.split('/')[0]
        day = login_date.split('/')[1]

        if start_month == month:
            day_num = int(day) - int(start_day)
        else:
            day_num = 0
            for m in range(int(start_month), int(month)):
                if m == int(start_month):
                    day_num += month_day_dict[m] - int(start_day)
                else:
                    day_num += month_day_dict[m]
            day_num += int(day)

        start_weekday_idx = weekday_list.index(start_weekday)
        weekday = weekday_list[(start_weekday_idx + day_num) % 7]
        weekday_idx = (start_weekday_idx + day_num) % 7

        if i == 1:
            prev_day_num = day_num
            if weekday_list[weekday_idx] not in ['SAT', 'SUN']:
                cnt += 1
            continue

        if weekday_list[weekday_idx] in ['SAT', 'SUN']:
            if day_num - prev_day_num <= 2:
                flag = True
                continue
            else:
                cnt = 1
        else:
            if flag:
                flag = False
                if weekday_list[weekday_idx] == 'MON':
                    cnt += 1
                else:
                    cnt = 1
            else:
                if prev_day_num + 1 == day_num:
                    cnt += 1
                else:
                    if weekday_list[weekday_idx] == 'MON' and day_num - prev_day_num <= 3:
                        cnt += 1
                    else:
                        cnt = 1
            prev_day_num = day_num

        max_cnt = max(max_cnt, cnt)


    answer = max_cnt
    return answer


if __name__ == '__main__':
    start_date = "05/27 SUN"
    end_date = "06/16"
    login_dates = ["05/31", "05/30", "06/01", "06/11", "06/12"]
    print(solution(start_date, end_date, login_dates))
