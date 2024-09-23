import pygame as py
import initials
import numpy as np



def photon_frequency_in_obs_system():
    if initials.x_velocity >0:
        initials.obsfreq = initials.idiofreq*(np.sqrt((1+initials.x_velocity)/(1-initials.x_velocity)))
    if initials.x_velocity < 0:
        initials.obsfreq = initials.idiofreq * (np.sqrt((1-np.abs(initials.x_velocity)) / (1+np.abs(initials.x_velocity))))

def color_in_obsosystem():
    if initials.obsfreq < 476*pow(10,12) and initials.obsfreq >= 429*pow(10,12):
        initials.obscolor='red'
    elif initials.obsfreq < 510*pow(10,12) and initials.obsfreq >= 476*pow(10,12):
        initials.obscolor='orange'
    elif initials.obsfreq < 535*pow(10,12) and initials.obsfreq >= 510*pow(10,12):
        initials.obscolor='yellow'
    elif initials.obsfreq < 600*pow(10,12) and initials.obsfreq >= 535*pow(10,12):
        initials.obscolor='green'
    elif initials.obsfreq < 680*pow(10,12) and initials.obsfreq >= 600*pow(10,12):
        initials.obscolor='blue'
    elif initials.obsfreq < 750*pow(10,12) and initials.obsfreq >= 680*pow(10,12):
        initials.obscolor='violet'
    else:
        initials.obscolor=(0,0,0)