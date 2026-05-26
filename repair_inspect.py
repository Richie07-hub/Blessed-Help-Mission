from pathlib import Path
path = Path('index.html')
text = path.read_text(encoding='utf-8')
start = text.find('        <a href="https://wa.me/+2348035713197"')
print('start', start)
comment = '<!-- ═════════════════════════════════════='
end_comment = text.find(comment, start)
print('comment pos', end_comment)
print(repr(text[end_comment-40:end_comment+40]))
