import streamlit as st
import tempfile
import os
import sys
import subprocess
import zipfile
import io
import logging
from PIL import Image

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def install_pdf2image():
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pdf2image"])
        logger.info("Successfully installed pdf2image")
    except subprocess.CalledProcessError:
        logger.error("Failed to install pdf2image")
        st.error("Failed to install required dependency. Please try again or install manually.")
        sys.exit(1)

try:
    from pdf2image import convert_from_bytes
except ImportError:
    st.warning("Installing required dependency: pdf2image")
    install_pdf2image()
    from pdf2image import convert_from_bytes

def convert_pdf_to_images(pdf_bytes, dpi=300):
    try:
        images = convert_from_bytes(pdf_bytes, dpi=dpi)
        return images
    except Exception as e:
        logger.error(f"Error converting PDF to images: {str(e)}")
        st.error("Failed to convert PDF to images. Please try again with a different file.")
        return None

def save_images(images, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    image_paths = []
    for i, image in enumerate(images):
        image_path = os.path.join(output_folder, f"page_{i + 1}.png")
        image.save(image_path, 'PNG')
        st.image(image_path, caption=f"Page {i + 1}", use_column_width=True)
        image_paths.append(image_path)
    return image_paths

def create_zip_file(image_paths):
    zip_buffer = io.BytesIO()
    with zipfile.ZipFile(zip_buffer, "w") as zip_file:
        for image_path in image_paths:
            zip_file.write(image_path, os.path.basename(image_path))
    return zip_buffer.getvalue()

def create_collage(images, max_images=4, orientation='horizontal'):
    # Determine the size of the collage
    num_images = min(len(images), max_images)
    if orientation == 'horizontal':
        cols = num_images
        rows = 1
    else:  # vertical
        cols = 1
        rows = num_images

    # Calculate the size of each thumbnail
    thumb_width = 300
    thumb_height = 300

    # Create a new image with a white background
    collage_width = thumb_width * cols
    collage_height = thumb_height * rows
    collage = Image.new('RGB', (collage_width, collage_height), (255, 255, 255))

    # Paste the thumbnails into the collage
    for i, img in enumerate(images[:num_images]):
        img.thumbnail((thumb_width, thumb_height))
        x = (i % cols) * thumb_width
        y = (i // cols) * thumb_height
        collage.paste(img, (x, y))

    return collage

def main():
    st.set_page_config(page_title="PDF to Images Converter", page_icon="📄")
    st.title("PDF to Images Converter")

    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

    if uploaded_file is not None:
        st.write("Converting PDF to images...")

        pdf_bytes = uploaded_file.read()
        images = convert_pdf_to_images(pdf_bytes)

        if images:
            with tempfile.TemporaryDirectory() as temp_dir:
                image_paths = save_images(images, temp_dir)

                st.success("Conversion complete!")

                zip_file = create_zip_file(image_paths)
                st.download_button(
                    label="Download All Images as ZIP",
                    data=zip_file,
                    file_name="converted_images.zip",
                    mime="application/zip"
                )

                for i, image_path in enumerate(image_paths):
                    with open(image_path, "rb") as file:
                        st.download_button(
                            label=f"Download Page {i+1}",
                            data=file,
                            file_name=f"page_{i+1}.png",
                            mime="image/png"
                        )

                # Create and display collage
                st.subheader("Image Collage")
                orientation = st.radio("Choose collage orientation:", ('Horizontal', 'Vertical'))
                collage = create_collage(images, orientation=orientation.lower())
                st.image(collage, caption=f"Collage of first 4 pages ({orientation})", use_column_width=True)

                # Save and provide download for collage
                collage_path = os.path.join(temp_dir, "collage.png")
                collage.save(collage_path, 'PNG')
                with open(collage_path, "rb") as file:
                    st.download_button(
                        label="Download Collage",
                        data=file,
                        file_name="collage.png",
                        mime="image/png"
                    )

    st.markdown("---")
    st.markdown("**Note:** This tool converts PDF files to images and creates a collage of the first 4 pages. For large PDFs, the process may take some time.")

if __name__ == "__main__":
    main()
