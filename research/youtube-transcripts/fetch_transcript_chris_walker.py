from youtube_transcript_api import YouTubeTranscriptApi

VIDEO_ID = "EIk7ofRYLug"
VIDEO_URL = "https://www.youtube.com/watch?v=EIk7ofRYLug"
VIDEO_TITLE = "LinkedIn Organic Isn't Dead | Demand Gen Live Keynote"
EXPERT_NAME = "Chris Walker"
CHANNEL = "Refine Labs"
OUTPUT_PATH = r"C:\Users\ACER\100hires-Test-Project\research\youtube-transcripts\chris-walker-linkedin-organic-isnt-dead.md"

ytt_api = YouTubeTranscriptApi()
transcript = ytt_api.fetch(VIDEO_ID)

lines = []
for entry in transcript:
    text = entry.text.strip()
    if text:
        lines.append(text)

full_text = " ".join(lines)

markdown = f"""# {VIDEO_TITLE}

**Expert:** {EXPERT_NAME}
**Channel:** {CHANNEL}
**Video URL:** {VIDEO_URL}

---

## Transcript

{full_text}
"""

with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
    f.write(markdown)

print(f"Saved transcript ({len(lines)} segments, {len(full_text)} chars) to {OUTPUT_PATH}")
