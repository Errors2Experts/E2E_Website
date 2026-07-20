import base64
import requests

def upload_image_to_imgbb(image_file):
    """
    Uploads an image file object to ImgBB and returns the hosted image URL string.
    """
    if not image_file:
        return None
        
    # If it's already an ImgBB URL string, leave it alone
    if isinstance(image_file, str) and image_file.startswith('http'):
        return image_file

    url = "https://api.imgbb.com/1/upload"
    api_key = "577c33696a252420e3730792fad0ef13"
    
    try:
        if hasattr(image_file, 'read'):
            image_file.seek(0)
            file_bytes = image_file.read()
        else:
            return None
            
        encoded_image = base64.b64encode(file_bytes)
        
        payload = {
            'key': api_key,
            'image': encoded_image,
        }
        
        response = requests.post(url, data=payload, timeout=30)
        result = response.json()
        
        if result.get('success'):
            return result['data']['url']
    except Exception as e:
        print(f"ImgBB upload error: {e}")
        
    return None