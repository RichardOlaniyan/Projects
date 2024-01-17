import gradio
from openai import OpenAI
from youtube_transcript_api import YouTubeTranscriptApi


def get_transcript(video_link):
    video_id = video_link.split("v=")[1]
    transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
    transcript = transcript_list.find_transcript(["en"])
    language = transcript.language
    captions = YouTubeTranscriptApi.get_transcript(video_id, languages=["en"])
    subtitles = "\n".join([caption["text"] for caption in captions])
    return subtitles


client = OpenAI(api_key="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")


def summarize_transcript(subtitles):
    response = client.chat.completions.create(
        model="gpt-4-1106-preview",
        messages=[{
            "role": "system",
            "content": "You will help summarize a transcript from a YouTube Video"
        },
            {
                "role": "user",
                "content": f"Summarize these subtitles: {subtitles}"
            }
        ]
    )
    return response.choices[0].message.content.strip()


def generate_summary(video_link):
    transcript = get_transcript(video_link)
    return summarize_transcript(transcript)


app = gradio.Interface(
    fn=generate_summary,
    inputs="text",
    outputs="text",
    title="YouTube Video Summarizer GPT"
)
app.launch(share=True)
