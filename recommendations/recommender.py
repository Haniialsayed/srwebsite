import pandas as pd
from scipy import sparse
from sklearn.metrics.pairwise import cosine_similarity
import random
import warnings
warnings.filterwarnings('ignore')


def standardize(row):
    new_row = (row - row.mean()) / (row.max() - row.min())
    return new_row


def initial():
    # get data
    ratings = pd.read_excel(r'/Users/hanialsayed/PycharmProjects/srwebsite/recommendations/response to stress.xlsx'
                            , index_col=0)
    ratings = ratings.fillna(0)
    # print(ratings)

    ratings_std = ratings.apply(standardize)
    # print(ratings_std)

    # taking transpose to get similarity between users in the same rows
    user_similarity = cosine_similarity(ratings_std)
    # print(user_similarity)

    user_similarity_dataframe = pd.DataFrame(user_similarity, index=ratings.index, columns=ratings.index)
    # print(user_similarity_df)
    return ratings, user_similarity_dataframe


ratings, user_similarity_df = initial()
# let's make recommendations

# stress_value = 4


def get_stress_reduction_method(user, stress_value, user_similarity_df):
    mean_rating = 2.5
    similar_score = user_similarity_df[user] * (stress_value - mean_rating)  # 2.5 is the mean of the ratings
    similar_score = similar_score.sort_values(ascending=False)

    return similar_score[:10]


num = random.randint(1, 38)
user = f"User {num}"
# similar_users = get_stress_reduction_method(user, stress_value)
# users = similar_users.index.values.tolist()


def next_similarity(ratings, users):
    new_ratings = ratings.loc[users, :]
    new_ratings = new_ratings.fillna(0)
    new_ratings_std = new_ratings.apply(standardize)
    # print(new_ratings_std)

    nan_list = new_ratings_std.columns[new_ratings_std.isna().any()].tolist()
    for method in nan_list:
        new_ratings_std.drop([method], axis=1)

    for method in nan_list:
        new_ratings_std[method] = new_ratings_std.mean(axis=1)

    # taking transpose to get similarity between items in the same rows
    item_similarity = cosine_similarity(new_ratings_std.T)
    # print(item_similarity)

    item_similarity_df = pd.DataFrame(item_similarity, index=ratings.columns, columns=ratings.columns)
    # print(item_similarity_df)
    return item_similarity_df

# pearson correlation
"""item_similarity_df = user_ratings.corr(method='pearson')
print(item_similarity_df.head(50))"""


# let's make recommendations
def get_stress_reduction_recommendation(method, rating, item_similarity_df):
    mean_rating = 2.5
    similar_score = item_similarity_df[method] * (rating - mean_rating)
    similar_score = similar_score.sort_values(ascending=False)
    return similar_score


def change_recommendations(final_recommend_list):
    recommend_list = []
    for item in final_recommend_list:
        if item == "Drinking 3 litres of water daily":
            recommend_list.append("You need to increase your water intake because it'd help regulate your Cortizol level")
        elif item == 'Taking a walk':
            recommend_list.append('You need to take more walks because making walks a part of your daily routine ' \
                                 'helps reduce tension and promote feelings of calm')
        elif item == 'laughter':
            recommend_list.append('Laugh more. Laughter strengthens your immune system, boosts mood, diminishes pain, ' \
                                 'and protects you from the damaging effects of stress')
        elif item == 'Meditation':
            recommend_list.append('Do some meditation. Spending even a few minutes in meditation can restore your ' \
                                 'calm and inner peace')
        elif item == 'Talking to your colleague':
            recommend_list.append('Talk to a colleague instead of bottling up your frustration. [Venting] helps take ' \
                                 'the feelings out from inside of yourself, it helps you to process them.')
        elif item == 'Avoid Tobacco and nicotine':
            recommend_list.append('Avoid Tobacco and nicotine. Smoking isn’t a long-term stress reliever. Try taking ' \
                                 'a walk instead')
        elif item == 'Avoiding Procrastination':
            recommend_list.append('Avoid Procrastinating. The key to breaking out of the procrastination-stress loop ' \
                                 'is to focus on critical parts of your life where you repeatedly put things off and ' \
                                 'make small, doable changes to help you get things done and, in turn, stress less')
        elif item == 'Deep Breating.':
            recommend_list.append('Practice deep breathing. Breathing exercises can help you relax because they make ' \
                                 'your body feel like it does when you are already relaxed.')
        elif item == 'Yoga':
            recommend_list.append('Do some Yoga. Yoga combines many popular stress-reducing techniques, including ' \
                                 'exercise and learning to control the breath, clear the mind, and relax the body.')
        elif item == 'Taking a break to relax':
            recommend_list.append('Engage your support group. If you want to improve your mental health and your ' \
                                  'ability to combat stress, surround yourself with at least a few good friends and ' \
                                  'confidants.')
        elif item == 'Listening to music':
            recommend_list.append('Listen to soothing music. This makes for a relaxing experience and a great way to ' \
                                  'manage the everyday stresses that pop up in our lives.')
        elif item == 'Taking Yoghurt':
            recommend_list.append("Take more Yoghurt. Eating probiotic-rich yogurt twice a day for a month could " \
                                  "help relieve anxiety and stress by reducing activity in the brain's emotional region")
        elif item == 'Eating Eggs':
            recommend_list.append('Eat more eggs. They help reduce the risk of anxiety, symptoms of depression, and ' \
                                  'naturally aiding sleep.')
        elif item == 'Taking Green Tea supplement':
            recommend_list.append('Take Green Tea Supplement. Drinking green tea or taking a green tea extract is ' \
                                  'also an excellent way to help relieve that anxiety you might be feeling.')
        elif item == 'Eating Turkey':
            recommend_list.append('Eat More Turkey because it is filled with an amino acid called tryptophan. ' \
                                  'Tryptophan helps our body produce serotonin which makes us feel happy')
        elif item == 'Taking Oatmeal':
            recommend_list.append('Include Oatmeal into your diet. According to a review published in July 2018 in ' \
                                  'the journal Nutritional Neuroscience, a high-fiber diet may be linked with ' \
                                  'reduced anxiety, depression, and stress')
        elif item == 'Eating Vegetables':
            recommend_list.append('Include more vegetables into your diet. Green leafy vegetables like spinach ' \
                                  'contain folate, which produces dopamine, a pleasure-inducing brain chemical, ' \
                                  'helping you keep calm')
        elif item == 'Eating Citrus Fruits like Oranges and Grapefruit':
            recommend_list.append('Eat more Citrus like Oranges and Grapefruit because Vitamin C is shown to reduce ' \
                                  'cortisol, one of the stress hormones')
        elif item == 'Prayer':
            recommend_list.append('Pray more. Prayer helps reduce anxiety and increase hope')
        elif item == 'Taking time off':
            recommend_list.append('Take some time off work. We take less vacation, work longer days, and retire ' \
                                  'later in life. All of these factors combined to provide for a perfect "stress" ' \
                                  'storm.')
        elif item == 'Sleep well':
            recommend_list.append('Sleep well. This is the period of rest when the body repairs and restores itself. ' \
                                  'Not getting enough sleep can even make your anxiety worse.')
        elif item == 'Avoiding Caffeine':
            recommend_list.append('Avoid Caffeine. Caffeine can inhibit the absorption of adenosine, which calms the ' \
                                  'body. This can make you feel alert in the short run but cause sleep problems later.')
        elif item == "Don't work more than 7 hours":
            recommend_list.append("Don't overwork yourself. Don't play the role of the victim and wait for your boss " \
                                  "or your company to step in and make your health a priority.")
        elif item == 'Avoid Negativity':
            recommend_list.append('Avoid Negativity. Releasing grudges, negative perspectives, toxic relationships, ' \
                                  'and other vessels of negativity in your life may feel challenging at first, but ' \
                                  'once you have started to release your grip, letting go becomes increasingly more ' \
                                  'accessible.')
    return recommend_list


def remove_bad_data(selection_dict):
    for key in list(selection_dict):
        if key == 'Talking to your colleague':
            del selection_dict[key]
    return selection_dict


def recommend_frontpage(recommend_str):
    if recommend_str == "You need to increase your water intake because it'd help regulate your Cortizol level":
        recommend_str = "We hope you have increased your water intake?"
    elif recommend_str == 'You need to take more walks because making walks a part of your daily routine helps ' \
                          'reduce tension and promote feelings of calm':
        recommend_str = "We hope you have been taking walks?"
    elif recommend_str == 'Laugh more. Laughter strengthens your immune system, boosts mood, diminishes pain, and ' \
                          'protects you from the damaging effects of stress':
        recommend_str = "We hope you have been laughing more"
    elif recommend_str == 'Do some meditation. Spending even a few minutes in meditation can restore your calm and ' \
                          'inner peace':
        recommend_str = "Have you been doing some meditation"
    elif recommend_str == 'Talk to a colleague instead of bottling up your frustration. [Venting] helps take the ' \
                          'feelings out from inside of yourself, it helps you to process them.':
        recommend_str = "Have you been sharing your issues with your colleagues?"
    elif recommend_str == 'Avoid Tobacco and nicotine. Smoking isn’t a long-term stress reliever. Try taking a walk ' \
                          'instead':
        recommend_str = "Have you been staying away from Tobacco and nicotine?"
    elif recommend_str == 'Avoid Procrastinating. The key to breaking out of the procrastination-stress loop is to ' \
                          'focus on critical parts of your life where you repeatedly put things off and make small, ' \
                          'doable changes to help you get things done and, in turn, stress less':
        recommend_str = "Have you been avoiding procrastination in the office?"
    elif recommend_str == 'Practice deep breathing. Breathing exercises can help you relax because they make your ' \
                          'body feel like it does when you are already relaxed.':
        recommend_str = "Have you been practicing deep breathing?"
    elif recommend_str == 'Do some Yoga. Yoga combines many popular stress-reducing techniques, including exercise ' \
                          'and learning to control the breath, clear the mind, and relax the body.':
        recommend_str = "Have you been doing some Yoga exercise?"
    elif recommend_str == 'Engage your support group. If you want to improve your mental health and your ability to ' \
                          'combat stress, surround yourself with at least a few good friends and confidants.':
        recommend_str = "Have you been engaging your support group?"
    elif recommend_str == 'Listen to soothing music. This makes for a relaxing experience and a great way to manage ' \
                          'the everyday stresses that pop up in our lives.':
        recommend_str = "Have you been listening to soothing music?"
    elif recommend_str == 'Take more Yoghurt. Eating probiotic-rich yogurt twice a day for a month could help ' \
                          "relieve anxiety and stress by reducing activity in the brain's emotional region":
        recommend_str = "Have you been taking yoghurt?"
    elif recommend_str == 'Eat more eggs. They help reduce the risk of anxiety, symptoms of depression, and ' \
                          'naturally aiding sleep.':
        recommend_str = "Have you added more eggs to your daily diet?"
    elif recommend_str == 'Take Green Tea Supplement. Drinking green tea or taking a green tea extract is also an ' \
                          'excellent way to help relieve that anxiety you might be feeling.':
        recommend_str = "Have you been taking green tea supplement?"
    elif recommend_str == 'Eat More Turkey because it is filled with an amino acid called tryptophan. Tryptophan ' \
                          'helps our body produce serotonin which makes us feel happy':
        recommend_str = "Have you increased your turkey intake?"
    elif recommend_str == 'Include Oatmeal into your diet. According to a review published in July 2018 in the ' \
                          'journal Nutritional Neuroscience, a high-fiber diet may be linked with reduced anxiety, ' \
                          'depression, and stress':
        recommend_str = "Have you added oatmeal your breakfast?"
    elif recommend_str == 'Include more vegetables into your diet. Green leafy vegetables like spinach contain ' \
                          'folate, which produces dopamine, a pleasure-inducing brain chemical, helping you keep calm':
        recommend_str = 'Do you include more vegetables in your diet?'
    elif recommend_str == 'Eat more Citrus like Oranges and Grapefruit because Vitamin C is shown to reduce ' \
                          'cortisol, one of the stress hormones':
        recommend_str = "Have you been taking more citrus?"
    elif recommend_str == 'Pray more. Prayer helps reduce anxiety and increase hope':
        recommend_str = "Have you been praying more?"
    elif recommend_str == 'Take some time off work. We take less vacation, work longer days, and retire later in ' \
                          'life. All of these factors combined to provide for a perfect "stress" storm.':
        recommend_str = "Have you taken some time off from work?"
    elif recommend_str == 'Sleep well. This is the period of rest when the body repairs and restores itself. Not ' \
                          'getting enough sleep can even make your anxiety worse.':
        recommend_str = "Have you been sleeping well this past few days?"
    elif recommend_str == 'Avoid Caffeine. Caffeine can inhibit the absorption of adenosine, which calms the body. ' \
                          'This can make you feel alert in the short run but cause sleep problems later.':
        recommend_str = "We hope you've been avoiding caffeine"
    elif recommend_str == "Don't overwork yourself. Don't play the role of the victim and wait for your boss or " \
                          "your company to step in and make your health a priority.":
        recommend_str = "We hope you haven't been overworking yourself"
    elif recommend_str == 'Avoid Negativity. Releasing grudges, negative perspectives, toxic relationships, and ' \
                          'other vessels of negativity in your life may feel challenging at first, but once you ' \
                          'have started to release your grip, letting go becomes increasingly more accessible.':
        recommend_str = "We hope you have avoiding colleagues with bad vibes at the office"
    return recommend_str

"""
print(get_stress_reduction_recommendation("Listening to music", 4))

stress_reduction_user = [("Taking Yoghurt", 4), ("Taking Green Tea supplement", 3), ("Yoga", 5)]

similar_method = pd.DataFrame()

for method, rating in stress_reduction_user:
    similar_method = similar_method.append(get_stress_reduction_recommendation(method, rating), ignore_index=True)

similar_method.head()

similar_method.sum().sort_values(ascending=False)
"""