var clearSlct = "getSelection" in window ? function () {//清除已选择，来自https://www.cnblogs.com/wangpeng-friend/p/6733070.html
    window.getSelection().removeAllRanges();
} : function () {
    document.selection.empty();
};