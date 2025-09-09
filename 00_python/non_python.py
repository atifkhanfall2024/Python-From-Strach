
# how to make chai ??

def make_chai():
    if not has_kettle():
        fill_kettle()
    plug_in_kettle()
    boil_water()

    if not clean_cups():
        clean_cups()
        pour_boil_water_to_cup()
        add_to_cup("tea leaves")
        add_to_cup("suger")
        pour('boil water')
        stie('cup')
        serve("chai or tea ")
