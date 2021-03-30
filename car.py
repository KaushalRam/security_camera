class Car(object):
    def __init__(self, model, color, company, speedlimit):
        self.model = model
        self.color = color
        self.company = company
        self.speedlimit = speedlimit

    def start(self):
        print('Started')

    def stop(self):
        print('Stopped')

    def changeGear(self,gearType):
        print('Gear changed')

audi = Car("a7","red","audi","50")
    