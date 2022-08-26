document.addEventListener('DOMContentLoaded', function() {
    const homeView = document.querySelector('#home').href
    const searchView = document.querySelector('#search').href
    const libraryView = document.querySelector('#library').href
    const currentPage = window.location.href

    if (currentPage === homeView) {
        home()
    } 
    else if (currentPage === searchView) {
        search()
    }
    else if (currentPage === libraryView) {
        library()
    }
})

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