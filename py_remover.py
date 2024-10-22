import os

# مسیر پوشه مورد نظر
folder_path = 'telegram'

# فرهنگ‌نامه‌ای برای نگهداری فایل‌ها بر اساس حجم
files_by_size = {}

# لیست کردن تمام فایل‌های موجود در پوشه
for root, dirs, files in os.walk(folder_path):
    for file in files:
        file_path = os.path.join(root, file)
        file_size = os.path.getsize(file_path)
        
        # فایل‌ها را بر اساس حجمشان دسته‌بندی می‌کنیم
        if file_size in files_by_size:
            files_by_size[file_size].append(file_path)
        else:
            files_by_size[file_size] = [file_path]

# حذف فایل‌های تکراری بر اساس حجم
for size, files in files_by_size.items():
    if len(files) > 1:
        # از بین فایل‌های تکراری، فقط اولین فایل را نگه می‌داریم
        for file in files[1:]:
            os.remove(file)
            print(f'File {file} deleted.')

print('Duplicate files by size removed.')
