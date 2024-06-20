from telegraph.aio import Telegraph
import asyncio

class Picsum:
    def __init__(self, token : str) -> None:
        self.tel = Telegraph(access_token = token)
        self.n = 1

    async def get_photo_poster_url(self, path : str) -> str:
       data = await self.tel.upload_file(path)
       if data:
           id = data[0].get('src')
           if id:
               return f"https://telegra.ph{id}"
            

if __name__ == '__main__':
    pass
    # pic = Picsum("Token")
    # asyncio.run(pic.get_photo_poster_url('data/photos/photo1.jpg'))
