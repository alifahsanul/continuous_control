import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def episode_reach_req(scores_np, requirement):
    diff_sign = np.sign(window_score - requirement)
    cond = (diff_sign>0).squeeze()
    index = np.where(cond)
    index = index[0][0]
    return index

scores_df = pd.read_csv('./checkpoint1/scores.csv')
scores = scores_df.values

window_score_df = pd.DataFrame(np.vstack((np.zeros((100,1)), scores))).rolling(100).mean()
window_score = window_score_df.values[100:]

fig, ax=plt.subplots(dpi=200)
plt.plot(np.arange(1, len(scores)+1), scores, c='b', label='Score per episode')
plt.plot(np.arange(1, len(window_score)+1), window_score, c='r', label='Avg score for 100 eps')
plt.ylim(0,)
plt.xlim(0, len(window_score)+1)
plt.hlines(30, *plt.gca().get_xlim(), color='orange', label='Required score to pass')
index_passed = episode_reach_req(window_score, 30)
plt.vlines(index_passed, 0, 30, color='g')
plt.text(index_passed + 2, 25, 'Task completed \nat episode {}'.format(index_passed))
plt.ylabel('Score')
plt.xlabel('Episode #')
plt.title('Continuous control assignment score')
plt.legend()
plt.show()