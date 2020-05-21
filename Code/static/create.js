var createSong = function() {
    var submit = true;

    var title = $("#title").val()
    var albumCover = $("#albumCover").val()
    var songDescription = $("#songDescription").val()
    var plays = $("#plays").val()
    var playsTest = plays.split(',').join('')
    var numbers = /^[0-9]+$/;
    var plat = $("#platforms").val()
    var platforms = plat.split(',')
    console.log(plays)
    if(platforms == '') {
        $("#platError").html('Enter in the platforms available')
        $("#songMade").html('')
        $("#newSong").html('')
        $("#newSong").removeClass('songSuccess')
        $("#platforms").focus()
        submit = false;
    }
    else {
        $("#platError").html('')
    }

     if(playsTest.match(numbers) == null){
        console.log("Not a number value")
        $("#playsError").html('Must be a valid number')
        $("#songMade").html('')
        $("#newSong").html('')
        $("#newSong").removeClass('songSuccess')
        $("#plays").focus()
        submit = false;
    } else {
        $("#playsError").html('')
    }
    if(songDescription == '') {
        $("#descError").html('Enter in a song description')
        $("#songMade").html('')
        $("#newSong").html('')
        $("#newSong").removeClass('songSuccess')
        $("#songDescription").focus()
        submit = false;
    }
    else {
        $("#descError").html('')
    }
    if(albumCover.substring(albumCover.length - 3, albumCover.length) != 'jpg' && albumCover.substring(albumCover.length - 3, albumCover.length) != 'png') {
        $("#albumError").html('Must be a .jpg or .png url')
        $("#songMade").html('')
        $("#newSong").html('')
        $("#newSong").removeClass('songSuccess')
        $("#albumCover").focus()
        submit = false;
        console.log('Must be a picture')
    } else {
        $("#albumError").html('') 
    }
    if(title == '') {
        $("#titleError").html('Enter in a title name')
        $("#songMade").html('')
        $("#newSong").html('')
        $("#newSong").removeClass('songSuccess')
        $("#title").focus()
        submit = false;
    }
    else {
        $("#titleError").html('')
    }
     if(submit == true){
        $("#albumError").html('') 
        $("#playsError").html('')
        $("#title").val('')
        $("#albumCover").val('')
        $("#songDescription").val('')
        $("#plays").val('')
        $("#platforms").val('')
        $("#title").focus() 
        submitSong(title, albumCover, songDescription, plays, platforms)
    }     
}


var submitSong = function(title, albumCover, songDescription, plays, platforms) {
    var data_to_save = {"title": title, "albumCover": albumCover, "songDescription" : songDescription, "plays": plays, "platforms": platforms}        
    $.ajax({
        type: "POST",
        url: "create_song",                
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify(data_to_save),
        success: function(result){
            console.log(result)
            var song_data = result.newSong.id
            console.log(song_data)
            linkToSong(song_data)
        },
        error: function(request, status, error){
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });
}

var linkToSong = function(song_data) {
    $("#songMade").html('New song successfully created!')
    $("#songMade").addClass('successMade')

    $("#newSong").html("Click here for new song!")
    $("#newSong").addClass('songSuccess')
    $("#newSong").click(function() {
        window.location.href= `http://127.0.0.1:5000/view/${song_data}`
    })
}

$(document).ready(function() {
    $("#submit").click(function() { 
        createSong()
    })
    $('#newSong').hover(function() {
        $(this).toggleClass('grab')
    }); 
})