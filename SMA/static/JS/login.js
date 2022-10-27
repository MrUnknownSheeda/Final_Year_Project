$(document).ready(function()
{
    // $('.header').height($(window).height());
   
    $(".header-buttons a").click(function()
    {
        $("body,html")
        .animate
        (
            {
                scrollTop:$("#" + $(this).data('value')).offset().top
            },
            1000
        )
    })
})
