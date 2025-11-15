import asyncio, logging
from bleak import BleakClient

logging.basicConfig(level=logging.DEBUG)
async def main():
    ble_targ = input("<Enter MAC>: ")
    async with BleakClient(ble_targ) as client:
        # read/write operations here
        print("Connected to BLE device")
        print(client.is_connected)

asyncio.run(main())
