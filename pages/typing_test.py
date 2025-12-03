import streamlit as st
import streamlit.components.v1 as components
import random
from wordgetter import get_random_word

# Page config
st.set_page_config(page_title="Typing Test", page_icon="⌨️", layout="wide")

# Back to Dashboard button
if st.button("⬅️ Back to Dashboard"):
    st.switch_page("dashboard.py")

# Title
st.title("⌨️ Typing Test")
st.markdown("---")

# Generate words for the test
num_words = 100
test_words = " ".join(get_random_word(num_words))

# HTML/CSS/JavaScript for real-time typing test
html_code = f"""
<!DOCTYPE html>
<html>
<head>
    <style>
        body {{
            font-family: monospace;
            background: #1e1e1e;
            color: #fff;
            padding: 20px;
            max-width: 800px;
            margin: 0 auto;
        }}
        
        #timer {{
            text-align: center;
            font-size: 1.5em;
            margin-bottom: 20px;
            color: #4CAF50;
        }}
        
        #stats {{
            display: flex;
            justify-content: space-around;
            margin-bottom: 30px;
            padding: 15px;
            background: #2d2d2d;
            border-radius: 8px;
        }}
        
        .stat {{
            text-align: center;
        }}
        
        .stat-value {{
            font-size: 1.8em;
            color: #4CAF50;
        }}
        
        .stat-label {{
            color: #888;
            font-size: 0.9em;
        }}
        
        #text-display {{
            font-size: 1.3em;
            line-height: 1.8em;
            padding: 25px;
            background: #2d2d2d;
            border-radius: 8px;
            margin-bottom: 15px;
            outline: none;
        }}
        
        .char {{
            color: #666;
        }}
        
        .char.correct {{
            color: #fff;
        }}
        
        .char.incorrect {{
            color: #f44336;
        }}
        
        .char.current {{
            border-left: 2px solid #4CAF50;
        }}
        
        .instructions {{
            text-align: center;
            color: #888;
            font-size: 0.9em;
        }}
        
        #results {{
            display: none;
            text-align: center;
            padding: 30px;
            background: #2d2d2d;
            border-radius: 8px;
        }}
        
        #results.show {{
            display: block;
        }}
        
        #results h2 {{
            color: #4CAF50;
            margin-bottom: 20px;
        }}
        
        .final-stats {{
            display: flex;
            justify-content: space-around;
            margin: 20px 0;
        }}
        
        .final-stat-value {{
            font-size: 2.5em;
            color: #4CAF50;
        }}
        
        .final-stat-label {{
            color: #888;
        }}
        
        button {{
            background: #4CAF50;
            color: white;
            border: none;
            padding: 12px 30px;
            font-size: 1em;
            border-radius: 5px;
            cursor: pointer;
            margin-top: 15px;
        }}
        
        button:hover {{
            background: #45a049;
        }}
    </style>
</head>
<body>
    <div id="timer">Time: 30s</div>
    
    <div id="stats">
        <div class="stat">
            <div class="stat-value" id="wpm">0</div>
            <div class="stat-label">WPM</div>
        </div>
        <div class="stat">
            <div class="stat-value" id="accuracy">100</div>
            <div class="stat-label">Accuracy</div>
        </div>
        <div class="stat">
            <div class="stat-value" id="errors">0</div>
            <div class="stat-label">Errors</div>
        </div>
    </div>
    
    <div id="text-display" tabindex="0"></div>
    
    <div class="instructions">Click above and start typing!</div>
    
    <div id="results">
        <h2>Test Complete! 🎉</h2>
        <div class="final-stats">
            <div>
                <div class="final-stat-value" id="final-wpm">0</div>
                <div class="final-stat-label">WPM</div>
            </div>
            <div>
                <div class="final-stat-value" id="final-accuracy">0</div>
                <div class="final-stat-label">Accuracy</div>
            </div>
            <div>
                <div class="final-stat-value" id="final-errors">0</div>
                <div class="final-stat-label">Errors</div>
            </div>
        </div>
        <button onclick="location.reload()">Try Again</button>
    </div>
    
    <script>
        const targetText = "{test_words}";
        let currentIndex = 0;
        let errors = 0;
        let startTime = null;
        let timerInterval = null;
        let timeLeft = 30;
        let testActive = false;
        
        const textDisplay = document.getElementById('text-display');
        const wpmEl = document.getElementById('wpm');
        const accuracyEl = document.getElementById('accuracy');
        const errorsEl = document.getElementById('errors');
        const timerEl = document.getElementById('timer');
        const resultsDiv = document.getElementById('results');
        const statsDiv = document.getElementById('stats');
        
        // Initialize
        textDisplay.innerHTML = targetText.split('').map((char, i) => 
            `<span class="char${{i === 0 ? ' current' : ''}}">${{char}}</span>`
        ).join('');
        textDisplay.focus();
        
        // Handle typing
        textDisplay.addEventListener('keydown', (e) => {{
            if (!testActive) {{
                testActive = true;
                startTime = Date.now();
                timerInterval = setInterval(() => {{
                    timeLeft--;
                    timerEl.textContent = `Time: ${{timeLeft}}s`;
                    if (timeLeft <= 0) endTest();
                }}, 1000);
            }}
            
            if (e.key.length === 1 || e.key === 'Backspace') e.preventDefault();
            
            const chars = textDisplay.querySelectorAll('.char');
            
            if (e.key === 'Backspace' && currentIndex > 0) {{
                currentIndex--;
                chars[currentIndex].className = 'char current';
                if (chars[currentIndex + 1]) chars[currentIndex + 1].className = 'char';
            }} else if (e.key.length === 1 && currentIndex < targetText.length) {{
                chars[currentIndex].className = e.key === targetText[currentIndex] ? 'char correct' : 'char incorrect';
                if (e.key !== targetText[currentIndex]) errors++;
                currentIndex++;
                if (currentIndex < targetText.length) chars[currentIndex].className = 'char current';
                
                const elapsed = (Date.now() - startTime) / 1000 / 60;
                const wpm = Math.round((currentIndex / 5) / elapsed);
                const accuracy = Math.round(((currentIndex - errors) / currentIndex) * 100) || 100;
                
                wpmEl.textContent = wpm;
                accuracyEl.textContent = accuracy;
                errorsEl.textContent = errors;
                
                if (currentIndex >= targetText.length) endTest();
            }}
        }});
        
        textDisplay.addEventListener('click', () => textDisplay.focus());
        
        function endTest() {{
            clearInterval(timerInterval);
            const elapsed = (Date.now() - startTime) / 1000 / 60;
            const wpm = Math.round((currentIndex / 5) / elapsed);
            const accuracy = Math.round(((currentIndex - errors) / currentIndex) * 100) || 100;
            
            document.getElementById('final-wpm').textContent = wpm;
            document.getElementById('final-accuracy').textContent = accuracy;
            document.getElementById('final-errors').textContent = errors;
            
            textDisplay.style.display = 'none';
            statsDiv.style.display = 'none';
            timerEl.style.display = 'none';
            resultsDiv.className = 'show';
        }}
    </script>
</body>
</html>
"""

# Display the typing test
components.html(html_code, height=600, scrolling=False)
