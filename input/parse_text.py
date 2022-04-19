from pathlib import Path

from third_party.dictify.dictify import dictify_text
from html_template import html_a, html_b, html_c, texts, text, text_bold, nodef_text, nodef_text_bold, en_title, en_entry, bo_title, bo_entry, defns, defn, dictdef_sep, dictdict_sep, title_start, title_end, bold_start, bold_end


def recursive_process(in_path, mode='en_bo', selection=None):
    in_path = Path(in_path)
    for f in sorted(list(in_path.rglob('*.txt'))):
        process_file(f, mode=mode, selection=selection)


def process_file(filename, mode='en_bo', selection=None):

    dump = filename.read_text()

    # cleanup text
    to_render, to_process = cleanup(dump)

    # get definitions
    defs = dictify_text(to_process, is_split=True, mode=mode, selection_yaml=selection)

    # retrieve cleaned text in defs
    defs = [(to_render[num], d[1]) for num, d in enumerate(defs)]

    # generate html
    html = gen_html(defs)

    out_folder = Path(__file__).parent.parent / Path(filename.parts[1])
    if 'en' in mode:
        name = '-'.join(filename.parts[2:-1]) + '-' + filename.stem + '_EN.html'
    else:
        name = '-'.join(filename.parts[2:-1]) + '-' + filename.stem + '.html'
    outfile = out_folder / name
    outfile.write_text(html)


def cleanup(text):
    text = text.replace('\n', ' \n ')
    tokens = text.split(' ')
    to_process = []
    to_render = []
    for t in tokens:
        if not t:
            continue
        r, p = t, t
        if p.endswith('*'):
            p = p[:-1]
        if '{' in t:
            r, p = t[:-1].split('{')
        if '-' in t:
            r, p = t.replace('-', ''), t
        if '_' in t:
            r, p = t.replace('_', ' '), t
        if '}*' in t:
            r, p = t[:-2].split('{')
            r += '*'

        to_render.append(r)
        to_process.append(p)

    return to_render, to_process


def gen_html(defs):
    total_text = []
    total_defns = []
    num = 0
    is_title = False
    level = None
    for word, dfs in defs:
        num += 1
        # parse titles
        if word.startswith('h'):
            is_title = True
            level = word
            total_text.append(title_start.format(level=word))
            continue

        if word == '\n' and is_title:
            is_title = False
            total_text.append(title_end.format(level=level))

        if word == '//*':
            total_text.append(bold_start)
            continue

        if word == '*//':
            total_text.append(bold_end)
            continue

        if '+' in word:
            word = word.replace('+', '&nbsp;' * 4)

        if not dfs['defs']:
            if word == '\n':
                word = '<br />'
            if word.endswith('*'):
                total_text.append(nodef_text_bold.format(word=word[:-1]))
            else:
                total_text.append(nodef_text.format(word=word))
            continue

        if word.endswith('*'):
            total_text.append(text_bold.format(idx=num, word=word[:-1]))
        else:
            total_text.append(text.format(idx=num, word=word))

        entry = []
        for lang, e in dfs['defs'].items():
            if lang == 'en':
                l_title = en_title.format(title=e[0])
                l_entry = en_entry.format(entry=e[1])
            elif lang == 'bo':
                l_title = bo_title.format(title=e[0])
                l_entry = bo_entry.format(entry=e[1])
            else:
                raise SyntaxError
            entry.append(l_title + dictdef_sep + l_entry)
        entry = dictdict_sep.join(entry)
        total_defns.append(defn.format(idx=num, text=entry, url=dfs['url']))

    total_text = ''.join(total_text)
    total_defns = '\n'.join(total_defns)
    total_texts = texts.format(total_texts=total_text)
    total_defns = defns.format(total_defns=total_defns)

    output = html_a + html_b.format(text=total_texts, defns=total_defns) + html_c
    return output


if __name__ == '__main__':
    in_path = 'content/'
    for mode in ['bo', 'bo_en']:
        dict_yaml = 'selection_tsikchen.yaml'
        recursive_process(in_path, mode=mode, selection=dict_yaml)
