from pathlib import Path
import re

from botok import Text


def basic_cleanup(text: str) -> str:
    text = text.strip().split('\n')
    text = [re.sub(r" +", " ", t).strip(' ') for t in text]
    return '\n'.join(text)


def post_process(tokens):
    words = []
    for t in tokens:
        if t.chunk_type != 'TEXT':
            words.append(t.text.replace(' ', '_'))
        else:
            newline = '\n' if t.text.endswith('\n') else ''
            text = t.text if not newline else t.text[:-1]

            if t.affix:
                text = '-' + text
            if t.syls[-1] == ['པ'] or t.syls[-1] == ['བ']:
                text = text + '{' + ''.join([''.join(s) + '་' for s in t.syls[:-1]]) + '}'
            text += newline
            text = text.replace(' ', '_')
            words.append(text)

    return ' '.join(words)


def segment(dump):
    # segment in sentences
    text = Text(dump, tok_params={})
    config = {"profile": "GMD", 'config': ''}
    sentences = text.custom_pipeline(
        basic_cleanup,
        "word_tok",
        "dummy",
        post_process,
        tok_params=config,
    )
    return sentences


in_file = Path('content/B1+/week2/A/2/ka-commentary.txt')
dump = in_file.read_text()
segmented = segment(dump)
in_file.write_text(segmented)
