import os
import re

def update_resume_skills(content):
    """Update the skills section according to requirements"""
    
    # Remove the entire Web Technologies line
    content = re.sub(r'\*\*Web Technologies:\*\*.*\n', '', content)
    
    # Update Programming Languages to include Gen AI and Data Science
    content = re.sub(
        r'\*\*Programming Languages:\*\* (.*)',
        r'**Programming Languages:** Python, Java, JavaScript, C++\n**AI/ML Technologies:** Gen AI, Data Science, Machine Learning, Deep Learning, Natural Language Processing',
        content
    )
    
    # Update Databases to keep only MySQL
    content = re.sub(
        r'\*\*Databases:\*\* (.*)',
        r'**Databases:** MySQL',
        content
    )
    
    # Update Tools & Technologies to include more AI/ML tools
    content = re.sub(
        r'\*\*Tools & Technologies:\*\* (.*)',
        r'**Tools & Technologies:** Git, Docker, AWS, VS Code, Jupyter Notebook, TensorFlow, Scikit-learn, Pandas, NumPy, Matplotlib, OpenAI API',
        content
    )
    
    return content

def process_all_resumes():
    """Process all resume files in the current directory"""
    
    # Get all resume files
    resume_files = [f for f in os.listdir('.') if f.endswith('_Resume.md')]
    resume_files.sort()  # Sort to process in order
    
    print(f"Found {len(resume_files)} resume files to update")
    
    for filename in resume_files:
        print(f"Processing: {filename}")
        
        # Read the file
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Update the skills section
        updated_content = update_resume_skills(content)
        
        # Write back to file
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        
        print(f"Updated: {filename}")
    
    print("All resumes have been updated successfully!")

if __name__ == "__main__":
    process_all_resumes()
