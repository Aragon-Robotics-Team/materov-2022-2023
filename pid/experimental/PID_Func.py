class PID:
    def __init__(self):
        self.proportionalGain = 1.0
        self.integralGain = 1.0
        self.derivativeGain = 1.0
        self.error = 0.0
        self.derivativeError = 0.0
        self.previousError = 0.0
        self.integralSum = 0.0
        self.pidOutput = 0.0

    def calcPID(self, depth, goal):

        self.error = goal - depth
        self.integralSum += self.error
        self.derivativeError = self.error - self.previousError;

        proportion = self.proportionalGain * self.error
        integral = self.integralGain * self.integralSum
        derivative = self.derivativeGain * self.derivativeError
        

        self.pidOutput = proportion + integral + derivative

        self.previousError = self.error
        
        return [self.pidOutput, proportion, integral, derivative]


    
    def tune_PID(self, proportional, integral, derivative):
        self.proportionalGain = proportional
        self.integralGain = integral
        self.derivativeGain = derivative

    #graphing stuff ;D
