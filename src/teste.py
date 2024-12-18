import requests
import pdfplumber
import io

def download_pdf(url):
    # Send a GET request to the URL to download the PDF
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        return response.content  # Return the PDF content
    else:
        raise Exception(f"Failed to download PDF. Status code: {response.status_code}")

def extract_text_from_pdf(pdf_content):
    # Use pdfplumber to open the PDF content
    with pdfplumber.open(io.BytesIO(pdf_content)) as pdf:
        text = ''
        # Iterate through each page and extract text
        for page in pdf.pages:
            text += page.extract_text()
    return text

def online_pdf_to_text(url):
    try:
        # Download PDF content
        pdf_content = download_pdf(url)
        
        # Extract text from the downloaded PDF content
        text = extract_text_from_pdf(pdf_content)
        
        return text
    except Exception as e:
        return str(e)

# Example usage
url = 'https://www.softouch.on.ca/kb/data/Atomic%20Design.pdf'  # Replace with the actual PDF URL
plain_text = online_pdf_to_text(url)

print(plain_text)  # Output the extracted text
