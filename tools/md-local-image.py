import os
import re
import argparse
import requests
from pathlib import Path

def process_markdown(md_path):
    """process the single markdown file"""
    target_dir = md_path.parent
    image_dir = target_dir / 'images' / md_path.stem
    image_dir.mkdir(parents=True, exist_ok=True)
    
    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()

    pattern = r'(<img\s+src=[\'"])(https://[^\'"]+)([\'"].*?>)|(!\[.*?\]\()(https://[^\)]+)(\))'
    matches = re.finditer(pattern, content)
    
    replacements = []
    for match in matches:
        if match.group(1):  # HTML img tag
            prefix, url, suffix = match.group(1), match.group(2), match.group(3)
        else:  # Markdown image
            prefix, url, suffix = match.group(4), match.group(5), match.group(6)
        
        clean_url = url.split('?')[0]
        filename = Path(clean_url).name
        
        local_path = image_dir / filename
        
        if not local_path.exists():
            try:
                response = requests.get(url, timeout=10)
                response.raise_for_status()
                local_path.write_bytes(response.content)
                print(f'✅ download sucess: {filename}')
            except Exception as e:
                print(f'❌ download failure {filename}: {str(e)}')
                continue
        
        rel_path = Path('images') / md_path.stem / filename
        replacements.append((match.group(0), f'{prefix}{rel_path.as_posix()}{suffix}'))
    
    for old, new in reversed(replacements):
        content = content.replace(old, new)
    
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'🔄 file {md_path.name} process complete.\n')

def process_directory(target_dir):
    for md_path in Path(target_dir).glob('**/*.md'):
        print(f'🔍 start to process: {md_path}')
        process_markdown(md_path)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Markdown image location tools')
    parser.add_argument('target_dir', help='the path of markdown files')
    args = parser.parse_args()
    
    print(f'🚀 start to process the path: {args.target_dir}')
    process_directory(args.target_dir)
    print('🎉 all files process complete！')
    print(f'image have been saved in : {Path(args.target_dir) / "images"}')