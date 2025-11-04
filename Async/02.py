# now check this that how it can handle multiple request
# now i see that if multpile request come then it will exectue in non blocking way
import asyncio
import logging

async def Prapare_chai(name:str):
    try:
        print(f'Order for {name} chai ')
        logging.info('Waiting......')
        await asyncio.sleep(3)
        print(f'Your Oder for {name} is Ready')
    except Exception as e:
        print(f'Got Some Error {e} ')

async def main():
    await asyncio.gather(
        Prapare_chai('Green'),
        Prapare_chai('Hot')
    )
asyncio.run(main())