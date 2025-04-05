// Text Animation
const rotatingTexts = [
    "Promoting Culture and Heritage",
    "Supporting Our Community",
    "Educational Workshops and Events",
    "Join Us and Get Involved"
];

let currentTextIndex = 0;
const rotatingTextElements = document.querySelectorAll('#rotating-text-language, #rotating-text-video, #rotating-text-football');

function updateRotatingText() {
    rotatingTextElements.forEach(element => {
        element.textContent = rotatingTexts[currentTextIndex];
    });
    currentTextIndex = (currentTextIndex + 1) % rotatingTexts.length;
}

setInterval(updateRotatingText, 3000); // Change text every 3 seconds

// Dynamic Content Update
const dynamicContentLanguage = document.getElementById('dynamic-content-language');
const dynamicContentVideo = document.getElementById('dynamic-content-video');
const dynamicContentFootball = document.getElementById('dynamic-content-football');

const dynamicContents = [
    '<img src="{{ url_for(\'static\', filename=\'images/event1.jpg\') }}" alt="Event 1">',
    '<img src="{{ url_for(\'static\', filename=\'images/event2.jpg\') }}" alt="Event 2">',
    '<video src="{{ url_for(\'static\', filename=\'videos/event.mp4\') }}" controls></video>',
    '<p>Upcoming Event: Cultural Festival</p>'
];

let currentContentIndex = 0;

function updateDynamicContent() {
    dynamicContentLanguage.innerHTML = dynamicContents[currentContentIndex];
    dynamicContentVideo.innerHTML = dynamicContents[currentContentIndex];
    dynamicContentFootball.innerHTML = dynamicContents[currentContentIndex];
    currentContentIndex = (currentContentIndex + 1) % dynamicContents.length;
}

setInterval(updateDynamicContent, 5000); // Change content every 5 seconds