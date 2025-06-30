# PDR.md - Project Development Roadmap

## 1. Project Vision & Goals

**Vision:** To create a powerful, local, and cost-free image-to-video generation toolkit that leverages the full potential of the MacBook Pro M4 Max. This project will provide a private, secure, and highly customizable alternative to commercial, API-based video generation services.

**Primary Goal:** Implement and optimize a state-of-the-art open-source image-to-video model (LTX-Video) that can be run entirely locally, producing high-quality, short-form videos from still images and text prompts.

**Success Criteria:**
- Successfully generate a 5-second, 1080p video from a local image.
- Generation time should be under 5 minutes per video.
- The process must be repeatable and well-documented.
- The final script should be easy to use for a non-expert.

## 2. Core Technology Stack

- **Primary Model:** LTX-Video (2.5B parameters)
  - **Reasoning:** Chosen for its optimal balance of quality, performance, and excellent Apple Silicon compatibility. It offers near real-time generation with manageable memory usage (16-24GB).
- **Core Library:** Hugging Face Diffusers
  - **Reasoning:** Provides a high-level, standardized interface for interacting with diffusion models, simplifying the implementation.
- **Environment Management:** MiniForge (Conda)
  - **Reasoning:** Ensures a clean, isolated Python environment optimized for Apple Silicon.
- **Compute Backend:** PyTorch with Metal Performance Shaders (MPS)
  - **Reasoning:** Leverages the M4 Max's GPU cores for hardware acceleration.

## 3. High-Level Implementation Plan

1.  **Phase 1: Environment Setup & Verification (Initial Task)**
    -   Install MiniForge and create a dedicated `video-ai` conda environment.
    -   Install all necessary Python dependencies (PyTorch, Diffusers, etc.).
    -   Verify that PyTorch can correctly identify and use the MPS backend.

2.  **Phase 2: Core Generation Script**
    -   Develop a Python script (`generate_video.py`) to handle the end-to-end video generation process.
    -   Implement logic to load the LTX-Video model from Hugging Face.
    -   Add functionality to accept a source image path and a text prompt.
    -   Implement the video generation pipeline using the Diffusers library.
    -   Save the generated video to a specified output path.

3.  **Phase 3: Optimization & Usability**
    -   Implement memory optimization techniques (e.g., attention slicing) if needed.
    -   Refine the script to be more user-friendly, with clear command-line arguments.
    -   Add progress indicators and informative logging.

## 4. Potential Risks & Mitigations

-   **Risk:** Model incompatibility or performance issues with the MPS backend.
    -   **Mitigation:** The chosen model (LTX-Video) has documented Apple Silicon support. If issues arise, we will fall back to the more stable but slower CogVideoX model.
-   **Risk:** Complex dependencies or installation issues.
    -   **Mitigation:** Using Conda (MiniForge) will manage most dependencies automatically, minimizing conflicts.
-   **Risk:** Out-of-memory errors despite the 128GB RAM.
    -   **Mitigation:** Implement memory-saving techniques like CPU offloading and attention slicing as documented in the initial research.
