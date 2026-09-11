
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


def downsample(img: np.ndarray, n: int) -> np.ndarray:
    return img[::n, ::n, :]


def re_expand(down_img: np.ndarray, n: int) -> np.ndarray:
    expanded = np.repeat(down_img, n, axis=0)
    expanded = np.repeat(expanded, n, axis=1)
    return expanded


def print_report(img: np.ndarray, down_img: np.ndarray, expanded: np.ndarray, n: int):
    orig_h, orig_w = img.shape[:2]
    down_h, down_w = down_img.shape[:2]

    dim_reduction = (1 - (down_h * down_w) ** 0.5 / (orig_h * orig_w) ** 0.5) * 100
    # per-axis reduction: e.g. 1080->135 and 1920->240 at N=8 is 87.5% per axis
    per_axis_reduction = (1 - 1 / n) * 100
    mem_savings = (1 - down_img.nbytes / img.nbytes) * 100

    print(f"--- DOWNSAMPLING ANALYSIS (N = {n}) ---")
    print(f"Original Shape     : {img.shape} | Memory: {img.nbytes:,} bytes")
    print(f"Downsampled Shape  : {down_img.shape} | Memory: {down_img.nbytes:,} bytes")
    print(f"Re-expanded Shape  : {expanded.shape} | Visual: Blocky Pixelation")
    print(f"Dimension Reduction: {per_axis_reduction:.2f}% reduction per axis")
    print(f"Memory Savings     : {mem_savings:.2f}% data reduction")


def main(path="sample.jpg", n=8, save_path="task4_downsample.png"):
    img = np.array(Image.open(path).convert("RGB"))
    down_img = downsample(img, n)
    expanded = re_expand(down_img, n)

    print_report(img, down_img, expanded, n)

    fig, axes = plt.subplots(1, 2, figsize=(13, 5.2))
    axes[0].imshow(img)
    axes[0].set_title(f"Original — {img.shape[1]}x{img.shape[0]}")
    axes[0].axis("off")

    axes[1].imshow(expanded)
    axes[1].set_title(f"Downsampled (N={n}) & Re-expanded — Pixelated")
    axes[1].axis("off")

    fig.suptitle("Task 4: Spatial Downsampling via NumPy Striding",
                  fontsize=14, fontweight="bold")
    fig.tight_layout()
    fig.savefig(save_path, dpi=150)
    plt.close(fig)


if __name__ == "__main__":
    main()
