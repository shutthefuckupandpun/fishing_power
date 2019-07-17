import pandas as pd
import math as math

file = r'fishing_table.csv'
master_list = pd.read_csv(file)

#Splits csv into respective data sets, drops unecessary coumns, resets indexes per data set
fishing_pole_list = master_list[master_list['type'].str.match('pole')].drop(['type'], axis=1).reset_index(inplace = False, drop = True)
bait = master_list[master_list['type'].str.match('bait')].drop(['type'], axis=1).reset_index(inplace = False, drop = True)
time_of_day = master_list[master_list['type'].str.match('time')].drop(['type'], axis=1).reset_index(inplace = False, drop = True)
moon_phase = master_list[master_list['type'].str.match('moon')].drop(['type'], axis=1).reset_index(inplace = False, drop = True)
weather = master_list[master_list['type'].str.match('weather')].drop(['type'], axis=1).reset_index(inplace = False, drop = True)

#Calculate Gear Equipped
clothing = int(input("How many peices of fishing clothing are you wearing? 0-3: "))*5
ear_power = int(input("Using Angler Earring?" + " No = 0 "+"| "+"Yes = 1 :"))
if ear_power == 1:
      ear_power = 10
else:
      pass
bag_power = int(input("Using Tackel Bag?" + " No = 0 "+"| "+"Yes = 1 :"))
if bag_power == 1:
      bag_power = 10
else:
      pass
potion_power = int(input("Using fishing potion?" + " No = 0 "+"| "+"Yes = 1 :"))
if potion_power == 1:
      potion_power = 15
else:
      pass


"""Begin Fishing Pole Pull"""
print(fishing_pole_list) #prints list for user to pick from
fishing_pole_pick = int(input("Enter pole in use: ")) #prompt user for pick
pole_power = fishing_pole_list.loc[fishing_pole_list.index == fishing_pole_pick, "power"].iloc[0] #gets power value in table based on user input

"""Begin Bait Pull"""
print(bait) #prints list for user to pick from
bait_pick = int(input("Enter bait in use: ")) #prompt user for pick
bait_power = bait.loc[bait.index == bait_pick, "power"].iloc[0]

"""Begin Time Pull"""
print(time_of_day) #prints list for user to pick from
time_pick = int(input("Enter time frame: ")) #prompt user for pick
time_power = time_of_day.loc[time_of_day.index == time_pick, "power"].iloc[0]

"""Begin Moon Pull"""
print(moon_phase) #prints list for user to pick from
moon_pick = int(input("Enter moon phase: ")) #prompt user for pick
moon_power = moon_phase.loc[moon_phase.index == moon_pick, "power"].iloc[0]

"""Begin Weather Pull"""
print(weather) #prints list for user to pick from
weather_pick = int(input("Enter weather: ")) #prompt user for pick
weather_power = weather.loc[weather.index == weather_pick, "power"].iloc[0]

"""Maths to calculate final fishing power"""
fishing_power = math.floor(clothing + pole_power + bait_power + potion_power + bag_power + ear_power)*(1+weather_power)*(1+time_power)*(1+moon_power)
#fishing_power = math.floor(clothing + pole_power + bait_power + potion_power) + ((clothing + pole_power + bait_power) * weather_power) + ((clothing + pole_power + bait_power) * time_power) + ((clothing + pole_power + bait_power) * moon_power)

print("Clothing power:", int(clothing),
      "\nBag power:", int(bag_power),
      "\nEar power:", int(ear_power),
      "\nPole power:", int(pole_power),
      "\nBait power:", int(bait_power),
      "\nTime power:", int(time_power*100),"%",
      "\nMoon power:", int(moon_power*100),"%",
      "\nWeather power:", int(weather_power*100),"%",
      "\nPotion power:", int(potion_power),
      "\n\nYour fishing power is: ", int(fishing_power))