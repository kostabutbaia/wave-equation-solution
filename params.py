import json
import numpy as np

""" Parameters """
with open('parameters.json') as f:
    params = json.load(f)

NAME = params['Solution_Name']
graph_ylim = params['Animation_Parameters']['graph_ylim']

# Physical
fixed_end = params['Physical_Parameters']['fixed_end']
speed = params['Physical_Parameters']['speed_of_wave']

# Function psi_func(x)
if not params['Initial_Conditions']['Initial_Speed']['use_custom']:
    width = params['Initial_Conditions']['Initial_Speed']['width']
    height = params['Initial_Conditions']['Initial_Speed']['height']
    init_pos = params['Initial_Conditions']['Initial_Speed']['init_pos']
    psi_func = lambda x: 0 if x <= init_pos - width/2 or x >= init_pos + width/2 else height
elif params['Initial_Conditions']['Initial_Speed']['custom_psi_func'] == '0':
    psi_func = lambda x: 0
else:
    psi_func = lambda x: eval(params['Initial_Conditions']['Initial_Speed']['custom_psi_func'])


# Animation
FPS = params['Animation_Parameters']['FPS']
L = params['Animation_Parameters']['max_x']
num_x = params['Animation_Parameters']['num_x']
max_t = params['Animation_Parameters']['max_t']
num_t = params['Animation_Parameters']['num_t']
integral_step = params['Animation_Parameters']['integral_step']

# Function phi_func(x)
if not params['Initial_Conditions']['Initial_Profile']['use_custom']:
    k = params['Initial_Conditions']['Initial_Profile']['Inclination_of_wave']
    h = params['Initial_Conditions']['Initial_Profile']['Width_of_wave']
    init_x = params['Initial_Conditions']['Initial_Profile']['init_pos']
    phi_func = lambda x: (np.abs(k*(x-init_x) - h)+np.abs(k*(x-init_x) + h) - 2*k*np.abs((x-init_x)))/2
elif params['Initial_Conditions']['Initial_Profile']['custom_phi_func'] == '0':
    phi_func = lambda x: 0
else:
    phi_func = lambda x: eval(params['Initial_Conditions']['Initial_Profile']['custom_phi_func'])
