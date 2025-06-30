# Local Video AI Generator

This project provides a complete, self-contained toolkit for running state-of-the-art, open-source image-to-video AI models locally on a powerful machine like the Apple MacBook Pro M4 Max. It offers a private, cost-free, and highly customizable alternative to commercial video generation services.

## Features

-   **100% Local & Private:** No data ever leaves your machine.
-   **Zero Cost:** Generate unlimited videos with no API fees.
-   **High Quality:** Leverages the LTX-Video model to produce high-resolution, cinematically coherent short videos.
-   **Apple Silicon Optimized:** Specifically designed to use the full power of the M4 Max's GPU cores via PyTorch and Metal Performance Shaders (MPS).

## Prerequisites

-   A MacBook Pro with an M-series chip (M3/M4 Max with 64GB+ RAM recommended).
-   [MiniForge](https://github.com/conda-forge/miniforge) installed.
-   A sample image to use as a source.

## Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd local-video-ai
    ```

2.  **Set up the environment:**
    The environment setup is handled by Conda. Detailed instructions are in the `TASKS.md` file and will be automated where possible.

## Usage

Once the setup is complete, you can generate a video using the main script:

```bash
python generate_video.py \
  --image "path/to/your/image.png" \
  --prompt "A gentle breeze rustles the leaves, cinematic 4k." \
  --output "output/final_video.mp4"
```

## Technology

-   **Model:** [LTX-Video](https://huggingface.co/docs/diffusers/main/en/api/pipelines/ltx_video)
-   **Framework:** [PyTorch](https://pytorch.org/)
-   **Library:** [Hugging Face Diffusers](https://huggingface.co/docs/diffusers/index)
