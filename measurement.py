def calculate_dimensions(raw_images, scale):
    h, w, _ = raw_images.shape

    width_mm = w * scale
    height_mm = h * scale

    return width_mm, height_mm