import asyncio
from notebooklm import NotebookLMClient
from notebooklm.rpc.types import artifact_status_to_str

NOTEBOOK_ID = '461907ec-55c9-4713-9b5c-dc540a312702'

async def main():
    async with await NotebookLMClient.from_storage() as client:
        videos = await client.artifacts.list_video(NOTEBOOK_ID)
        print('found', len(videos), 'video artifacts')
        for v in videos:
            vid = getattr(v, 'id', None) or getattr(v, 'artifact_id', None)
            status = getattr(v, 'status', None)
            print('artifact', vid)
            print('  title', getattr(v, 'title', None))
            print('  status', status, artifact_status_to_str(status))
            print('  url', getattr(v, 'url', None))
            print('  created_at', getattr(v, 'created_at', None))
            print('---')

asyncio.run(main())
