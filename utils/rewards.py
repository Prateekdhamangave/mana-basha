import random

# 🎯 Define possible badges for each type
BADGES = {
    "story": [
        {"badge_name_tel": "కథ చెబుడు వీరుడు", "badge_emoji": "📖", "points": 10},
        {"badge_name_tel": "ఊరిపాటల పరుగు", "badge_emoji": "🗣️", "points": 8}
    ],
    "recipe": [
        {"badge_name_tel": "అమ్మవంటి వంటవాడు", "badge_emoji": "🍲", "points": 10},
        {"badge_name_tel": "రుచి రాజు", "badge_emoji": "🍛", "points": 8}
    ],
    "meme": [
        {"badge_name_tel": "మీమ్ మాస్టర్", "badge_emoji": "😂", "points": 6},
        {"badge_name_tel": "తెలుగు ట్రోలర్", "badge_emoji": "🤣", "points": 5}
    ],
    "art": [
        {"badge_name_tel": "శిల్ప కళాకారుడు", "badge_emoji": "🎨", "points": 10},
        {"badge_name_tel": "గ్రామ కళాకారుడు", "badge_emoji": "🖌️", "points": 8}
    ]
}

# 🎉 Reward function
def award_user(content_type):
    if content_type not in BADGES:
        return {"badge_name_tel": "సహభాగిత బొమ్మ", "badge_emoji": "🎁", "points": 5}
    return random.choice(BADGES[content_type])
