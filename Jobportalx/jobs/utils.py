from pypdf import PdfReader
import re

def extract_text_from_pdf(file_path):
    """
    Extracts text from a PDF file.
    """
    text = ""
    try:
        reader = PdfReader(file_path)
        for page in reader.pages:
            text += page.extract_text() + "\n"
    except Exception as e:
        print(f"Error extracting text from PDF: {e}")
    return text

def calculate_resume_score(resume_text, job_description):
    """
    Calculates a match score (0-100) between resume text and job description.
    Uses a simple keyword matching approach (Jaccard similarity on significant words).
    """
    if not resume_text or not job_description:
        return 0

    def clean_text(text):
        # Convert to lowercase and remove non-alphanumeric characters
        text = text.lower()
        text = re.sub(r'[^a-z0-9\s]', '', text)
        return text

    resume_words = set(clean_text(resume_text).split())
    job_words = set(clean_text(job_description).split())

    # Filter out common stop words (basic list)
    stop_words = {
        'the', 'a', 'an', 'and', 'or', 'but', 'is', 'are', 'was', 'were',
        'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by', 'from', 'about',
        'as', 'can', 'be', 'this', 'that', 'it', 'you', 'we', 'they', 'he',
        'she', 'his', 'her', 'their', 'my', 'your', 'our', 'will', 'would',
        'should', 'could', 'have', 'has', 'had', 'do', 'does', 'did', 'not',
        'no', 'yes', 'so', 'if', 'when', 'where', 'why', 'how', 'what', 'which',
        'who', 'whom', 'whose', 'ok', 'up', 'down', 'out', 'over', 'under',
        'again', 'further', 'then', 'once', 'here', 'there', 'all', 'any',
        'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'only',
        'own', 'same', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 
        'should', 'now'
    }

    resume_words = {w for w in resume_words if w not in stop_words and len(w) > 2}
    job_words = {w for w in job_words if w not in stop_words and len(w) > 2}

    if not job_words:
        return 0

    # Calculate intersection (matching keywords)
    intersection = resume_words.intersection(job_words)
    
    # Calculate score based on how many job keywords are covered in the resume
    # Doing (intersection / job_keywords) gives a "Coverage Score"
    # Using Jaccard (intersection / union) gives a similarity score
    
    # For a resume scanner, Coverage Score is often more intuitive for recruiters
    # (i.e., "Does this candidate have the skills I asked for?")
    # Let's use Coverage Score primarily, maybe weighted slightly with Jaccard?
    # Let's stick to Coverage Score for simplicity and clarity.
    
    # Calculate score based on how many job keywords are covered in the resume
    match_count = len(intersection)
    total_job_keywords = len(job_words)
    
    score = (match_count / total_job_keywords) * 100 if total_job_keywords > 0 else 0
    
    return {
        'score': round(score),
        'matched_keywords': sorted(list(intersection))
    }
