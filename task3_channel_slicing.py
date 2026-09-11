
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


def load_image_array(path: str) -> np.ndarray:
    return np.array(Image.open(path).convert("RGB"))


def extract_channels(img: np.ndarray):
    """Return 2D intensity grids for R, G, B using Axis-2 slicing."""
    red_2d = img[:, :, 0]
    green_2d = img[:, :, 1]
    blue_2d = img[:, :, 2]
    return red_2d, green_2d, blue_2d


def build_single_channel_images(img: np.ndarray, red_2d, green_2d, blue_2d):
    """Build 3D arrays where only one channel is active, others zeroed."""
    red_only = np.zeros_like(img)
    red_only[:, :, 0] = red_2d

    green_only = np.zeros_like(img)
    green_only[:, :, 1] = green_2d

    blue_only = np.zeros_like(img)
    blue_only[:, :, 2] = blue_2d

    return red_only, green_only, blue_only


def print_report(img, red_2d, green_2d, blue_2d):
    print("--- CHANNEL EXTRACTION SUMMARY ---")
    print(f"Original Image Shape : {img.shape}")
    print(f"Red Channel 2D Shape  : {red_2d.shape} | Mean Intensity: {red_2d.mean():.2f}")
    print(f"Green Channel 2D Shape: {green_2d.shape} | Mean Intensity: {green_2d.mean():.2f}")
    print(f"Blue Channel 2D Shape : {blue_2d.shape} | Mean Intensity: {blue_2d.mean():.2f}")
    print("Display Window : Matplotlib 2x3 Subplot Grid Rendered.")


def main(path="sample.jpg", save_path="task3_channels.png"):
    img = load_image_array(path)
    red_2d, green_2d, blue_2d = extract_channels(img)
    red_only, green_only, blue_only = build_single_channel_images(img, red_2d, green_2d, blue_2d)

    print_report(img, red_2d, green_2d, blue_2d)

    fig, axes = plt.subplots(2, 3, figsize=(13, 7))

    top_row = [(red_only, "Red-Only"), (green_only, "Green-Only"), (blue_only, "Blue-Only")]
    for col, (channel_img, title) in enumerate(top_row):
        axes[0, col].imshow(channel_img)
        axes[0, col].set_title(title)
        axes[0, col].axis("off")

    bottom_row = [
        (red_2d, "Red Channel (Grayscale)"),
        (green_2d, "Green Channel (Grayscale)"),
        (blue_2d, "Blue Channel (Grayscale)"),
    ]
    for col, (channel_2d, title) in enumerate(bottom_row):
        axes[1, col].imshow(channel_2d, cmap="gray")
        axes[1, col].set_title(title)
        axes[1, col].axis("off")

    fig.suptitle("Task 3: RGB Channel Extraction & Isolation",
                  fontsize=14, fontweight="bold")
    fig.tight_layout()
    fig.savefig(save_path, dpi=150)
    plt.close(fig)


if __name__ == "__main__":
    main()
