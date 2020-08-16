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
<div class="code" id="%s">
    <button class="copy_button"
        onclick="
            var parent_ = document.getElementById('%s');
            var content_ = parent_.children[1];
            var btn = parent_.children[0];

            var clearSlct = 'getSelection' in window ? function () {//清除已选择，来自https://www.cnblogs.com/wangpeng-friend/p/6733070.html
                window.getSelection().removeAllRanges();} : 
                function () {document.selection.empty();};

            btn.innerHTML = 'Copied';

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
                console.warn('none');
            }
            document.execCommand('Copy'); // 执行浏览器复制命令
            clearSlct();

            setTimeout(function () { btn.innerHTML = 'Click to Copy'; }, 500);
        ">Click to Copy</button>
    <div class="highlight">
        %s
    </div>

</div>
"""%(code_id,code_id,html)

print(final_text)
