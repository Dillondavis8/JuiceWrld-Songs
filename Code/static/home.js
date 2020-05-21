var homeDisplay = function(songs) {
    var topItemsHtml = '';
    var lowItemsHtml = '';
    songs.slice().reverse().forEach((song, index) => {
        var img = song.albumCover
        var title = song.title
        var id = song.id
        var plays = song.plays
        if(index < 5) {
            topItemsHtml = topItemsHtml + `
            <div class="col-md-2 f${index}">
            <div class="card" style="width: 16rem;">
               <div class="card-img-top ">
                <a href="http://127.0.0.1:5000/view/${id}"> 
                   <img class="card-img-top" alt="${title}" src="${img}" height="200"/>
                   </a>
                   </div> 

                <div class="card-body">
                    <h5 class="card-title">${title}</h5>
                    <p><i class="fa fa-play-circle-o"></i> ${plays}</p>
                </div>
            </div>
        </div>
            `
        }
        else if(index < 10) {
            lowItemsHtml = lowItemsHtml + `
            <div class="col-md-2 f${index}">
            <div class="card" style="width: 16rem;">
               <div class="card-img-top ">
                <a href="http://127.0.0.1:5000/view/${id}">
                   <img class="card-img-top" alt="${title}" src="${img}" height="200"/>
                   </a>
                   </div> 

                <div class="card-body">
                    <h5 class="card-title">${title}</h5>
                    <p><i class="fa fa-play-circle-o"></i> ${plays}</p>
                </div>
            </div>
        </div> 
            `
            
        }

    })

    $("#top").html(topItemsHtml);
    $("#low").html(lowItemsHtml);
}

$(document).ready(function() {
    homeDisplay(songs)
})