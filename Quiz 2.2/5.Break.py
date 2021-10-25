number = 0
for number in range(10):
    if number == 5:
        break    # El break hace que el bucle “for” se rompa y gracias a esto el bucle se acabara e imprimirá “Fuera de ciclo”
    print('Number is ' + str(number))
print('Fuera del ciclo')
