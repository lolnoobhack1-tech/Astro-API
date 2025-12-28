from typing import Dict, Any

# ----------------------------------
# Static Vedic Tables
# ----------------------------------

VARNA_ORDER = ["Shudra", "Vaishya", "Kshatriya", "Brahmin"]

VARNA_MAP = {
    "Cancer": "Brahmin", "Scorpio": "Brahmin", "Pisces": "Brahmin",
    "Leo": "Kshatriya", "Sagittarius": "Kshatriya",
    "Aries": "Vaishya", "Taurus": "Vaishya",
    "Gemini": "Shudra", "Virgo": "Shudra", "Libra": "Shudra", "Aquarius": "Shudra", "Capricorn": "Shudra"
}

VASHYA_MAP = {
    "Aries": ["Leo", "Scorpio"],
    "Taurus": ["Cancer", "Libra"],
    "Gemini": ["Virgo"],
    "Cancer": ["Scorpio", "Pisces"],
    "Leo": ["Aries"],
    "Virgo": ["Pisces", "Gemini"],
    "Libra": ["Virgo", "Capricorn"],
    "Scorpio": ["Cancer"],
    "Sagittarius": ["Pisces"],
    "Capricorn": ["Aries", "Aquarius"],
    "Aquarius": ["Aries"],
    "Pisces": ["Capricorn"]
}

TARA_POINTS = [3, 5, 7]  # Favorable offsets

YONI_MAP = {
    "Ashwini": "Horse", "Bharani": "Elephant", "Krittika": "Sheep",
    "Rohini": "Serpent", "Mrigashira": "Serpent", "Ardra": "Dog",
    "Punarvasu": "Cat", "Pushya": "Sheep", "Ashlesha": "Cat",
    "Magha": "Rat", "Purva Phalguni": "Rat", "Uttara Phalguni": "Cow",
    "Hasta": "Buffalo", "Chitra": "Tiger", "Swati": "Buffalo",
    "Vishakha": "Tiger", "Anuradha": "Deer", "Jyeshtha": "Deer",
    "Mula": "Dog", "Purva Ashadha": "Monkey", "Uttara Ashadha": "Mongoose",
    "Shravana": "Monkey", "Dhanishta": "Lion", "Shatabhisha": "Horse",
    "Purva Bhadrapada": "Lion", "Uttara Bhadrapada": "Cow", "Revati": "Elephant"
}

ENEMY_YONIS = {
    ("Cat", "Rat"), ("Dog", "Deer"), ("Lion", "Elephant"),
    ("Monkey", "Sheep"), ("Horse", "Buffalo")
}

GANA_MAP = {
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

NADI_MAP = {
    "Ashwini": "Adi", "Bharani": "Madhya", "Krittika": "Antya",
    "Rohini": "Adi", "Mrigashira": "Madhya", "Ardra": "Antya",
    "Punarvasu": "Adi", "Pushya": "Madhya", "Ashlesha": "Antya",
    "Magha": "Adi", "Purva Phalguni": "Madhya", "Uttara Phalguni": "Antya",
    "Hasta": "Adi", "Chitra": "Madhya", "Swati": "Antya",
    "Vishakha": "Adi", "Anuradha": "Madhya", "Jyeshtha": "Antya",
    "Mula": "Adi", "Purva Ashadha": "Madhya", "Uttara Ashadha": "Antya",
    "Shravana": "Adi", "Dhanishta": "Madhya", "Shatabhisha": "Antya",
    "Purva Bhadrapada": "Adi", "Uttara Bhadrapada": "Madhya", "Revati": "Antya"
}

RASHI_ADHIPATI = {
    "Aries": "Mars", "Taurus": "Venus", "Gemini": "Mercury",
    "Cancer": "Moon", "Leo": "Sun", "Virgo": "Mercury",
    "Libra": "Venus", "Scorpio": "Mars", "Sagittarius": "Jupiter",
    "Capricorn": "Saturn", "Aquarius": "Saturn", "Pisces": "Jupiter"
}

ZODIAC_ORDER = ["Aries","Taurus","Gemini","Cancer","Leo","Virgo","Libra",
                "Scorpio","Sagittarius","Capricorn","Aquarius","Pisces"]

# ----------------------------------
# Core Engine
# ----------------------------------

def generate_ashta_koota(k1: Dict[str, Any], k2: Dict[str, Any]) -> Dict[str, Any]:
    moon1, moon2 = k1["moon_sign"], k2["moon_sign"]
    nak1, nak2 = k1["nakshatra"], k2["nakshatra"]

    score = 0
    breakdown = {}

    # 1. Varna (1)
    v1, v2 = VARNA_MAP[moon1], VARNA_MAP[moon2]
    varna_points = 1 if VARNA_ORDER.index(v1) <= VARNA_ORDER.index(v2) else 0
    score += varna_points
    breakdown["Varna"] = (varna_points, 1)

    # 2. Vashya (2)
    vashya_points = 2 if moon2 in VASHYA_MAP.get(moon1, []) else 0
    score += vashya_points
    breakdown["Vashya"] = (vashya_points, 2)

    # 3. Tara (3)
    tara_diff = (list(YONI_MAP.keys()).index(nak2) - list(YONI_MAP.keys()).index(nak1)) % 27
    tara_points = 3 if tara_diff in TARA_POINTS else 0
    score += tara_points
    breakdown["Tara"] = (tara_points, 3)

    # 4. Yoni (4)
    y1, y2 = YONI_MAP[nak1], YONI_MAP[nak2]
    yoni_points = 4 if (y1 == y2 or (y1, y2) not in ENEMY_YONIS) else 0
    score += yoni_points
    breakdown["Yoni"] = (yoni_points, 4)

    # 5. Graha Maitri (5)
    lord1, lord2 = RASHI_ADHIPATI[moon1], RASHI_ADHIPATI[moon2]
    graha_points = 5 if lord1 == lord2 else 3
    score += graha_points
    breakdown["Graha Maitri"] = (graha_points, 5)

    # 6. Gana (6)
    g1, g2 = GANA_MAP[nak1], GANA_MAP[nak2]
    gana_points = 6 if g1 == g2 else (3 if "Manushya" in (g1, g2) else 0)
    score += gana_points
    breakdown["Gana"] = (gana_points, 6)

    # 7. Bhakoot (7)
    idx1, idx2 = ZODIAC_ORDER.index(moon1), ZODIAC_ORDER.index(moon2)
    diff = (idx2 - idx1) % 12
    bhakoot_points = 0 if diff in [6, 8] else 7
    score += bhakoot_points
    breakdown["Bhakoot"] = (bhakoot_points, 7)

    # 8. Nadi (8)
    nadi_points = 0 if NADI_MAP[nak1] == NADI_MAP[nak2] else 8
    score += nadi_points
    breakdown["Nadi"] = (nadi_points, 8)

    return {
        "total_gunas": score,
        "max_gunas": 36,
        "breakdown": breakdown,
        "verdict": verdict(score)
    }

def verdict(score: int) -> str:
    if score >= 30:
        return "Excellent Match"
    if score >= 24:
        return "Very Good Match"
    if score >= 18:
        return "Average / Acceptable"
    return "Low Compatibility"
