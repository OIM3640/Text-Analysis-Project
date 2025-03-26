# Text-Analysis-Project

Please read the [instructions](instructions.md).

1. Project Overview

This initiative explored the intriguing nexus between classic literature and current news. A lively stream of current Diwali news stories that I gathered from a News API and the classic book "The Dawn and the Day; Or, The Buddha and the Christ, Part I" from Project Gutenberg were the two different sources I combined. My objective was to use word frequency analysis and fuzzy matching algorithms' nuanced power to reveal hidden relationships between these seemingly unrelated texts. I aimed to investigate whether some themes or language persisted across the ages, emphasizing the possibility of communication between historical narratives and contemporary situations.

2. Implementation

The project has three major components: data retrieval, text processing, and analysis. Data retrieval was handled by the access_api function, which extracts article content from both sources. BeautifulSoup was used for HTML parsing, making it easier to identify certain portions like the "Introduction" in the Project Gutenberg text. During the analysis phase, thefuzz library was used to compute fuzzy matching ratios such as similarity, partial, and token sort ratios. These three ratios gave nuanced information about how closely the two texts aligned.

One key design decision was to use many fuzzy matching algorithms to ensure extensive comparisons. While fuzz.ratio() calculates similarity directly, fuzz.token_sort_ratio() ignores word order, which is useful for comparing texts with rearranged word sequences. GenAI tools made it easier to learn about various fuzzy matching approaches and the best ways to use them.

3. Results

When comparing the modern news snippet "Millions of Indians celebrate Diwali, the festival of lights" to the historic text "The Dawn and the Day; Or, The Buddha and the Christ, Part I," the fuzzy matching results revealed a moderate connection. The similarity ratio of 37, partial ratio of 44, and token sort ratio of 42 suggested that, while both works discussed culture and philosophy, their vocabulary and organization varied greatly.

The word frequency analysis revealed this disparity even further. The current article used words like "Diwali," "light," and "festival," showing its emphasis on a lively celebration. In contrast, the original text used more words like "men," "age," and "peace," indicating an examination of ageless human characteristics and philosophical issues. These contrasts in word choice and emphasis successfully reflect each text's unique focus, highlighting the contrast between a current celebration and a timeless philosophical investigation.
4. Reflection

This project, which was originally scheduled for a speedier turnaround, was delayed due to the requirement to install new libraries for proper analysis of varied source materials. The purpose was to comprehend the differences between a recent news story about Diwali and a historic literary work, "The Dawn and the Day; Or, The Buddha and the Christ, Part I," from Project Gutenberg. This entailed regularly iterating and ensuring that the API was working properly while accessing and printing articles to test each feature.

The project effectively combined fuzzy matching with word frequency analysis. Text normalization presented a substantial problem because formatting discrepancies had an impact on similarity ratings. This was solved by performing preprocessing techniques such as punctuation removal and lowercase transformation, resulting in uniform text data.

The primary takeaway was the significance of using appropriate text-processing methods to gain relevant insights. GenAI technologies made complex algorithms easier to understand and troubleshoot. Moving forward, objectives include improving tokenization and maybe introducing more advanced language models for richer comparisons. Looking back, having a better understanding of text normalization techniques and a structured testing approach to validate each component's output would have been advantageous.