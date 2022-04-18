from pathlib import Path

from botok import Text

in_file = Path('content/B1/Week1/B/2/ཆ ༽ ཚིག་གནད།.txt')
dump = in_file.read_text()
segmented = Text(dump).tokenize_words_raw_lines
in_file.write_text(segmented)
