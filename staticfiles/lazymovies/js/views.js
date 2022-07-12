/* Function views for lazymovies */

// Imports
import {
    container_trends_main,
    main,
    aside,
    title_window,

    // Function create_elements
    api,
} from './main.js'

// Import utils
import {
    create_elements,
    $,
    img_size_3,
    create_node,
    main_container_grid,
    h2_title,
    section_movie,
} from './utils.js'

/* Home view */

// Get trends movies in HOME
export const get_trends_home = async () => {
    // GET from tmdb (trends)
    const { data } = await api('trending/movie/day')

    // GET all results
    const movies = data.results

    // inactive
    container_trends_main.classList.remove('inactive')

    // Reset container
    container_trends_main.innerHTML = ''

    /* Create global elements */
    const container_article_trends = create_node('div')

    // classList
    container_article_trends.classList = 'container-trendings-imgs'

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

// Categories links
export const categories_links = async () => {
    /* Get movies category */
    const { data } = await api('/genre/movie/list')
    const res = data.genres

    // Change title window
    title_window.innerHTML = 'Lazymovies | Categories'

    // Reset container
    aside.innerHTML = ''

    /* Create elements */

    // Title
    const h2_title = create_node('h2')
    h2_title.innerHTML = 'Categories'

    // container
    const section_category = create_node('section')
    const container_category = create_node('div')

    // classList //

    // Title
    h2_title.classList = 'title'

    // Containers
    section_category.classList = 'main-section'
    container_category.classList = 'align-cnt'

    // Appends
    h2_title.innerHTML = 'Categories'
    container_category.appendChild(h2_title)
    section_category.appendChild(container_category)
    aside.appendChild(section_category)
    // Create links to each category
    res.forEach((category) => {
        // Category
        const category_btn = create_node('button')
        category_btn.innerHTML = category.name
        category_btn.id = category.id

        // classList
        category_btn.classList = `fs-6 btn btn-primary mrg-1 ctgy`
        container_category.appendChild(category_btn)
    })

    // Select any category and go to movies and change hash
    document.querySelectorAll('.ctgy').forEach((category) => {
        category.addEventListener('click', () => {
            location.hash = `#category=${category.id}`
        })
    })
}

// If select one category, return a view with this category
export const category_select_view = async (category_id) => {
    let all_movies
    let genres_
    let ctgy_name = undefined
    let i = 0

    /* Active */
    container_trends_main.classList.add('inactive')

    // Reset container
    main.innerHTML = ''
    main_container_grid.innerHTML = ''

    /* Global elements*/

    // classList
    h2_title.classList = 'title left'

    // Appends
    section_movie.append(h2_title, main_container_grid)
    main.appendChild(section_movie)
    axios
        .all([await api('/discover/movie'), await api('/genre/movie/list')])
        .then(
            axios.spread((data, categories) => {
                // Get movies and categories
                all_movies = data.data.results
                genres_ = categories.data.genres

                // Get name of category select
                while (ctgy_name == undefined) {
                    if (genres_[i].id == category_id) {
                        ctgy_name = genres_[i].name
                        break
                    }
                    i += 1
                }
                // Add title
                h2_title.innerHTML = `${ctgy_name}`
                // Change title window
                title_window.innerHTML = `Lazymovies | ${ctgy_name}`

                // Get movies with the category select
                all_movies.forEach((category_movie) => {
                    category_movie.genre_ids.forEach((id) => {
                        if (id == category_id) {
                            create_elements(category_movie)
                        }
                    })
                })
            })
        )
}

// Search movies
export const search_movies = async (query_movie) => {
    const { data } = await api('/search/movie', {
        params: {
            query: query_movie,
            include_adult: false,
        },
    })

    /* Active */
    container_trends_main.classList.add('inactive')

    // Title and view construction
    const title_for_view = `Results to search ${query_movie}`
    create_view(data.results, title_for_view)
}

// Movie details

export const movie_details = async (movie_id) => {

    const { data } = api(`movie/${movie_id}`)
    console.log(data)

    // Create elements

    const container_detail_img = create_node('div')
    const detail_img = create_node('img')

    // Containers

    // Reset container
    main.innerHTML = ''
}
