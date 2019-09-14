import matplotlib.pyplot as plot
import math
import numpy as np

pt = []
Neve = 0
n = 0
dy = 0.5
PI = math.pi
bin_num = 10
pt_low = 0.0
pt_high = 2.0
pt_range = np.linspace(pt_low,pt_high,bin_num+1)
sum_v2 = np.zeros(bin_num)
N_v2 = np.zeros(bin_num)
print(pt_range)

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

					if(abs(ID) == 211):
						
						p_pt = math.sqrt(px**2 + py**2)
						energy = math.sqrt(px**2 + py**2 +pz**2 + mass**2)
						rapidity = 1/2 * math.log((energy+pz)/(energy-pz))
						if(math.fabs(rapidity) < dy):
							pt.append(p_pt)
							n=n+1
							v2 = (px**2 - py**2) / (px**2 + py**2)
							for i in range(0,bin_num):
								if(p_pt > pt_range[i] and p_pt<pt_range[i+1]):
									sum_v2[i] = sum_v2[i] + v2
									N_v2[i] = N_v2[i] + 1

print(n)
print(sum_v2)
print(N_v2)

c = np.divide(sum_v2,N_v2)
dpt = np.linspace(pt_high/(2*bin_num),pt_high - pt_high/(2*bin_num),bin_num, dtype = float)
print(c)
print(dpt)

plot.plot(dpt,c)
plot.title("Pion v2")
plot.xlabel("Pt")
plot.ylabel("v2")
plot.show()



dat.close
