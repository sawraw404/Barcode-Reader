# 📊 Barcode Reader - Custom Barcode Encoder & Decoder

A Python-based custom barcode encoding and decoding system with an interactive Streamlit web interface. This project allows you to convert text into unique visual barcodes and decode them back to text.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.31.0-red.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## 🌐 Live Demo

Try the application online: **[Barcode Reader Web App](https://barcode-reader-1001.streamlit.app/)**

## 🌟 Features

- **Text to Barcode Encoding**: Convert any text (letters and spaces) into a custom barcode format
- **Barcode to Text Decoding**: Upload barcode images and decode them back to original text
- **Interactive Web Interface**: User-friendly Streamlit app for easy encoding/decoding
- **Download Capability**: Save generated barcodes as PNG images
- **Custom Algorithm**: Unique encoding scheme where each letter has a different bar width

## 🎯 How It Works

### Encoding Algorithm
- Each letter (a-z) is represented by a black bar with width proportional to its position in the alphabet
  - 'a' = 1 pixel wide
  - 'b' = 2 pixels wide
  - ...
  - 'z' = 26 pixels wide
- Spaces are represented by shorter bars (height 150-250 vs 10-350 for letters)
- Bars are separated by 9 pixels of white space

### Decoding Algorithm
1. Converts the image to grayscale and reads the middle row
2. Identifies black bars representing letters
3. Measures bar widths to determine which letter each represents
4. Analyzes white space gaps to identify word boundaries
5. Reconstructs the original text

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/sawraw404/Barcode-Reader.git
cd Barcode-Reader
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

### Running the Application

#### Option 1: Streamlit Web App (Recommended)
```bash
streamlit run app.py
```
Then open your browser to `http://localhost:8501`

#### Option 2: Command Line Scripts

**Encode text to barcode:**
```bash
python encode.py
```
This will generate `output.png` with the encoded barcode.

**Decode barcode to text:**
```bash
python decode.py
```
This will read `output.png` and print the decoded text.

## 📁 Project Structure

```
Barcode-Reader/
├── app.py              # Streamlit web application
├── encode.py           # Command-line encoder script
├── decode.py           # Command-line decoder script
├── requirements.txt    # Python dependencies
├── README.md          # Project documentation
└── output.png         # Sample barcode output
```

## 💻 Usage Examples

### Using the Web Interface

1. **Encoding:**
   - Enter your text in the input field
   - Click "Generate Barcode"
   - Download the generated barcode image

2. **Decoding:**
   - Switch to the "Decode Barcode" tab
   - Upload a barcode image
   - Click "Decode Barcode" to see the original text

### Using Python Scripts

**Encoding:**
```python
from encode import encode

# Encode text to barcode
encode("Your Text Here")
# Saves to output.png
```

**Decoding:**
```python
from decode import decode

# Decode barcode image
text = decode("output.png")
print(text)
```

## 🛠️ Technologies Used

- **Python**: Core programming language
- **Streamlit**: Web interface framework
- **Pillow (PIL)**: Image processing
- **NumPy**: Array operations and image manipulation

## 📸 Screenshots

### Encoding Interface
*Convert text to custom barcodes with a single click*

### Decoding Interface
*Upload and decode barcode images instantly*

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/improvement`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add new feature'`)
5. Push to the branch (`git push origin feature/improvement`)
6. Create a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Syeda Sara Afzaal**
- GitHub: [@sawraw404](https://github.com/sawraw404)

## 🙏 Acknowledgments

- Thanks to the Streamlit team for their amazing framework
- Inspired by traditional barcode systems with a custom twist

## 📧 Contact

For questions or feedback, please open an issue on GitHub or reach out through the repository.

---

⭐ If you found this project helpful, please give it a star!
