import yt_dlp
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def get_stream_data(video_url):
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'noplaylist': True,
        'quiet': True
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(video_url, download=False)
        formats = info_dict.get('formats', [])

    return formats

def animate(i, line, bitrates):
    line.set_ydata(bitrates[:i])  # update the data
    line.set_xdata(range(len(bitrates[:i])))  # update the x-axis data
    return line,

def visualize_stream_data(formats):
    bitrates = []
    durations = []

    for fmt in formats:
        if fmt.get('vcodec') != 'none':  # Exclude audio-only formats
            bitrate = fmt.get('tbr')
            duration = fmt.get('filesize') / (bitrate * 1000 / 8) if fmt.get('filesize') else None
            if bitrate and duration:
                bitrates.append(bitrate)
                durations.append(duration)

    fig, ax = plt.subplots()
    line, = ax.plot([], [], 'r-')
    ax.set_xlim(0, len(durations))
    ax.set_ylim(0, max(bitrates))
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Bitrate (Kbps)')
    ax.set_title('Bitrate over Time for YouTube Video Streams')

    ani = animation.FuncAnimation(fig, animate, fargs=(line, bitrates), frames=len(bitrates), interval=1000, blit=True)
    plt.show()

if __name__ == '__main__':
    video_url = 'https://www.youtube.com/watch?v=pzHR4zKqL4A&t=1s'  # Replace with your YouTube video URL
    formats = get_stream_data(video_url)
    visualize_stream_data(formats)
