# Shapiro-Steps
Python code to generate the DC I-V characteristics of a RCSJ circuit aka "Shapiro steps" by solving the following ODE:
$$
  I_{DC} + I_{AC} \sin(\omega t) = \frac{\hbar C}{2e} \frac{d^2\gamma}{dt^2} + \frac{\hbar}{2eR} \frac{d\gamma}{dt} + I_c \sin(\gamma)
$$
