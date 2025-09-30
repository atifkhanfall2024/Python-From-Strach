colors  = [
    "grey blue",
    "black brown",
    "black berry" ,
    "dark white"
]

# suppose i want to pick all black combination

pick_black_combinations = [pick for pick in colors if "black" in pick]

print(pick_black_combinations)