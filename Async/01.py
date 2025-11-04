# working with async io
# it execute the code in async fasion

import asyncio

async def Prapare_chai():
    print('Chai is on Fire wait ......')

    await asyncio.sleep(3)
    print('Your Chai is Ready')

asyncio.run(Prapare_chai())