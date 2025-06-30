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

---

## Setup & Usage

### Hugging Face Authentication

An authenticated Hugging Face account is required to download the models used in this project.

#### What are User Access Tokens?
User Access Tokens are the preferred way to authenticate an application or notebook to Hugging Face services. You can manage your access tokens in your settings. Access tokens allow applications and notebooks to perform specific actions specified by the scope of the roles shown in the following:

-   **`fine-grained`**: tokens with this role can be used to provide fine-grained access to specific resources, such as a specific model or models in a specific organization. This type of token is useful in production environments, as you can use your own token without sharing access to all your resources.
-   **`read`**: tokens with this role can only be used to provide read access to repositories you could read. That includes public and private repositories that you, or an organization you’re a member of, own. Use this role if you only need to read content from the Hugging Face Hub (e.g. when downloading private models or doing inference).
-   **`write`**: tokens with this role additionally grant write access to the repositories you have write access to. Use this token if you need to create or push content to a repository (e.g., when training a model or modifying a model card).

For this project, a **`read`** token is sufficient, but a **`write`** token provides maximum flexibility for future enhancements.

#### How to use User Access Tokens?
The scripts in this project will automatically use the token saved on your machine. You can log in via the command line:
```bash
huggingface-cli login --token <YOUR_TOKEN>
```

---

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/vincentortegajr/local-video-ai.git
    cd local-video-ai
    ```

2.  **Set up the environment:**
    The environment setup is handled by Conda. Follow the installation steps in `TASKS.md` to set up the `video-ai` environment and all dependencies.

### Running the Generator

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