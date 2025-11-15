#!/usr/bin/env python3
"""
Step 1: Extract Source Content

This script extracts content from various sources (papers, articles, docs).
Supports:
- arXiv papers (PDF)
- Web pages (HTML)
- Local files (PDF, TXT, MD)
"""

import argparse
import os
import subprocess
import sys
from pathlib import Path
import requests
from urllib.parse import urlparse


def extract_arxiv_paper(arxiv_url: str, output_dir: str) -> str:
    """
    Extract text from an arXiv paper.
    
    Args:
        arxiv_url: URL to arXiv paper (abs or pdf)
        output_dir: Directory to save extracted text
        
    Returns:
        Path to extracted text file
    """
    # Convert abs URL to PDF URL if needed
    if '/abs/' in arxiv_url:
        pdf_url = arxiv_url.replace('/abs/', '/pdf/') + '.pdf'
    else:
        pdf_url = arxiv_url
    
    # Download PDF
    print(f"Downloading PDF from {pdf_url}...")
    response = requests.get(pdf_url)
    response.raise_for_status()
    
    pdf_path = os.path.join(output_dir, 'source.pdf')
    with open(pdf_path, 'wb') as f:
        f.write(response.content)
    
    # Extract text using pdftotext
    print("Extracting text from PDF...")
    txt_path = os.path.join(output_dir, 'source.txt')
    subprocess.run(['pdftotext', pdf_path, txt_path], check=True)
    
    print(f"✅ Text extracted to: {txt_path}")
    return txt_path


def extract_webpage(url: str, output_dir: str) -> str:
    """
    Extract text from a web page.
    
    Args:
        url: URL to web page
        output_dir: Directory to save extracted text
        
    Returns:
        Path to extracted text file
    """
    print(f"Fetching content from {url}...")
    response = requests.get(url)
    response.raise_for_status()
    
    # Simple text extraction (you might want to use BeautifulSoup for better results)
    from html.parser import HTMLParser
    
    class TextExtractor(HTMLParser):
        def __init__(self):
            super().__init__()
            self.text = []
        
        def handle_data(self, data):
            if data.strip():
                self.text.append(data.strip())
    
    parser = TextExtractor()
    parser.feed(response.text)
    
    txt_path = os.path.join(output_dir, 'source.txt')
    with open(txt_path, 'w') as f:
        f.write('\n\n'.join(parser.text))
    
    print(f"✅ Text extracted to: {txt_path}")
    return txt_path


def extract_local_file(file_path: str, output_dir: str) -> str:
    """
    Extract text from a local file.
    
    Args:
        file_path: Path to local file
        output_dir: Directory to save extracted text
        
    Returns:
        Path to extracted text file
    """
    file_path = Path(file_path)
    
    if file_path.suffix == '.pdf':
        print(f"Extracting text from PDF: {file_path}...")
        txt_path = os.path.join(output_dir, 'source.txt')
        subprocess.run(['pdftotext', str(file_path), txt_path], check=True)
    elif file_path.suffix in ['.txt', '.md']:
        print(f"Copying text file: {file_path}...")
        txt_path = os.path.join(output_dir, 'source.txt')
        with open(file_path, 'r') as src, open(txt_path, 'w') as dst:
            dst.write(src.read())
    else:
        raise ValueError(f"Unsupported file type: {file_path.suffix}")
    
    print(f"✅ Text extracted to: {txt_path}")
    return txt_path


def main():
    parser = argparse.ArgumentParser(
        description='Extract content from various sources'
    )
    parser.add_argument(
        'source',
        help='URL or file path to extract from'
    )
    parser.add_argument(
        '--output-dir',
        default='./extracted',
        help='Directory to save extracted content'
    )
    
    args = parser.parse_args()
    
    # Create output directory
    os.makedirs(args.output_dir, exist_ok=True)
    
    # Determine source type and extract
    if args.source.startswith('http'):
        parsed = urlparse(args.source)
        if 'arxiv.org' in parsed.netloc:
            extract_arxiv_paper(args.source, args.output_dir)
        else:
            extract_webpage(args.source, args.output_dir)
    else:
        extract_local_file(args.source, args.output_dir)
    
    return 0


if __name__ == '__main__':
    sys.exit(main())
