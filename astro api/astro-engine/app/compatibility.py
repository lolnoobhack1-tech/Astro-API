from typing import Dict, Any

# ==========================================
# 1. PARĀŚARA CONSTANTS (STRICT)
# ==========================================

RASHI_ORDER = [
    "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
    "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"
]

NAKSHATRA_ORDER = [
    "Ashwini", "Bharani", "Krittika", "Rohini", "Mrigashira", "Ardra",
    "Punarvasu", "Pushya", "Ashlesha", "Magha", "Purva Phalguni", "Uttara Phalguni",
    "Hasta", "Chitra", "Swati", "Vishakha", "Anuradha", "Jyeshtha", "Mula",
    "Purva Ashadha", "Uttara Ashadha", "Shravana", "Dhanishta", "Shatabhisha",
    "Purva Bhadrapada", "Uttara Bhadrapada", "Revati"
]

VARNA_ORDER = ["Shudra", "Vaishya", "Kshatriya", "Brahmin"]

VARNA_BY_RASHI = {
    "Aries": "Kshatriya", "Leo": "Kshatriya", "Sagittarius": "Kshatriya",
    "Taurus": "Vaishya", "Virgo": "Vaishya", "Capricorn": "Vaishya",
    "Gemini": "Shudra", "Libra": "Shudra", "Aquarius": "Shudra",
    "Cancer": "Brahmin", "Scorpio": "Brahmin", "Pisces": "Brahmin"
}

VASHYA = {
    "Aries": ["Leo", "Scorpio"], "Taurus": ["Cancer", "Libra"],
    "Gemini": ["Virgo"], "Cancer": ["Scorpio", "Pisces"],
    "Leo": ["Libra"], "Virgo": ["Pisces", "Gemini"],
    "Libra": ["Virgo", "Capricorn"], "Scorpio": ["Cancer"],
    "Sagittarius": ["Pisces"], "Capricorn": ["Aries", "Aquarius"],
    "Aquarius": ["Aries"], "Pisces": ["Capricorn"]
}

# FRIENDSHIPS (MITRA)
GRAHA_MAITRI_FRIEND = {
    "Sun": ["Moon", "Mars", "Jupiter"],
    "Moon": ["Sun", "Mercury"],
    "Mars": ["Sun", "Moon", "Jupiter"],
    "Mercury": ["Sun", "Venus"],
    "Jupiter": ["Sun", "Moon", "Mars"],
    "Venus": ["Mercury", "Saturn"],
    "Saturn": ["Mercury", "Venus"]
}

# NEUTRALS (SAMA) - FIXED MOON BUG HERE
GRAHA_NEUTRAL = {
    "Sun": ["Mercury"],
    "Moon": ["Mars", "Jupiter", "Venus", "Saturn"], # <-- FIXED: Moon has no enemies
    "Mars": ["Venus"],
    "Mercury": ["Mars", "Jupiter", "Saturn"],
    "Jupiter": ["Saturn"],
    "Venus": ["Mars", "Jupiter"],
    "Saturn": ["Jupiter"]
}

RASHI_LORD = {
    "Aries": "Mars", "Taurus": "Venus", "Gemini": "Mercury",
    "Cancer": "Moon", "Leo": "Sun", "Virgo": "Mercury",
    "Libra": "Venus", "Scorpio": "Mars", "Sagittarius": "Jupiter",
    "Capricorn": "Saturn", "Aquarius": "Saturn", "Pisces": "Jupiter"
}

GANA = {
    "Ashwini": "Deva", "Bharani": "Manushya", "Krittika": "Rakshasa",
    "Rohini": "Manushya", "Mrigashira": "Deva", "Ardra": "Manushya",
    "Punarvasu": "Deva", "Pushya": "Deva", "Ashlesha": "Rakshasa",
    "Magha": "Rakshasa", "Purva Phalguni": "Manushya", "Uttara Phalguni": "Manushya",
    "Hasta": "Deva", "Chitra": "Rakshasa", "Swati": "Deva",
    "Vishakha": "Rakshasa", "Anuradha": "Deva", "Jyeshtha": "Rakshasa",
    "Mula": "Rakshasa", "Purva Ashadha": "Manushya", "Uttara Ashadha": "Manushya",
    "Shravana": "Deva", "Dhanishta": "Rakshasa", "Shatabhisha": "Rakshasa",
    "Purva Bhadrapada": "Manushya", "Uttara Bhadrapada": "Manushya", "Revati": "Deva"
}

YONI = {
    "Ashwini": "Horse", "Bharani": "Elephant", "Krittika": "Sheep",
    "Rohini": "Serpent", "Mrigashira": "Deer", "Ardra": "Dog",
    "Punarvasu": "Cat", "Pushya": "Sheep", "Ashlesha": "Cat",
    "Magha": "Rat", "Purva Phalguni": "Rat", "Uttara Phalguni": "Cow",
    "Hasta": "Buffalo", "Chitra": "Tiger", "Swati": "Buffalo",
    "Vishakha": "Tiger", "Anuradha": "Deer", "Jyeshtha": "Deer",
    "Mula": "Dog", "Purva Ashadha": "Monkey", "Uttara Ashadha": "Mongoose",
    "Shravana": "Monkey", "Dhanishta": "Lion", "Shatabhisha": "Horse",
    "Purva Bhadrapada": "Lion", "Uttara Bhadrapada": "Cow",
    "Revati": "Elephant"
}

YONI_ENEMIES = {
    ("Rat", "Cat"), ("Cat", "Rat"),
    ("Lion", "Elephant"), ("Elephant", "Lion"),
    ("Dog", "Deer"), ("Deer", "Dog"),
    ("Monkey", "Sheep"), ("Sheep", "Monkey"),
    ("Mongoose", "Serpent"), ("Serpent", "Mongoose"),
    ("Cow", "Tiger"), ("Tiger", "Cow"),
    ("Horse", "Buffalo"), ("Buffalo", "Horse"),
    ("Rat", "Lion"), ("Lion", "Rat")
}

NADI = {
    "Ashwini": "Adi", "Bharani": "Madhya", "Krittika": "Antya",
    "Rohini": "Adi", "Mrigashira": "Madhya", "Ardra": "Antya",
    "Punarvasu": "Adi", "Pushya": "Madhya", "Ashlesha": "Antya",
    "Magha": "Antya", "Purva Phalguni": "Adi", "Uttara Phalguni": "Madhya",
    "Hasta": "Antya", "Chitra": "Adi", "Swati": "Madhya", "Vishakha": "Antya",
    "Anuradha": "Adi", "Jyeshtha": "Madhya", "Mula": "Antya",
    "Purva Ashadha": "Adi", "Uttara Ashadha": "Madhya", "Shravana": "Antya",
    "Dhanishta": "Adi", "Shatabhisha": "Madhya", "Purva Bhadrapada": "Adi",
    "Uttara Bhadrapada": "Madhya", "Revati": "Antya"
}

# ==========================================
# 2. CORE LOGIC (SAFE)
# ==========================================

def generate_ashta_koota(bride: Dict[str, Any], groom: Dict[str, Any]) -> Dict[str, Any]:
    score = 0
    breakdown = {}

    # Self-Contained Index Lookup (Prevents API crashes)
    try:
        b_nak_idx = NAKSHATRA_ORDER.index(bride["nakshatra"])
        g_nak_idx = NAKSHATRA_ORDER.index(groom["nakshatra"])
    except ValueError:
        return {"error": "Invalid Nakshatra Name"}

    # 1. VARNA (1 Point)
    if VARNA_ORDER.index(VARNA_BY_RASHI[groom["moon_sign"]]) >= \
       VARNA_ORDER.index(VARNA_BY_RASHI[bride["moon_sign"]]):
        breakdown["Varna"] = 1
    else:
        breakdown["Varna"] = 0
    score += breakdown["Varna"]

    # 2. VASHYA (2 Points) - Mutual Only
    if (
        groom["moon_sign"] in VASHYA.get(bride["moon_sign"], [])
        and bride["moon_sign"] in VASHYA.get(groom["moon_sign"], [])
    ):
        breakdown["Vashya"] = 2
    else:
        breakdown["Vashya"] = 0
    score += breakdown["Vashya"]

    # 3. TARA (3 Points)
    t = (g_nak_idx - b_nak_idx) % 9
    breakdown["Tara"] = 3 if t not in [0, 2, 4, 6] else 0
    score += breakdown["Tara"]

    # 4. YONI (4 Points)
    y1, y2 = YONI[bride["nakshatra"]], YONI[groom["nakshatra"]]
    breakdown["Yoni"] = 0 if (y1, y2) in YONI_ENEMIES else 4
    score += breakdown["Yoni"]

    # 5. GRAHA MAITRI (5 Points) - 3 Tier
    l1, l2 = RASHI_LORD[bride["moon_sign"]], RASHI_LORD[groom["moon_sign"]]
    
    is_friend_1 = l2 in GRAHA_MAITRI_FRIEND.get(l1, [])
    is_friend_2 = l1 in GRAHA_MAITRI_FRIEND.get(l2, [])
    
    if is_friend_1 and is_friend_2:
        breakdown["Graha Maitri"] = 5
    elif (
        l2 in GRAHA_NEUTRAL.get(l1, [])
        or l1 in GRAHA_NEUTRAL.get(l2, [])
    ):
        breakdown["Graha Maitri"] = 3
    else:
        breakdown["Graha Maitri"] = 0
    score += breakdown["Graha Maitri"]

    # 6. GANA (6 Points)
    g1, g2 = GANA[bride["nakshatra"]], GANA[groom["nakshatra"]]
    if g1 == g2:
        breakdown["Gana"] = 6
    elif {"Deva", "Manushya"} == {g1, g2}:
        breakdown["Gana"] = 5
    elif {"Rakshasa", "Manushya"} == {g1, g2}:
        breakdown["Gana"] = 1
    else:
        breakdown["Gana"] = 1 # Deva-Rakshasa default
    score += breakdown["Gana"]

    # 7. BHAKOOT (7 Points)
    r1, r2 = RASHI_ORDER.index(bride["moon_sign"]), RASHI_ORDER.index(groom["moon_sign"])
    dist = (r2 - r1) % 12
    if dist in [1, 5, 7, 11, 4, 8]:
        breakdown["Bhakoot"] = 0
    else:
        breakdown["Bhakoot"] = 7
    score += breakdown["Bhakoot"]

    # 8. NADI (8 Points)
    breakdown["Nadi"] = 0 if NADI[bride["nakshatra"]] == NADI[groom["nakshatra"]] else 8
    score += breakdown["Nadi"]

    return {
        "total_score": score,
        "max_score": 36,
        "breakdown": breakdown,
        "verdict": "Good" if score >= 18 else "Low"
    }
