"""
Market-Making & Betting-Game Simulator

Assembled from your step-by-step solutions.
"""

import numpy as np

# Step 1 - expected_value
def expected_value(values, probabilities):
    # TODO: return the expected value of the discrete distribution (values, probabilities).

    expVal = 0
    for i in range(0, len(values)):
        expVal += values[i] * probabilities[i]
    return expVal

# Step 2 - one_reroll_die_value
import math
def one_reroll_die_value(sides):
    # TODO: return {'value': expected winnings under optimal reroll policy, 'reroll_faces': sorted faces to reroll}
    threshold = (sides + 1)/2
    values = [0] * sides
    probabilities = [1/sides] * sides
    for i in range(1, sides + 1):
        if i < threshold:
            values[i - 1] = threshold
        else:
            values[i - 1] = i
    value = expected_value(values, probabilities)
    reroll_faces = list(range(1, math.ceil(threshold)))
    return {'value' : value, 'reroll_faces' : reroll_faces}

# Step 3 - pay_per_reroll_die_game
def pay_per_reroll_die_game(sides, reroll_cost):
    # TODO: return {'threshold': t, 'value': V} for the pay-per-reroll die game under the optimal threshold policy.
    t_star = 0
    v_star = 0
    for t in range(1, sides + 1):
        v = (t + sides) / 2 - reroll_cost * (t - 1) / (sides - t + 1)
        if v > v_star:
            t_star = t
            v_star = v
    return {'threshold': t_star, 'value': v_star}

# Step 4 - red_black_card_game_value (not yet solved)
# TODO: implement

# Step 5 - make_quotes (not yet solved)
# TODO: implement

# Step 6 - execute_trade (not yet solved)
# TODO: implement

# Step 7 - mark_to_market_pnl (not yet solved)
# TODO: implement

# Step 8 - adverse_selection_loss (not yet solved)
# TODO: implement

# Step 9 - uncertainty_spread (not yet solved)
# TODO: implement

# Step 10 - inventory_skewed_quotes (not yet solved)
# TODO: implement

# Step 11 - update_fair_value_from_trade (not yet solved)
# TODO: implement

# Step 12 - update_remaining_card_value (not yet solved)
# TODO: implement

# Step 13 - run_market_making_episode (not yet solved)
# TODO: implement

# Step 14 - summarize_episode_pnls (not yet solved)
# TODO: implement

