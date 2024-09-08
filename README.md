

# PDF to Images Converter

![PDF to Images Converter](https://img.shields.io/badge/PDF%20to%20Images%20Converter-v1.0-blue)

## Overview

**PDF to Images Converter** is a lightweight web application powered by Streamlit, designed to convert PDF files into high-quality images. Users can download individual images, all pages as a ZIP file, or create a collage of selected pages for easy sharing. The tool is ideal for anyone looking to extract visual content from PDFs quickly and efficiently.

## Features

- **PDF to Image Conversion**: Convert every page of a PDF document into high-quality PNG images.
- **Bulk Download**: Download all converted images as a ZIP file for convenience.
- **Collage Maker**: Create a collage from the first few PDF pages to share an overview.
- **Streamlit-Powered UI**: Simple and intuitive web interface for fast and easy use.

## Installation

### Prerequisites

- Python 3.6 or higher
- Poppler for `pdf2image` dependency (installation instructions below)

### Installation Steps

1. **Clone the repository**:
   
   ```bash
   git clone https://github.com/SauravSrivastav/pdf-to-images-converter.git
   cd pdf-to-images-converter
   ```

2. **Install dependencies**:
   
   Install the required Python packages by running:
   
   ```bash
   pip install -r requirements.txt
   ```

3. **Install Poppler**:
   
   - **Linux**: `sudo apt-get install poppler-utils`
   - **macOS**: `brew install poppler`
   - **Windows**: Download Poppler [here](https://blog.alivate.com.au/poppler-windows/) and add the `bin` directory to your system PATH.

4. **Run the Application**:
   
   Start the Streamlit app by executing the following command:
   
   ```bash
   streamlit run app.py
   ```

   Navigate to the provided local URL (e.g., `http://localhost:8501`) in your browser to use the app.

## Usage

1. **Upload a PDF**: Select and upload the PDF file using the interface.
2. **View Converted Images**: The app will display the PDF pages as images.
3. **Download Options**:
   - Download individual images directly.
   - Download all images as a compressed ZIP file.
   - Generate and download a collage of the first few pages.

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/SauravSrivastav/pdf-to-images-converter/issues).

If you'd like to contribute, please fork the repository and make your changes in a feature branch before submitting a pull request.

## License

This project is licensed under the MIT License. For more details, refer to the [LICENSE](LICENSE) file.

## Contact

Have any questions or suggestions? Reach out to me:

- **Email**: [Sauravsrivastav2205@gmail.com](mailto:Sauravsrivastav2205@gmail.com)
- **LinkedIn**: [Saurav Srivastav](https://www.linkedin.com/in/sauravsrivastav2205)
- **GitHub**: [SauravSrivastav](https://github.com/SauravSrivastav)

## Acknowledgements

Thanks to the Streamlit and `pdf2image` communities for providing the core tools used in this project.

