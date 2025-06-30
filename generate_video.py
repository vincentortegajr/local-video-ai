import argparse
import torch
from diffusers import LTXImageToVideoPipeline
from diffusers.utils import load_image, export_to_video
import os

def generate_video(image_path: str, prompt: str, output_path: str):
    """
    Generates a video from a source image and a text prompt using the LTX-Video model.

    Args:
        image_path (str): Path to the source image.
        prompt (str): Text prompt to guide the video generation.
        output_path (str): Path to save the generated MP4 video.
    """
    print("--- Starting Video Generation ---")
    
    # 1. Verify inputs
    if not os.path.exists(image_path):
        print(f"Error: Input image not found at '{image_path}'")
        return

    print(f"Loading image from: {image_path}")
    print(f"Using prompt: '{prompt}'")

    # 2. Set up the pipeline
    try:
        device = "mps"
        dtype = torch.float16
        
        print(f"Loading LTX-Video model... (This may take a few minutes on first run)")
        pipe = LTXImageToVideoPipeline.from_pretrained("lightricks/ltx-video", torch_dtype=dtype)
        pipe.to(device)
        print("Model loaded successfully.")

    except Exception as e:
        print(f"Error loading the model pipeline: {e}")
        print("Please ensure you have a stable internet connection for the first download.")
        return

    # 3. Load the source image
    image = load_image(image_path).resize((768, 768))

    # 4. Generate the video frames
    print("Generating video frames... This is the main processing step.")
    try:
        video_frames = pipe(
            prompt=prompt,
            image=image,
            num_frames=20, # Approx 4-5 seconds at 4-5 fps
            num_inference_steps=50,
            guidance_scale=7.5,
        ).frames[0]
        print("Frame generation complete.")
    except Exception as e:
        print(f"An error occurred during frame generation: {e}")
        return

    # 5. Export the frames to a video file
    try:
        print(f"Exporting video to: {output_path}")
        # Ensure the output directory exists
        output_dir = os.path.dirname(output_path)
        if output_dir:
            os.makedirs(output_dir, exist_ok=True)
            
        export_to_video(video_frames, output_path, fps=5)
        print("--- Video Generation Complete! ---")
        print(f"Video saved successfully at: {output_path}")
    except Exception as e:
        print(f"An error occurred while exporting the video: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a video from an image and a prompt.")
    parser.add_argument(
        "--image",
        type=str,
        required=True,
        help="Path to the source image file."
    )
    parser.add_argument(
        "--prompt",
        type=str,
        default="A gentle breeze, cinematic, 4k, photorealistic.",
        help="Text prompt to guide the video generation."
    )
    parser.add_argument(
        "--output",
        type=str,
        default="output/generated_video.mp4",
        help="Path to save the output MP4 video."
    )

    args = parser.parse_args()
    
    generate_video(args.image, args.prompt, args.output)