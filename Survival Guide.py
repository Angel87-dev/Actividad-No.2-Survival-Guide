print("Bienvenido al Survival Guide")
print("A continuación se mostraran los 4 nieveles que debes pasar")
print("En cada nivel, si tienes 2 respuestas correctas, tienes la posibilidad de avanzar al siguiente")

print("============")
correctas = 0
while True:
    print("")
    print("La Cámara de las Reglas: Donde se explican las normas de convivencia y asistencia.")
    print("Conforme a las siguientes opciones...")
    print("1. Respeto, 2. Falta de compromiso, 3. Ser grosero")
    respuesta = input("¿Que se tiene que mostrar en clase?: ")
    if respuesta == "1":
        print("Respuesta correcta")
        correctas += 1
        print("Llevas: " ,correctas, "respuestas correctas")
    else:
        print("Respuesta equivocada")
        print("Llevas: " ,correctas, "respuestas correctas")

    print("")
    print("Es _______ particiar en clase")
    print("1. Irrelevante, 2. Importante, 3. Considerable")
    respuesta = input("¿Cual es tu respuesta?: ")
    if respuesta == "2":
        print("Respuesta correcta")
        correctas += 1
        print("Llevas: " ,correctas, "respuestas correctas")
        if correctas >= 2:
            decision = input("¿Quieres pasar al siguiente nivel? (1=Si/0=No): ")
            if decision == "1":
                break
    else:
        print("Respuesta equivocada")
        print("Llevas: " ,correctas, "respuestas correctas")

    print("")
    print("¿A las cuantas faltas te vas a final del parcial?")
    print("1. Dos faltas, 2. Tres faltas, 3. Cinco faltas")
    respuesta = input("¿Cuál es tu respuesta?: ")
    if respuesta == "2":
        print("Respuesta correcta")
        correctas += 1
        print("Llevas: " ,correctas, "respuestas correctas")
        if correctas >= 2:
            decision = input("¿Quieres pasar al siguiente nivel? (1=Si/0=No): ")
            if decision == "1":
                break
    else:
        print("Respuesta equivocada")
        print("Llevas: " ,correctas, "respuestas correctas")
        if correctas >= 2:
            decision = input("¿Quieres pasar al siguiente nivel? (1=Si/0=No): ")
            if decision == "1":
                break

    print("")
    print("¿Cuál es la calificación máxima en un final?")
    print("1. Diez, 2. Nueve, 3. Ocho, 4. Siete")
    respuesta = input("¿Cuál es tu respuesta?: ")
    if respuesta == "3":
        print("Respuesta correcta")
        correctas += 1
        print("Llevas: " ,correctas, "respuestas correctas")
        if correctas >= 2:
            decision = input("¿Quieres pasar al siguiente nivel? (1=Si/0=No): ")
            if decision == "1":
                break
    else:
        print("Respuesta equivocada")
        print("Llevas: " ,correctas, "respuestas correctas")
        if correctas >= 2:
            decision = input("¿Quieres pasar al siguiente nivel? (1=Si/0=No): ")
            if decision == "1":
                break

    print("")
    print("¿Qué pasa si se encuentra plagio en los trabajos?")
    print("1. Cero para todos, 2. Se puede volver a hacer el trabajo, 3. Cero solamente para la persona que copio")
    respuesta = input("¿Cuál es tu respuesta?: ")
    if respuesta == "1":
        print("Respuesta correcta")
        correctas += 1
        print("Llevas: " ,correctas, "respuestas correctas")
        if correctas >= 2:
            decision = input("¿Quieres pasar al siguiente nivel? (1=Si/0=No): ")
            if decision == "1":
                break
    else:
        print("Respuesta equivocada")
        print("Llevas: " ,correctas, "respuestas correctas")
        if correctas >= 2:
            decision = input("¿Quieres pasar al siguiente nivel? (1=Si/0=No): ")
            if decision == "1":
                break

    print("")
    print("¿Como se tienen que entregar los trabajos?")
    print("1. Incompletos, 2. Minimo con la mitad de lo que se requiere, 3. Completos")
    respuesta = input("¿Cuál es tu respuesta?: ")
    if respuesta == "3":
        print("Respuesta correcta")
        correctas += 1
        if correctas >= 2:
            print("Obtuviste" ,correctas, "respuestas correctas, puedes avanzar")
            break
    else:
        print("Respuesta equivocada")
        if correctas >= 2:
            print("Obtuviste" ,correctas, "respuestas correctas, puedes avanzar")
            break

print("")
print("============")
correctas = 0
while True:
    print("")
    print("El Oráculo de las Notas: Donde se detallan los porcentajes de evaluación.")
    print("¿Cuanto vale la evidencia de conocimiento 1P?")
    print("1. 35%, 2. 40%, 3. 45%")
    respuesta = input("¿Cuál es tu respuesta?: ")
    if respuesta == "2":
        print("Respuesta correcta")
        correctas += 1
        print("Llevas: " ,correctas, "respuestas correctas")
    else:
        print("Respuesta equivocada")
        print("Llevas: " ,correctas, "respuestas correctas")

    print("")
    print("¿Cuanto vale el PI en el primer y segundo parcial?")
    print("1. 10%, 2. 15%, 3. 20%")
    respuesta = input("¿Cual es tu respuesta?: ")
    if respuesta == "1":
        print("Respuesta correcta")
        correctas += 1
        print("Llevas: " ,correctas, "respuestas correctas")
        if correctas >= 2:
            decision = input("¿Quieres pasar al siguiente nivel? (1=Si/0=No): ")
            if decision == "1":
                break
    else:
        print("Respuesta equivocada")
        print("Llevas: " ,correctas, "respuestas correctas")

    print("")
    print("¿Cuanto vale la evidencia de desempeño en el 2P?")
    print("1. 20%, 2. 25%, 3. 30%")
    respuesta = input("¿Cuál es tu respuesta?: ")
    if respuesta == "1":
        print("Respuesta correcta")
        correctas += 1
        print("Llevas: " ,correctas, "respuestas correctas")
        if correctas >= 2:
            decision = input("¿Quieres pasar al siguiente nivel? (1=Si/0=No): ")
            if decision == "1":
                break
    else:
        print("Respuesta equivocada")
        print("Llevas: " ,correctas, "respuestas correctas")
        if correctas >= 2:
            decision = input("¿Quieres pasar al siguiente nivel? (1=Si/0=No): ")
            if decision == "1":
                break

    print("")
    print("¿Cuanto vale la evidencia de conocimiento en el 3P?")
    print("1. 30%, 2. 20%, 3. 10%")
    respuesta = input("¿Cuál es tu respuesta?: ")
    if respuesta == "3":
        print("Respuesta correcta")
        correctas += 1
        print("Llevas: " ,correctas, "respuestas correctas")
        if correctas >= 2:
            decision = input("¿Quieres pasar al siguiente nivel? (1=Si/0=No): ")
            if decision == "1":
                break
    else:
        print("Respuesta equivocada")
        print("Llevas: " ,correctas, "respuestas correctas")
        if correctas >= 2:
            decision = input("¿Quieres pasar al siguiente nivel? (1=Si/0=No): ")
            if decision == "1":
                break

    print("")
    print("¿Cuanto vale la evidencia de producto en el 3P?")
    print("1. 20%, 2. 30%, 3. 40%")
    respuesta = input("¿Cuál es tu respuesta?: ")
    if respuesta == "2":
        print("Respuesta correcta")
        correctas += 1
        print("Llevas: " ,correctas, "respuestas correctas")
        if correctas >= 2:
            decision = input("¿Quieres pasar al siguiente nivel? (1=Si/0=No): ")
            if decision == "1":
                break
    else:
        print("Respuesta equivocada")
        print("Llevas: " ,correctas, "respuestas correctas")
        if correctas >= 2:
            decision = input("¿Quieres pasar al siguiente nivel? (1=Si/0=No): ")
            if decision == "1":
                break

    print("")
    print("¿Cuanto vale el PI en el 3P?")
    print("1. 30%, 2. 40%, 3. 50%")
    respuesta = input("¿Cuál es tu respuesta?: ")
    if respuesta == "3":
        print("Respuesta correcta")
        correctas += 1
        if correctas >= 2:
            print("Obtuviste" ,correctas, "respuestas correctas, puedes avanzar")
            break
    else:
        print("Respuesta equivocada")
        if correctas >= 2:
            print("Obtuviste" ,correctas, "respuestas correctas, puedes avanzar")
            break

print("")
print("============")
correctas = 0
while True:
    print("")
    print("Skills a desbloquear: Aquí se detallan el objetivo general y particular de la materia")
    print("El primer punto del objetivo general de la materia es: ")
    print("1. App web o móvil, 2. API, 3. Base de datos")
    respuesta = input("¿Cuál es tu respuesta?: ")
    if respuesta == "1":
        print("Respuesta correcta")
        correctas += 1
        print("Llevas: " ,correctas, "respuestas correctas")
    else:
        print("Respuesta equivocada")
        print("Llevas: " ,correctas, "respuestas correctas")

    print("")
    print("El segundo punto menciona internet ¿que tipo es?")
    print("1. Privado, 2. Público")
    respuesta = input("¿Cual es tu respuesta?: ")
    if respuesta == "2":
        print("Respuesta correcta")
        correctas += 1
        print("Llevas: " ,correctas, "respuestas correctas")
        if correctas >= 2:
            decision = input("¿Quieres pasar al siguiente nivel? (1=Si/0=No): ")
            if decision == "1":
                break
    else:
        print("Respuesta equivocada")
        print("Llevas: " ,correctas, "respuestas correctas")

    print("")
    print("Fatan tres puntos del objetivo general ¿Cuál es el orden?")
    print("1. Servidor web/API/Base de datos, 2. Base de datos/Servidor web/API, 3. API/Servidor web/Base de datos")
    respuesta = input("¿Cuál es tu respuesta?: ")
    if respuesta == "3":
        print("Respuesta correcta")
        correctas += 1
        print("Llevas: " ,correctas, "respuestas correctas")
        if correctas >= 2:
            decision = input("¿Quieres pasar al siguiente nivel? (1=Si/0=No): ")
            if decision == "1":
                break
    else:
        print("Respuesta equivocada")
        print("Llevas: " ,correctas, "respuestas correctas")
        if correctas >= 2:
            decision = input("¿Quieres pasar al siguiente nivel? (1=Si/0=No): ")
            if decision == "1":
                break

    print("")
    print("¿Qué usaremos en el objetivo específico?")
    print("1. HTML, 2. JS, 3. Figma")
    respuesta = input("¿Cuál es tu respuesta?: ")
    if respuesta == "2":
        print("Respuesta correcta")
        correctas += 1
        print("Llevas: " ,correctas, "respuestas correctas")
        if correctas >= 2:
            decision = input("¿Quieres pasar al siguiente nivel? (1=Si/0=No): ")
            if decision == "1":
                break
    else:
        print("Respuesta equivocada")
        print("Llevas: " ,correctas, "respuestas correctas")
        if correctas >= 2:
            decision = input("¿Quieres pasar al siguiente nivel? (1=Si/0=No): ")
            if decision == "1":
                break

    print("")
    print("¿Cual es la otra herramienta que usaremos?")
    print("1. React Native, 2. Flutter, 3. Ionic")
    respuesta = input("¿Cuál es tu respuesta?: ")
    if respuesta == "1":
        print("Respuesta correcta")
        correctas += 1
        print("Llevas: " ,correctas, "respuestas correctas")
        if correctas >= 2:
            decision = input("¿Quieres pasar al siguiente nivel? (1=Si/0=No): ")
            if decision == "1":
                break
    else:
        print("Respuesta equivocada")
        print("Llevas: " ,correctas, "respuestas correctas")
        if correctas >= 2:
            decision = input("¿Quieres pasar al siguiente nivel? (1=Si/0=No): ")
            if decision == "1":
                break

    print("")
    print("En relación a la pregunta anterior ¿Cuáles son las características?")
    print("1. Componentes, Screens, Navigations y Comunicación con API")
    print("2. Componentes, Ventanas, Conexiones locales y Bases de datos")
    print("3. Interfaces, Navegación, Diseño visual y Configuración de servidores")
    respuesta = input("¿Cuál es tu respuesta?: ")
    if respuesta == "1":
        print("Respuesta correcta")
        correctas += 1
        if correctas >= 2:
            print("Obtuviste" ,correctas, "respuestas correctas, puedes avanzar")
            break
    else:
        print("Respuesta equivocada")
        if correctas >= 2:
            print("Obtuviste" ,correctas, "respuestas correctas, puedes avanzar")
            break

print("============")
print("La Línea del Tiempo: Donde se muestran las fechas clave del semestre.")

print("============")
print("Felicidades, haz sobrevivido... por el momento")