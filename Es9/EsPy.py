import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm

#--------------------------Distance function-----------------------------------------

def distance(x, y, z, i):   
    r = np.zeros(len(x))
    for j in range(len(x)):
        r[j] = ((x[i] - x[j])**2 + (y[i] - y[j])**2 + (z[i] - z[j])**2)**0.5
    return r

#--------------------------Read File-------------------------------------------------

data_filename = 'file2_Groups_AGN-wWU_500Mpc_Data.txt'
data = np.loadtxt(data_filename, skiprows = 1, unpack = True)		#file reading and unpacking 

TotMass = data[0]
GasMass = data[1]
DMMass = data[2]
StMass = data[3]
BHMass = data[4]
PosX = data[5]
PosY = data[6]
PosZ = data[7]

BarMass = GasMass + StMass	

#---------------------------DM-BM Graph----------------------------------------------
mask = BarMass > 1e-9

BarMass_fit1 = BarMass[mask] * 1e10		#eliminating points with 0 barionic mass for log scale
DMMass_fit1 = DMMass[mask] * 1e10

sorted_indices = np.argsort(BarMass_fit1)	#sorting the points in BarMass array for fitting purpouses 
BarMass_fit = np.sort(BarMass_fit1)		
DMMass_fit = [DMMass_fit1[i] for i in sorted_indices]	#DMMass reordered following BarMass indices 

coeffs = np.polyfit(BarMass_fit, DMMass_fit, deg=1, rcond=None, full=False, w=None, cov=False)		#def of fitted function as linear 
p = np.poly1d(coeffs)
print (coeffs)

m, q = coeffs
m = round(m, 2)
q = round(q, 2)

plt.scatter(BarMass_fit, DMMass_fit, c='orchid', edgecolors='black', marker='.', s=150)
plt.xlabel('Barionic Mass [M_sun]')
plt.ylabel('Dark Matter Mass [M_sun]')

plt.plot(BarMass_fit, p(BarMass_fit), label='fit y={0}x {1}'.format(m, q))

plt.xscale('log')
plt.yscale('log')
plt.title(label='Dark matter mass - Barionic mass relation')

plt.legend()
plt.show()

#---------------------------Mass-Distance Relation----------------------------------

Dist = np.zeros(len(TotMass))
index = np.where(TotMass == np.max(TotMass))[0].item()	#index of most massive galaxy in the TotMass array
TotMass1 = TotMass * 1e10
Dist = distance(PosX, PosY, PosZ, index) 		#calculate distances with distance function

plt.scatter(Dist, TotMass1, c='orchid', edgecolors='black', marker='.', s=150)
plt.xlabel('Distance [c kpc/h]')
plt.ylabel('Total Mass [Msun]')

plt.yscale('log')       
#plt.xscale('log')
plt.title(label='Mass - Distance from most massive galaxy relation')
plt.legend()
plt.show()

#---------------------------DM Mass Histogram---------------------------------------

DMMass1 = DMMass * 1e10

Med = np.median(DMMass1)
Mean = np.mean(DMMass1)

hist, bins = np.histogram(DMMass1, bins=20)
logbins = np.logspace(np.log10(bins[0]), np.log10(bins[-1]), len(bins))     #define bins over logarithmic scale axis
hist, logbins, _ = plt.hist(DMMass1, bins=logbins)

plt.axvline(x=Med, color='black', linestyle='-', linewidth=2, label='Median')	#median and mean lines set on values calculated above
plt.axvline(x=Mean, color='black', linestyle='-.', linewidth=2, label='Mean')

plt.xscale('log')       #A log scale is used to better appreciate the distribution of masses in the observed group
plt.xlabel('Dark Matter mass [Msun]')
plt.ylabel('Number of objects')
plt.title(label='Dark matter mass distribution histogram')

plt.legend()
plt.show()

#---------------------------Position-Stellar/Dark Mass------------------------------

sizes = np.zeros(len(StMass))
colors = DMMass

for i in range(len(StMass)):			#set points dim based on Stellar Mass. StMass=0 points are set to size 5 
    if StMass[i] != 0:
        sizes[i] = (np.log10(StMass[i]) + 5) * 20 
    else:
        sizes[i] = 3

fig = plt.figure(figsize=(16, 9))
gs = fig.add_gridspec(2, 2)  

norm = LogNorm(vmin=np.min(DMMass), vmax=np.max(DMMass))

ax1 = fig.add_subplot(gs[0, 0])
im1 = ax1.scatter(PosX, PosY, s=sizes, color=plt.cm.viridis(norm(colors)))
ax1.set_xlabel('x-position [c kpc/h]')
ax1.set_ylabel('y-position [c kpc/h]')

ax2 = fig.add_subplot(gs[0, 1])
im2 = ax2.scatter(PosY, PosZ, s=sizes, color=plt.cm.viridis(norm(colors)))
ax2.set_xticks(ax1.get_xticks())
ax2.set_xlabel('y-position [c kpc/h]')
ax2.set_ylabel('z-position [c kpc/h]')

ax3 = fig.add_subplot(gs[1, 0])
im3 = ax3.scatter(PosX, PosZ, s=sizes, color=plt.cm.viridis(norm(colors)))
ax3.set_xlabel('x-position [c kpc/h]')
ax3.set_ylabel('z-position [c kpc/h]')

# Colorbar in the bottom-right 
cbar_ax = fig.add_subplot(gs[1, 1])
cbar = fig.colorbar(im3, cax=cbar_ax, norm=norm, cmap=plt.cm.bwr(norm(colors)), label='Dark Matter Mass 10^10 [Msun]')	#should use bwr to scale colors but is broken due to special colorbar positioning and displays only viridis. Either leave blank space or keep viridis colorcoding feature TBA

cbar.set_ticks([np.min(norm(colors)), np.max(norm(colors))])  # Set ticks to the range of scaled color values
cbar.set_ticklabels([f'{np.min(DMMass):.2f}', f'{np.max(DMMass):.2f}'])  # Labels for actual DMMass values

fig.tight_layout(rect=[0, 0, 0.90, 1])  # Adjust layout to leave space for the colorbar
plt.show()

#----------------------------------------BH vs Stellar mass------------------------------------------------------


limMass = BHMass >= 8e-5		

BHMass2 = np.extract(limMass, BHMass) 		#filter only points with BHMass > 8e-5
StMass2 = np.extract(limMass, StMass)

sorted_indices = np.argsort(StMass2)		#sorting for fitting purpouses
StMass1 = np.sort(StMass2) 
BHMass1 = [BHMass2[i] for i in sorted_indices] 

coeffs1 = np.polyfit(StMass1, BHMass1, deg=1, rcond=None, full=False, w=None, cov=False)	#coefficients for linear fitting 
p1 = np.poly1d(coeffs1)

m, q = coeffs
m = round(m, 2)
q = round(q, 2)

print (coeffs1)

plt.scatter(StMass1, BHMass1, c='orchid', edgecolors='black', marker='.', s=150)
plt.xlabel('Stellar Mass 10^10[Msun]')
plt.ylabel('Black Hole Mass 10^10[Msun]')
plt.plot(StMass1, p1(StMass1), label='fit y={0}x {1}'.format(m, q))

#plt.xscale('log')		#log scale looks bad since q coefficient is negative resulting in -inf after the first points
#plt.yscale('log')
plt.title(label='Most massive black hole masses - Stellar mass relation')

plt.legend()
plt.show()	

#-----------------------------------------2D mass-distance histogram-----------------------------------------------

ind = np.argpartition(GasMass, -5)[-5:]
dist = np.zeros((len(ind), len(PosX)))	

for i in range(len(ind)):
	dist[i] = distance(PosX, PosY, PosZ, ind[i])

dist_flat = dist.flatten()
TotMass_flat = np.repeat(TotMass, len(ind)) 
TotMass_flat = TotMass_flat * 1e10
plt.figure(figsize=(16,8))

x_bins = np.logspace(np.log10(min(TotMass_flat)), np.log10(max(TotMass_flat)), 50)
y_bins = np.linspace(min(dist_flat), max(dist_flat), 50)

plt.hist2d(TotMass_flat, dist_flat, bins=[x_bins, y_bins], cmap='Purples')

plt.xscale('log')
plt.colorbar()
plt.xlabel('Gas Mass 10^10 Msun')
plt.ylabel('Distance from most massive 5 objects [c kpc/h]')
plt.title(label='Cumulative 2D histogram of distance from most massive 5 - total mass')

plt.show()

