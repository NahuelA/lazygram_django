import { API_KEY } from './config.js'
import { $ } from './utils.js'

// Axios use
export const api = axios.create({
    baseURL: 'https://api.themoviedb.org/3/',
    headers: {
        'Content-Type': 'application/json;charset=utf-8',
    },
    params: {
        api_key: `${API_KEY}`,
    },
})

/* Get elements from navigation */
export const go_back_lazygram = $('#gb-lazygram')
export const home_menu = $('#home-menu')
/* Top rated */
export const top_rated = $('#top-rated')
export const trends = $('#trends')
/* Search button */
export const search_btn = $('#search-mv')
export const inp_search_mv = $('#inp-search-mv')
/* Title window */
export const title_window = $('#title-window')

/* Containers for do not overload */
export const main = $('#main')
main.classList = 'col-sm-10'
export const aside = $('#aside-bar')
export const aside_container = $('#aside')
export const relative_container = $('#relative-container')

// Trends
export const container_trends_main = $('#container-trends')

