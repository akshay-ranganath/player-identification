"""
CFL Player Identification Prompt
Prompt for identifying Canadian Football League players from images with JSON output
"""

CFL_PLAYER_IDENTIFICATION_PROMPT = """
Analyze this image and identify any CFL (Canadian Football League) players visible. Return your analysis as valid JSON following this exact structure:

{
  "image_analysis": {
    "total_players_visible": <number>,
    "image_quality": "<excellent|good|fair|poor>",
    "viewing_angle": "<front|side|back|overhead|unclear>"
  },
  "players": [
    {
      "player_id": 1,
      "name": {
        "value": "<player name or 'Unknown'>",
        "confidence": "<high|medium|low>"
      },
      "jersey_number": {
        "value": "<number>",
        "confidence": "<high|medium|low>"
      },
      "team": {
        "name": "<team name>",
        "colors_visible": ["<color1>", "<color2>"],
        "confidence": "<high|medium|low>"
      },
      "position": {
        "value": "<position or 'Unknown'>",
        "confidence": "<high|medium|low>"
      },
      "visual_evidence": [
        "<evidence point 1>",
        "<evidence point 2>"
      ],
      "distinctive_features": "<description or null>",
      "bounding_box": {
        "description": "<location in image, e.g., 'center left', 'foreground right'>"
      },
      "overall_confidence": "<high|medium|low>"
    }
  ],
  "context": {
    "game_situation": "<description or null>",
    "stadium": "<stadium name or 'Unknown'>",
    "approximate_date": "<YYYY or 'Unknown'>",
    "additional_notes": "<any other relevant context>"
  }
}

CONFIDENCE LEVEL GUIDELINES:
- HIGH: Jersey number clearly visible, team logo/colors unmistakable, or player face recognizable
- MEDIUM: Partial information visible (e.g., team colors clear but logo obscured, number partially visible)
- LOW: Inference based on context clues (body type, position on field, etc.)

CRITICAL RULES:
- OMIT "jersey_number" field entirely if number is not clearly visible or readable
- OMIT "team" object entirely if team cannot be confidently determined from uniform/logos
- Each field (name, jersey_number, team, position) has its own confidence level
- "overall_confidence" represents the combined confidence across all identifications for that player
- Be conservative with identifications - if confidence would be "low", consider omitting the field

Example with mixed confidence:
{
  "player_id": 1,
  "name": {
    "value": "Unknown",
    "confidence": "low"
  },
  "jersey_number": {
    "value": "23",
    "confidence": "high"
  },
  "team": {
    "name": "Toronto Argonauts",
    "colors_visible": ["blue", "white"],
    "confidence": "high"
  },
  "position": {
    "value": "Running Back",
    "confidence": "medium"
  },
  "visual_evidence": [
    "Jersey number 23 clearly visible on back",
    "Toronto Argonauts logo on helmet",
    "Body position suggests ball carrier"
  ],
  "bounding_box": {"description": "center foreground"},
  "overall_confidence": "high"
}

Return ONLY the JSON, no additional text before or after.

If you cannot identify any players with reasonable confidence, return:
{
  "error": "Unable to identify players",
  "reason": "<explanation>",
  "visible_details": "<what you can see>"
}
"""


def get_prompt():
    """Return the CFL player identification prompt."""
    return CFL_PLAYER_IDENTIFICATION_PROMPT


# Example usage
if __name__ == "__main__":
    print("CFL Player Identification Prompt")
    print("=" * 50)
    print(get_prompt())