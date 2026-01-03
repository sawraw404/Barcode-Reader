import streamlit as st
from PIL import Image
import numpy as np
import io

# Set page config
st.set_page_config(
    page_title="Barcode Encoder/Decoder",
    page_icon="🔲",
    layout="wide"
)

def encode_barcode(text):
    """Encode text into a barcode image"""
    width, height = 400, 800  # Fixed: 400 width x 800 height
    step = 9
    img = np.ones((height, width), dtype=np.uint8) * 255  # white canvas

    x = 0
    encoding_log = []
    
    for ch in text:
        if ch == ' ':
            bar_width = 1
            top, bottom = 150, 250
            encoding_log.append(f"Space: width={bar_width}, x={x}-{x+bar_width}")
        else:
            pos = ord(ch.lower()) - ord('a') + 1  # 'a'=1, 'b'=2, 'c'=3, etc.
            bar_width = pos + 1  # 'a'=2, 'b'=3, 'c'=4, etc.
            top, bottom = 10, 350
            encoding_log.append(f"'{ch}': position={pos}, width={bar_width}, x={x}-{x+bar_width}")

        img[top:bottom, x:x+bar_width] = 0
        x += bar_width + step

    return Image.fromarray(img), encoding_log

def decode_barcode(img):
    """Decode a barcode image to text"""
    img = img.convert("L")  # convert to grayscale
    arr = np.array(img)
    height, width = arr.shape
    scan_row = 200  # Fixed: scan at row 200
    row = arr[scan_row] < 128  # True for black pixels

    decoding_log = []
    decoding_log.append(f"Image size: {width}x{height}")
    decoding_log.append(f"Scanning row: {scan_row}")
    decoding_log.append(f"Black pixels found: {np.sum(row)}")

    # Decode by measuring consecutive black pixel runs
    result = ""
    i = 0
    bar_count = 0
    while i < width:
        if row[i]:  # black pixel
            w = 0
            while i < width and row[i]:
                w += 1
                i += 1
            bar_count += 1
            decoding_log.append(f"Bar {bar_count}: width = {w}")
            if w == 1:
                result += " "
                decoding_log.append(f"  -> Added space")
            else:
                pos = w - 1  # width = pos + 1, so pos = width - 1
                if 1 <= pos <= 26:  # 'a'=1, 'b'=2, ..., 'z'=26
                    char = chr(ord("a") + pos - 1)  # Convert back
                    result += char
                    decoding_log.append(f"  -> Added character: {char}")
                else:
                    result += "?"  # unexpected width
                    decoding_log.append(f"  -> Added ? (unexpected width: {w})")
        else:
            i += 1  # skip white pixels

    decoding_log.append(f"Decoded text: {result}")
    return result, decoding_log

# App title and description
st.title("Barcode Encoder & Decoder")
st.markdown("Convert text to custom barcodes and decode them back!")

# Create tabs
tab1, tab2 = st.tabs(["Encode Text", "Decode Barcode"])

# Encode Tab
with tab1:
    st.header("Encode Text to Barcode")
    
    # Input text
    input_text = st.text_input(
        "Enter text to encode:",
        value="Syeda Sara Afzaal",
        help="Enter any text with letters and spaces"
    )
    
    col1, col2 = st.columns([1, 3])
    
    with col1:
        show_log = st.checkbox("Show encoding details", value=False)
        
        if st.button("Generate Barcode", type="primary", use_container_width=True):
            if input_text:
                with st.spinner("Generating barcode..."):
                    barcode_img, encoding_log = encode_barcode(input_text)
                    st.session_state.barcode_img = barcode_img
                    st.session_state.encoding_log = encoding_log
                    st.success("Barcode generated successfully!")
            else:
                st.warning("Please enter some text to encode")
    
    # Display barcode if generated
    if 'barcode_img' in st.session_state:
        st.image(st.session_state.barcode_img, caption="Generated Barcode (400x800 pixels)", use_container_width=True)
        
        # Show encoding log if checkbox is checked
        if show_log and 'encoding_log' in st.session_state:
            with st.expander("Encoding Details", expanded=True):
                for log_entry in st.session_state.encoding_log:
                    st.code(log_entry, language=None)
        
        # Download button
        buf = io.BytesIO()
        st.session_state.barcode_img.save(buf, format="PNG")
        byte_im = buf.getvalue()
        
        st.download_button(
            label="Download Barcode",
            data=byte_im,
            file_name="barcode.png",
            mime="image/png",
            use_container_width=True
        )
    
    # Explanation
    with st.expander("ℹ️ How does encoding work?"):
        st.markdown("""
        **Encoding Algorithm:**
        - Image dimensions: 400 pixels wide × 800 pixels tall
        - Each letter (a-z) is represented by a black bar:
          - 'a' = position 1 → width 2 pixels
          - 'b' = position 2 → width 3 pixels
          - 'c' = position 3 → width 4 pixels
          - ... and so on up to 'z'
        - Spaces are represented by 1-pixel wide bars (height 150-250)
        - Regular letters have bars with height 10-350
        - Bars are separated by 9 pixels of white space
        - **Scan line at row 200** for decoding
        """)

# Decode Tab
with tab2:
    st.header("Decode Barcode to Text")
    
    # File uploader
    uploaded_file = st.file_uploader(
        "Upload a barcode image:",
        type=['png', 'jpg', 'jpeg'],
        help="Upload a barcode image generated by this app"
    )
    
    if uploaded_file is not None:
        # Display uploaded image
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Uploaded Barcode")
            uploaded_img = Image.open(uploaded_file)
            st.image(uploaded_img, use_container_width=True)
        
        with col2:
            st.subheader("Decoded Text")
            show_decode_log = st.checkbox("Show decoding details", value=False)
            
            if st.button("Decode Barcode", type="primary", use_container_width=True):
                with st.spinner("Decoding barcode..."):
                    decoded_text, decoding_log = decode_barcode(uploaded_img)
                    st.session_state.decoded_text = decoded_text
                    st.session_state.decoding_log = decoding_log
            
            if 'decoded_text' in st.session_state:
                st.success("Decoding complete!")
                st.code(st.session_state.decoded_text, language=None)
                
                # Show decoding log if checkbox is checked
                if show_decode_log and 'decoding_log' in st.session_state:
                    with st.expander("Decoding Details", expanded=True):
                        for log_entry in st.session_state.decoding_log:
                            st.text(log_entry)
    
    # Explanation
    with st.expander("How does decoding work?"):
        st.markdown("""
        **Decoding Algorithm:**
        1. Convert image to grayscale
        2. Scan at **row 200** (middle of the barcode)
        3. Identify black bars and measure their widths
        4. Decode each bar:
           - Width 1 = space
           - Width 2-27 = letters ('a' through 'z')
           - Width = position + 1, so reverse: position = width - 1
        5. Reconstruct the original text from bar measurements
        """)

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center'>
        <p>Made with Streamlit | 
        <a href='https://github.com/sawraw404/Barcode-Reader' target='_blank'>GitHub Repository</a></p>
    </div>
    """,
    unsafe_allow_html=True
)
