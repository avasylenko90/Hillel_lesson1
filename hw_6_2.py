user_input = input("Please enter any number > 0 and < 8640000.: ")
days = int(user_input)//(24*60*60)
days_balance = int(user_input)%(24*60*60)
hours = days_balance//(60*60)
hours_balance = days_balance%(60*60)
minutes = hours_balance//(60)
minutes_balance = hours_balance%(60)
seconds = int(minutes_balance)%60
if days % 10 == 1 and days % 100 != 11:
    day_word = "день"
elif days % 10 in [2, 3, 4] and days % 100 not in [12, 13, 14]:
    day_word = "дні"
else:
    day_word = "днів"

print(str(days).zfill(2) + " " + day_word + "," + str(hours).zfill(2) + ":" + str(minutes).zfill(2) + ":" + str(seconds).zfill(2))
