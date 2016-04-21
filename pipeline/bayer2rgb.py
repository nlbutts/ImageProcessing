import numpy as np
import cv2

x=np.fromfile('/media/ztemp/snap_1_32_600.raw', dtype='uint16')
y=np.reshape(x, (1944,2592))
z=cv2.cvtColor(y, cv2.COLOR_BayerRG2BGR)

#White balance
mt=np.mean(z)
mb=np.mean(z[:,:,0])
mg=np.mean(z[:,:,1])
mr=np.mean(z[:,:,2])
z[:,:,0] = z[:,:,0] * mt/mb
z[:,:,1] = z[:,:,1] * mt/mg
z[:,:,2] = z[:,:,2] * mt/mr

#Gamma correct
gamma=0.5
bs16=np.linspace(0, 1, 4096)
bs8=bs16**gamma*255
gamma_corrected = bs8[z]

#Convert to 8bpp and save
rgb8=gamma_corrected.astype('uint8')
cv2.imwrite('/media/ztemp/rgb.tif', rgb8)
