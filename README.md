# GIF Creator Using Python

## Overview
This Python project generates a GIF from a sequence of images using the `imageio` library. The script reads images from a specified list, converts them into frames, and then saves them as a GIF file.

## Prerequisites
Ensure you have Python installed on your system. Additionally, install the required library before running the script:

```sh
pip install imageio
```

## Project Structure
```
project-folder/
│-- gif using python/
│   │-- dog bottom.png
│   │-- dog top.png
│-- script.py  # (your main Python script)
│-- dog.gif  # (generated output file)
```

## Usage
1. Place the images you want to include in the GIF inside the `gif using python` folder.
2. Update the `filenames` list in the script to include the correct image file paths.
3. Run the script:

```sh
python script.py
```

4. The generated GIF file (`dog.gif`) will be created in the project directory.

## Code Explanation
```python
import imageio as iio

# List of image file paths
filenames = ['gif using python/dog bottom.png', 'gif using python/dog top.png']
images = []

# Read each image and append to the list
for i in filenames:
    images.append(iio.imread(i))

# Save the images as a GIF with a duration of 500ms per frame
iio.mimsave('dog.gif', images, duration=500, loop=0)
```

- The script reads images from the `filenames` list.
- It appends each image to the `images` list.
- The `mimsave` function creates a GIF with a frame duration of 500ms and loops infinitely.

## Notes
- Ensure the image paths are correct, and the images exist in the specified directory.
- You can modify the `duration` parameter to adjust the frame speed.
- The `loop=0` parameter ensures the GIF loops indefinitely. Change it if needed.

## License
This project is open-source and available for personal and educational use.

