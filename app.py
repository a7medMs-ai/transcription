import streamlit as st
import tempfile
import os
import time
from transcript_to_srt import mock_transcribe_and_convert

# عنوان التطبيق
st.set_page_config(page_title="YouTube Transcriber", layout="centered")
st.title("🎧 YouTube Transcriber Tool")

st.markdown("ارفع ملف الفيديو أو الصوت، واختر الإعدادات المناسبة، وسنقوم بإنشاء ملف الترجمة التلقائي لك.")

# 1. رفع الملف
uploaded_file = st.file_uploader("📤 ارفع المقطع الصوتي أو الفيديو", type=["mp4", "mp3", "wav", "mov", "mkv"])

# 2. الإعدادات
col1, col2 = st.columns(2)

with col1:
    lang = st.selectbox("🌐 اختر لغة المقطع", ["ar", "en", "fr", "de", "es"], index=0)

with col2:
    file_type = st.selectbox("📄 اختر نوع الملف المطلوب", ["srt"], index=0)

media_type = st.radio("🎞️ نوع المقطع", ["🎧 صوتي", "📹 فيديو"])

# زر التشغيل
if uploaded_file and st.button("ابدأ المعالجة 🚀"):
    with st.spinner("🚀 جاري رفع المقطع ومعالجته..."):
        # حفظ الملف مؤقتًا
        with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
            tmp_file.write(uploaded_file.read())
            file_path = tmp_file.name

        # محاكاة رفع ومعالجة الفيديو (لاحقًا استبدالها بـ youtube_utils)
        time.sleep(2)
        srt_content = mock_transcribe_and_convert(file_path, lang=lang)

        # حفظ ملف SRT مؤقتًا
        srt_path = file_path + ".srt"
        with open(srt_path, "w", encoding="utf-8") as f:
            f.write(srt_content)

        st.success("🎉 تم إنشاء ملف الترجمة بنجاح!")
        st.download_button("⬇️ تحميل ملف SRT", data=srt_content, file_name="transcript.srt", mime="text/plain")

        os.remove(file_path)
        os.remove(srt_path)
