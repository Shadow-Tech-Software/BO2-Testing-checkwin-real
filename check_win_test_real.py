import asyncio

from BinaryOptionsToolsV2.pocketoption import PocketOptionAsync


# Main part of the code
async def main(ssid: str):
    # The api automatically detects if the 'ssid' is for real or demo account
    api = PocketOptionAsync(ssid)
    await asyncio.sleep(5)
    while True:
        input("Press Enter to make a buy and sell trade with check_win=False and then check the results with api.check_win()")
        (buy_id, _) = await api.buy(
            asset="EURUSD_otc", amount=1.0, time=5, check_win=False
        )
        print(buy_id)
        # This is the same as setting checkw_win to true on the api.buy and api.sell functions
        buy_data = await api.check_win(buy_id)
        print(f"Buy trade result: {buy_data['result']}\nBuy trade data: {buy_data}")


if __name__ == "__main__":
    ssid = input("Please enter your ssid: ")
    asyncio.run(main(ssid))

