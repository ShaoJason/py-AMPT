import matplotlib.pyplot as plot
import math

pt = []
n = 0
Neve = 0
dpt = 0.2
dy = 1.0
weight = []
we = []
PI = math.pi
with open("datalist.list","r+") as datalist:
	while True:
		filename = str(datalist.readline().strip())
		if not filename:
			break
		print(filename)
		with open(filename,"r+") as dat:
			while True:
				line = dat.readline()
				if not line:
					break
				#print (line)
				nevent, nrun, multi, impactpar, NpartP, NpartT, NELP, NINP, NELT, NINT, passhead = [float(i) for i in line.split()]


				#print (multi)
				Neve = Neve + 1

				multi = int(multi)
				#print (multi)
				for i in range(0,multi):
					line = dat.readline()
					ID, px, py, pz, mass, cx, cy, cz, time = [float(i) for i in line.split()]

					if(ID == 211):
						n=n+1
						p_pt = math.sqrt(px**2 + py**2)
						energy = math.sqrt(px**2 + py**2 +pz**2 + mass**2)
						rapidity = 1/2 * math.log((energy+pz)/(energy-pz))
						if(math.fabs(rapidity) < dy):
							pt.append(p_pt)
							dndy = 1/(2 * PI * p_pt * dpt * 2* dy)
							weight.append(dndy)

print(n)

for x in weight:
	w = x * (1/Neve)
	we.append(w)

plot.hist(pt, bins=10, range=(0,2), histtype='step', weights=we)
plot.semilogy()
plot.ylim(1e-2,1e3)
plot.show()	


dat.close
