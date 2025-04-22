

from TikTokApi import TikTokApi
import asyncio

async def fetch_user_info(username: str):
    async with TikTokApi() as api:
        user = await api.user(username=username)
        return {
            "id": user.id,
            "unique_id": user.unique_id,
            "nickname": user.nickname,
            "signature": user.signature,
            "verified": user.verified,
            "follower_count": user.follower_count,
            "following_count": user.following_count,
            "heart_count": user.heart_count,
            "video_count": user.video_count,
            "avatar_url": user.avatar_thumb_url
        }

if __name__ == "__main__":
    username = "example_user"  # replace with the TikTok handle you want
    info = asyncio.run(fetch_user_info(username))
    print("TikTok User Info:")
    for key, val in info.items():
        print(f"{key}: {val}")
