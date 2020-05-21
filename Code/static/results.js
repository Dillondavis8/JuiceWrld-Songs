var displaySearchResults = function(songs) {
    $("#songResults").empty()
    var count = 0;
    var itemsHtml = '';
        songs.forEach((song, index) => {
                itemsHtml = itemsHtml + `
                <div class="row item-row">
                    <div class="col-md-6 dank" data-index="${song.id}">
                        <div class="dope">
                        <div class="post">
                        <i class="fa fa-music"></i>
                        ${song.title}
                        </div>
                        <div class="songInfo"> 
                            ${song.songDescription}
                            </div>
                        </div>
                    </div>
                </div>
                `
            count++;
        })
            console.log("FUCKER")
            if(count == 0) {
               $("#numResults").addClass('noResults')
               $("#numResults").html('Results: ' + count) 
            } else {
                $("#numResults").html('Results: ' + count)
            }
            $("#songResults").html(itemsHtml);  
    
            $(".dank").click(function() {
                var index = Number(this.getAttribute("data-index"))
                window.location.href=`/view/${index}`
            })
            $(".dank").hover(function() {
                $(this).toggleClass('grab')
            }); 

            $(".delete-button").click(function() {
                var index = Number(this.getAttribute("data-index"))
                deleteSong(index)
            })
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
    displaySearchResults(songs)


})