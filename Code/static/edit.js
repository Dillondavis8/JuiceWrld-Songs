var addOrigDescription = function(song) {
    var desc = song.songDescription
    $("#editText").val(desc)
}

var saveEdit = function(id, title, img, changes, plays, platforms) {
    var data_to_save = {"id": id, "title": title, "albumCover": img, "songDescription" : changes, "plays": plays, "platforms": platforms}         
    $.ajax({
        type: "POST",
        url: `/edit/${id}`,                
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify(data_to_save),
        success: function(result){
            console.log(result)
            window.location.href= `http://127.0.0.1:5000/view/${id}`
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
    addOrigDescription(song)
    var id = song.id;
    var title = song.title;
    var img = song.albumCover;
    var plays = song.plays;
    var platforms = song.platforms;

    $("#submit").click(function() {
        var changes = $("#editText").val()
        saveEdit(id, title, img, changes, plays, platforms)
    })

    $("#discard").click(function() {
        window.location.href= `http://127.0.0.1:5000/view/${id}`
    })

})