
import numpy as np


def build_quadrant_image(h: int = 300, w: int = 400, c: int = 3) -> np.ndarray:
    img = np.zeros((h, w, c), dtype=np.uint8)

    mid_h, mid_w = h // 2, w // 2

    img[0:mid_h, 0:mid_w] = [255, 0, 0]        # Top-Left: Red
    img[0:mid_h, mid_w:w] = [0, 255, 0]        # Top-Right: Green
    img[mid_h:h, 0:mid_w] = [0, 0, 255]        # Bottom-Left: Blue
    img[mid_h:h, mid_w:w] = [255, 255, 255]    # Bottom-Right: White

    return img


def print_report(img: np.ndarray) -> None:
    print("--- SYNTHETIC MATRIX METRICS ---")
    print(f"Array Shape (H, W, C) : {img.shape}")
    print(f"Data Type             : {img.dtype}")
    print(f"Total Elements        : {img.size:,} values")
    print(f"Memory Footprint      : {img.nbytes:,} bytes ({img.nbytes/1024:.2f} KB)")


def main():
    img = build_quadrant_image()
    print_report(img)
    return img


if __name__ == "__main__":
    main()
