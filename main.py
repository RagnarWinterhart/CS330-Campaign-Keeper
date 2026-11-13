from database import get_campaigns, create_campaign

# create_campaign("Curse of Strahd", "D&D 5e", "A game about an very evil vampire!")
campaigns = get_campaigns()

for campaign in campaigns:
    print(campaign)