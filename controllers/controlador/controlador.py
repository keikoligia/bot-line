from controller import Robot

def seguirLinha(robot):
    maxSpeed = 1.2
    timestep = 32
    
    motor_esq = robot.getDevice("left wheel motor")
    motor_esq.setPosition(float('inf'))
    motor_esq.setVelocity(0.0)
    
    motor_dir = robot.getDevice("right wheel motor")
    motor_dir.setPosition(float('inf'))
    motor_dir.setVelocity(0.0)
    
    dsEsq = robot.getDevice("sensor0")
    dsEsq.enable(timestep)
    
    dsDir = robot.getDevice("sensor1")
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
    seguirLinha(robot)