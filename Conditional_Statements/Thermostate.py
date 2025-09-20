# smart thermostate system 

device_status = "active"
temperature = 35

if device_status == 'active':
    if(temperature>=35):
        print('Temperature is high')
    else:
        print('Temperature is Normal')
else:
    print('Sataus of device is off')