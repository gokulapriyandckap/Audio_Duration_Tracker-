from pydub import AudioSegment

def get_audio_duration(audio_file_path):
    audio = AudioSegment.from_file(audio_file_path)
    duration_ms = len(audio)
    duration_s = duration_ms / 1000.0  # Convert milliseconds to seconds
    return duration_s


audio_file_path = "morning_alarm.mp3"  # Replace with your audio file path
duration = get_audio_duration(audio_file_path)
print(f"Audio File: {audio_file_path} duration is  {duration} Seconds")
