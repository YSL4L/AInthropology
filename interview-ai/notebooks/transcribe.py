import whisper
import os

# Modell laden
model = whisper.load_model("base")  # auch möglich: "small", "medium", "large"

# Pfade
audio_dir = "/Users/ulrichschuetz/Documents/GitHub/AInthropology/interview-ai/data/audio"
output_dir = "/Users/ulrichschuetz/Documents/GitHub/AInthropology/interview-ai/data/transcripts"
os.makedirs(output_dir, exist_ok=True)

# Schleife über alle Audiodateien
for filename in os.listdir(audio_dir):
    if filename.endswith((".mp3", ".wav", ".m4a")):
        filepath = os.path.join(audio_dir, filename)
        print(f"→ Transkribiere: {filename}")
        
        try:
            result = model.transcribe(filepath)
            transcript = result["text"]

            # Richtiger Dateiname ohne doppelte Endung
            name_only = os.path.splitext(filename)[0]
            outpath = os.path.join(output_dir, name_only + ".txt")

            with open(outpath, "w", encoding="utf-8") as f:
                f.write(transcript)

            print(f"✅ Gespeichert: {outpath}\n")

        except Exception as e:
            print(f"⚠️ Fehler bei {filename}: {e}")
