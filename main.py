import random
import pygments
from pygments import lexers,formatters
lex=lexers.PythonLexer()
HTML=formatters.HtmlFormatter()
with open("text.py","rb") as f:
    content=f.read().decode("utf8")
html=pygments.highlight(content,lex,HTML)

random_str=lambda:"".join([(lambda:random.choice("0123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"))() for i in range(64)])
code_id=random_str()
final_text="""
<div class="code">
    <script id=%s>
        function copyText%s() {
            var parent_ = document.getElementById("%s").parentElement;
            var content_ = parent_.children[2];
            var btn = parent_.children[1];

            btn.innerHTML = "Copied";

            if (document.body.createTextRange) {
                var range = document.body.createTextRange();
                range.moveToElementText(content_);
                range.select();
            }
            else if (window.getSelection) {
                var selection = window.getSelection();
                var range = document.createRange();
                range.selectNodeContents(content_);
                selection.removeAllRanges();
                selection.addRange(range);
            }
            else {
                console.warn("none");
            }
            document.execCommand("Copy"); // 执行浏览器复制命令
            clearSlct();

            setTimeout(function () { btn.innerHTML = "Click to Copy"; }, 500);
        }
    </script>
    <button class="copy_button" onclick="copyText%s()">Click to Copy</button>
    %s
</div>
"""%(code_id,code_id,code_id,code_id,html)

print(final_text)
