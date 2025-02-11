import scipy.stats
import streamlit as st
import time

st.header('Tossing a Coin')

# Store progress in a list
progress = []

# Create a line chart
chart = st.line_chart(progress)

def toss_coin(n):
    trial_outcomes = scipy.stats.bernoulli.rvs(p=0.5, size=n)

    outcome_1_count = 0
    outcome_no = 0

    # Loop through the outcomes and update chart data
    for r in trial_outcomes:
        outcome_no += 1
        if r == 1:
            outcome_1_count += 1
        mean = outcome_1_count / outcome_no
        
        # Append the mean to the progress list for chart update
        progress.append(mean)
        
        # Redraw the chart with updated progress
        chart.line_chart(progress)
        
        # Add a slight delay for smooth animation
        time.sleep(0.05)

    return mean

# Add widgets
number_of_trials = st.slider('Number of trials?', 1, 1000, 10)
start_button = st.button('Run')

if start_button:
    st.write(f'Running the experiment of {number_of_trials} trials.')
    toss_coin(number_of_trials)
    toss_coin(number_of_trials)
