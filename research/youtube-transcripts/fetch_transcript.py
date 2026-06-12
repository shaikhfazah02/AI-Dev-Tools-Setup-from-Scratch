from youtube_transcript_api import YouTubeTranscriptApi

VIDEO_ID = "nGPpct0KWbc"
VIDEO_URL = "https://www.youtube.com/watch?v=nGPpct0KWbc"
VIDEO_TITLE = "Turn LinkedIn Into a $30M ARR Growth Machine | Adam Robinson (Retention.com, RB2B)"
EXPERT_NAME = "Adam Robinson"
OUTPUT_PATH = r"C:\Users\ACER\100hires-Test-Project\research\youtube-transcripts\adam-robinson-linkedin-30m-arr.md"

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
**Video URL:** {VIDEO_URL}

---

## Transcript

{full_text}
"""

with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
    f.write(markdown)

print(f"Saved transcript ({len(lines)} segments, {len(full_text)} chars) to {OUTPUT_PATH}")
