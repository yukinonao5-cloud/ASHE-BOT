import os
import discord
from discord.ext import commands

# =========================
# 기본 설정
# =========================

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(
    command_prefix="!",
    intents=intents
)

# 자기소개 채널 이름
INTRO_CHANNEL_NAME = "💬・自己紹介・자기소개"

# 자기소개 양식
INTRO_MESSAGE = """╭────────────── ✦ ──────────────╮
        ❄️ 自己紹介・자기소개
╰────────────── ✦ ──────────────╯

🎭 性別・성별 :
🎮 LoL ID・롤 아이디 :
🏆 ティア・티어 :
🌏 主なサーバー・주 서버 :
🎯 主なポジション・주 포지션 :
⭐ メインチャンピオン・주 챔피언 :

✦ コピーして記入してください！
✦ 복사해서 작성해주세요!"""


# =========================
# 봇이 켜졌을 때
# =========================

@bot.event
async def on_ready():
    print(f"애쉬봇 로그인 완료! {bot.user}")

    for guild in bot.guilds:
        channel = discord.utils.get(
            guild.text_channels,
            name=INTRO_CHANNEL_NAME
        )

        if channel:
            await channel.send(INTRO_MESSAGE)
            print(f"자기소개 양식 전송 완료: {guild.name}")


# =========================
# 메시지가 올라왔을 때
# =========================

@bot.event
async def on_message(message):

    # 봇이 보낸 메시지는 무시
    if message.author.bot:
        return

    # 자기소개 채널에서 메시지가 올라오면
    # 양식을 다시 아래쪽에 보냄
    if message.channel.name == INTRO_CHANNEL_NAME:
        await message.channel.send(INTRO_MESSAGE)

    # 명령어 작동을 위해 필요
    await bot.process_commands(message)


# =========================
# 봇 로그인
# =========================

token = os.getenv("DISCORD_TOKEN")

if not token:
    print("❌ DISCORD_TOKEN을 찾을 수 없습니다.")
else:
    bot.run(token)