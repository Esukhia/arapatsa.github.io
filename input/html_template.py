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
                popperOptions: {
                    strategy: 'fixed',
                    modifiers: [
                        {
                            name: 'flip',
                            options: {
                                fallbackPlacements: ['right', 'left'],
                            },
                        },
                        {
                            name: 'preventOverflow',
                            options: {
                                altAxis: true,
                                tether: false,
                            },
                        }, 
                    ],
                },
            });
        </script>
        <script>
            function expand(dots,moreText,btnText) {
                if (dots.style.display === "none") {
                    dots.style.display = "inline";
                    btnText.innerHTML = "🢀🢂";
                    moreText.style.display = "none";
                } else {
                    dots.style.display = "none";
                    btnText.innerHTML = "🢂🢀";
                    moreText.style.display = "inline";
                }
            }
        </script>
    </body>
    </html>
    """)

texts = '<p id="ROOTEXT">{total_texts}</p>'

text = '<span id="word" data-template="{idx}">{word}</span>'
text_bold = '<span id="word" data-template="{idx}" style="font-weight: bold;">{word}</span>'
nodef_text = '<span id="NODEF">{word}</span>'
nodef_text_bold = '<span id="NODEF" style="font-weight: bold;">{word}</span>'

defns = dedent("""\
        <div style="display: none;">
            {total_defns}
        </div>""")

defn = dedent("""\
        <div id="{idx}">
            {text}
            <br /><div style="width: 350px;"></div>
            <a href="{url}" target="_blank"><img alt="ཚིག་མཛོད།" src="../assets/dict_icon.png" width=27" height="22"></a>
        </div>""")

en_title = '<div id="ENTITLE"><center>{title}</center></div>'
en_entry = '<div id="ENENTRY">{entry}</div>'
bo_title = '<div id="BOTITLE"><center>{title}</center></div>'
bo_entry = '<div id="BOENTRY">{entry}</div>'

sense = dedent("""\
        <button onclick="expand(document.getElementById('dots{sense_idx}'),document.getElementById('more{sense_idx}'),document.getElementById('myBtn{sense_idx}'))" id="myBtn{sense_idx}" style="border:1px solid lightblue; border-radius: 25%; color:lightblue; background-color: transparent;">🢀🢂</button>
        {sense_head}<span id="dots{sense_idx}" style="display: inline; color: lightblue;">་་་</span><span id="more{sense_idx}" style="display: none;">{sense_body}</span>""")
sense_sep = '<br />'

dictdef_sep = ''
dictdict_sep = '<br /><br />'

title_start = '</p><{level}>'
title_end = '</{level}><p id="ROOTEXT">'

bold_start = '<b>'
bold_end = '</b>'
