var display_song = function(song) {
    console.log(song) 
    var sp = song.platforms
    console.log(sp.name)
    var id = song.id
    var undoButtons = '';
    var delButtons = '';
    var platformHtml = '';
    sp.forEach((plat, index) => {
        if(plat.marked_as_deleted == 'false') {
            if(sp.length -1 == index) {
                platformHtml = platformHtml + plat.name;
            } else {
                platformHtml = platformHtml + `${plat.name}, `
            }
            delButtons = delButtons + `<button type="button" class="close delete-button" aria-label="Close" data-index="${index}"><span class="delete" aria-hidden="true">×</span></button>`
         }
    })
    $("#deleteButtons").html(delButtons)

    $(".delete-button").click(function() {
        var index = Number(this.getAttribute("data-index"))
        console.log(index)
        undoButtons = undoButtons + `<button type="button" class="undo undo-button"  data-index="${index}"><span class="undoText" aria-hidden="true">Undo</span></button>`
        $("#undoButtons").html(undoButtons) 
        deleteSong(id, index)
    })

    $(".undo-button").click(function() {
        var index = Number(this.getAttribute("data-index"))
        $("#undoButtons").html('') 
        console.log(index)
        undoDeleteSong(id, index)
    })
    
    var img = song.albumCover
    $("#platformsAvailable").html(platformHtml)
    $("#title").html(song.title);
    $("#description").html(song.songDescription);
    $("#plays").html(song.plays);
    $('#albumCover').html(`<img id="theImg" alt="${song.title}" src=${img} />`)
}

var editStreamNum = function (song, text) {
    console.log(song)
    $("#editNum").empty() 
    $("#editNum").val(text)
    $("#editNum").addClass("show")
    $("#submitNum").addClass("showButton")
    $("#discardNum").addClass("showButton")
    $("#plays").addClass("hide")
    $("#numEdit").addClass("hide")

    $("#submitNum").click(function() {
        var id = song.id
        var changes = $("#editNum").val()
        $("#plays").html(changes) 
        $("#plays").removeClass("hide")
        $("#numEdit").removeClass("hide")
        $("#editNum").removeClass("show")
        $("#submitNum").removeClass("showButton")
        $("#discardNum").removeClass("showButton")
        saveNumEdit(id, changes)

        
    })

    $("#discardNum").click(function() {
        var id = song.id
        console.log(text)
        $("#editNum").val(text)
        $("#plays").removeClass("hide")
        $("#numEdit").removeClass("hide")
        $("#editNum").removeClass("show")
        $("#submitNum").removeClass("showButton")
        $("#discardNum").removeClass("showButton")
        
    })
}

var editSong = function(song, text) {
    console.log(song)
    $("#editDesc").empty() 
    $("#editDesc").val(text)
    $("#editDesc").addClass("show")
    $("#submitDesc").addClass("showButton")
    $("#discardDesc").addClass("showButton")
    $("#description").addClass("hide")
    $("#edit").addClass("hide")

    $("#submitDesc").click(function() {
        var id = song.id
        var changes = $("#editDesc").val()
        $("#description").html(changes) 
        $("#description").removeClass("hide")
        $("#edit").removeClass("hide")
        $("#editDesc").removeClass("show")
        $("#submitDesc").removeClass("showButton")
        $("#discardDesc").removeClass("showButton")
        saveEdit(id, changes)

        
    })

    $("#discardDesc").click(function() {
        var id = song.id
        console.log(text)
        $("#editDesc").val(text)
        $("#description").removeClass("hide")
        $("#edit").removeClass("hide")
        $("#editDesc").removeClass("show")
        $("#submitDesc").removeClass("showButton")
        $("#discardDesc").removeClass("showButton")
        
    })
}

var saveEdit = function(id, changes) {
    var data_to_save = {"id": id, "songDescription" : changes}         
    $.ajax({
        type: "POST",
        url: `/view/${id}`,                
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify(data_to_save),
        success: function(result){
            console.log(result)
        
        },
        error: function(request, status, error){
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });
}

var saveNumEdit = function(id, changes) {
    var data_to_save = {"id": id, "plays" : changes}         
    $.ajax({
        type: "POST",
        url: `/num/${id}`,                
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify(data_to_save),
        success: function(result){
            console.log(result)
        
        },
        error: function(request, status, error){
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });
}

var deleteSong = function(id, index) {
    var data_to_delete = {"id": id, "index": index}
    $.ajax({
        type: "DELETE",
        url: `/view/${id}/${index}`,                
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        success: function(result){
            console.log(data_to_delete)
            var song_data = result["songs"]
            display_song(song_data)
        },
        error: function(request, status, error){
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    }); 
}

var undoDeleteSong = function(id, index) {
    var data_to_delete = {"id": id, "index": index}
    $.ajax({
        type: "DELETE",
        url: `/undo/${id}/${index}`,                
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        success: function(result){
            console.log(data_to_delete)
            var song_data = result["songs"]
            display_song(song_data)
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
    display_song(song)

    $('.adjust').hover(function() {
        $(this).toggleClass('grab')
    }); 

    $("#edit").click(function() {
        console.log('clicked')
        var text = $("#description").text()
        editSong(song, text)
    })

    $("#numEdit").click(function() {
        console.log('clicked')
        var text = $("#plays").text()
        editStreamNum(song, text)
    })



    
})