import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt 
import time

def space():
    print("\n\n")
    print("-".center(50,"-"))
    time.sleep(1)

def domains():
    # here we assume the various fuzzy domains as:-

    """ 
    soil moisture can be defined in the range [0, 100], where 0 represents completely dry soil and 100 represents fully saturated soil
    type of soil can be defined as a linguistic variable with three membership functions: "Clayey", "Loamy", and "Sandy"
    type of crop can be defined as a linguistic variable with three membership functions: "Low-water crops", "Medium-water crops", and "High-water crops"
    type of weather can be defined as a linguistic variable with three membership functions: "Dry", "Moderate", and "Wet".
     
    """

    soil_moisture = soil()
    type_soil = t_soil()
    type_crop = t_crop()
    type_weather = t_weather()

    '''
    now we define fuzzy rules that will control the pump based on the conditions that we have. 
    These can be as follows->

    r1 -> If soil moisture is Dry and type of soil is Sandy, then pump = 1 (full power)
    r2 -> If soil moisture is Wet and type of crop is Low-water crops, then pump = 0.2
    r3 -> If soil moisture is Moist and type of weather is Wet, then pump = 0.5
    r4 -> If type of soil is Clayey and type of weather is Dry, then pump = 0.7 
    '''

    print("\nAccording to your inputs:\n\nsoil moisture:",soil_moisture,"\ntype of soil:",type_soil,"\ntype of crop:",type_crop,"\ntype of weather:",type_weather,"\n\n")

    power = 0.0
    # rule 1
    if soil_moisture <= 20 and (type_soil == "Sandy" or type_weather == "D"):
        power = 1.0
        print("Rule 1 got triggered")
    # rule 2
    elif soil_moisture >= 80 and type_crop == "L":
        power = 0.2
        print("Rule 2 got triggered")
    # rule 3
    elif 20 < soil_moisture < 80 and type_weather == "W" and type_soil == "Loamy":
        power = 0.5
        print("Rule 3 got triggered")
    # rule 4
    elif type_soil == "Clayey" and type_weather == "D":
        power = 0.7
        print("Rule 4 got triggered")
    else:
        # default power of pump
        power = 0.5
        print("Pump runs on default setting")
    print("Pump is running with power = ", end="")
    return power


def soil():
    while True:
        s = int(input("\n0 represents completely dry soil and 100 represents fully saturated soil\n\nEnter value between 0 to 100: "))
        if 0 <= s <= 100:
            space()
            break
        else:
            print("\nInvalid input\n\n")
    return s

def t_soil():
    while True:
        t = str(input("\nClayey Loamy or Sandy\n\nEnter type of soil: "))
        if t in ["Clayey", "Loamy", "Sandy"]:
            space()
            break
        else:
            print("\nInvalid input\n\n")
    return t

def t_crop():
    while True:
        c = str(input("\nLow-water crops(L), Medium-water crops(M) and High-water crops(H)\n\nEnter type of crop: "))
        if c in ["L","M","H"]:
            space()
            break
        else:
            print("\nInvalid input\n\n")
    return c

def t_weather():
    while True:
        w = str(input("\nDry(D), Moderate(M) and Wet(W)\n\nEnter type of weather: "))
        if w in ["D","M","W"]:
            space()
            break
        else:
            print("\nInvalid input\n\n")
    return w


def plotting():
     # range of soil moisture
    soil_moisture = np.arange(0, 100, 1)  

    # membership function for soil moisture factors
    low = fuzz.trimf(soil_moisture, [0, 0, 50])
    medium = fuzz.trimf(soil_moisture, [0, 40, 90]) 
    high = fuzz.trimf(soil_moisture, [0, 50, 100]) 
    
    # range of type of soil
    type_soil = np.arange(0, 12, 1)  

    # membership function for type of soil factors
    Clayey = fuzz.trimf(type_soil, [0, 5, 11])
    Loamy = fuzz.trimf(type_soil, [0, 0, 5]) 
    Sandy = fuzz.trimf(type_soil, [0, 2, 7]) 

    # range of type of crop
    type_crop = np.arange(0, 12, 1)  

    # membership function for type of crop factors
    Low_water = fuzz.trimf(type_crop, [0, 2, 11])
    Medium_water = fuzz.trimf(type_crop, [5, 9, 11]) 
    High_water = fuzz.trimf(type_crop, [0, 0, 7]) 

    # range of weather
    weather = np.arange(0, 12, 1)  

    # membership function for weather
    dry = fuzz.trimf(weather, [0, 0, 9])
    moderate = fuzz.trimf(weather, [3, 3, 11]) 
    wet = fuzz.trimf(weather, [0, 3, 5]) 

    fig, (ax0,ax1,ax2, ax3) = plt.subplots(nrows=4, figsize=(12, 7))

    ax0.plot(soil_moisture, low, 'b', linewidth=1.5, label='Low')  
    ax0.plot(soil_moisture, medium, 'g', linewidth=1.5, label='Medium')  
    ax0.plot(soil_moisture, high, 'r', linewidth=1.5, label='High')  
    ax0.set_title('Soil Moisture')  
    ax0.legend()  
    
    ax1.plot(type_soil, Clayey, 'b', linewidth=1.5, label='Clayey')  
    ax1.plot(type_soil, Loamy, 'g', linewidth=1.5, label='Loamy')  
    ax1.plot(type_soil, Sandy, 'r', linewidth=1.5, label='Sandy')  
    ax1.set_title('Type of Soil')  
    ax1.legend()  
        
    ax2.plot(type_crop, Low_water, 'b', linewidth=1.5, label='Low_water')  
    ax2.plot(type_crop, Medium_water, 'g', linewidth=1.5, label='Medium_water')  
    ax2.plot(type_crop, High_water, 'r', linewidth=1.5, label='High_water')  
    ax2.set_title('Type of Crop')  
    ax2.legend()  

    ax3.plot(weather, dry, 'b', linewidth=1.5, label='Dry')  
    ax3.plot(weather, moderate, 'g', linewidth=1.5, label='Moderate')  
    ax3.plot(weather, wet, 'r', linewidth=1.5, label='Wet')  
    ax3.set_title('Weather')  
    ax3.legend()  
        
    for ax in (ax0,ax1):
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.get_xaxis().tick_bottom()
        ax.get_yaxis().tick_left()
        plt.tight_layout()
    
    plt.show()
    space()

def main():

    plotting()

    pump_power = domains()

    print(pump_power)

space()
main()