/* Function views for lazymovies */

// Imports
import {
    container_trends_main,
    main,
    title_window,

    // Function create_elements
    create_node,
    img_size_3,
    api,
    $,
} from './main.js'

/* Home view */

// Get trends movies in HOME
export const get_trends_home = async () => {
    // GET from tmdb (trends)
    const { data } = await api('trending/movie/day')

    // GET all results
    const movies = data.results

    // Reset container
    container_trends_main.innerHTML = ''

    /* Create global elements */
    const container_article_trends = create_node('div')

    // classList
    container_article_trends.classList = 'container-trendings-imgs'
    main.classList = 'position-relative-1x'

    movies.forEach((src) => {
        // Img
        const poster_popular = create_node('img')

        // class List
        poster_popular.classList = 'trendings-imgs'
        poster_popular.src = img_size_3 + src.poster_path
        poster_popular.loading = 'lazy'

        // Container div
        const container_trends_ = create_node('div')
        container_trends_.classList = 'container-categories-abs'

        // Appends
        container_trends_.appendChild(poster_popular)
        container_article_trends.appendChild(container_trends_)
        container_trends_main.appendChild(container_article_trends)
    })
}

// Principal title
const h2_principal = create_node('h2')
h2_principal.innerHTML = 'The Movigram TV for lazygrams users'
h2_principal.classList = 'principal-title'

// GET movies in HOME
export const get_home = async (url_movie_home, title, principal_title=false) => {

    /* GET movies in home section */
    const { data } = await api(url_movie_home)
    const results = data.results

    // Change title window
    title_window.innerHTML='Lazymovies | Home'

    /* Active */
    container_trends_main.classList.remove('inactive')

    /* Global elements */

    // Titles
    const h3_title = create_node('h3')
    
    // Containers
    const section_movie = create_node('section')
    const container_movies = create_node('div')
    
    /* classList */
    section_movie.classList = 'main-section'
    container_movies.classList = 'main-container'
    h3_title.classList = 'title'

    
    // Appends
    h3_title.innerHTML = `${title}`

    section_movie.appendChild(container_movies)
    section_movie.insertBefore(h3_title, container_movies)

    results.forEach((result) => {

        /* Get popularity,poster_path,release_date */
        let { popularity, poster_path, release_date } = result

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
        article_movie.classList = 'container-poster'
        
        // Img and lazyloading
        poster_img.classList = 'poster-movi'
        poster_img.loading = 'lazy'
        poster_img.src = img_size_3 + poster_path

        // Rated
        container_popularity.classList = 'grid-cols'
        star_rated.classList = 'fa-solid fa-star'
        
        // Date
        container_date.classList = 'date-movies'
        date.classList = 'date-text'

        // Appends
        container_popularity.append(star_rated, rated)
        rated.textContent = `${popularity}`

        container_date.appendChild(date)
        date.innerHTML = `${release_date}`

        article_movie.append(
                    poster_img,
                    container_popularity,
                    container_date,
                )
        container_movies.appendChild(article_movie)
        section_movie.appendChild(container_movies)

        // For add principal title one time
        if (principal_title == true){
            main.appendChild(h2_principal)
        }

        main.appendChild(section_movie)
    })
}

// Movies views
export const get_views = async (url_movie_class, title) => {

    /* Get movie class general in main section */
    const { data } = await api(url_movie_class)
    const res = data.results

    /* Inactive */
    container_trends_main.classList.add('inactive')

    // Reset container
    main.innerHTML = '' 
    // Change title window
    title_window.innerHTML = `Lazymovies | ${title}`

    /* Global elements*/

    // Title
    const h2_title = create_node('h2')

    // Containers
    const section_movie = create_node('section')
    const main_container_grid = create_node('div')

    /* classList */

    // Title
    h2_title.classList = 'principal-title'
    main.classList = 'position-relative-1x'
    
    // Containers
    section_movie.classList = 'main-section'
    main_container_grid.classList = 'main-container-grid'
    
    // Appends
    h2_title.innerHTML = `${title}`
    
    res.forEach((result) => {

        /* Get popularity,poster_path,release_date */
        const { popularity, poster_path, release_date } = result

        /* Create elements */

        // Container
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
        article_movie.classList = 'container-article'

        // Img and lazyloading
        poster_img.classList = 'poster-movi'
        poster_img.loading = 'lazy'
        poster_img.src = img_size_3 + poster_path

        // Rated
        container_popularity.classList = 'grid-cols'
        star_rated.classList = 'fa-solid fa-star'

        // Date
        container_date.classList = 'date-movies'
        date.classList = 'date-text'

        // Appends
        rated.innerHTML = `${popularity}`
        container_popularity.append(star_rated, rated)

        date.innerHTML = `${release_date}`
        container_date.appendChild(date)

        article_movie.append(
                    poster_img,
                    container_popularity,
                    container_date,
                )
        main_container_grid.appendChild(article_movie)
        section_movie.append(main_container_grid)

        main.append(h2_title, section_movie)
    })
}

/* Categories function view */
const categories_view = () => {}

// If select one category, return a view with this category
const category_select_view = (category) => {}

/* Search function view */
const search_view = () => {}
