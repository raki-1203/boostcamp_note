# [필수과제 4] Baseball

main() 함수를 제외하고는 쉽게 작성했는데 main() 함수에서 시간이 좀 걸렸다.

```python
def main():
    print("Play Baseball")
    random_number = str(get_not_duplicated_three_digit_number())
    print("Random Number is : ", random_number)
    while True:
        user_input = input("Input guess number : ")
        if user_input in ('0', '00', '000'):
            break
        # ===Modify codes below=============
        # 위의 코드를 포함하여 자유로운 수정이 가능함
        if is_validated_number(user_input):
            result = get_strikes_or_ball(user_input, random_number)
            if result == [3, 0]:
                print(f"{random_number} {user_input} {result[0]} "
                        f"Strikes {result[1]} Balls")
                while True:
                    replay_input = input("One more? ")                    
                    if is_yes(replay_input):
                        break
                    elif is_no(replay_input):
                        break
                    elif replay_input in ('0', '00', '000'):
                        break
                    else:
                        print("Wrong Input")
                        continue
                if is_yes(replay_input):
                    # print("Play Baseball")
                    random_number = str(get_not_duplicated_three_digit_number())
                    print("Random Number is : ", random_number)
                    continue
                elif is_no(replay_input):
                    break
                elif replay_input in ('0', '00', '000'):
                    break
            else:
                print(f"{random_number} {user_input} {result[0]} "
                        f"Strikes {result[1]} Balls")
                continue
        else:
            print("Wrong Input")
            continue

    # ==================================
    print("Thank you for using this program")
    print("End of the Game")
```

그리고.... 출력문장을 맞추는데 애를 좀 먹었다.

그래도 알던 게임을 코드로 구현하니 재밌었다.