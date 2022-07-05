import { API_KEY } from "./config.js";

// IMG size
export const img_size_3 = "https://image.tmdb.org/t/p/w500/";

// Query selector
export const $ = (id) => {
  return document.querySelector(id);
};

// Axios use
export const api = axios.create({
  baseURL: "https://api.themoviedb.org/3/",
  headers: {
    "Content-Type": "application/json;charset=utf-8",
  },
  params: {
    api_key: `${API_KEY}`,
  },
});

// Create elements
export const create_node = (elemn) => {
  return document.createElement(elemn);
};

/* Get elements from navigation */
export const go_back_lazygram = $("#gb-lazygram");
export const home_menu = $("#home-menu");
/* Categories */

// export const ctgy_action = $('#28').addEventListener('click', ()=>{category_select_view(37)})
// export const ctgy_adventure = $('#12').addEventListener('click', ()=>{category_select_view(37)})
// export const ctgy_animation = $('#16').addEventListener('click', ()=>{category_select_view(37)})
// export const ctgy_comedy = $('#35').addEventListener('click', ()=>{category_select_view(37)})
// export const ctgy_crime = $('#80').addEventListener('click', ()=>{category_select_view(37)})
// export const ctgy_documentary = $('#99').addEventListener('click', ()=>{category_select_view(37)})
// export const ctgy_drama = $('#18').addEventListener('click', ()=>{category_select_view(37)})
// export const ctgy_family = $('#10751').addEventListener('click', ()=>{category_select_view(37)})
// export const ctgy_fantasy = $('#14').addEventListener('click', ()=>{category_select_view(37)})
// export const ctgy_history = $('#36').addEventListener('click', ()=>{category_select_view(37)})
// export const ctgy_horror = $('#27').addEventListener('click', ()=>{category_select_view(37)})
// export const ctgy_music = $('#10402').addEventListener('click', ()=>{category_select_view(37)})
// export const ctgy_mystery = $('#9648').addEventListener('click', ()=>{category_select_view(37)})
// export const ctgy_romance = $('#10749').addEventListener('click', ()=>{category_select_view(37)})
// export const ctgy_science_fiction = $('#878').addEventListener('click', ()=>{category_select_view(37)})
// export const ctgy_tv_movie = $('#10770').addEventListener('click', ()=>{category_select_view(37)})
// export const ctgy_thriller = $('#53').addEventListener('click', ()=>{category_select_view(37)})
// export const ctgy_war = $('#10752').addEventListener('click', ()=>{category_select_view(37)})
// export const ctgy_western = $('#37').addEventListener('click', ()=>{category_select_view(37)})

/* Top rated */
export const trends = $("#trends");
/* Search button */
export const search_btn = $("#search-mv");
export const inp_search_mv = $("#inp-search-mv");
/* Title window */
export const title_window = $("#title-window");

/* Containers for do not overload */

export const main = $("#main");
export const aside = $('#aside-bar')

// Trends
export const container_trends_main = $("#container-trends");