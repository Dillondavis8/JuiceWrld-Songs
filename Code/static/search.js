

var searchSong = function(songName) {
    window.location.href=`/search_list?q=${songName}`
        
}

var viewSong = function(index) {
    var data_to_save = {"id": index}         
    $.ajax({
        type: "POST",
        url: `view/${index}`,                
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify(data_to_save),
        success: function(result){
            console.log(data_to_save)
            var song_data = result["songs"]
            window.location.href=`/view/${index}`
        },
        error: function(request, status, error){
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });
}

var deleteSong = function(index) {
    var data_to_delete = {"id": index}
    $.ajax({
        type: "DELETE",
        url: `song/${index}`,                
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        success: function(result){
            console.log(data_to_delete)
            var song_data = result["songs"]
            displaySearchResults(song_data)
        },
        error: function(request, status, error){
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    }); 
}


$(document).ready(function() {

    $("#submitSong").click(function() {
        console.log("Here submitting")
        var songName = $("#songSearch").val()
        if(songName.length != 0) {
            searchSong(songName)

        }
    })

    $("#songSearch").keypress(function(e) {
            if(e.keyCode == '13') {
                console.log("here in search")
                var songName = $("#songSearch").val()
                 if(songName.length != 0) {
                    searchSong(songName)
                }
            }
            
    })

    $(".post").click(function() {
        viewSong(songName)
    })
})