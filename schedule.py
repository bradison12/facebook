from crontab import CronTab

# Створюємо об'єкт CronTab для поточного користувача
cron = CronTab(user='bradi')

# Створюємо нову задачу cron
job = cron.new(command='/usr/bin/python3 main.py')

# Встановлюємо розклад виконання задачі
job.setall('1 * * * *')

# Записуємо задачу до cron-розкладу
cron.write()
