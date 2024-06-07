# pdf2-500.py
#  needs pip install pdfminer.six
import os
import glob
from pdfminer.high_level import extract_text

def main():
    # Specify the input directory containing PDF files
    input_dir = '/Users/hugodiaz/RIDOT/2017'
    # Specify the output directory for the new text files
    output_dir = '/Users/hugodiaz/RIDOT/small'

    pdf_files = glob.glob(os.path.join(input_dir, '*.pdf'))
    total_pdf_count = len(pdf_files)

    # Create a new text file for every 100 PDF files  ## Change the count to 200?##
    chunk_size = 100
    for i in range(0, total_pdf_count, chunk_size):
        chunk_pdf_files = pdf_files[i:i + chunk_size]
        output_text_path = os.path.join(output_dir, f'text_{i // chunk_size}.txt')

        with open(output_text_path, 'w') as output_text_file:
            for pdf_file in chunk_pdf_files:
                extracted_text = extract_text(pdf_file)
                output_text_file.write(extracted_text + '\n')

        print(f"Created text file '{output_text_path}' with {len(chunk_pdf_files)} PDF files.")

if __name__ == "__main__":
    main()

