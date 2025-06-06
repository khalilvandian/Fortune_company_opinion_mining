# Social Media Analysis on Fortune 1000 Companies

This repository contains a project that analyzes how social media users perceive and engage with Fortune 1000 companies. The project leverages natural language processing (NLP) techniques to examine language patterns, sentiment, and behavioral cues in social media data.

## Introduction

Social media platforms offer valuable, unfiltered insights into people’s opinions and experiences. This project goes beyond basic sentiment analysis by examining the nuanced language and stereotypes people use when discussing companies. It applies behavioral theories, such as the Theory of Reasoned Action (Fishbein & Ajzen, 1980), to explore how attitudes and social norms influence perceptions of these companies.

The insights gained can inform marketing, branding, and customer relationship strategies in competitive markets.

## Data Acquisition and Exploration

- **Source:** Social media posts from Reddit and Twitter (X), collected between 3 February and 10 March 2025.
- **Main dataset:** [Kaggle Dataset](https://www.kaggle.com/datasets/jarredgaudineer/social-media-posts-fortune-1000-companies)
- **Enrichment data:** 2024 Fortune 1000 Companies list for industry and sector details.
- **Final dataset:** Merged file containing company name, ticker, sector, industry, post content, and source platform.

## Data Preprocessing

1. Masked frequently mentioned company names and tickers as `TargetedCompany`.
2. Removed mentions, links, emojis, non-English content, and duplicates.
3. Tokenization and lemmatization using spaCy for optimal results.
4. Created Bag-of-Words (BoW) vectors with a vocabulary of 1622 terms.

## Topic Modeling

**Method:** Latent Dirichlet Allocation (LDA)

- LDA assumes that each document is a mixture of topics, where each topic is a distribution of words.
- Determined optimal number of topics (20) based on coherence scores.
- Topics like “Health and Diseases” emerged only at higher topic counts, illustrating the importance of fine-tuning the model.
- Twitter posts focused mainly on finance and politics, while Reddit had a broader topic range.

## Personality Analysis with Big Five Traits

Building on Park et al. (2015), we inferred Big Five personality traits of commenters using the `KevSun/Personality_LM` model (RoBERTa-based, trained on PANDORA dataset).

- **Traits:** Openness, Conscientiousness, Extraversion, Agreeableness, Neuroticism
- **Model performance:** 0.80 accuracy and 0.78 F1-score.
- Trait scores were aggregated to create composite corporate profiles.
- Low variance observed in scores, likely due to dataset noise and aggregation limitations.

## Conclusion

- Dataset noise from homographs and broad company-based filtering introduced challenges.
- Aggregation by company and industry overlooked user-level differences.
- Future work should incorporate user-level metadata (e.g., social groups) to reveal deeper patterns.

## Future Considerations

- Incorporate semi-supervised topic modeling methods (e.g., Fraser et al., 2022) to refine topics and improve document categorization.
- Enhance personality analysis by adding user-level and social-group data to increase variance and reveal more nuanced findings.

## Sources

1. Fishbein, M., & Ajzen, I. (1980). *Predicting and understanding consumer behavior*.
2. Gaudineer, J. L., 2025. *Social Media Posts- Fortune 1000 Companies*.
3. Fraser, K. C., Kiritchenko, S., & Nejadgholi, I. (2022). *Extracting age-related stereotypes from social media texts*.
4. Park G. et al. (2015). *Automatic personality assessment through social media language*.
