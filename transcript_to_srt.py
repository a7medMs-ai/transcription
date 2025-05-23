def mock_transcribe_and_convert(file_path, lang="ar"):
    # نموذج بسيط لترجمة وهمية
    from datetime import timedelta
    import srt

    transcript = [
        {"start": 0, "duration": 4, "text": "مرحبًا بك في هذا المقطع"},
        {"start": 5, "duration": 3, "text": "هذا مثال على ملف الترجمة"},
    ]

    subtitles = []
    for i, entry in enumerate(transcript):
        start = timedelta(seconds=entry["start"])
        duration = timedelta(seconds=entry["duration"])
        end = start + duration
        subtitles.append(srt.Subtitle(index=i + 1, start=start, end=end, content=entry["text"]))

    return srt.compose(subtitles)
