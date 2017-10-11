import numpy as np

Radcliffe_A = 2800 #collecting area (cm^2)
Radcliffe_T = 0.35 #combined transmission efficiency
Radcliffe_eta = 0.55 #CCD quantum efficiency
Radcliffe_deltalambda = 1000 #bandwidth of filter/spectograph per pixel (Å)
Radcliffe_s_sky = 10 #sq. arcsec
Radcliffe_n_pix = 20 #pixels

Allen_A = 2800 #collecting area (cm^2)
Allen_T = 0.01 #combined transmission efficiency
Allen_eta = 0.8 #CCD quantum efficiency
Allen_deltalambda = 0.6 #bandwidth of filter/spectograph per pixel (Å)
Allen_s_sky = 3 #sq. arcsec
Allen_n_pix = 7 #pixels

F_vega = 1000 #vega photon flux (photons/sec/cm^2/Å)
m_sky = 17 #V sky magnitude per square arcsecond
N_dark = 0.2 #dark current flux (electron/sec/pixel)


k = 0.2 #extinction coefficient
X = 1.5 #airmasses
a = 10**(-0.4*k*X)


def RadcliffeSourceFlux(m_s):
    '''Returns source flux when magnitude is inputted'''
    F_s = F_vega * (10**(-0.4*m_s))
    Radcliffe_flux = float(F_s * a * Radcliffe_A * Radcliffe_T * Radcliffe_eta * Radcliffe_deltalambda)
    return Radcliffe_flux

print("The Radcliffe source flux, Ṅ_s, for star of magnitude 8 is", RadcliffeSourceFlux(8) ,"photons/sec")
print("The Radcliffe source flux, Ṅ_s, for star of magnitude 13 is", RadcliffeSourceFlux(13) ,"photons/sec")
print("The Radcliffe source flux, Ṅ_s, for star of magnitude 18 is", RadcliffeSourceFlux(18) ,"photons/sec")

def AllenSourceFlux(m_s):
    '''Returns source flux when magnitude is inputted'''
    F_s = F_vega * (10**(-0.4*m_s))
    Allen_flux = float(F_s * a * Allen_A * Allen_T * Allen_eta * Allen_deltalambda)
    return Allen_flux

print("\n") #line break

print("The Allen source flux, Ṅ_s, for star of magnitude 3 is", AllenSourceFlux(3) ,"photons/sec")
print("The Allen source flux, Ṅ_s, for star of magnitude 6 is", AllenSourceFlux(6) ,"photons/sec")
print("The Allen source flux, Ṅ_s, for star of magnitude 8 is", AllenSourceFlux(8) ,"photons/sec")

print("\n") #line break
##########################################
SkyFluxRadcliffe = F_vega * (10**(-0.4*m_sky))* Radcliffe_A * Radcliffe_T * Radcliffe_eta * Radcliffe_deltalambda * Radcliffe_s_sky
DarkFluxRadcliffe = N_dark * Radcliffe_n_pix
RadcliffeBackgroundFlux = SkyFluxRadcliffe + DarkFluxRadcliffe   

SkyFluxAllen = F_vega * (10**(-0.4*m_sky))* Allen_A * Allen_T * Allen_eta * Allen_deltalambda * Allen_s_sky
DarkFluxAllen = N_dark * Allen_n_pix
AllenBackgroundFlux = SkyFluxAllen + DarkFluxAllen 
    
print("Radcliffe background flux, Ṅ_B, is" , RadcliffeBackgroundFlux , "photons/sec")
print("Allen background flux, Ṅ_B, is" , AllenBackgroundFlux , "photons/sec")
##########################################

def Radcliffe_SNR(m_s , t):
    '''Outputs SNR given input exposure time and target V mag'''
    R_SNR = (RadcliffeSourceFlux(m_s)*t)/(((RadcliffeSourceFlux(m_s)*t)+(2*RadcliffeBackgroundFlux*t))**0.5)
    return R_SNR

print("\n") #break line

print("Radcliffe SNR of 100s exposure of a magnitude 8 target = " , Radcliffe_SNR(8,100))
print("Radcliffe SNR of 100s exposure of a magnitude 13 target = " , Radcliffe_SNR(13,100))
print("Radcliffe SNR of 100s exposure of a magnitude 18 target = " , Radcliffe_SNR(18,100))

##########################################

print("\n")

def RadcliffeExposureTime(m_s , SNR):
    '''Outputs required exposure time given target mag and desired SNR'''
    ExpTime = ((RadcliffeSourceFlux(m_s) + (2*RadcliffeBackgroundFlux))*SNR**2)/(RadcliffeSourceFlux(m_s)**2)
    return ExpTime

print("Radcliffe exposure time required to detect a V = 18 source at an SNR of 10 =" , RadcliffeExposureTime(18,10) , "s")
print("The uncertainty in measured V magnitude will be approximately 0.1 (reciprocal of SNR).")
