    //获得文章
    if (location.search.length == 0) { var url = location.protocol + "/404.html"; }
    else { var url = location.protocol + "/articles/" + location.search.substr(1, location.search.length - 1) + ".html"; }
    var httpRequest = new XMLHttpRequest();//创建HttpRequest对象
    httpRequest.open('GET', url, true); //打开连接
    httpRequest.send();

    httpRequest.onreadystatechange = function () {//回调函数
        if (httpRequest.readyState == 4 && httpRequest.status == 200) {//如果成功
            var html = httpRequest.responseText;//获取到服务端返回的数据
            document.getElementById("main_content").innerHTML = html + document.getElementById("main_content").innerHTML;
        }
        else if (httpRequest.status == 404) {//如果没有获取到
            location.href = location.protocol + "/article.html";//用一种奇奇怪怪的方式跳转到404页面
        }
    };