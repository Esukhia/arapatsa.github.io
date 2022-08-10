from pathlib import Path

for week in range(4, 35, 1):
    week_dir = Path(f'week{week}')
    week_dir.mkdir(exist_ok=True)

    for section in ['A', 'B']:
        section_dir = week_dir / section
        section_dir.mkdir(exist_ok=True)

        one_dir = section_dir / '1'
        one_dir.mkdir(exist_ok=True)
        (one_dir / 'ka-root_text.txt').write_text('')
        (one_dir / 'ga-important_vocab.txt').write_text('')

        two_dir = section_dir / '2'
        two_dir.mkdir(exist_ok=True)
        (two_dir / 'ka-commentary.txt').write_text('')
        (two_dir / 'cha-important_vocab.txt').write_text('')

        three_dir = section_dir / '3'
        three_dir.mkdir(exist_ok=True)
        (three_dir / 'ka-root_commentary.txt').write_text('')
