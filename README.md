# Local Video AI Generator

This project provides a complete, self-contained toolkit for running state-of-the-art, open-source image-to-video AI models locally on a powerful machine like the Apple MacBook Pro M4 Max. It offers a private, cost-free, and highly customizable alternative to commercial video generation services.

## Model Recommendations for M4 Max

Based on extensive research, here is a tiered guide to the best open-source models for your machine.

### 1. Primary Workflow: LTX-Video (Best Overall Performance)
- **Parameters:** 2.5B
- **Memory Usage:** 16-24GB
- **Speed (5s video):** 30-60 seconds
- **Quality:** Excellent
- **Use Case:** The optimal choice for rapid iteration, creative exploration, and preview generation. Its speed, efficiency, and excellent Apple Silicon compatibility make it the ideal starting point.

### 2. Quality Refinement: CogVideoX-5B (Most Reliable & Versatile)
- **Parameters:** 5B
- **Memory Usage:** 20-25GB
- **Speed (5s video):** 3-5 minutes
- **Quality:** Very Good
- **Use Case:** Deploy for reliable production output. Its strong community support, ComfyUI integration, and extensive customization options make it a workhorse for final renders.

### 3. Maximum Quality: HunyuanVideo (Resource Intensive)
- **Parameters:** 13B
- **Memory Usage:** 45GB+ (with optimization)
- **Speed (5s video):** 8-12 minutes
- **Quality:** Superior
- **Use Case:** Reserve for final, high-stakes renders where quality is the absolute priority and longer generation times are acceptable.

## Features

-   **100% Local & Private:** No data ever leaves your machine.
-   **Zero Cost:** Generate unlimited videos with no API fees.
-   **High Quality:** Leverages state-of-the-art models to produce high-resolution, cinematically coherent short videos.
-   **Apple Silicon Optimized:** Specifically designed to use the full power of the M4 Max's GPU cores via PyTorch and Metal Performance Shaders (MPS).

## Prerequisites

-   A MacBook Pro with an M-series chip (M3/M4 Max with 64GB+ RAM recommended).
-   [MiniForge](https://github.com/conda-forge/miniforge) installed.
-   A sample image to use as a source.

## Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/vincentortegajr/local-video-ai.git
    cd local-video-ai
    ```

2.  **Set up the environment:**
    The environment setup is handled by Conda. Follow the installation steps in `TASKS.md` to set up the `video-ai` environment and all dependencies.

## Usage

Once the setup is complete, you can generate a video using the main script:

```bash
# Activate the environment first
conda activate video-ai

# Run the generation script
python generate_video.py \
  --image "path/to/your/image.png" \
  --prompt "A gentle breeze rustles the leaves, cinematic 4k." \
  --output "output/final_video.mp4"
```

## Technology

-   **Initial Model:** [LTX-Video](https://huggingface.co/docs/diffusers/main/en/api/pipelines/ltx_video)
-   **Framework:** [PyTorch](https://pytorch.org/)
-   **Library:** [Hugging Face Diffusers](https://huggingface.co/docs/diffusers/index)