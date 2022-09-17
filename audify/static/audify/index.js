$(document).ready(() => {
    const homeView = document.querySelector('#home').href
    const searchView = document.querySelector('#search').href
    const libraryView = document.querySelector('#library').href
    const currentPage = window.location.href

    if (currentPage === homeView) {
        // Active home button 
        home()
    } 
    else if (currentPage === searchView) {
        // Active search button
        search()
    }
    else if (currentPage === libraryView) {
        // Active library button 
        library()
    }
});


function dataCollected() {
    const token = 'obcGyJOTKyGYqcMcxFdKfKrDRfLpWnajbwVsatIS'
        
    for (let id = 0; id < 25; id++) {
        const url = `https://api.discogs.com/artists/${id}?token=${token}`;

        $.getJSON(url,
            function (data, textStatus) {
                const artists =
                `<div class="col">
                    <div class="card h-100">
                        <img src="${data.images[0].uri}" class="card-img-top" alt="Image">
                        <div class="card-body">
                            <h5 class="card-title">${data.name}</h5>
                            <p class="card-text">${data.realname}</p>
                            <a href="">Check</a>
                        </div>
                    </div>
                </div>`

                $('.artists').append(artists)
                console.log(textStatus)
            }
        );
    }
}


function home() {
    const home = document.querySelector('#home')
    home.ariaCurrent = 'page'
    home.className = 'nav-link active'

    const search = document.querySelector('#search')
    search.ariaCurrent = ''
    search.className = 'nav-link'

    const library = document.querySelector('#library')
    library.ariaCurrent = ''
    library.className = 'nav-link'
}


function search() {
    const search = document.querySelector('#search')
    search.ariaCurrent = 'page'
    search.className = 'nav-link active'

    const home = document.querySelector('#home')
    home.ariaCurrent = ''
    home.className = 'nav-link'

    const library = document.querySelector('#library')
    library.ariaCurrent = ''
    library.className = 'nav-link'
}


function library() {
    const library = document.querySelector('#library')
    library.ariaCurrent = 'page'
    library.className = 'nav-link active'

    const home = document.querySelector('#home')
    home.ariaCurrent = ''
    home.className = 'nav-link'

    const search = document.querySelector('#search')
    search.ariaCurrent = ''
    search.className = 'nav-link'
}