from try_gsdmm import *
# Import wordcloud library
from wordcloud import WordCloud

# Get topic word distributions from gsdmm model
cluster_word_distribution = gsdmm.cluster_word_distribution

# Select topic you want to output as dictionary (using topic_number)
topic_dict = sorted(cluster_word_distribution[topic_number].items(), key=lambda k: k[1], reverse=True)[:values]

# Generate a word cloud image
wordcloud = WordCloud(background_color='#fcf2ed',
                            width=1800,
                            height=700,
                            font_path=path_to_font,
                            colormap='flag').generate_from_frequencies(topic_dict)

# Print to screen
fig, ax = plt.subplots(figsize=[20,10])
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off");

# Save to disk
wordcloud_24.to_file(path_to_file)