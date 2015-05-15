/**
 * Created by emreaksu on 03/05/15.
 */
$(document).ready(function() {
    /*
    $('form#comment_form').submit(function(e){
        e.preventDefault();
        var form = $(this);
        $.ajax({
            url: form.attr('action'),
            type: form.attr('method'),
            data: form.serialize(),
            success: function(data) {
                $("#sidebar").html(data);
            },
             error : function(xhr,errmsg,err) {
            $('#sidebar').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
        });
        return false;
    });
    */
    $('#course-list').change(function(){
            var course;
            course = $(this).val();
            $.get('/network/getsections/',{course:course},function(data){
                $('#sections-list').html(data);
                $('#sections-list').attr('disabled', false);
            });
    });

    $('#university-dropdown').change(function(){
            var university;
            if($(this).val() == ''){
                $('#faculty-dropdown').html("<option>Faculty</option>");
                $('#faculty-dropdown').attr('disabled', true);
            }
            else{
                university = $(this).val();
                $.get('/network/getfaculties/',{university:university},function(data){
                $('#faculty-dropdown').html(data);
                $('#faculty-dropdown').attr('disabled', false);
            });
        }
    });

    var $btns = $('.course-list-obj').click(function() {
        if (this.id == 'all') {
            $('#feed-list > div').fadeIn(450);
        } else {
            var $el = $('.' + this.id).fadeIn(450);
            $('#feed-list > div').not($el).hide();
        }
        $btns.removeClass('m-active');
        $(this).addClass('m-active');
    });

    /* comment_form
    $('.btn').click(function(){
        var my_form = $(this).parent().children('#comment_form');
        $.ajax({
            url: $('#comment_form').attr('action').val(),
            type: 'POST',
            data: $('#comment_form').serialize(),
            success: function(data) {
                $("#sidebar").html(data);
            },
             error : function(xhr,errmsg,err) {
            $('#sidebar').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
        });
    });
    */

    $('#faculty-dropdown').change(function(){
            var faculty;
            var university;
            if($(this).val() == ''){
                $('#department-dropdown').html("<option>Department</option>");
                $('#department-dropdown').attr('disabled', true);
            }
            else{
                university = $('#university-dropdown').val();
                faculty = $(this).val();
                $.get('/network/getdepartments/',{faculty:faculty},function(data){
                $('#department-dropdown').html(data);
                $('#department-dropdown').attr('disabled', false);
            });
        }
    });

    $('.comment-button').click(function(){
        $(this).parent().children('.comments').slideToggle("fast");
        /*$('.comments').slideToggle("fast");*/
    });

   $(".top-nav-opt").click(function () {
        var id = $(this).attr("id");
        $('#' + id).siblings().find(".selected").removeClass("selected");
        $('#' + id).addClass("selected");
        localStorage.setItem("selectedolditem", id);
    });
    var selectedolditem = localStorage.getItem('selectedolditem');

    if (selectedolditem != null) {
        $('#' + selectedolditem).siblings().find(".selected").removeClass("selected");
        $('#' + selectedolditem).addClass("selected");
    }




    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');

    /*
    The functions below will create a header with csrftoken
    */

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    function sameOrigin(url) {
        // test that a given url is a same-origin URL
        // url could be relative or scheme relative or absolute
        var host = document.location.host; // host + port
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        // Allow absolute or scheme relative URLs to same origin
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            // or any other URL that isn't scheme relative or absolute i.e relative.
            !(/^(\/\/|http:|https:).*/.test(url));
    }

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
                // Send the token to same-origin, relative URLs only.
                // Send the token only if the method warrants CSRF protection
                // Using the CSRFToken value acquired earlier
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });
});