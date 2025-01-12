import streamlit as st
import cloudinary
import cloudinary.uploader
import cloudinary.api
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def upload_image_to_cloudinary(image_file):
    try:
        response = cloudinary.uploader.upload(image_file)
        return response['secure_url']
    except Exception as e:
        st.error(f"ไม่สามารถอัปโหลดรูปภาพได้: {str(e)}")
        return None

def display_image(image_url, size=150):
    try:
        st.image(image_url, width=size)
    except Exception as e:
        st.error(f"ไม่สามารถแสดงรูปภาพได้: {str(e)}")
       
# Configure Cloudinary
cloudinary.config(
    cloud_name=os.getenv('CLOUDINARY_CLOUD_NAME'),
    api_key=os.getenv('CLOUDINARY_API_KEY'),
    api_secret=os.getenv('CLOUDINARY_API_SECRET')
)
