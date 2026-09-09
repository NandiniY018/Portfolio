import os
import glob

directory = r"D:\Portfolio\templates\partials"
files = glob.glob(os.path.join(directory, "*.html"))

container_old1 = 'class="section-container"'
container_new1 = 'class="max-w-[1200px] mx-auto px-4 sm:px-5 md:px-6 lg:px-8"'

container_old2 = 'class="section-container '
container_new2 = 'class="max-w-[1200px] mx-auto px-4 sm:px-5 md:px-6 lg:px-8 '

py_old1 = 'class="section-py '
py_new1 = 'class="py-14 sm:py-16 md:py-20 lg:py-24 '

py_old2 = ' section-py '
py_new2 = ' py-14 sm:py-16 md:py-20 lg:py-24 '

for file_path in files:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    new_content = content.replace(container_old1, container_new1)
    new_content = new_content.replace(container_old2, container_new2)
    new_content = new_content.replace(py_old1, py_new1)
    new_content = new_content.replace(py_old2, py_new2)
    
    if new_content != content:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated {file_path}")
print("Done")
