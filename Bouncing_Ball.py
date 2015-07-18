import math

def fall(n):
    
    YPos = 200
    YVelocity = 0
    YAcceleration = -9.81
    mass = 10
    r = 0.25
    e = -0.7
    YForce = 0
    time = 0.1
    fluidDensity = 1.2
    dragCoefficient = 0.47
    suffaceArea = math.pi * r * r
    averageYAcceleration = YAcceleration
    
    for i in range(1, n):

        YPos -= YVelocity * time + (0.5 * averageYAcceleration * time * time)
        
        YForce = mass * -1 * YAcceleration
        #Air resistance
        YForce -= 0.5 * fluidDensity * YVelocity * YVelocity * dragCoefficient * suffaceArea
        
        newYAcceleration = YForce / mass
        averageYAcceleration = 0.5 * ((-1 * averageYAcceleration) + newYAcceleration)
        YVelocity += averageYAcceleration * time
        averageYAcceleration *= -1

        if YPos < 0 and YVelocity > 0:
            YVelocity *= e
            YPos -= (YVelocity * time + (0.5 * averageYAcceleration * time * time))

        print(i)                
        print(YPos, end='\n')
        print(YVelocity, end='\n')
        print(averageYAcceleration, end='\n')
        print(YForce, end='\n')
        print()

fall(750)
