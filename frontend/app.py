import streamlit as st
import sys
import os

# Add backend directory to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../backend')))
from qr_processor import generate_qr_code, decode_qr_code

st.set_page_config(
    page_title="QR Code Generator & Scanner",
    page_icon="🔲",
    layout="centered"
)

st.title("🔲 QR Code Generator and Scanner")
st.write("Easily generate custom QR codes or decode existing ones instantly.")

# Create tabs for Generate and Scan features
tab1, tab2 = st.tabs(["✨ Generate QR Code", "📷 Scan / Decode QR Code"])

with tab1:
    st.subheader("Generate QR Code from Text or URL")
    qr_text = st.text_area("Enter text, link, or data to encode:", placeholder="https://example.com")
    output_filename = st.text_input("Output filename:", value="qrcode.png")
    
    if st.button("Generate QR Code"):
        if not qr_text.strip():
            st.error("Please enter valid text or URL to generate a QR code.")
        else:
            with st.spinner("Generating QR code..."):
                qr_bytes = generate_qr_code(qr_text)
                st.success("QR Code generated successfully!")
                
                # Display Image Preview
                st.image(qr_bytes, caption="Generated QR Code Preview", width=250)
                
                # Download Button
                st.download_button(
                    label="Download QR Code Image",
                    data=qr_bytes,
                    file_name=output_filename,
                    mime="image/png"
                )

with tab2:
    st.subheader("Decode QR Code from Image")
    uploaded_file = st.file_uploader("Upload QR Code image (.png or .jpg)", type=["png", "jpg", "jpeg"])
    
    if uploaded_file is not None:
        st.image(uploaded_file, caption="Uploaded Image", width=250)
        
        if st.button("Decode QR Code"):
            with st.spinner("Decoding image..."):
                image_bytes = uploaded_file.read()
                decoded_text = decode_qr_code(image_bytes)
                
                if decoded_text.startswith("Error"):
                    st.error(decoded_text)
                else:
                    st.success("QR Code Decoded Successfully!")
                    st.text_area("Extracted Data:", value=decoded_text, height=100)

# Privacy Notice
st.markdown("---")
st.markdown("### 🔒 Privacy Notice")
st.info("Your data is processed dynamically in-memory. The application **does not permanently store** your generated text or uploaded images.")
