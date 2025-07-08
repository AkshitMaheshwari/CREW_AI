from crewai_tools import YoutubeChannelSearchTool
import time
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import YouTubeRequestFailed

class SafeYoutubeTool(YoutubeChannelSearchTool):
    def run(self, query: str, max_results=3):  
        print(f"🔍 Searching for videos with topic: {query}")
        try:
            videos = super().run(query)
            safe_videos = []
            for video in videos[:max_results]:
                try:
                    video_id = video['url'].split("v=")[-1]
                    transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=["en"])
                    video['transcript'] = transcript
                    safe_videos.append(video)
                    time.sleep(5)  
                except YouTubeRequestFailed as e:
                    print(f"Transcript not available or rate limit hit for {video['url']}: {e}")
                except Exception as e:
                    print(f"Unexpected error for {video['url']}: {e}")
            return safe_videos
        except Exception as e:
            print(f" Youtube tool error: {e}")
            return []

yt_tool = SafeYoutubeTool(youtube_channel_handle="@campusx-official")
