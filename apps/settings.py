import os
from pathlib import Path

# icons
AI_ICON = "ai_icon"
USER_ICON = "user_icon"
CHAT_ICON = "chat-icon"

# css classes
CHAT_ROW = "chat-row"
ROW_REVERSE = "row-reverse"
CHAT_BUBBLE = "chat-bubble"
AI_BUBBLE = "ai-bubble"
HUMAN_BUBBLE = "human-bubble"

# files & dirs
BASE_DIR = ROOT_DIR = str(Path(os.getcwd()).resolve())
STATIC_DIR = BASE_DIR + "/static"
IMAGES_DIR = STATIC_DIR + "/images"
CHAT_ICON_PATH = "{}.png"
APP_HTML = STATIC_DIR + "/app.js"
