import base64
import requests

URL = "http://127.0.0.1:8080"


def base64_to_image(base64_string, save_path='output_image.png'):
    with open(save_path, 'wb') as f:
        f.write(base64.b64decode(base64_string))


def text_to_image():
    print("Starting Inference")
    payload = {
        "prompt": "A beautiful dawn in the forest",
        "negative_prompt": "worst quality, low quality, watermark, text, error, blurry, jpeg artifacts, cropped, jpeg artifacts, signature, watermark, username, artist name, bad anatomy",
        "num_inference_steps": 25,
        "guidance_scale": 7.5,
        "width": 512,
        "height": 512,
    }

    response = requests.post(f"{URL}/api/v1/generatebase64/", json=payload)
    resp_json = response.json()
    print("Inference Completed")
    base64_to_image(resp_json['image'], f"output_image.png")
    print("Image saved")

if __name__ == "__main__":
    text_to_image()