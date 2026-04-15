// Element selections
const landingSection = document.getElementById('landing-section');
const mainInterface = document.getElementById('main-interface');
const startBtn = document.getElementById('start-btn');
const predictionForm = document.getElementById('prediction-form');

const initialMessage = document.getElementById('initial-message');
const outputSection = document.getElementById('output-section');
const yieldResult = document.getElementById('yield-result');
const summaryList = document.getElementById('summary-list');
const resetBtn = document.getElementById('reset-btn');

let npkChart = null; // Store chart instance

// 1. Transition to App
startBtn.addEventListener('click', () => {
    landingSection.classList.add('hidden');
    mainInterface.classList.remove('hidden');
});

// 2. Handle Form Submission
predictionForm.addEventListener('submit', (e) => {
    e.preventDefault();

    // Gather inputs
    const rain = parseFloat(document.getElementById('rainfall').value);
    const temp = parseFloat(document.getElementById('temperature').value);
    const hum = parseFloat(document.getElementById('humidity').value);
    const n = parseFloat(document.getElementById('nitrogen').value);
    const p = parseFloat(document.getElementById('phosphorus').value);
    const k = parseFloat(document.getElementById('potassium').value);

    // Provide a mock machine learning "prediction" (Math formula just for show)
    // Formula purely for demonstration purposes to generate a realistic looking number
    let baseYield = 2.5; 
    let prediction = baseYield + (temp * 0.02) + (rain * 0.005) + ((n + p + k) * 0.003) - (Math.abs(hum - 60) * 0.01);
    
    // Hardcoded format based on instructions: "🌾 Predicted Yield: 3.5 tons/hectare"
    // Using simple formatting to look good.
    const finalYield = Math.max(0.5, prediction).toFixed(2);
    yieldResult.innerText = finalYield;

    // Show output section
    initialMessage.classList.add('hidden');
    outputSection.classList.remove('hidden');
    resetBtn.classList.remove('hidden');

    // Update Enhancements (Input Summary)
    summaryList.innerHTML = `
        <li><strong>Rainfall:</strong> ${rain} mm</li>
        <li><strong>Temperature:</strong> ${temp} °C</li>
        <li><strong>Humidity:</strong> ${hum} %</li>
        <li><strong>NPK Ratio:</strong> ${n} : ${p} : ${k}</li>
    `;

    // Render Small Chart
    renderChart(n, p, k);
});

// 3. Reset Application
resetBtn.addEventListener('click', () => {
    predictionForm.reset();
    
    // Reset slider displays
    document.getElementById('rain-val').textContent = '150';
    document.getElementById('temp-val').textContent = '25';
    document.getElementById('hum-val').textContent = '60';

    outputSection.classList.add('hidden');
    resetBtn.classList.add('hidden');
    initialMessage.classList.remove('hidden');
});

// 4. Charting Logic
function renderChart(n, p, k) {
    const ctx = document.getElementById('npkChart').getContext('2d');
    
    // Destroy existing chart if user predicts multiple times
    if (npkChart) {
        npkChart.destroy();
    }

    npkChart = new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: ['Nitrogen (N)', 'Phosphorus (P)', 'Potassium (K)'],
            datasets: [{
                data: [n, p, k],
                backgroundColor: [
                    '#4caf50', // Green
                    '#ff9800', // Orange
                    '#2196f3'  // Blue
                ],
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    position: 'right',
                    labels: {
                        boxWidth: 12
                    }
                }
            }
        }
    });
}
