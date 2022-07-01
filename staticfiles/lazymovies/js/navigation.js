// Navigation logic, to change the resources consumed
import { 
    // Get elements from navigation menu
    home_menu,
    main,
    trends,
    categories_menu,
    action_cm,
    romance_cm,
    horror_cm,
    drama_cm,
    search_btn,
    inp_search_mv,
    go_back_lazygram

} from "./main.js"

// Functions view
import { 
         // Views to home
         get_trends_home,
         // Views to trends
         get_home,
         get_views
        } from "./views.js"

const hashChange = () =>{

    if (location.hash.startsWith('#trends')){
        get_views('/trending/movie/day','Trends')
    }
    else if (location.hash.startsWith('#top_rated')){
        get_views('/movie/top_rated','Top rated')
    }
    else if (location.hash.startsWith('#all_categories')) get_categories_view()
    else if (location.hash.startsWith('#search=')) get_search_res_view(inp_search_mv.value)
    else get_home_view()
}

// Events Hash change in window-DOM
window.addEventListener('hashchange', hashChange, false)
window.addEventListener('DOMContentLoaded',hashChange, false)

// Events click change hash

/* Home hash*/
home_menu.addEventListener('click',()=>{
    location.hash = '#home'
})

/* Categories hash*/
categories_menu.addEventListener('click',()=>{
    location.hash = '#all_categories'
})

/* Sub categories hash*/
action_cm.addEventListener('click',()=>location.hash='#action')
romance_cm.addEventListener('click',()=>location.hash='#romance')
horror_cm.addEventListener('click',()=>location.hash='#horror')
drama_cm.addEventListener('click',()=>location.hash='#drama')

/* Top rated hash*/
trends.addEventListener('click',()=>{
    location.hash = '#trends'
})

/* Search has*/
search_btn.addEventListener('click',()=>{
    location.hash = `#search=${inp_search_mv.value}`
})

/* GO BACK LAZYGRAM APP*/
go_back_lazygram.addEventListener('click',(e)=>{

    const scheme = location.protocol+'//'
    const url = `${scheme}${location.hostname}:${location.port}/home/`
    location.href = url
    location.replace(url)
})

// Get views

/* CATEGORIES VIEW*/
const get_categories_view = () => {

    title_window.innerHTML='Lazymovies | Categories'
}

/* HOME VIEW*/
const get_home_view = async () => {

    main.innerHTML = ''
    get_trends_home()
    await get_home('/movie/top_rated', 'Top rated', true)
    await get_home('/movie/popular', 'Most popular')
    await get_home('/movie/upcoming', 'Upcoming')
}

/* SEARCH VIEW*/
const get_search_res_view = (mv)=>{
    console.log(mv)
}

/* Logout ... COMMING SOON */