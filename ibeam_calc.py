from typing import List
import numpy as np


def ibeam(sigma: float, 
          force_applied: float, 
          beam_thick: float, 
          distances: List[float]):
    
    tol = 2.0 # tolerance for the system (how close we want our desired shear modulus to be to the limit)
    
    height_vals = np.arange(1, 1001-2*beam_thick, step=1) # Height of I-beam (mm)
    width_vals  = np.arange(1, 1001-2*beam_thick, step=1) # width of I-beam (mm)

    return_data_dict = {}
    return_data_list = []
    for distance in distances:
        width_data = []
        
        for height in height_vals:
            row_data = []
        
            for width in width_vals:
                # calculating moment (Nmm)
                moment_Nm = force_applied * distance

                # calculating shear modulus based on given conditions
                zShear = moment_Nm / sigma

                # calculating XSA for each height/w combination   
                xsa = 2*beam_thick*width + beam_thick*height 

                # calculating ix (i.e. inertia of rotation about the x-axis) for each h/w combination
                ix = (beam_thick*height**3)/12 + (width/12) * ((2*beam_thick+height)**3 - height**3) 

                # calculating neutral axis for each h combination 
                y = height/2 + beam_thick

                # calculating zInt for each Ix/y combination
                zInt = ix / y

                # check to see if zInt <= zShear or >= tol * zShear since this is not ideal
                if zInt <= zShear or zInt >= tol * zShear:
                    zInt = 0

                # Creating the relationship between zInt and XSA
                geom = round(zInt /  xsa, 2)

                row_data.append([height, width, distance, geom])
            
            width_data.extend(row_data)
        
        # max geom value determines optimal height and width
        max_row = max(width_data, key=lambda x: x[-1]) 
        
        return_data_dict = {
            "height" : max_row[0],
            "width" : max_row[1],
            "distance" : max_row[2],
        }
        return_data_list.append(return_data_dict)

    return return_data_list 