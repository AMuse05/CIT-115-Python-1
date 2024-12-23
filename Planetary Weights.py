fMercury = 0.38
fVenus = 0.91
fMoon = 0.165
fMars = 0.38
fJupiter = 2.34
fSaturn = 0.93
fUranus = 0.92
fNeptune = 1.12
fPluto = 0.066

fWeight = float(input("What is your weight?"))

fMercuryWeight = fMercury * fWeight
fVenusWeight = fVenus * fWeight
fMoonWeight = fMoon * fWeight
fMarsWeight = fMars * fWeight
fJupiterWeight = fJupiter * fWeight
fSaturnWeight = fSaturn * fWeight
fUranusWeight = fUranus * fWeight
fNeptuneWeight = fNeptune * fWeight
fPlutoWeight = fPluto * fWeight

print(f'You are {fMercuryWeight:.2f}lbs on Mercury')
print(f'You are {fVenusWeight:.2f}lbs on Venus')
print(f'You are {fMoonWeight:.2f}lbs on the Moon')
print(f'You are {fMarsWeight:.2f}lbs on Mars')
print(f'You are {fJupiterWeight:.2f}lbs on Jupiter')
print(f'You are {fSaturnWeight:.2f}lbs on Saturn')
print(f'You are {fUranusWeight:.2f}lbs on Uranus')
print(f'You are {fNeptuneWeight:.2f}lbs on Neptune')
print(f'You are {fPlutoWeight:.2f}lbs on Pluto')
