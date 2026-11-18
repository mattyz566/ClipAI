from clipper import process_video
import os
import streamlit as st

from clipper import process_video

st.set_page_config(
    page_title="ClipAI",
    page_icon="🎮",
    layout="wide"
)

st.title("🎮 ClipAI")
st.subheader("AI-powered gaming highlight generator")

st.write(
    "Upload a gaming recording and let ClipAI "
    "find exciting moments automatically."
)

os.makedirs("uploads", exist_ok=True)
os.makedirs("clips", exist_ok=True)

uploaded_file = st.file_uploader(
    "Upload your gaming recording",
    type=["mp4", "mov", "mkv"]
)

if uploaded_file:

    st.video(uploaded_file)

    if st.button("🚀 Generate Gaming Clips"):

        video_path = os.path.join(
            "uploads",
            uploaded_file.name
        )

        with open(video_path, "wb") as file:
            file.write(uploaded_file.getbuffer())

        with st.spinner("Analysing your gameplay..."):

            try:
                results = process_video(
                    video_path,
                    "clips"
                )

                if results:
                    st.success(
                        f"Created {len(results)} clips!"
                    )

                    for clip in results:

                        st.video(clip)

                        with open(clip, "rb") as file:
                            st.download_button(
                                label="Download clip",
                                data=file.read(),
                                file_name=os.path.basename(clip),
                                mime="video/mp4"
                            )

                else:
                    st.warning(
                        "No suitable audio highlights found."
                    )

            except Exception as error:
                st.error(f"Something went wrong: {error}")
