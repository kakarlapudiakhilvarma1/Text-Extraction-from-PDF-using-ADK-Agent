# Text-Extraction-from-PDF-using-ADK-Agent

A simple and efficient PDF text extraction tool built using Google's Agent Development Kit (ADK) and Gemini 2.0 Flash model. This project demonstrates how to create an AI agent that can extract text from PDF files with minimal processing overhead.

## 🚀 Features

- **Simple PDF Text Extraction**: Clean text extraction from PDF files using PyPDF2
- **AI-Powered Agent**: Built with Google's ADK and Gemini 2.0 Flash model
- **Error Handling**: Robust error handling for various PDF formats and edge cases
- **File Information**: Basic file metadata extraction (size, filename)
- **JSON Serializable Output**: All responses are JSON serializable for easy integration

## 📋 Prerequisites

Before running this project, ensure you have:

- Python 3.7+
- Google API Key with access to Gemini models
- Required Python packages (see Installation section)

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/kakarlapudiakhilvarma1/Text-Extraction-from-PDF-using-ADK-Agent.git
   cd Text-Extraction-from-PDF-using-ADK-Agent
   ```

2. **Install required dependencies**
   ```bash
   pip install google-adk PyPDF2
   ```

3. **Set up environment variables**
   
   Create a `.env` file in the root directory and add your Google API key:
   ```env
   GOOGLE_API_KEY = "your_google_api_key_here"
   GOOGLE_GENAI_USE_VERTEXTAI = FALSE
   ```

## 🏗️ Project Structure

```
├── .env                    # Environment variables
├── agent.py               # Main agent configuration
├── tools.py               # PDF extraction and utility functions
├── __init__.py            # Package initialization
└── README.md              # This file
```

## 📖 Usage

### Basic Usage

```python
from your_package.agent import root_agent

# The agent automatically handles PDF text extraction
# Example usage would depend on how you invoke the ADK agent
```

### Available Tools

The agent comes with two main tools:

#### 1. `extract_pdf_text(file_path)`
Extracts text content from PDF files.

**Parameters:**
- `file_path` (str): Path to the PDF file

**Returns:**
- Dictionary with status, message, and extracted text

**Example Response:**
```json
{
    "status": "success",
    "message": "Extracted text from 5 pages",
    "text": "Your extracted PDF content here..."
}
```

#### 2. `get_simple_info(file_path)`
Retrieves basic file information.

**Parameters:**
- `file_path` (str): Path to the file

**Returns:**
- Dictionary with file metadata

**Example Response:**
```json
{
    "status": "success",
    "filename": "document.pdf",
    "size_bytes": 1048576,
    "size_mb": 1.0
}
```

## 🔧 Configuration

### Agent Configuration

The agent is configured in `agent.py` with the following settings:

- **Name**: `simple_pdf_extractor`
- **Model**: `gemini-2.0-flash`
- **Purpose**: Simple PDF text extraction without analysis

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `GOOGLE_API_KEY` | Your Google API key for Gemini access | Yes |
| `GOOGLE_GENAI_USE_VERTEXTAI` | Whether to use Vertex AI (set to FALSE for standard API) | Yes |

## ⚠️ Error Handling

The tool includes comprehensive error handling for:

- **File Not Found**: Returns error when PDF file doesn't exist
- **Invalid File Type**: Validates that the file is actually a PDF
- **Corrupted PDFs**: Handles PDFs that can't be processed
- **Empty PDFs**: Manages PDFs with no extractable text
- **Page-level Errors**: Skips problematic pages and continues processing

## 🎯 Use Cases

This tool is perfect for:

- **Document Processing Pipelines**: Integrate into larger document processing workflows
- **Content Analysis**: Extract text for further AI analysis
- **Data Migration**: Convert PDF archives to text format
- **Research Tools**: Extract text from academic papers and reports
- **Compliance**: Extract text from regulatory documents

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🐛 Troubleshooting

### Common Issues

**Issue**: "File not found" error
- **Solution**: Verify the file path is correct and the file exists

**Issue**: "Not a PDF file" error  
- **Solution**: Ensure the file has a `.pdf` extension and is a valid PDF

**Issue**: "No text found in PDF" warning
- **Solution**: The PDF might be image-based or have no selectable text

**Issue**: Google API authentication errors
- **Solution**: Verify your API key is correct in the `.env` file

## 📧 Support

For questions and support:
- Open an issue on GitHub
- Check existing issues for solutions
- Review the troubleshooting section

## 🙏 Acknowledgments

- Google ADK team for the Agent Development Kit
- PyPDF2 contributors for the PDF processing library
- Gemini 2.0 Flash model for AI capabilities

---

**Note**: This tool extracts text only and does not perform analysis or processing of the content. For advanced PDF processing needs, consider extending the agent with additional tools and capabilities.
