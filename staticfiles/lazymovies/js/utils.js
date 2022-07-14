// Global utils for aplication

// Imports
import {
    container_trends_main,
    main,
    title_window,

    // Function create_elements
    api,
    aside_container,
    relative_container,
} from './main.js'

import { categories_links } from './views.js'
/* Global elements*/

// Create elements
export const create_node = (elemn) => {
    return document.createElement(elemn)
}

// Query selector
export const $ = (id) => {
    return document.querySelector(id)
}

/* Global const */

// Title
export const h2_title = create_node('h2')

// Containers
export const section_movie = create_node('section')
export const main_container_grid = create_node('div')

// classList
main_container_grid.classList = 'main-container-grid'
section_movie.classList = 'main-section'

// IMG size
export const img_size_3 = 'https://image.tmdb.org/t/p/w500/'
export const original_size = 'https://image.tmdb.org/t/p/original/'

/* Functions views */

// Create articles for movies
export function create_elements(res_) {
    /* Get popularity,poster_path,release_date */
    const { vote_average, poster_path, release_date, id } = res_

    // Create elements //

    // Containers
    const article_movie = create_node('article')

    // Img
    const poster_img = create_node('img')

    // Rated
    const container_popularity = create_node('div')
    const star_rated = create_node('i')
    const rated = create_node('p')

    // Date
    const container_date = create_node('div')
    const date = create_node('p')

    // classList //

    // Containers
    article_movie.classList = 'container-article hover-opacity'

    // Img and lazyloading
    poster_img.classList = 'poster-movi'
    poster_img.src = img_size_3 + poster_path
    // poster_img.dataset.src = img_size_3 + poster_path

    // Rated
    container_popularity.classList = 'grid-cols'
    star_rated.classList = 'fa-solid fa-star'

    // Date
    container_date.classList = 'date-movies'
    date.classList = 'date-text'

    // Appends //

    // Rated
    rated.innerHTML = `${vote_average.toFixed(1)}`
    container_popularity.append(star_rated, rated)

    // Date
    date.innerHTML = `${release_date}`
    container_date.appendChild(date)

    // Add details
    article_movie.addEventListener('click', () => {
        location.hash = `#movie=${id}`
    })

    // Containers
    article_movie.append(poster_img, container_popularity, container_date)
    main_container_grid.appendChild(article_movie)
}

/* Create template view for any movies */
export const create_view = (query, title) => {
    // Reset containers
    main.innerHTML = ''
    main.classList = 'col-sm-10'
    main_container_grid.innerHTML = ''

    // Change title window
    title_window.innerHTML = `Lazymovies | ${title}`

    // classList

    // Title
    h2_title.classList = 'title left'

    // Containers
    section_movie.classList = 'main-section'
    main_container_grid.classList = 'main-container-grid'

    // Appends
    h2_title.innerHTML = `${title}`
    section_movie.append(h2_title, main_container_grid)

    main.append(section_movie)

    query.forEach((res) => {
        create_elements(res)
    })
}

// Movies views
export const get_views = async (url_movie_class, title) => {
    /* Get movie class general in main section */
    const { data } = await api(url_movie_class)
    const res = data.results

    /* Reset */
    container_trends_main.classList.add('inactive')
    relative_container.classList = 'position-relative-1x row'
    main.innerHTML = ''
    main.classList = 'col-sm-10'
    section_movie.innerHTML = ''
    section_movie.classList = 'main-section'
    aside_container.classList.remove('inactive')

    create_view(res, title)
    await categories_links()
}

// GET movies in HOME
// Principal title
const h2_principal = create_node('h2')
h2_principal.innerHTML = 'The Movigram TV for lazygrams users'
h2_principal.classList = 'align-cnt title'

export const get_home = async (
    url_movie_home,
    title,
    section_class='main-section',
    principal_title = false
) => {
    /* GET movies in home section */
    const { data } = await api(url_movie_home)
    const results = data.results

    // Change title window
    title_window.innerHTML = 'Lazymovies | Home'

    /* Global elements */

    // Titles
    const h3_title = create_node('h3')

    // Containers
    const section_movie = create_node('section')
    const container_movies = create_node('div')

    /* classList */
    section_movie.classList = section_class
    container_movies.classList = 'main-container'
    h3_title.classList = 'title'

    // Appends
    h3_title.innerHTML = `${title}`

    section_movie.appendChild(container_movies)
    section_movie.insertBefore(h3_title, container_movies)

    results.forEach((result) => {
        /* Get popularity,poster_path,release_date */

        let { vote_average, poster_path, release_date, id } = result

        /* Create elements */

        // Containers
        const article_movie = create_node('article')

        // Img
        const poster_img = create_node('img')

        // Rated
        const container_popularity = create_node('div')
        const star_rated = create_node('i')
        const rated = create_node('p')

        // Date
        const container_date = create_node('div')
        const date = create_node('p')

        /* classList */

        // Containers
        article_movie.classList = 'container-poster hover-opacity'

        // Img
        poster_img.classList = 'poster-movi lazy'
        poster_img.src = img_size_3 + poster_path
        // poster_img.dataset.src = img_size_3 + poster_path

        // Rated
        container_popularity.classList = 'grid-cols'
        star_rated.classList = 'fa-solid fa-star'

        // Date
        container_date.classList = 'date-movies'
        date.classList = 'date-text'

        // Add details
        article_movie.addEventListener('click', () => {
            location.hash = `#movie=${id}`
        })

        // Appends
        container_popularity.append(star_rated, rated)
        rated.textContent = `${vote_average.toFixed(1)}`

        container_date.appendChild(date)
        date.innerHTML = `${release_date}`

        article_movie.append(poster_img, container_popularity, container_date)
        container_movies.appendChild(article_movie)
        section_movie.appendChild(container_movies)

        // For add principal title one time
        if (principal_title == true) {
            main.appendChild(h2_principal)
        }

        main.appendChild(section_movie)
    })
}
