import torch

def verify():
    """
    Verifies the PyTorch and MPS (Apple Silicon GPU) setup.
    """
    print("--- PyTorch Setup Verification ---")
    
    # 1. Check PyTorch version
    print(f"PyTorch version: {torch.__version__}")

    # 2. Check if MPS is built-in
    print(f"MPS available: {torch.backends.mps.is_available()}")

    # 3. Check if MPS is the default device
    if torch.backends.mps.is_available():
        try:
            # Attempt to move a tensor to the MPS device
            device = torch.device("mps")
            x = torch.ones(1, device=device)
            print("Successfully created a tensor on the 'mps' (GPU) device.")
            print("Your environment is correctly configured to use the M4 Max GPU.")
        except Exception as e:
            print(f"An error occurred while testing the MPS device: {e}")
            print("There might be an issue with your MPS drivers or PyTorch installation.")
    else:
        print("MPS device not found. The script will run on the CPU, which will be very slow.")
        print("Please ensure you are on a Mac with Apple Silicon and have a compatible PyTorch version.")

    print("------------------------------------")

if __name__ == "__main__":
    verify()
