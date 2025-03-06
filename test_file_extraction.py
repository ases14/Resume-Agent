# test_file_extraction.py
print("Starting test_file_extraction")
from utils.file_utils import handle_file_upload

def handle_file_upload_simulated(file_content: bytes, file_type: str) -> str:
    # For simulation, assume file_content is a plain text file.
    return file_content.decode("utf-8")

if __name__ == "__main__":
    # Simulated file contents (as bytes)
    resume_bytes = "John Doe\nSoftware Developer at XYZ Corp\nSkills: Python, AI, ML".encode("utf-8")
    job_desc_bytes = "We are seeking a Software Developer experienced in Python and AI technologies.".encode("utf-8")
    
    resume_text = handle_file_upload_simulated(resume_bytes, "text")
    job_desc_text = handle_file_upload_simulated(job_desc_bytes, "text")
    
    print("Extracted Resume Text:")
    print(resume_text)
    print("\nExtracted Job Description Text:")
    print(job_desc_text)
