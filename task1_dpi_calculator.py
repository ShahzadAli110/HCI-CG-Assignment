
import math

def compute_display_metrics(w_px: int, h_px: int, d_inches: float) -> dict:
    """Compute total pixels, aspect ratio, and DPI for a display."""
    total_pixels = w_px * h_px

    divisor = math.gcd(w_px, h_px)
    aspect_ratio = f"{w_px // divisor}:{h_px // divisor}"

    diagonal_px = math.sqrt(w_px ** 2 + h_px ** 2)
    dpi = diagonal_px / d_inches

    if dpi < 100:
        category = "Low Density (Standard Monitor)"
    elif dpi <= 200:
        category = "Medium Density (HD Display)"
    else:
        category = "High Density (Retina / Mobile)"

    return {
        "total_pixels": total_pixels,
        "aspect_ratio": aspect_ratio,
        "dpi": round(dpi, 2),
        "category": category,
    }


def print_report(w_px: int, h_px: int, d_inches: float) -> None:
    m = compute_display_metrics(w_px, h_px, d_inches)
    print("--- DISPLAY METRICS ANALYSIS ---")
    print(f"Total Pixel Count : {m['total_pixels']:,} pixels")
    print(f"Aspect Ratio      : {m['aspect_ratio']}")
    print(f"Calculated DPI    : {m['dpi']:.2f} DPI")
    print(f"Density Category  : {m['category']}")


def main():
    w_px = int(input("Enter horizontal resolution (pixels): "))
    h_px = int(input("Enter vertical resolution (pixels): "))
    d_inches = float(input("Enter physical diagonal size (inches): "))
    print()
    print_report(w_px, h_px, d_inches)


if __name__ == "__main__":
    main()
