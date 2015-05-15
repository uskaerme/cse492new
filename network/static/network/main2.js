/**
 * Created by emreaksu on 13/05/15.
 */
$(document).ready(function() {

    $('.comment-button').click(function(){
        $(this).parent().children('.comments').slideToggle("fast");
        /*$('.comments').slideToggle("fast");*/
    });

});