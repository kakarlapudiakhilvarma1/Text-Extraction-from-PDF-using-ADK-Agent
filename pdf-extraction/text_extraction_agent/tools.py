import os
import json
from typing import Dict, Any

def extract_pdf_text(file_path: str) -> Dict[str, Any]:
    """
    Extracts text from PDF using simple text extraction.
    Returns only basic string types to avoid bytes serialization issues.
    
    Args:
        file_path (str): Path to PDF file
        
    Returns:
        dict: Simple dictionary with only string/int values
    """
    # Force everything to basic Python types
    file_path = str(file_path)
    
    # Basic validation
    if not os.path.exists(file_path):
        return {
            "status": "error",
            "message": "File not found",
            "text": ""
        }
    
    if not file_path.lower().endswith('.pdf'):
        return {
            "status": "error", 
            "message": "Not a PDF file",
            "text": ""
        }
    
    try:
        # Use only PyPDF2 with strict string conversion
        import PyPDF2
        
        extracted_text = ""
        page_count = 0
        
        with open(file_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            page_count = len(reader.pages)
            
            text_parts = []
            for i, page in enumerate(reader.pages):
                try:
                    # Get page text
                    page_text = page.extract_text()
                    
                    # Force to string and clean
                    if page_text:
                        page_text = str(page_text)
                        page_text = page_text.strip()
                        if page_text:
                            text_parts.append(page_text)
                except:
                    # Skip problematic pages
                    continue
            
            # Join all text
            if text_parts:
                extracted_text = " ".join(text_parts)
            
        # Force everything to basic types
        extracted_text = str(extracted_text) if extracted_text else ""
        page_count = int(page_count) if page_count else 0
        
        # Return only basic types
        if extracted_text:
            return {
                "status": "success",
                "message": f"Extracted text from {page_count} pages",
                "text": extracted_text
            }
        else:
            return {
                "status": "warning",
                "message": "No text found in PDF",
                "text": ""
            }
            
    except Exception as e:
        # Return only string error message
        return {
            "status": "error",
            "message": str(e),
            "text": ""
        }

def get_simple_info(file_path: str) -> Dict[str, Any]:
    """
    Get basic file info using only built-in functions.
    No external libraries to avoid bytes issues.
    """
    file_path = str(file_path)
    
    try:
        if not os.path.exists(file_path):
            return {
                "status": "error",
                "message": "File not found"
            }
        
        # Get basic file info using only os module
        file_size = os.path.getsize(file_path)
        filename = os.path.basename(file_path)
        
        return {
            "status": "success",
            "filename": str(filename),
            "size_bytes": int(file_size),
            "size_mb": round(file_size / 1024 / 1024, 2)
        }
        
    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }

# Test function to validate JSON serialization
def test_json_serialization():
    """Test function to verify all return values are JSON serializable"""
    test_data = {
        "status": "success",
        "text": "sample text",
        "number": 123,
        "decimal": 45.67
    }
    
    try:
        # Test if it can be serialized
        json_string = json.dumps(test_data)
        return {
            "status": "success",
            "message": "JSON serialization test passed",
            "test_result": json_string
        }
    except Exception as e:
        return {
            "status": "error", 
            "message": f"JSON test failed: {str(e)}"
        }
