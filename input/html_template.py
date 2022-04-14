from textwrap import dedent

html_a = dedent("""\
    <html lang="en">
    <!DOCTYPE html>
    <head>
        <meta charset="UTF-8">
        <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Jomolhari">
        <link rel="stylesheet" href="https://unpkg.com/tippy.js@6/animations/light.css"/>
        <link rel="stylesheet" href="../general.css">
    </head>
    
    <body>
    """)

html_b = dedent("""\

        {text}
    
        {defns}
        """)
        
html_c = dedent("""\
        <script src="https://unpkg.com/@popperjs/core@2"></script>
        <script src="https://unpkg.com/tippy.js@6"></script>
        <script>
            const word1 = document.getElementById('word1');
    
            tippy('#word', {
                content(reference) {
                    const id = reference.getAttribute('data-template');
                    const template = document.getElementById(id);
                    return template.innerHTML;
                },
                allowHTML: true,
                animation: 'fade',
                arrow: false,
                duration: [2000, 500],
                interactive: true,
                maxWidth: 350,
                offset: [0, 0],
                placement: 'bottom-start',
                theme: 'popup',
                delay: 700,
            });
        </script>
    </body>
    </html>
    """)

texts = '<p id="ROOTEXT">{total_texts}</p>'

text = '<span id="word" data-template="{idx}">{word}</span>'

nodef_text = '<span id="NODEF">{word}</span>'

defns = dedent("""\
<div style="display: none;">
    {total_defns}
</div>""")

defn = dedent("""\
<div id="{idx}">
    <a href="{url}" target="_blank"><img alt="ཚིག་མཛོད།" src="../assets/dict_icon.png" width=27" height="22"></a>
    <br />
    {text}
</div>""")

en_title = '<div id="ENTITLE">{title}</div>'
en_entry = '<div id="ENENTRY">{entry}</div>'
bo_title = '<div id="BOTITLE">{title}</div>'
bo_entry = '<div id="BOENTRY">{entry}</div>'

dictdef_sep = ''
dictdict_sep = '<br /><br />'
