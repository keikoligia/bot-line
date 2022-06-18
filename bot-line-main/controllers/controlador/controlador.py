"""from controller import Robot

def seguirLinha(robot):
    maxSpeed = 1.2
    timestep = 32
    
    motor_esq = robot.getDevice("left wheel motor")
    motor_esq.setPosition(float('inf'))
    motor_esq.setVelocity(0.0)
    
    motor_dir = robot.getDevice("right wheel motor")
    motor_dir.setPosition(float('inf'))
    motor_dir.setVelocity(0.0)
    
    dsEsq = robot.getDevice("ds0")
    dsEsq.enable(timestep)
    
    dsDir = robot.getDevice("ds1")
    dsDir.enable(timestep)
    count = 1
    while robot.step(timestep) != -1:
        print("entrou")
        esqVal = dsEsq.getValue()
        dirVal = dsDir.getValue()
        
        veloE = maxSpeed * 0.95
        veloD = maxSpeed * 0.95
        
        print("dir: " + str(dirVal) + " esq: " + str(esqVal))
        
        if (esqVal > dirVal) and (0 < esqVal < 1001):
            print("esq")
            veloE = -maxSpeed * 0.25
        elif (dirVal > esqVal) and (0 < dirVal < 1011):
            print("dir")
            veloD = -maxSpeed * 0.25

        motor_esq.setVelocity(veloE)
        motor_dir.setVelocity(veloD)
        count = count + 1
        print("fim: " + str(count))
        
if __name__ == "__main__":
    robot = Robot()
    seguirLinha(robot) """
from controller import Robot

# create the Robot instance.
robot = Robot()

# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())

motor_esq = robot.getDevice("left wheel motor")
motor_esq.setPosition(float('+inf'))
motor_esq.setVelocity(0.0)


motor_dir = robot.getDevice("right wheel motor")
motor_dir.setPosition(float('+inf'))
motor_dir.setVelocity(0.0)

ds0 = robot.getDevice("ds0")
ds0.enable(timestep)

ds1 = robot.getDevice("ds1")
ds1.enable(timestep)

veloE = 2.0
veloD = 2.0

# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:
    # Read the sensors:
    # Enter here functions to read sensor data, like:
    val  = ds0.getValue()
    val1 = ds1.getValue()
    
    print("{:.1f}".format(val))
    
    if val > 800:
        veloD = 0
        velo = 1.0

    # Process sensor data here.

    # Enter here functions to send actuator commands, like:
    motor_esq.setVelocity(veloD)
    motor_dir.setVelocity(veloE)
    pass
