
# Weather Dashboard HTML
weather_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Weather Dashboard - Day 5</title>
    <link rel="stylesheet" href="weather-dashboard.css">
</head>
<body>
    <div class="container">
        <header>
            <h1>🌤️ Weather Dashboard</h1>
            <p>Async JavaScript & API Integration Demo</p>
        </header>

        <div class="search-section">
            <input 
                type="text" 
                id="cityInput" 
                placeholder="Enter city name (e.g., London, Tokyo, New York)" 
                autocomplete="off"
            />
            <button id="searchBtn">Search Weather</button>
        </div>

        <div id="loadingState" class="loading hidden">
            <div class="spinner"></div>
            <p>Loading weather data...</p>
        </div>

        <div id="errorState" class="error hidden">
            <p id="errorMessage"></p>
        </div>

        <div id="weatherDisplay" class="weather-display hidden">
            <div class="weather-main">
                <h2 id="cityName"></h2>
                <div class="temperature">
                    <span id="temp"></span>
                    <span class="unit">°C</span>
                </div>
                <p id="description"></p>
                <img id="weatherIcon" src="" alt="Weather icon" />
            </div>

            <div class="weather-details">
                <div class="detail-item">
                    <span class="detail-label">Feels Like</span>
                    <span id="feelsLike" class="detail-value"></span>
                </div>
                <div class="detail-item">
                    <span class="detail-label">Humidity</span>
                    <span id="humidity" class="detail-value"></span>
                </div>
                <div class="detail-item">
                    <span class="detail-label">Wind Speed</span>
                    <span id="windSpeed" class="detail-value"></span>
                </div>
                <div class="detail-item">
                    <span class="detail-label">Pressure</span>
                    <span id="pressure" class="detail-value"></span>
                </div>
            </div>
        </div>

        <div class="info-section">
            <h3>How to use this dashboard:</h3>
            <ol>
                <li>Enter a city name in the search box</li>
                <li>Click "Search Weather" or press Enter</li>
                <li>View real-time weather data fetched from OpenWeatherMap API</li>
                <li>The app demonstrates <code>fetch()</code>, <code>async/await</code>, and error handling</li>
            </ol>
            <p class="note"><strong>Note:</strong> This demo uses OpenWeatherMap API. You need an API key for production use.</p>
        </div>
    </div>

    <script src="weather-dashboard.js"></script>
</body>
</html>"""

weather_css = """/* Weather Dashboard Styles */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    min-height: 100vh;
    padding: 20px;
    color: #333;
}

.container {
    max-width: 800px;
    margin: 0 auto;
}

header {
    text-align: center;
    color: white;
    margin-bottom: 30px;
}

header h1 {
    font-size: 2.5rem;
    margin-bottom: 10px;
}

header p {
    font-size: 1.1rem;
    opacity: 0.9;
}

.search-section {
    display: flex;
    gap: 10px;
    margin-bottom: 20px;
}

#cityInput {
    flex: 1;
    padding: 15px 20px;
    font-size: 1rem;
    border: none;
    border-radius: 10px;
    outline: none;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
}

#searchBtn {
    padding: 15px 30px;
    font-size: 1rem;
    background: #4CAF50;
    color: white;
    border: none;
    border-radius: 10px;
    cursor: pointer;
    font-weight: bold;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    transition: background 0.3s, transform 0.1s;
}

#searchBtn:hover {
    background: #45a049;
}

#searchBtn:active {
    transform: scale(0.98);
}

.loading, .error, .weather-display, .info-section {
    background: white;
    border-radius: 15px;
    padding: 30px;
    margin-bottom: 20px;
    box-shadow: 0 8px 16px rgba(0,0,0,0.1);
}

.hidden {
    display: none;
}

.loading {
    text-align: center;
}

.spinner {
    width: 50px;
    height: 50px;
    border: 5px solid #f3f3f3;
    border-top: 5px solid #667eea;
    border-radius: 50%;
    animation: spin 1s linear infinite;
    margin: 0 auto 20px;
}

@keyframes spin {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
}

.error {
    background: #ffebee;
    border-left: 4px solid #f44336;
    color: #c62828;
}

.weather-main {
    text-align: center;
    margin-bottom: 30px;
}

#cityName {
    font-size: 2rem;
    color: #667eea;
    margin-bottom: 20px;
}

.temperature {
    font-size: 4rem;
    font-weight: bold;
    color: #333;
    margin: 20px 0;
}

.unit {
    font-size: 2rem;
    color: #666;
}

#description {
    font-size: 1.3rem;
    color: #666;
    text-transform: capitalize;
    margin: 10px 0;
}

#weatherIcon {
    width: 100px;
    height: 100px;
}

.weather-details {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
    gap: 20px;
    margin-top: 30px;
}

.detail-item {
    text-align: center;
    padding: 20px;
    background: #f5f5f5;
    border-radius: 10px;
}

.detail-label {
    display: block;
    font-size: 0.9rem;
    color: #666;
    margin-bottom: 10px;
}

.detail-value {
    display: block;
    font-size: 1.5rem;
    font-weight: bold;
    color: #333;
}

.info-section h3 {
    color: #667eea;
    margin-bottom: 15px;
}

.info-section ol {
    margin-left: 20px;
    line-height: 1.8;
}

.info-section code {
    background: #f5f5f5;
    padding: 2px 6px;
    border-radius: 3px;
    font-family: 'Courier New', monospace;
}

.note {
    margin-top: 15px;
    padding: 15px;
    background: #fff3cd;
    border-left: 4px solid #ffc107;
    border-radius: 5px;
}

@media (max-width: 600px) {
    header h1 {
        font-size: 2rem;
    }

    .temperature {
        font-size: 3rem;
    }

    .search-section {
        flex-direction: column;
    }
}"""

weather_js = """// ============================================================
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
console.log('\\nAsync patterns demonstrated:');
console.log('- fetch() with async/await');
console.log('- Error handling with try/catch');
console.log('- Loading states');
console.log('- Promise.all() for parallel requests');
console.log('- Promise.race() for fastest response');

// Load default city on page load
window.addEventListener('load', () => {
    cityInput.value = 'London';
    handleSearch();
});"""

with open('weather-dashboard.html', 'w', encoding='utf-8') as f:
    f.write(weather_html)
with open('weather-dashboard.css', 'w', encoding='utf-8') as f:
    f.write(weather_css)
with open('weather-dashboard.js', 'w', encoding='utf-8') as f:
    f.write(weather_js)

print("✓ Generated: weather-dashboard.html")
print("✓ Generated: weather-dashboard.css")
print("✓ Generated: weather-dashboard.js")
