import json
import numpy as np

""" Parameters """
with open('parameters.json') as f:
    params = json.load(f)

NAME = params['Solution_Name']

# Physical
fixed_end = params['Physical_Parameters']['fixed_end']
speed = params['Physical_Parameters']['speed_of_wave']


# Solution Parameters
k = params['Initial_Conditions']['Initial_Profile']['Inclination_of_wave']
h = params['Initial_Conditions']['Initial_Profile']['Width_of_wave']
init_x = params['Initial_Conditions']['Initial_Profile']['Init_pos']

# Function psi_func(x)


if params['Initial_Conditions']['Initial_Speed']['psi_func'] == "0":
    psi_func = lambda x: 0
else:
    psi_func = lambda x: eval(params['Initial_Conditions']['Initial_Speed']['psi_func'])



# Animation
FPS = params['Animation_Parameters']['FPS']
L = params['Animation_Parameters']['max_x']
num_x = params['Animation_Parameters']['num_x']
max_t = params['Animation_Parameters']['max_t']
num_t = params['Animation_Parameters']['num_t']
integral_step = params['Animation_Parameters']['integral_step']

# Function phi_func(x)
def phi_func(x: float) -> float:
    return (np.abs(k*(x-init_x) - h)+np.abs(k*(x-init_x) + h) - 2*k*np.abs((x-init_x)))/2
