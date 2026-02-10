import os

def summarize(file_path):
    # placeholder – just report file size
    size = os.path.getsize(file_path)
    return {"reads": size//1000, "avg_length": 1500}
