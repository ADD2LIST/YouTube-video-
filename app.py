import streamlit as st
from pytube import YouTube

def download_youtube_video(video_url, quality, save_path):
    try:
        yt = YouTube(video_url)
        stream = yt.streams.filter(res=quality, file_extension="mp4").first()
        if stream:
            st.write(f"Downloading {yt.title} at {quality}...")
            stream.download(output_path=save_path)
            st.success("Download completed successfully!")
        else:
            st.warning("Video not found or not accessible.")
    except Exception as e:
        st.error(f"An error occurred: {e}")

def main():
    st.title("YouTube Video Downloader")

    video_url = st.text_input("Enter the YouTube video URL:")

    quality_options = ["360p", "480p"]
    selected_quality = st.selectbox("Select the video quality:", quality_options)

    save_path = st.text_input("Enter the path to save the downloaded video:")

    if st.button("Download"):
        if video_url and save_path:
            download_youtube_video(video_url, selected_quality, save_path)
        else:
            st.warning("Please provide both the video URL and save path.")

if __name__ == "__main__":
    main()
