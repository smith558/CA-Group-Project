import math
class Voltage():
      def _init_(self):
            self.Vr=0
            self.Vs=0
            self.Vl=0
            self.o=0
            self.Z=0
            self.Xl=0
            self.Xc=0

      def r_voltage(self,I,R):
            self.Vr=I*R
            return self.Vr

      def s_voltage_rl(self):
            self.Vs = math.sqrt(self.Vr**2 + self.Vl**2)
            return self.Vs

      def l_voltage(self,I):
            self.Vl = self.Xl*I
            return self.Vl
      
      def angle(self,R):
            a=((self.Xl-self.Xc)/R) 
            self.o = math.atan(a)
            return self.o

      



     


