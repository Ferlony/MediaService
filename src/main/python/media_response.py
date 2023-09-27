from stat import S_ISREG

from aiofiles import os, threadpool
from starlette.responses import (FileResponse, Scope, Receive, Send)


class MediaResponse(FileResponse):
    def __init__(self, *args, **kwargs):
        self.offset = kwargs.pop('offset')
        super(MediaResponse, self).__init__(*args, **kwargs)

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        if self.stat_result is None:
            try:
                stat_result = await os.stat(self.path)
                self.set_stat_headers(stat_result)
            except FileNotFoundError:
                raise RuntimeError(f"File at path {self.path} does not exist.")
            else:
                mode = stat_result.st_mode
                if not S_ISREG(mode):
                    raise RuntimeError(f"File at path {self.path} is not a file.")
        await send(
            {
                "type": "http.response.start",
                "status": self.status_code,
                "headers": self.raw_headers,
            }
        )
        if self.send_header_only:
            await send({"type": "http.response.body", "body": b"", "more_body": False})
        else:
            async with threadpool.open(self.path, mode='rb') as file:
                await file.seek(self.offset)
                more_body = True
                while more_body:
                    chunk = await file.read(self.chunk_size)
                    more_body = len(chunk) == self.chunk_size
                    await send(
                        {
                            "type": "http.response.body",
                            "body": chunk,
                            "more_body": more_body,
                        }
                    )
        if self.background is not None:
            await self.background()
