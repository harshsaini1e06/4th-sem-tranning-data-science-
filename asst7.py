import os
import shutil
def jecrc():
    if not os.path.exists("JECRC"):
        os.makedirs("JECRC")
    files_to_copy = ["Data Science with ML & AI-45 Days.pdf", "FullStack Web Development-45 Days.pdf", "txt1.txt", "txt2.txt", "pexels-esmihel-muhammad-19223070.jpg", "pexels-mohit-hambiria-20507732.jpg"]
    for file in files_to_copy:
        shutil.copy(file, "JECRC")
def filter_files():
    folders = ["image_folder", "text_folder", "pdf_folder"]
    for folder in folders:
        if not os.path.exists(folder):
            os.makedirs(folder)
    for file in os.listdir("JECRC"):
        if file.endswith(".jpg"):
            shutil.move(os.path.join("JECRC", file), os.path.join("image_folder", file))
        elif file.endswith(".txt"):
            shutil.move(os.path.join("JECRC", file), os.path.join("text_folder", file))
        elif file.endswith(".pdf"):
            shutil.move(os.path.join("JECRC", file), os.path.join("pdf_folder", file))
def main():
    jecrc()
    filter_files()
    print("Files filtered and moved successfully!")
main()
