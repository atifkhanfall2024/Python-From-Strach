# here we will be talking about error handling

menu = {"Drinks" :"Chai" ,"Meal": "Parata" ,"Fresh" :"Samosa" ,"Hot": "pikora"}

try:
 menu["aloparata"]

except KeyError:
 print("This Key that you are Access are not present")

print("Come For Tea Rainy Day")