# Definición de los movimientos del robot
def car_back():
    mecanumRobotV2.motor(LR.UPPER_LEFT, MD.BACK, 50)
    mecanumRobotV2.motor(LR.LOWER_LEFT, MD.BACK, 50)
    mecanumRobotV2.motor(LR.UPPER_RIGHT, MD.BACK, 50)
    mecanumRobotV2.motor(LR.LOWER_RIGHT, MD.BACK, 50)
def car_left():
    mecanumRobotV2.motor(LR.UPPER_LEFT, MD.BACK, 50)
    mecanumRobotV2.motor(LR.LOWER_LEFT, MD.BACK, 50)
    mecanumRobotV2.motor(LR.UPPER_RIGHT, MD.FORWARD, 50)
    mecanumRobotV2.motor(LR.LOWER_RIGHT, MD.FORWARD, 50)
def car_forward():
    mecanumRobotV2.motor(LR.UPPER_LEFT, MD.FORWARD, 50)
    mecanumRobotV2.motor(LR.LOWER_LEFT, MD.FORWARD, 50)
    mecanumRobotV2.motor(LR.UPPER_RIGHT, MD.FORWARD, 50)
    mecanumRobotV2.motor(LR.LOWER_RIGHT, MD.FORWARD, 50)
def car_right():
    mecanumRobotV2.motor(LR.UPPER_LEFT, MD.FORWARD, 50)
    mecanumRobotV2.motor(LR.LOWER_LEFT, MD.FORWARD, 50)
    mecanumRobotV2.motor(LR.UPPER_RIGHT, MD.BACK, 50)
    mecanumRobotV2.motor(LR.LOWER_RIGHT, MD.BACK, 50)
distance_r = 0
distance_l = 0
distance = 0
RR = 0
CC = 0
LL = 0
# Inicialización de variables y LED
led.enable(False)
basic.show_icon(IconNames.HAPPY)
# Función principal en bucle
# Ejecutar la función principal continuamente

def on_forever():
    global LL, CC, RR, distance, distance_l, distance_r
    # Lectura de sensores de línea
    LL = mecanumRobotV2.line_tracking(LT.LEFT)
    CC = mecanumRobotV2.line_tracking(LT.CENTER)
    RR = mecanumRobotV2.line_tracking(LT.RIGHT)
    # Lectura del sensor ultrasónico para evitar obstáculos
    distance = mecanumRobotV2.ultra()
    if distance < 20:
        # Si se detecta un obstáculo, retroceder y elegir una dirección basada en el sensor ultrasónico
        car_back()
        mecanumRobotV2.state()
        basic.pause(500)
        mecanumRobotV2.set_servo(180)
        basic.pause(500)
        distance_l = mecanumRobotV2.ultra()
        basic.pause(500)
        mecanumRobotV2.set_servo(0)
        basic.pause(500)
        distance_r = mecanumRobotV2.ultra()
        basic.pause(500)
        if distance_l > distance_r:
            car_left()
            mecanumRobotV2.set_servo(90)
            basic.pause(300)
        else:
            car_right()
            mecanumRobotV2.set_servo(90)
            basic.pause(300)
    elif LL == 0 and (CC == 0 and RR == 0):
        mecanumRobotV2.state()
    elif LL == 0 and (CC == 0 and RR == 1):
        car_right()
    elif LL == 0 and (CC == 1 and RR == 0):
        car_forward()
    elif LL == 0 and (CC == 1 and RR == 1):
        car_right()
    elif LL == 1 and (CC == 0 and RR == 0):
        car_left()
    elif LL == 1 and (CC == 0 and RR == 1):
        car_forward()
    elif LL == 1 and (CC == 1 and RR == 0):
        car_left()
    elif LL == 1 and (CC == 1 and RR == 1):
        car_forward()
basic.forever(on_forever)
