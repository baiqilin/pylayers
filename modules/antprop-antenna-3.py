import matplotlib.pyplot as plt
from pylayers.antprop.antenna import *
A = Antenna('defant.trx')
fig,ax = A.polar(k=[0,10,50])
