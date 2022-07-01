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
export const categories_menu = $("#categories-menu");
export const action_cm = $("#action-cm");
export const romance_cm = $("#romance-cm");
export const horror_cm = $("#horror-cm");
export const drama_cm = $("#drama-cm");
/* Top rated */
export const trends = $("#trends");
/* Search button */
export const search_btn = $("#search-mv");
export const inp_search_mv = $("#inp-search-mv");
/* Title window */
export const title_window = $("#title-window");

/* Containers for do not overload */

export const main = $("#main");
// Trends
export const container_trends_main = $("#container-trends");