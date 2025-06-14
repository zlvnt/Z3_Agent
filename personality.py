import json
from config import PERSONALITY_PATH

def load_personality(path=PERSONALITY_PATH):
    with open(path, "r") as f:
        data = json.load(f)
    return data

def get_identity(personality):
    return personality.get("identity", {})

def get_tone(personality, tone_key):
    return personality.get("tone", {}).get(tone_key)

def get_rules(personality):
    return personality.get("rules", {})

def get_prompt(personality, prompt_type="caption"):
    return personality.get("prompts", {}).get(prompt_type, "")

def get_posts(personality):
    return personality.get("posts", [])

def get_post_by_id(personality, post_id):
    for post in personality.get("posts", []):
        if post.get("post_id") == post_id:
            return post
    return None

def get_caption_by_post_id(personality, post_id):
    post = get_post_by_id(personality, post_id)
    if post:
        return post.get("caption", "")
    return ""

