// ============================================================
// Weather Dashboard - Async JS & API Integration
// Day 5: fetch(), async/await, Error Handling
// ============================================================

// OpenWeatherMap API configuration
// NOTE: For production, get your own API key from https://openweathermap.org/api
const API_KEY = 'demo'; // Replace with actual API key for production
const API_BASE_URL = 'https://api.openweathermap.org/data/2.5/weather';

// DOM Elements
const cityInput = document.getElementById('cityInput');
const searchBtn = document.getElementById('searchBtn');
const loadingState = document.getElementById('loadingState');
const errorState = document.getElementById('errorState');
const weatherDisplay = document.getElementById('weatherDisplay');
const errorMessage = document.getElementById('errorMessage');

// ============================================================
// FETCH WEATHER DATA USING ASYNC/AWAIT
// ============================================================

/**
 * Fetches weather data for a given city
 * Demonstrates: async/await, fetch API, error handling
 * @param {string} city - City name to search
 * @returns {Promise<Object>} Weather data object
 */
async function fetchWeatherData(city) {
    try {
        // Show loading state
        showLoading();

        // Build API URL with query parameters
        const url = `${API_BASE_URL}?q=${encodeURIComponent(city)}&appid=${API_KEY}&units=metric`;

        // Fetch data from API
        const response = await fetch(url);

        // Check if response is successful
        if (!response.ok) {
            if (response.status === 404) {
                throw new Error('City not found. Please check the spelling and try again.');
            } else if (response.status === 401) {
                // For demo purposes, use mock data if API key is invalid
                console.warn('API key not configured. Using mock data for demonstration.');
                return getMockWeatherData(city);
            } else {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
        }

        // Parse JSON response
        const data = await response.json();

        // Hide loading state
        hideLoading();

        return data;

    } catch (error) {
        hideLoading();

        // Handle different types of errors
        if (error.name === 'TypeError') {
            throw new Error('Network error. Please check your internet connection.');
        } else {
            throw error;
        }
    }
}

/**
 * Mock weather data for demonstration when API key is not available
 */
function getMockWeatherData(city) {
    const mockData = {
        name: city.charAt(0).toUpperCase() + city.slice(1),
        main: {
            temp: 22,
            feels_like: 20,
            humidity: 65,
            pressure: 1013
        },
        weather: [
            {
                description: 'partly cloudy',
                icon: '02d'
            }
        ],
        wind: {
            speed: 5.5
        }
    };

    return mockData;
}

// ============================================================
// DISPLAY WEATHER DATA
// ============================================================

/**
 * Displays weather information in the UI
 * @param {Object} data - Weather data from API
 */
function displayWeather(data) {
    // Extract data from response
    const {
        name,
        main: { temp, feels_like, humidity, pressure },
        weather,
        wind: { speed }
    } = data;

    // Update DOM elements
    document.getElementById('cityName').textContent = name;
    document.getElementById('temp').textContent = Math.round(temp);
    document.getElementById('description').textContent = weather[0].description;
    document.getElementById('weatherIcon').src = `https://openweathermap.org/img/wn/${weather[0].icon}@2x.png`;

    document.getElementById('feelsLike').textContent = `${Math.round(feels_like)}°C`;
    document.getElementById('humidity').textContent = `${humidity}%`;
    document.getElementById('windSpeed').textContent = `${speed} m/s`;
    document.getElementById('pressure').textContent = `${pressure} hPa`;

    // Show weather display
    weatherDisplay.classList.remove('hidden');
}

// ============================================================
// UI STATE MANAGEMENT
// ============================================================

function showLoading() {
    loadingState.classList.remove('hidden');
    weatherDisplay.classList.add('hidden');
    errorState.classList.add('hidden');
}

function hideLoading() {
    loadingState.classList.add('hidden');
}

function showError(message) {
    errorMessage.textContent = message;
    errorState.classList.remove('hidden');
    weatherDisplay.classList.add('hidden');
}

function hideError() {
    errorState.classList.add('hidden');
}

// ============================================================
// SEARCH HANDLER WITH ERROR HANDLING
// ============================================================

/**
 * Handles weather search with comprehensive error handling
 */
async function handleSearch() {
    const city = cityInput.value.trim();

    // Validate input
    if (!city) {
        showError('Please enter a city name');
        return;
    }

    hideError();

    try {
        // Fetch weather data
        const weatherData = await fetchWeatherData(city);

        // Display weather information
        displayWeather(weatherData);

    } catch (error) {
        // Show user-friendly error message
        showError(error.message);
        console.error('Weather fetch error:', error);
    }
}

// ============================================================
// EVENT LISTENERS
// ============================================================

// Search button click
searchBtn.addEventListener('click', handleSearch);

// Enter key press in input field
cityInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
        handleSearch();
    }
});

// ============================================================
// DEMONSTRATION OF ASYNC PATTERNS
// ============================================================

// Example 1: Promise with .then() (older style)
function fetchWithPromise(city) {
    return fetch(`${API_BASE_URL}?q=${city}&appid=${API_KEY}`)
        .then(response => response.json())
        .then(data => {
            console.log('Promise style:', data);
            return data;
        })
        .catch(error => {
            console.error('Promise error:', error);
        });
}

// Example 2: Multiple parallel requests with Promise.all()
async function fetchMultipleCities(cities) {
    try {
        const promises = cities.map(city => fetchWeatherData(city));
        const results = await Promise.all(promises);
        console.log('Multiple cities:', results);
        return results;
    } catch (error) {
        console.error('Multiple fetch error:', error);
    }
}

// Example 3: Race condition with Promise.race()
async function fetchFastest(cities) {
    try {
        const promises = cities.map(city => fetchWeatherData(city));
        const fastest = await Promise.race(promises);
        console.log('Fastest response:', fastest);
        return fastest;
    } catch (error) {
        console.error('Race error:', error);
    }
}

// Log async examples
console.log('Weather Dashboard loaded!');
console.log('Try searching for cities like: London, Tokyo, New York, Paris');
console.log('\nAsync patterns demonstrated:');
console.log('- fetch() with async/await');
console.log('- Error handling with try/catch');
console.log('- Loading states');
console.log('- Promise.all() for parallel requests');
console.log('- Promise.race() for fastest response');

// Load default city on page load
window.addEventListener('load', () => {
    cityInput.value = 'London';
    handleSearch();
});