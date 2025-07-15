// DOM Elements
const form = document.getElementById('predictionForm');
const locationSelect = document.getElementById('location');
const sqftInput = document.getElementById('sqft');
const bathInput = document.getElementById('bath');
const bhkInput = document.getElementById('bhk');
const predictBtn = document.getElementById('predictBtn');
const resultContainer = document.getElementById('resultContainer');
const priceValue = document.getElementById('priceValue');
const resultLocation = document.getElementById('resultLocation');
const resultSqft = document.getElementById('resultSqft');
const resultConfig = document.getElementById('resultConfig');
const loadingOverlay = document.getElementById('loadingOverlay');
const errorModal = document.getElementById('errorModal');
const closeModal = document.getElementById('closeModal');
const errorMessage = document.getElementById('errorMessage');

// API Configuration
const API_BASE_URL = 'http://localhost:8000';

// Bangalore locations data (from columns.json)
const locations = [
    "1st block jayanagar", "1st phase jp nagar", "2nd phase judicial layout", "2nd stage nagarbhavi", 
    "5th block hbr layout", "5th phase jp nagar", "6th phase jp nagar", "7th phase jp nagar", 
    "8th phase jp nagar", "9th phase jp nagar", "aecs layout", "abbigere", "akshaya nagar", 
    "ambalipura", "ambedkar nagar", "amruthahalli", "anandapura", "ananth nagar", "anekal", 
    "anjanapura", "ardendale", "arekere", "attibele", "beml layout", "btm 2nd stage", "btm layout", 
    "babusapalaya", "badavala nagar", "balagere", "banashankari", "banashankari stage ii", 
    "banashankari stage iii", "banashankari stage v", "banashankari stage vi", "banaswadi", 
    "banjara layout", "bannerghatta", "bannerghatta road", "basavangudi", "basaveshwara nagar", 
    "battarahalli", "begur", "begur road", "bellandur", "benson town", "bharathi nagar", 
    "bhoganhalli", "billekahalli", "binny pete", "bisuvanahalli", "bommanahalli", "bommasandra", 
    "bommasandra industrial area", "bommenahalli", "brookefield", "budigere", "cv raman nagar", 
    "chamrajpet", "chandapura", "channasandra", "chikka tirupathi", "chikkabanavar", 
    "chikkalasandra", "choodasandra", "cooke town", "cox town", "cunningham road", "dasanapura", 
    "dasarahalli", "devanahalli", "devarachikkanahalli", "dodda nekkundi", "doddaballapur", 
    "doddakallasandra", "doddathoguru", "domlur", "dommasandra", "epip zone", "electronic city", 
    "electronic city phase ii", "electronics city phase 1", "frazer town", "gm palaya", 
    "garudachar palya", "giri nagar", "gollarapalya hosahalli", "gottigere", "green glen layout", 
    "gubbalala", "gunjur", "hal 2nd stage", "hbr layout", "hrbr layout", "hsr layout", 
    "haralur road", "harlur", "hebbal", "hebbal kempapura", "hegde nagar", "hennur", "hennur road", 
    "hoodi", "horamavu agara", "horamavu banaswadi", "hormavu", "hosa road", "hosakerehalli", 
    "hoskote", "hosur road", "hulimavu", "isro layout", "itpl", "iblur village", "indira nagar", 
    "jp nagar", "jakkur", "jalahalli", "jalahalli east", "jigani", "judicial layout", "kr puram", 
    "kadubeesanahalli", "kadugodi", "kaggadasapura", "kaggalipura", "kaikondrahalli", 
    "kalena agrahara", "kalyan nagar", "kambipura", "kammanahalli", "kammasandra", "kanakapura", 
    "kanakpura road", "kannamangala", "karuna nagar", "kasavanhalli", "kasturi nagar", 
    "kathriguppe", "kaval byrasandra", "kenchenahalli", "kengeri", "kengeri satellite town", 
    "kereguddadahalli", "kodichikkanahalli", "kodigehaali", "kodigehalli", "kodihalli", "kogilu", 
    "konanakunte", "koramangala", "kothannur", "kothanur", "kudlu", "kudlu gate", 
    "kumaraswami layout", "kundalahalli", "lb shastri nagar", "laggere", "lakshminarayana pura", 
    "lingadheeranahalli", "magadi road", "mahadevpura", "mahalakshmi layout", "mallasandra", 
    "malleshpalya", "malleshwaram", "marathahalli", "margondanahalli", "marsur", "mico layout", 
    "munnekollal", "murugeshpalya", "mysore road", "ngr layout", "nri layout", "nagarbhavi", 
    "nagasandra", "nagavara", "nagavarapalya", "narayanapura", "neeladri nagar", "nehru nagar", 
    "ombr layout", "old airport road", "old madras road", "padmanabhanagar", "pai layout", 
    "panathur", "parappana agrahara", "pattandur agrahara", "poorna pragna layout", "prithvi layout", 
    "r.t. nagar", "rachenahalli", "raja rajeshwari nagar", "rajaji nagar", "rajiv nagar", 
    "ramagondanahalli", "ramamurthy nagar", "rayasandra", "sahakara nagar", "sanjay nagar", 
    "sarakki nagar", "sarjapur", "sarjapur  road", "sarjapura - attibele road", "sector 2 hsr layout", 
    "sector 7 hsr layout", "seegehalli", "shampura", "shivaji nagar", "singasandra", 
    "somasundara palya", "sompura", "sonnenahalli", "subramanyapura", "sultan palaya", "tc palaya", 
    "talaghattapura", "thanisandra", "thigalarapalya", "thubarahalli", "tindlu", "tumkur road", 
    "ulsoor", "uttarahalli", "varthur", "varthur road", "vasanthapura", "vidyaranyapura", 
    "vijayanagar", "vishveshwarya layout", "vishwapriya layout", "vittasandra", "whitefield", 
    "yelachenahalli", "yelahanka", "yelahanka new town", "yelenahalli", "yeshwanthpur"
];

// Initialize the application
document.addEventListener('DOMContentLoaded', function() {
    initializeApp();
});

// Initialize application
function initializeApp() {
    populateLocations();
    setupEventListeners();
    addInteractiveEffects();
    
    // Check API health on startup and then periodically
    checkAPIHealth();
    
    // Set up periodic health checks every 30 seconds
    setInterval(checkAPIHealth, 30000);
}

// Populate location dropdown
function populateLocations() {
    // Sort locations alphabetically for better UX
    const sortedLocations = [...locations].sort();
    
    sortedLocations.forEach(location => {
        const option = document.createElement('option');
        option.value = location;
        option.textContent = location.charAt(0).toUpperCase() + location.slice(1);
        locationSelect.appendChild(option);
    });
}

// Setup event listeners
function setupEventListeners() {
    // Form submission
    form.addEventListener('submit', handleFormSubmit);
    
    // Number input controls
    setupNumberControls();
    
    // Input focus effects
    setupInputEffects();
    
    // Modal controls
    closeModal.addEventListener('click', hideErrorModal);
    errorModal.addEventListener('click', function(e) {
        if (e.target === errorModal) {
            hideErrorModal();
        }
    });
    
    // Keyboard shortcuts
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape') {
            hideErrorModal();
        }
        if (e.key === 'Enter' && e.ctrlKey) {
            handleFormSubmit(e);
        }
    });
}

// Setup number input controls
function setupNumberControls() {
    const numberBtns = document.querySelectorAll('.number-btn');
    
    numberBtns.forEach(btn => {
        btn.addEventListener('click', function() {
            const target = this.dataset.target;
            const input = document.getElementById(target);
            const isPlus = this.classList.contains('plus');
            const currentValue = parseInt(input.value);
            const min = parseInt(input.min);
            const max = parseInt(input.max);
            
            let newValue;
            if (isPlus) {
                newValue = currentValue < max ? currentValue + 1 : max;
            } else {
                newValue = currentValue > min ? currentValue - 1 : min;
            }
            
            input.value = newValue;
            
            // Add click animation
            this.style.transform = 'scale(0.9)';
            setTimeout(() => {
                this.style.transform = '';
            }, 150);
        });
    });
}

// Setup input focus effects
function setupInputEffects() {
    const inputs = document.querySelectorAll('input, select');
    
    inputs.forEach(input => {
        input.addEventListener('focus', function() {
            this.parentElement.classList.add('focused');
        });
        
        input.addEventListener('blur', function() {
            this.parentElement.classList.remove('focused');
        });
        
        // Add typing animation for text inputs
        if (input.type === 'number' && input.id === 'sqft') {
            input.addEventListener('input', function() {
                if (this.value) {
                    this.style.background = 'linear-gradient(90deg, rgba(0, 245, 255, 0.1) 0%, rgba(255, 255, 255, 0.05) 100%)';
                } else {
                    this.style.background = 'rgba(255, 255, 255, 0.05)';
                }
            });
        }
    });
}

// Add interactive effects
function addInteractiveEffects() {
    // Parallax effect for floating shapes
    document.addEventListener('mousemove', function(e) {
        const shapes = document.querySelectorAll('.shape');
        const mouseX = e.clientX / window.innerWidth;
        const mouseY = e.clientY / window.innerHeight;
        
        shapes.forEach((shape, index) => {
            const speed = (index + 1) * 0.5;
            const x = (mouseX - 0.5) * speed * 20;
            const y = (mouseY - 0.5) * speed * 20;
            
            shape.style.transform = `translate(${x}px, ${y}px)`;
        });
    });
    
    // Card hover effects
    const cards = document.querySelectorAll('.feature-card, .form-container, .result-container');
    cards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-5px) scale(1.02)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = '';
        });
    });
    
    // Button ripple effect
    const buttons = document.querySelectorAll('.predict-btn, .number-btn');
    buttons.forEach(button => {
        button.addEventListener('click', function(e) {
            const ripple = document.createElement('span');
            const rect = this.getBoundingClientRect();
            const size = Math.max(rect.width, rect.height);
            const x = e.clientX - rect.left - size / 2;
            const y = e.clientY - rect.top - size / 2;
            
            ripple.style.cssText = `
                position: absolute;
                border-radius: 50%;
                background: rgba(255, 255, 255, 0.3);
                transform: scale(0);
                left: ${x}px;
                top: ${y}px;
                width: ${size}px;
                height: ${size}px;
                pointer-events: none;
                animation: ripple 0.6s ease-out;
            `;
            
            this.appendChild(ripple);
            
            setTimeout(() => {
                ripple.remove();
            }, 600);
        });
    });
    
    // Add ripple animation
    const style = document.createElement('style');
    style.textContent = `
        @keyframes ripple {
            to {
                transform: scale(2);
                opacity: 0;
            }
        }
    `;
    document.head.appendChild(style);
}

// Track API connection state
let isFirstConnection = true;
let lastApiStatus = null;

// Check API health
async function checkAPIHealth() {
    try {
        const response = await fetch(`${API_BASE_URL}/health`);
        if (!response.ok) {
            throw new Error('API not available');
        }
        const data = await response.json();
        console.log('API Health:', data);
        
        // Show API status in UI
        showAPIStatus(data);
        
        // Only show notifications on status changes or first connection
        if (!data.model_loaded && (lastApiStatus === null || lastApiStatus.model_loaded !== data.model_loaded)) {
            showNotification('Warning: ML model not loaded properly', 'warning');
        } else if (data.model_loaded && isFirstConnection) {
            showNotification('API connected successfully!', 'success');
            isFirstConnection = false;
        }
        
        lastApiStatus = data;
    } catch (error) {
        console.error('API Health Check Failed:', error);
        showAPIStatus({ status: 'unhealthy', model_loaded: false });
        
        // Only show error notification if status changed
        if (lastApiStatus === null || lastApiStatus.status !== 'unhealthy') {
            showNotification('API connection failed. Please ensure the server is running.', 'error');
        }
        
        lastApiStatus = { status: 'unhealthy', model_loaded: false };
    }
}

// Show API status in UI
function showAPIStatus(data) {
    // Create or update status indicator
    let statusIndicator = document.getElementById('api-status');
    if (!statusIndicator) {
        statusIndicator = document.createElement('div');
        statusIndicator.id = 'api-status';
        statusIndicator.style.cssText = `
            position: fixed;
            top: 10px;
            left: 10px;
            padding: 0.5rem 1rem;
            border-radius: 20px;
            font-size: 0.8rem;
            z-index: 1000;
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.1);
        `;
        document.body.appendChild(statusIndicator);
    }
    
    const isHealthy = data.status === 'healthy' && data.model_loaded;
    statusIndicator.textContent = `API: ${data.status.toUpperCase()} | Model: ${data.model_loaded ? 'LOADED' : 'NOT LOADED'}`;
    statusIndicator.style.background = isHealthy ? 
        'linear-gradient(135deg, #00f5ff, #0080ff)' : 
        'linear-gradient(135deg, #ff4444, #ff8800)';
    statusIndicator.style.color = 'white';
}

// Handle form submission
async function handleFormSubmit(e) {
    e.preventDefault();
    
    // Get form data
    const formData = {
        location: locationSelect.value,
        sqft: parseFloat(sqftInput.value),
        bath: parseInt(bathInput.value),
        bhk: parseInt(bhkInput.value)
    };
    
    // Validate form data
    if (!validateFormData(formData)) {
        return;
    }
    
    // Show loading state
    showLoading(true);
    
    try {
        // Make prediction request
        const prediction = await makePrediction(formData);
        
        // Display results
        displayResults(prediction, formData);
        
        // Show success notification
        showNotification('Price prediction successful!', 'success');
        
    } catch (error) {
        console.error('Prediction Error:', error);
        showErrorModal(error.message || 'Failed to predict house price. Please try again.');
    } finally {
        showLoading(false);
    }
}

// Validate form data
function validateFormData(data) {
    if (!data.location) {
        showErrorModal('Please select a location.');
        return false;
    }
    
    if (!data.sqft || data.sqft < 100) {
        showErrorModal('Please enter a valid square feet (minimum 100).');
        return false;
    }
    
    if (!data.bath || data.bath < 1) {
        showErrorModal('Please enter a valid number of bathrooms.');
        return false;
    }
    
    if (!data.bhk || data.bhk < 1) {
        showErrorModal('Please enter a valid BHK value.');
        return false;
    }
    
    return true;
}

// Make prediction API call
async function makePrediction(data) {
    const response = await fetch(`${API_BASE_URL}/predict`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data)
    });
    
    if (!response.ok) {
        let errorMessage = `HTTP ${response.status}: ${response.statusText}`;
        try {
            const errorData = await response.json();
            errorMessage = errorData.detail || errorMessage;
        } catch (parseError) {
            console.error('Error parsing error response:', parseError);
        }
        throw new Error(errorMessage);
    }
    
    return await response.json();
}

// Display prediction results
function displayResults(prediction, formData) {
    // Animate price value
    animateValue(priceValue, 0, prediction.predicted_price, 1500);
    
    // Update result details
    resultLocation.textContent = formData.location.charAt(0).toUpperCase() + formData.location.slice(1);
    resultSqft.textContent = `${formData.sqft.toLocaleString()} sq ft`;
    resultConfig.textContent = `${formData.bhk} BHK, ${formData.bath} Bath`;
    
    // Show result container with animation
    resultContainer.classList.add('show');
    
    // Scroll to results
    setTimeout(() => {
        resultContainer.scrollIntoView({ 
            behavior: 'smooth', 
            block: 'nearest' 
        });
    }, 500);
    
    // Add celebration effect
    createCelebrationEffect();
}

// Animate number value
function animateValue(element, start, end, duration) {
    const range = end - start;
    const startTime = Date.now();
    
    function updateValue() {
        const elapsed = Date.now() - startTime;
        const progress = Math.min(elapsed / duration, 1);
        
        // Easing function for smooth animation
        const easeOutQuart = 1 - Math.pow(1 - progress, 4);
        const currentValue = start + (range * easeOutQuart);
        
        element.textContent = currentValue.toFixed(2);
        
        if (progress < 1) {
            requestAnimationFrame(updateValue);
        }
    }
    
    updateValue();
}

// Create celebration effect
function createCelebrationEffect() {
    const colors = ['#00f5ff', '#ff00ff', '#ffff00', '#00ff00', '#ff4500'];
    
    for (let i = 0; i < 50; i++) {
        setTimeout(() => {
            createConfetti(colors[Math.floor(Math.random() * colors.length)]);
        }, i * 20);
    }
}

// Create confetti particle
function createConfetti(color) {
    const confetti = document.createElement('div');
    confetti.style.cssText = `
        position: fixed;
        width: 6px;
        height: 6px;
        background: ${color};
        left: ${Math.random() * 100}vw;
        top: -10px;
        border-radius: 50%;
        pointer-events: none;
        z-index: 999;
        animation: confetti-fall 3s linear forwards;
        box-shadow: 0 0 10px ${color};
    `;
    
    document.body.appendChild(confetti);
    
    // Add confetti animation if not exists
    if (!document.querySelector('#confetti-style')) {
        const style = document.createElement('style');
        style.id = 'confetti-style';
        style.textContent = `
            @keyframes confetti-fall {
                0% {
                    transform: translateY(-10px) rotate(0deg);
                    opacity: 1;
                }
                100% {
                    transform: translateY(100vh) rotate(720deg);
                    opacity: 0;
                }
            }
        `;
        document.head.appendChild(style);
    }
    
    setTimeout(() => {
        confetti.remove();
    }, 3000);
}

// Show/hide loading overlay
function showLoading(show) {
    if (show) {
        loadingOverlay.classList.add('show');
        predictBtn.classList.add('loading');
        predictBtn.disabled = true;
        
        // Update loading text randomly
        const loadingTexts = [
            'Analyzing market data...',
            'Processing location factors...',
            'Calculating price trends...',
            'Applying ML algorithms...',
            'Finalizing prediction...'
        ];
        
        let textIndex = 0;
        const textInterval = setInterval(() => {
            if (loadingOverlay.classList.contains('show')) {
                document.querySelector('.loading-text').textContent = loadingTexts[textIndex];
                textIndex = (textIndex + 1) % loadingTexts.length;
            } else {
                clearInterval(textInterval);
            }
        }, 800);
        
    } else {
        loadingOverlay.classList.remove('show');
        predictBtn.classList.remove('loading');
        predictBtn.disabled = false;
    }
}

// Show error modal
function showErrorModal(message) {
    errorMessage.textContent = message;
    errorModal.classList.add('show');
    
    // Add shake animation to modal
    const modal = errorModal.querySelector('.modal');
    modal.style.animation = 'shake 0.5s ease-in-out';
    
    setTimeout(() => {
        modal.style.animation = '';
    }, 500);
}

// Hide error modal
function hideErrorModal() {
    errorModal.classList.remove('show');
}

// Show notification
function showNotification(message, type = 'info') {
    // Remove existing notification
    const existingNotification = document.querySelector('.notification');
    if (existingNotification) {
        existingNotification.remove();
    }
    
    const notification = document.createElement('div');
    notification.className = `notification notification-${type}`;
    notification.innerHTML = `
        <div class="notification-content">
            <i class="fas fa-${getNotificationIcon(type)}"></i>
            <span>${message}</span>
        </div>
        <button class="notification-close">
            <i class="fas fa-times"></i>
        </button>
    `;
    
    // Add notification styles
    notification.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        background: ${getNotificationColor(type)};
        color: white;
        padding: 1rem 1.5rem;
        border-radius: 10px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
        z-index: 1002;
        display: flex;
        align-items: center;
        gap: 1rem;
        transform: translateX(100%);
        transition: transform 0.3s ease;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        max-width: 400px;
    `;
    
    document.body.appendChild(notification);
    
    // Animate in
    setTimeout(() => {
        notification.style.transform = 'translateX(0)';
    }, 100);
    
    // Setup close button
    notification.querySelector('.notification-close').addEventListener('click', () => {
        notification.style.transform = 'translateX(100%)';
        setTimeout(() => notification.remove(), 300);
    });
    
    // Auto remove after 5 seconds
    setTimeout(() => {
        if (notification.parentElement) {
            notification.style.transform = 'translateX(100%)';
            setTimeout(() => notification.remove(), 300);
        }
    }, 5000);
}

// Get notification icon
function getNotificationIcon(type) {
    const icons = {
        success: 'check-circle',
        error: 'exclamation-triangle',
        warning: 'exclamation-circle',
        info: 'info-circle'
    };
    return icons[type] || 'info-circle';
}

// Get notification color
function getNotificationColor(type) {
    const colors = {
        success: 'linear-gradient(135deg, #43e97b 0%, #38f9d7 100%)',
        error: 'linear-gradient(135deg, #f093fb 0%, #f5576c 100%)',
        warning: 'linear-gradient(135deg, #ffa726 0%, #fb8c00 100%)',
        info: 'linear-gradient(135deg, #4facfe 0%, #00f2fe 100%)'
    };
    return colors[type] || colors.info;
}

// Add shake animation
const shakeStyle = document.createElement('style');
shakeStyle.textContent = `
    @keyframes shake {
        0%, 100% { transform: translateX(0); }
        10%, 30%, 50%, 70%, 90% { transform: translateX(-5px); }
        20%, 40%, 60%, 80% { transform: translateX(5px); }
    }
`;
document.head.appendChild(shakeStyle);

// Add performance monitoring
let performanceMetrics = {
    apiCalls: 0,
    averageResponseTime: 0,
    errors: 0
};

// Wrap fetch function to monitor performance
const originalFetch = window.fetch;
window.fetch = async function(...args) {
    const startTime = Date.now();
    performanceMetrics.apiCalls++;
    
    try {
        const response = await originalFetch.apply(this, args);
        const endTime = Date.now();
        const responseTime = endTime - startTime;
        
        // Update average response time
        performanceMetrics.averageResponseTime = 
            (performanceMetrics.averageResponseTime * (performanceMetrics.apiCalls - 1) + responseTime) / 
            performanceMetrics.apiCalls;
        
        return response;
    } catch (error) {
        performanceMetrics.errors++;
        throw error;
    }
};

// Console welcome message
console.log(`
🏠 Bangalore House Price Predictor
🚀 Version 1.0.0
💫 Powered by Machine Learning

Performance Metrics Available:
- console.log(performanceMetrics)

API Endpoints:
- Health: ${API_BASE_URL}/health
- Predict: ${API_BASE_URL}/predict

Built with ❤️ and lots of ☕
`);

// Add easter egg
let clickCount = 0;
document.querySelector('.logo').addEventListener('click', function() {
    clickCount++;
    if (clickCount === 5) {
        showNotification('🎉 Easter egg found! You clicked the logo 5 times!', 'success');
        createCelebrationEffect();
        clickCount = 0;
    }
});

// Add keyboard shortcuts info
document.addEventListener('keydown', function(e) {
    if (e.key === 'F1') {
        e.preventDefault();
        showNotification(`
            ⌨️ Keyboard Shortcuts:
            • Ctrl + Enter: Submit form
            • Escape: Close modals
            • F1: Show this help
        `, 'info');
    }
});

// Add smooth scrolling for better UX
document.documentElement.style.scrollBehavior = 'smooth';