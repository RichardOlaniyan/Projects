import cv2
import base64
from openai import OpenAI

v_path = "samplevideo.mp4"

video = cv2.VideoCapture(v_path)

base64Frames = []

while video.isOpened():
    success, frame = video.read()

    if not success:
        break

    _, buffer = cv2.imencode(".jpg", frame)
    base64Frames.append(base64.b64encode(buffer).decode("utf-8"))
video.release()

client = OpenAI(api_key="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")

prompts = [
    {
        "role": "user",
        "content": [
            '''Here are the frames of video, generate a voiceover script for this video. 
            Include only narration and no other text or preamble. The length of the voiceover should align with 
            the duration of the video which is about 23secs long''',
            *map(lambda x: {"image": x, "resize": 768}, base64Frames[0::50])
        ]
    }
]
parameters = {
    "model": "gpt-4-vision-preview",
    "messages": prompts,
    "max_tokens": 200
}

result = client.chat.completions.create(**parameters)

print(result.choices[0].message.content.strip())
