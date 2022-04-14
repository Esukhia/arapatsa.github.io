from pathlib import Path

from third_party.dictify.dictify import dictify_text
from html_template import html_a, html_b, html_c, texts, text, nodef_text, en_title, en_entry, bo_title, bo_entry, defns, defn, dictdef_sep, dictdict_sep


def recursive_process(in_path):
    in_path = Path(in_path)
    for f in in_path.rglob('*.txt'):
        process_file(f)


def process_file(filename):
    dump = filename.read_text()

    # get definitions
    defs = dictify_text(dump)

    # generate html
    html = gen_html(defs)

    outfile = filename.parent / (filename.stem + '.html')
    outfile.write_text(html)


def gen_html(defs):
    total_text = []
    total_defns = []
    num = 1
    for word, dfs in defs:
        if not dfs['defs']:
            if word == '\n':
                word = '<br />'
            total_text.append(nodef_text.format(word=word))
            continue

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
        num += 1

    print()
    total_text = ''.join(total_text)
    total_defns = '\n'.join(total_defns)
    total_texts = texts.format(total_texts=total_text)
    total_defns = defns.format(total_defns=total_defns)

    output = html_a + html_b.format(text=total_texts, defns=total_defns) + html_c
    return output


if __name__ == '__main__':
    in_path = 'content'
    recursive_process(in_path)