
class TV:
    _numTv = 1;

    def __init__(self, marca, estado):
        self._marca = marca;
        self._estado = estado;
        self._canal = 1;
        self._precio = 500;
        self._volumen = 1;

        TV._numTv+=1;
    
    @classmethod
    def setNumTV(self, numTv):
        self._numTv = numTv;
    

    def volumenUp(self):
        if(not self.isOn()):
            return False;
        
        if(self.isInValidLimitsVolume("UP")):
            self._volumen += 1;
            return True;
        
        return False;
    

    def volumenDown(self):
        if(not self.isOn()):
            return False;
        
        if(isInValidLimitsVolume("DOWN")):
            self._volumen -= 1;
            return True;
        
        return False;
    

    def isInValidLimitsVolume(self, upOrDown):
        if (upOrDown == "UP"):
            if(self._volumen + 1 > 7):
                return False;
            
            return True;
        
        if (upOrDown == "DOWN"):
            if(self._canal - 1 < 0):
                return False;
            
            return True;
        
        return False;
    

    def canalUp(self):
        if (not self.isOn()):
            return False;
        
        if (self.isInValidLimitsChannels("UP")):
            self._canal += 1;
            return True;
        
        return False;
    

    def canalDown(self):
        if (not self.isOn()):
            return False;
        
        if (self.isInValidLimitsChannels("DOWN")):
            self._canal -= 1;
            return True;
        
        return False;
    

    def isInValidLimitsChannels(self, upOrDown):
        if (upOrDown == "UP"):
            if (self._canal + 1 > 120):
                return False;
            
            return True;
        
        if (upOrDown == "DOWN"):
            if(self._canal - 1 < 1):
                return False;
            
            return True;
        
        return False;
    
    def isOn(self):
        return self._estado;
    

    def turnOn(self):
        self._estado = True;
        return True;
    
    def turnOff(self):
        self._estado = False;
        return False;
    
    @classmethod
    def getNumTV(self):
        return self._numTv;
    

    def getMarca(self):
        return self._marca;
    

    def setMarca(self, _marca):
        self._marca = _marca;
    

    def getCanal(self):
        return self._canal;
    

    def setCanal(self, canal):
        if (not self.isOn()):
            return;
        
        if (canal > 120 or canal < 1):
            return;
        
        self._canal = canal;
    

    def getPrecio(self ):
        return self._precio;
    

    def setPrecio(self,  _precio):
        self._precio = _precio;
    

    def getVolumen(self ):
        return self._volumen;
    

    def setVolumen(self,  _volumen):
        self._volumen = _volumen;
    

    def getControl(self):
        return self._control;
    

    def setControl(self, control):
        self._control = control;
    

    def getEstado(self):
        return self._estado;
    

