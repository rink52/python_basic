import random

first_team = [round(random.uniform(5,10), 2) for _ in range(20)]
second_team = [round(random.uniform(5,10), 2) for _ in range(20)]
winner = [first_team[cnt]
          if first_team[cnt] > second_team[cnt]
          else second_team[cnt]
          for cnt in range(20)]

print('Первая команда: ', first_team)
print('Вторая команда: ', second_team)
print('Победители тура: ', winner)