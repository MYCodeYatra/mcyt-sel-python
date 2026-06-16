import os
import time
from PyPDF2 import PdfReader
from selenium.webdriver.common.by import By
def test_invoice_pdf_contents(driver):
    # 1. UI ACTION: Trigger the Download
    driver.get("https://mycodeyatra.com/orders/latest")
    driver.find_element(By.ID, "download-invoice-btn").click()
    # Wait for the file to download completely
    time.sleep(3) 
    # 2. LOCATE THE FILE
    # In a real framework, you should configure your WebDriver download directory
    # and fetch the most recently created file programmatically.
    download_dir = "/Users/qa/Downloads/"
    pdf_path = os.path.join(download_dir, "invoice_INV-8890.pdf")
    assert os.path.exists(pdf_path), "PDF Invoice failed to download!"
    # 3. DOCUMENT ASSERTION: Parse the PDF
    print(f"\n[Validation] Opening PDF: {pdf_path}")
    with open(pdf_path, 'rb') as file:
        pdf = PdfReader(file)
        # Verify it's not a blank document
        num_pages = len(pdf.pages)
        assert num_pages > 0, "The generated PDF is completely blank!"
        # Extract text from the first page
        first_page = pdf.pages[0]
        pdf_text = first_page.extract_text()
        print("\n--- Extracted PDF Content ---")
        print(pdf_text[:200]) # Print first 200 characters for debugging
        print("-----------------------------\n")
        # 4. CRITICAL ASSERTIONS
        assert "Invoice #INV-8890" in pdf_text, "Incorrect Invoice Number!"
        assert "Total: $1,450.00" in pdf_text, "Financial Total is incorrect!"
        assert "Status: PAID" in pdf_text, "Payment status is wrong!"