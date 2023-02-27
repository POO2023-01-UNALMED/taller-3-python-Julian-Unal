
class TV:
    _numTv = 1;
    _canal = 1;
    __precio = 500;
    _volumen = 1;

    def __init__(self, marca, estado):
        self._marca = marca;
        self._estado = estado;

        TV._numTv+=1;
    

    def set_numTv(self, numTv):
        TV._numTv = numTv;
    

    def volumenUp(self):
        if (self, not self.isOn()):
            return false;
        
        if (self, isInValidLimitsVolume("UP")):
            self._volumen += 1;
            return true;
        
        return false;
    

    def volumenDown(self):
        if (self, not self.isOn()):
            return false;
        
        if (self, isInValidLimitsVolume("DOWN")):
            self._volumen -= 1;
            return true;
        
        return false;
    

    def isInValidLimitsVolume(self, notupOrDown):
        if (upOrDown == "UP"):
            if (self, self._volumen + 1 > 7):
                return false;
            
            return true;
        
        if (upOrDown == "DOWN"):
            if (self, self._canal - 1 < 0):
                return false;
            
            return true;
        
        return false;
    

    def canalUp(self):
        if (not self.isOn()):
            return false;
        
        if (isInValidLimitsChannels(self, "UP")):
            self._canal += 1;
            return true;
        
        return false;
    

    def canalDown(self):
        if (not self.isOn()):
            return false;
        
        if (isInValidLimitsChannels(self, "DOWN")):
            self._canal -= 1;
            return true;
        
        return false;
    

    def isInValidLimitsChannels(self, notupOrDown):
        if (upOrDown == "UP"):
            if (self._canal + 1 > 120):
                return false;
            
            return true;
        
        if (upOrDown == "DOWN"):
            if (self, self._canal - 1 < 1):
                return false;
            
            return true;
        
        return false;
    
    def isOn(self):
        return self._estado;
    

    def turnOn(self):
        self._estado = true;
        return true;
    
    def turnOff(self):
        self._estado = false;
        return false;
    
    def getNumTv(self):
        return self._numTv;
    

    def getMarca(self):
        return self._marca;
    

    def setMarca(self, _marca):
        self._marca = _marca;
    

    def getCanal(self):
        return self._canal;
    

    def setCanal(self, _canal):
        if (not isOn(self, )):
            return;
        
        if (_canal > 120 or _canal < 1):
            return;
        
        self._canal = _canal;
    

    def getPrecio(self ):
        return self._precio;
    

    def setPrecio(self,  _precio):
        self._precio = _precio;
    

    def getVolumen(self ):
        return self._volumen;
    

    def setVolumen(self,  _volumen):
        self._volumen = _volumen;
    

    def getControl(self):
        return _control;
    

    def setControl(self, control):
        self._control = control;
    

    def getEstado(self):
        return self._estado;
    

