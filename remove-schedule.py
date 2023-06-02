from crontab import CronTab

# Створюємо об'єкт CronTab для поточного користувача
cron = CronTab(user='bradi')

# Видаляємо всі задачі
cron.remove_all()
