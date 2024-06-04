#### Day 91: Portfolio Project - Image Colour Palette Generator
**Challenge:** Create a program that generates a color palette from an image.

```python
from PIL import Image
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import numpy as np

def get_palette(image_path, n_colors=5):
    image = Image.open(image_path)
    image = image.resize((image.width // 10, image.height // 10))
    pixels = np.array(image).reshape(-1, 3)
    kmeans = KMeans(n_clusters=n_colors)
    kmeans.fit(pixels)
    palette = kmeans.cluster_centers_.astype(int)
    return palette

def plot_palette(palette):
    plt.figure(figsize=(8, 2))
    plt.imshow([palette], aspect='auto')
    plt.axis('off')
    plt.show()

image_path = 'image.jpg'
palette = get_palette(image_path)
plot_palette(palette)
```


