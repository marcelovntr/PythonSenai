import datetime

hora_atual = input('insira a hora(HH:MM):')

hora_digitada = datetime.datetime.strptime(hora_atual, "%H:%M").time()
print(hora_digitada)   # Saída: 14:30:00
print(hora_digitada.hour)  # Saída: 14
print(hora_digitada.minute)  # Saída: 30

print(datetime.datetime.now())
print(datetime.datetime.now().time())
agora = datetime.datetime.now()

print(agora.strftime("%Y-%m-%d %H:%M:%S"))
print(agora.strftime("%H:%M:%S"))
print(agora.strftime("%H:%M"))


def cumprimentar(hora): 
    if hora.hour > 6 and hora.hour < 12: #if 6 <= hora.hour < 12:
        print('bom dia')
    elif hora.hour > 12 and hora.hour< 18: #elif 12 <= hora.hour < 18:
        print('boa tarde')
    else:
        print('boa noite')

cumprimentar(hora_digitada)