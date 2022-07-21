# 1. Первым числом он вводит количество клиентов, которые посетили сегодня офис.
# 2. Далее он вводит оценки от клиентов подряд. Оценок ровно столько, сколько он указал клиентов.

user_scores = []
clients_count = int(input('Введите количество клиентов: '))
for i in range(clients_count):
    new_score = int(input('Введите оценку клиента: ')) # считайте новое значение с экрана
    user_scores.append(new_score) # добавьте его в user_scores с помощью append
print(user_scores)


# Представьте, что вы работаете с почасовой оплатой в день. Стоимость одного часа вашей работы —
# 100 рублей в будние и в два раза больше в выходные. Давайте посчитаем, сколько денег вы бы заработали
# по таким расценкам за одну неделю.
# 1. Заполните список `working_hours` семью значениями: количество часов, отработанных в
# день (каждый элемент соответствует одному из дней недели: 0 — понедельник, 1 — вторник, 2 — среда и так далее).
# 2. Посчитайте стоимость вашей работы в выходные дни (суббота, воскресенье).
# 3. Посчитайте стоимость вашей работы в будние дни.
# 4. Посчитайте стоимость вашей работы за все дни недели.

rub_per_hour = 100
working_hours = [8, 5, 9, 12, 4, 0, 2]
weekday_salary = (working_hours[0] + working_hours[1] + working_hours[2] +
                  working_hours[3] + working_hours[4]) * 100
print('Зарплата за будние дни:', weekday_salary)

weekend_salary = (working_hours[5] + working_hours[6]) * 200
print('Зарплата за выходные дни:', weekend_salary)

total_salary = weekday_salary + weekend_salary
print('Зарплата за все дни недели:', total_salary)