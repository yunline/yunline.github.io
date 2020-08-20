$(function() {
    $('.side_btn').on('mouseover', function() {
        var side_btn = $(this).attr('id');
        $('#'+side_btn).css({background: '#70b7d3'});
    });

    $('.side_btn').on('mouseleave', function() {
        var side_btn = $(this).attr('id');
        $('#'+side_btn).css({background: '#43698b'});
    });

});