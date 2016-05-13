raw_votes = []

def save_vote(vote):
    """Save a vote"""
    global raw_votes
    raw_votes.append(vote.lower())
    print(raw_votes)

def get_vote_counts(votes):
    vote_counts = []
    vanilla_votes = votes.count('vanilla')
    vote_counts.append(vanilla_votes)
    chocolate_votes = votes.count('chocolate')
    vote_counts.append(chocolate_votes)
    strawberry_votes = votes.count('strawberry')
    vote_counts.append(strawberry_votes)
    return vote_counts

def get_vote_percent(total, counts):
    flavors_and_percent = []
    flavors_and_percent.append({'flavor': 'vanilla', 'percentage': round(counts[0] / total, 2)})
    flavors_and_percent.append({'flavor': 'chocolate', 'percentage': round(counts[1] / total, 2)})
    flavors_and_percent.append({'flavor': 'strawberry', 'percentage': round(counts[2] / total, 2)})
    print(flavors_and_percent)
    return flavors_and_percent

def get_summary():
    global raw_votes
    total_votes = len(raw_votes)
    counts = get_vote_counts(raw_votes)
    flavor_to_percent = get_vote_percent(total_votes, counts)
    return flavor_to_percent
