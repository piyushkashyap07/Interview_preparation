from PIL import Image, ImageSequence

# Load your images
image_paths = [r"C:\Piyush\Scripts\ModernPortfolioTemplate-master\assets\img\piyushkashyap.jpeg", r"C:\Piyush\Scripts\ModernPortfolioTemplate-master\assets\img\pk.jpeg"]  # Provide paths to your images
images = [Image.open(path) for path in image_paths]

# Resize images to fit 500x500
for i in range(len(images)):
    images[i] = images[i].resize((500, 500), Image.ANTIALIAS)

# Create a new GIF
gif_path = "output.gif"
images[0].save(gif_path, save_all=True, append_images=images[1:], optimize=False, duration=500, loop=0)

print("GIF created successfully.")
