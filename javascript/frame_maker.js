// 处理图片框
$(
function load_image_frame(){
    var frames = document.getElementsByClassName("img_frame");
    for (i = 0; i < frames.length; i++) {
        var frame = frames[i];
        if(typeof(frame)=="object"){
            var img_src=frame.getAttribute("image");
            var text=frame.getAttribute("text");
            var size=(frame.getAttribute("size") ? Number(frame.getAttribute("size")) : 1);
            frame.innerHTML="<div><img id=\"imgframe\" src=\""+img_src+"\"></div>";
            var child_div=frame.firstChild;
            var img_ele=child_div.firstChild;
            var width=img_ele.width;
            var height=img_ele.height;
            var size_css=function(exx,exy){return "width:"+String(width*size+exx)+"px;height:"+String(height*size+exy)+"px;";}
            var div_css=(child_div.getAttribute("style") ? child_div.getAttribute("style") : "")+size_css(30,60)+"position:relative;left:10px;top:5px;box-shadow:0px 0px 10px #888888";
            var img_css=(img_ele.getAttribute("style") ? img_ele.getAttribute("style") : "")+size_css(0,0)+"position:relative;left:15px;top:15px;";
            var frame_css=(frame.getAttribute("style") ? frame.getAttribute("style") : "")+size_css(50,0);
            img_ele.setAttribute("style",img_css);
            child_div.setAttribute("style",div_css);
            frame.setAttribute("style",frame_css);
            child_div.innerHTML+=("<p style='position:relative;box_shadow:0px 0px 10px #888888'>"+text+"</p>");
        }
    }
});
setTimeout(load_image_frame,100)