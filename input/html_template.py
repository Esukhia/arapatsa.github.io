from textwrap import dedent

html_a = dedent("""\
    <html>
    <!DOCTYPE html>
    <html lang="en">
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
            });
        </script>
    </body>
    </html>
    """)

texts = '<p id="ROOTEXT">{total_texts}</p>'

text = '<span id="word" data-template="{idx}">{word}</span>'

nodef_text = '<span>{word}</span>'

defns = dedent("""\
<div style="display: none;">
    {total_defns}
</div>""")

defn = dedent("""\
<div id="{idx}">
    {text}
    <br /><br />
    <a href="{url}" target="_blank"><img alt="ཚིག་མཛོད།" src="../assets/dict_icon.png" width=27" height="22"></a>
</div>""")

en_title = '<div class="ENTITLE">{title}</div>'
en_entry = '<div class="ENENTRY">{entry}</div>'
bo_title = '<div class="BOTITLE">{title}</div>'
bo_entry = '<div class="BOENTRY">{entry}</div>'

dictdef_sep = '<br />'
dictdict_sep = '<br /><br />'
