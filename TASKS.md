# TASKS.md - Project Implementation Checklist

## Phase 1: Environment & Project Setup

-   [x] Create project directory (`local-video-ai`).
-   [x] Initialize Git repository.
-   [x] Create `PDR.md`.
-   [ ] Create `TASKS.md`.
-   [ ] Create `README.md`.
-   [ ] Create `.gitignore` file.
-   [ ] Make the initial Git commit.
-   [ ] Create remote repository on GitHub and push initial commit.

## Phase 2: Local Environment Configuration

-   [ ] Install MiniForge for Apple Silicon.
-   [ ] Create a new conda environment named `video-ai`.
-   [ ] Activate the `video-ai` environment.
-   [ ] Install core Python dependencies: `torch`, `torchvision`, `torchaudio`.
-   [ ] Install AI/ML dependencies: `diffusers`, `transformers`, `accelerate`.
-   [ ] Create a `verify_setup.py` script to confirm PyTorch and MPS are working correctly.
-   [ ] Run `verify_setup.py` and confirm success.

## Phase 3: Core Video Generation Script

-   [ ] Create the main script file: `generate_video.py`.
-   [ ] Add argument parsing to accept an image path, a prompt, and an output path.
-   [ ] Implement model loading for LTX-Video using `diffusers`.
-   [ ] Implement image loading and preprocessing.
-   [ ] Implement the main video generation pipeline call.
-   [ ] Implement video saving logic.
-   [ ] Perform an initial test run with a sample image and prompt.
-   [ ] Debug and refine the script until a video is successfully generated.

## Phase 4: Finalization & Documentation

-   [ ] Add detailed comments and docstrings to `generate_video.py`.
-   [ ] Update `README.md` with final usage instructions and examples.
-   [ ] Clean up any temporary or test files.
-   [ ] Make the final Git commit.
-   [ ] Push all changes to the GitHub repository.
