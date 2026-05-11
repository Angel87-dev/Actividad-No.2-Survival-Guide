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

print("============")
print("El Oráculo de las Notas: Donde se detallan los porcentajes de evaluación.")

print("============")
print("Skills a desbloquear: Aquí se detallan el objetivo general y particular de la materia")

print("============")
print("La Línea del Tiempo: Donde se muestran las fechas clave del semestre.")

print("============")
print("Felicidades, haz sobrevivido... por el momento")