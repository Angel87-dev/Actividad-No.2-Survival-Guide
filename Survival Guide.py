print("Bienvenido al Survival Guide")
print("A continuación se mostraran los 4 nieveles que debes pasar")

print("============")
correctas = 0
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

print("")
print("Es _______ particiar en clase")
print("1. Irrelevante, 2. Importante, 3. Considerable")
respuesta = input("¿Cual es tu respuesta?: ")
if respuesta == "2":
    print("Respuesta correcta")
    correctas += 1
    print("Llevas: " ,correctas, "respuestas correctas")
else:
    print("Respuesta equivocada")

print("============")
print("El Oráculo de las Notas: Donde se detallan los porcentajes de evaluación.")

print("============")
print("Skills a desbloquear: Aquí se detallan el objetivo general y particular de la materia")

print("============")
print("La Línea del Tiempo: Donde se muestran las fechas clave del semestre.")

print("============")
print("Felicidades, haz sobrevivido... por el momento")