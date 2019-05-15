class Multiplicacion(object):
    def __init__(self):
        pass
    def mul(self,m1,m2):
        if isinstance (m1,list) and isinstance (m2,list):
            return self.mul_aux(m1,m2,0,0,0,[])
        else : return "error"

    def mul_aux(self,m1,m2,i1,i2,i3,resul):
        if i1== len(m1) and i3 == len(m2[0]):
            return resul
        elif i2 == len(m1[0]) or i2 == len(m2):
            return self.mul_aux(m1,m2,i1+1 ,0,i3+1,resul + m1[i1][i2]* m2[i2][i3])
        else: return self.mu_aux(m1,m2,i1,i2+1,i3,[m1[i1][i2]*m2[i2][i3*]])
        
