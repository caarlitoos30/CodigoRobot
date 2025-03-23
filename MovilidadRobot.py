"""

Variables globales

"""
# Funciones de movimiento
def car_back():
    mecanumRobotV2.motor(LR.UPPER_LEFT, MD.BACK, 50)
    mecanumRobotV2.motor(LR.LOWER_LEFT, MD.BACK, 50)
    mecanumRobotV2.motor(LR.UPPER_RIGHT, MD.BACK, 50)
    mecanumRobotV2.motor(LR.LOWER_RIGHT, MD.BACK, 50)
# Función para evitar obstáculos
def avoid_obstacles():
    global distance2, distance_l, distance_r
    distance2 = mecanumRobotV2.ultra()
    if distance2 < 20:
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
    else:
        car_forward()
def car_left():
    mecanumRobotV2.motor(LR.UPPER_LEFT, MD.BACK, 50)
    mecanumRobotV2.motor(LR.LOWER_LEFT, MD.BACK, 50)
    mecanumRobotV2.motor(LR.UPPER_RIGHT, MD.FORWARD, 50)
    mecanumRobotV2.motor(LR.LOWER_RIGHT, MD.FORWARD, 50)
# Inicialización
def initialize():
    basic.show_icon(IconNames.HAPPY)
    mecanumRobotV2.set_servo(90)
# Función para el control manual con el mando
def manual_control():
    global val3
    val3 = irRemote.return_ir_button()
    if val3 != 0:
        val22 = val3
        if val22 == 70:
            mecanumRobotV2.motor(LR.UPPER_LEFT, MD.FORWARD, 50)
            mecanumRobotV2.motor(LR.LOWER_LEFT, MD.FORWARD, 50)
            mecanumRobotV2.motor(LR.UPPER_RIGHT, MD.FORWARD, 50)
            mecanumRobotV2.motor(LR.LOWER_RIGHT, MD.FORWARD, 50)
        elif val22 == 68:
            mecanumRobotV2.motor(LR.UPPER_LEFT, MD.BACK, 50)
            mecanumRobotV2.motor(LR.LOWER_LEFT, MD.BACK, 50)
            mecanumRobotV2.motor(LR.UPPER_RIGHT, MD.FORWARD, 50)
            mecanumRobotV2.motor(LR.LOWER_RIGHT, MD.FORWARD, 50)
        elif val22 == 67:
            mecanumRobotV2.motor(LR.UPPER_LEFT, MD.FORWARD, 50)
            mecanumRobotV2.motor(LR.LOWER_LEFT, MD.FORWARD, 50)
            mecanumRobotV2.motor(LR.UPPER_RIGHT, MD.BACK, 50)
            mecanumRobotV2.motor(LR.LOWER_RIGHT, MD.BACK, 50)
        elif val22 == 21:
            mecanumRobotV2.state()
def car_forward():
    mecanumRobotV2.motor(LR.UPPER_LEFT, MD.FORWARD, 50)
    mecanumRobotV2.motor(LR.LOWER_LEFT, MD.FORWARD, 50)
    mecanumRobotV2.motor(LR.UPPER_RIGHT, MD.FORWARD, 50)
    mecanumRobotV2.motor(LR.LOWER_RIGHT, MD.FORWARD, 50)
# Función de seguimiento de línea
def line_tracking():
    global LL, CC, RR
    LL = mecanumRobotV2.line_tracking(LT.LEFT)
    CC = mecanumRobotV2.line_tracking(LT.CENTER)
    RR = mecanumRobotV2.line_tracking(LT.RIGHT)
def follow_line():
    line_tracking()
    if LL == 0 and CC == 0 and RR == 0:
        mecanumRobotV2.state()
    elif LL == 0 and CC == 0 and RR == 1:
        mecanumRobotV2.motor(LR.UPPER_LEFT, MD.FORWARD, 85)
        mecanumRobotV2.motor(LR.LOWER_LEFT, MD.FORWARD, 85)
        mecanumRobotV2.motor(LR.UPPER_RIGHT, MD.BACK, 60)
        mecanumRobotV2.motor(LR.LOWER_RIGHT, MD.BACK, 60)
    elif LL == 0 and CC == 1 and RR == 0:
        mecanumRobotV2.motor(LR.UPPER_LEFT, MD.FORWARD, 40)
        mecanumRobotV2.motor(LR.LOWER_LEFT, MD.FORWARD, 40)
        mecanumRobotV2.motor(LR.UPPER_RIGHT, MD.FORWARD, 40)
        mecanumRobotV2.motor(LR.LOWER_RIGHT, MD.FORWARD, 40)
    elif LL == 0 and CC == 1 and RR == 1:
        mecanumRobotV2.motor(LR.UPPER_LEFT, MD.FORWARD, 85)
        mecanumRobotV2.motor(LR.LOWER_LEFT, MD.FORWARD, 85)
        mecanumRobotV2.motor(LR.UPPER_RIGHT, MD.BACK, 60)
        mecanumRobotV2.motor(LR.LOWER_RIGHT, MD.BACK, 60)
    elif LL == 1 and CC == 0 and RR == 0:
        mecanumRobotV2.motor(LR.UPPER_LEFT, MD.BACK, 60)
        mecanumRobotV2.motor(LR.LOWER_LEFT, MD.BACK, 60)
        mecanumRobotV2.motor(LR.UPPER_RIGHT, MD.FORWARD, 85)
        mecanumRobotV2.motor(LR.LOWER_RIGHT, MD.FORWARD, 85)
    elif LL == 1 and CC == 0 and RR == 1:
        mecanumRobotV2.motor(LR.UPPER_LEFT, MD.FORWARD, 40)
        mecanumRobotV2.motor(LR.LOWER_LEFT, MD.FORWARD, 40)
        mecanumRobotV2.motor(LR.UPPER_RIGHT, MD.FORWARD, 40)
        mecanumRobotV2.motor(LR.LOWER_RIGHT, MD.FORWARD, 40)
    elif LL == 1 and CC == 1 and RR == 0:
        mecanumRobotV2.motor(LR.UPPER_LEFT, MD.BACK, 60)
        mecanumRobotV2.motor(LR.LOWER_LEFT, MD.BACK, 60)
        mecanumRobotV2.motor(LR.UPPER_RIGHT, MD.FORWARD, 85)
        mecanumRobotV2.motor(LR.LOWER_RIGHT, MD.FORWARD, 85)
    elif LL == 1 and CC == 1 and RR == 1:
        mecanumRobotV2.motor(LR.UPPER_LEFT, MD.FORWARD, 40)
        mecanumRobotV2.motor(LR.LOWER_LEFT, MD.FORWARD, 40)
        mecanumRobotV2.motor(LR.UPPER_RIGHT, MD.FORWARD, 40)
        mecanumRobotV2.motor(LR.LOWER_RIGHT, MD.FORWARD, 40)
def car_right():
    mecanumRobotV2.motor(LR.UPPER_LEFT, MD.FORWARD, 50)
    mecanumRobotV2.motor(LR.LOWER_LEFT, MD.FORWARD, 50)
    mecanumRobotV2.motor(LR.UPPER_RIGHT, MD.BACK, 50)
    mecanumRobotV2.motor(LR.LOWER_RIGHT, MD.BACK, 50)
mode = 0
val4 = 0
RR = 0
CC = 0
LL = 0
val3 = 0
distance_r = 0
distance_l = 0
distance2 = 0
val2 = 0
val = 0
distance = 0
led.enable(False)
# Inicialización
initialize()
# Bucle principal

def on_forever():
    global val4, mode
    val4 = irRemote.return_ir_button()
    if val4 != 0:
        val23 = val4
        if val23 == 1:
            mode = 1
            basic.show_icon(IconNames.HAPPY)
        elif val23 == 2:
            mode = 2
            basic.show_icon(IconNames.GHOST)
    # Modo espera
    if mode == 0:
        basic.show_icon(IconNames.DUCK)
        basic.pause(1000)
    elif mode == 1:
        # Modo seguir la línea
        follow_line()
    elif mode == 2:
        # Modo control manual por mando
        manual_control()
    # Modo evitación de obstáculos
    avoid_obstacles()
basic.forever(on_forever)
