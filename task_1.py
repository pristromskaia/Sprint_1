time_string = '1h 45m,360s,25m,30m 120s,2h 60s'

#Разделяем строку на отдельные временные значения
time_values = time_string.split(',') 
total_minutes = 0   

for value in time_values:
    minutes = 0

    # Если есть часы — извлекаем число до "h" и конвертируем в минуты
    if 'h' in value: 
        hours_part = value.split('h')[0].strip() 
        hours = int(hours_part)
        minutes += hours * 60
        # Удаляем обработанную часть часов
        value = value.replace(hours_part + 'h', '')

    # Если есть минуты — извлекаем число до "m"
    if 'm' in value: 
        minutes_part = value.split('m')[0].strip()          
        minutes += int(minutes_part)
        value = value.replace(minutes_part + 'm', '') 

    # Если есть секунды — извлекаем число до "s" и конвертируем в минуты
    if 's' in value: 
        seconds_part = value.split('s')[0].strip() 
        seconds = int(seconds_part)
        minutes += seconds // 60
        value = value.replace(seconds_part + 's', '') 
    
    # Суммируем минуты кажого блока
    total_minutes += minutes 

# Печать результата
print (total_minutes)