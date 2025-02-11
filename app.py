import pandas as pd
import scipy.stats
import streamlit as st
import time

# these are stateful variables which are preserved as Streamlit reruns this script
if 'experiment_no' not in st.session_state:
    st.session_state['experiment_no'] = 0
if 'df_experiment_results' not in st.session_state:
    st.session_state['df_experiment_results'] = pd.DataFrame(columns=['no', 'iterations', 'mean'])

st.header('Tossing a Coin')

# Create a placeholder for chart
chart_placeholder = st.empty()

def toss_coin(n):
    trial_outcomes = scipy.stats.bernoulli.rvs(p=0.5, size=n)

    outcome_1_count = 0
    outcome_no = 0
    means = []  # List to store means for plotting

    # Loop through the outcomes and update chart data
    for r in trial_outcomes:
        outcome_no += 1
        if r == 1:
            outcome_1_count += 1
        mean = outcome_1_count / outcome_no
        means.append(mean)

        # Update the chart with the list of means
        chart_placeholder.line_chart(means)

        # Add a slight delay for smooth animation
        time.sleep(0.05)

    return means[-1]  # Return the final mean

# Add widgets for user input
number_of_trials = st.slider('Number of trials?', 1, 1000, 10)
start_button = st.button('Run')

if start_button:
    st.write(f'Running the experiment of {number_of_trials} trials.')
    st.session_state['experiment_no'] += 1
    final_mean = toss_coin(number_of_trials)
    
    # Add new results to the DataFrame
    st.session_state['df_experiment_results'] = pd.concat([
        st.session_state['df_experiment_results'],
        pd.DataFrame(data=[[st.session_state['experiment_no'],
                            number_of_trials,
                            final_mean]],
                     columns=['no', 'iterations', 'mean'])
        ],
        axis=0)
    st.session_state['df_experiment_results'] = \
        st.session_state['df_experiment_results'].reset_index(drop=True)

# Display the experiment results
st.write(st.session_state['df_experiment_results'])
