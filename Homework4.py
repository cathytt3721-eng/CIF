weatherlist = [
    ["Sunday",[0, -4,"Snowing"]],
    ["Monday",[-2,-4,"Mix of sun and clouds"]],
    ["Tuesday",[2,-3, "A mix of sun andd clound with a changes of snow"]],
    ["Wednesday",[6,2,"Raining"]],
    ["Thursday",[6,-2, "Chance of shower"]],
    ["Friday",[4,-3, "Mainly sunny"]],
    ["Saturday",[2,-3, "Cloudy with a chance of rain"]],
]

print("Weather forecast from Nov 9 to Nov 15")

for day in weatherlist:
    print(f"{day[0]}: high = {day[1][0]}°C, low = {day[1][1]}°C, the weather is {day[1][2]}")