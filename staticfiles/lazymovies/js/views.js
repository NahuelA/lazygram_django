/* Function views for lazymovies */

// Imports
import {
    container_trends_main,
    main,
    aside,
    aside_container,
    title_window,
    relative_container,

    // Function create_elements
    api,
} from './main.js'

// Import utils
import {
    create_elements,
    $,
    img_size_3,
    original_size,
    create_node,
    get_home,
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
        const { poster_path, id } = src
        // Img
        const poster_popular = create_node('img')

        // classList
        poster_popular.classList = 'trendings-imgs'
        poster_popular.src = img_size_3 + poster_path

        // Containers
        const container_opacity_hover = create_node('div')
        const container_trends_ = create_node('div')

        // classList
        container_trends_.classList =
            'position-relative-0x container-categories-abs'
        container_opacity_hover.classList = 'position-absolutex hover-opacity'

        // Add details
        container_trends_.addEventListener('click', () => {
            location.hash = `#movie=${id}`
        })

        // Appends
        container_trends_.append(container_opacity_hover, poster_popular)
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

    /* Deactive */
    main.classList = 'col-sm-10'
    container_trends_main.classList.add('inactive')
    aside_container.classList.remove('inactive')
    relative_container.classList = 'position-relative row'
    section_movie.innerHTML = ''
    section_movie.classList = 'main-section'

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

    /* Deactive */
    container_trends_main.classList.add('inactive')
    aside_container.classList.remove('inactive')

    // Title and view construction
    const title_for_view = `Results to search ${query_movie}`
    create_view(data.results, title_for_view)
}

// Movie details
export const movie_details = async (movie_id) => {
    const { data } = await api(`movie/${movie_id}`)
    console.log(data)

    // Reset container
    container_trends_main.classList.add('inactive')
    container_trends_main.innerHTML = ''
    main.innerHTML = ''
    section_movie.innerHTML = ''

    // Reset classList
    main.classList = ''
    relative_container.classList = 'position-relative'
    aside_container.classList.add('inactive')

    // Create elements

    // Principal img
    const container_detail_img = create_node('div')
    const detail_img = create_node('img')
    detail_img.src = original_size + data.backdrop_path

    // Containers
    const container_title_rate = create_node('div')

    // Rated
    const container_popularity = create_node('div')
    const container_grid_popularity = create_node('div')
    const star_rated = create_node('i')
    const rated = create_node('p')

    // Title
    const container_title = create_node('div')

    // Description
    const description_p = create_node('p')

    // Categories
    const container_category = create_node('div')

    if (data.genres.length > 1) {
        data.genres.forEach((category) => {
            // Category
            const category_btn = create_node('button')
            category_btn.innerHTML = category.name
            category_btn.id = category.id

            // classList
            category_btn.classList = `fs-6 btn btn-primary mrg-1 ctgy`
            container_category.appendChild(category_btn)
        })
    } else {
        // Category
        const category_btn = create_node('button')
        category_btn.innerHTML = data.genres.name
        category_btn.id = data.genres.id

        // classList
        category_btn.classList = `fs-6 btn btn-primary mrg-1 ctgy`
        container_category.appendChild(category_btn)
    }

    // classList

    // Img
    container_detail_img.classList = 'container-detail-img'
    detail_img.classList = 'detail-img'

    // Title and Rate
    container_title_rate.classList = 'row mt-4'
    container_title.classList = 'col-sm-8'

    container_popularity.classList = 'col-sm'
    container_grid_popularity.classList = 'grid-cols-details fs-4'
    star_rated.classList = 'fa-solid fa-star'

    // Description
    description_p.classList = 'fs-5'

    // Container
    section_movie.classList = 'main-section-detail details'

    // Appends

    // Rated
    rated.innerHTML = `${data.vote_average.toFixed(1)}`
    container_grid_popularity.append(star_rated, rated)
    container_popularity.appendChild(container_grid_popularity)

    // Title
    h2_title.innerHTML = `${data.title}`
    container_title.append(h2_title, description_p)

    // Description
    description_p.innerHTML = `${data.overview}`

    // Img
    container_detail_img.appendChild(detail_img)

    // Containers
    container_title_rate.append(container_title, container_popularity)
    section_movie.append(container_title_rate, container_category)
    main.append(container_detail_img, section_movie)

    // Select any category and go to movies and change hash
    document.querySelectorAll('.ctgy').forEach((cat) => {
        cat.addEventListener('click', () => {
            location.hash = `#category=${cat.id}`
        })
    })
    await get_home(`/movie/${movie_id}/recommendations`, 'Recommended','main-section-detail')
}
