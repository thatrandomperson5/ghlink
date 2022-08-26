import github
import asyncio

async def main():
  client = await github.GHClient()

  user = await client.get_user(user='Github Actions')

  print(user)
  print(user.html_url)

asyncio.run(main())
