// Navigation logic, to change the resources consumed
import {
    // Get elements from navigation menu
    home_menu,
    main,
    aside_container,
    relative_container,
    trends,
    search_btn,
    inp_search_mv,
    go_back_lazygram,
    top_rated,
} from './main.js'

// Functions view
import {
    // Views to home
    get_trends_home,
    // Views to trends
    categories_links,
    category_select_view,
    search_movies,
    movie_details,
} from './views.js'

import { get_views, get_home } from './utils.js'

const hashChange = async () => {
    if (location.hash.startsWith('#trends')) {
        get_views('/trending/movie/day', 'Trends')
    } else if (location.hash.startsWith('#top_rated')) {
        get_views('/movie/popular', 'Top rated')
    } else if (location.hash.startsWith('#category=')) {
        category_select_view(parseInt(location.hash.split('=')[1]))
        categories_links()
    } else if (location.hash.startsWith('#search=')) {
        search_movies(inp_search_mv.value)
    } else if (location.hash.startsWith('#movie=')) {
        movie_details(location.hash.split('=')[1])
    } else {
        await get_home_view()
    }

    // Scroll top after view loads
    scroll({
        top: 0,
        behavior: 'smooth',
    })
}

// Events Hash change in window-DOM
window.addEventListener('hashchange', hashChange, false)
window.addEventListener('DOMContentLoaded', hashChange, false)

// Events click change hash

/* Home hash*/
home_menu.addEventListener('click', () => {
    location.hash = '#home'
})

/* Sub categories hash*/

/* Trends hash*/
trends.addEventListener('click', () => {
    location.hash = '#trends'
})

/* Top rated hash*/
top_rated.addEventListener('click', () => {
    location.hash = '#top_rated'
})

/* Search hash*/
search_btn.addEventListener('click', () => {
    location.hash = `#search=${inp_search_mv.value}`
})

/* GO BACK LAZYGRAM APP*/
go_back_lazygram.addEventListener('click', (e) => {
    const scheme = location.protocol + '//'
    const url = `${scheme}${location.hostname}:${location.port}/home/`
    location.href = url
    location.replace(url)
})

// Get views

/* HOME VIEW*/
const get_home_view = async () => {
    main.innerHTML = ''
    main.classList = 'col-sm-10'
    aside_container.classList.remove('inactive')
    relative_container.classList = 'position-relative row'

    await get_trends_home()
    // Load categories
    await categories_links()
    await get_home('/movie/top_rated', 'Top rated', 'main-section',true)
    await get_home('/movie/popular', 'Most popular')
    await get_home('/movie/upcoming', 'Upcoming')
}
