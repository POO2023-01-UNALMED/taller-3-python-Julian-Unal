
class Control:
    def enlazar(self, tv):
        self.tv = tv;
        self.tv.setControl(self);
        return true;
    
    def volumenUp(self):

        return self.tv.volumenUp();
    

    def volumenDown(self):

        return self.tv.volumenDown();
    

    def canalUp(self):

        return self.tv.canalUp();
    

    def canalDown(self):

        return self.tv.canalDown();
    

    def turnOn(self):
        return self.tv.turnOn();
    
    def turnOff(self):
        return self.tv.turnOff();
    

    def setCanal(self, canal):
        self.tv.setCanal(canal);
        return true;
    

    def getTv(self):
        return self.tv;
    

    def setTv(self, tv):
        self.tv = tv;
    

