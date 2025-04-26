def dictatorship(preferences, agent):
    '''
    Implements the Dictatorship voting rule.
    The winner is the candidate ranked highest by the specified dictator agent.

    :param preferences: Preference object containing voter rankings.
    :param agent: The agent whose preferences dictate the winner.
    :return: The candidate ranked highest by the agent.
    :raises ValueError: If the agent is not a valid voter.

    '''
    # Get the list of voters
    voters = preferences.voters()
    # Check if the agent index is valid
    if agent not in voters:
        raise ValueError(f"Agent {agent} not valid.")

    # Get the candidates and find the one ranked highest by the agent
    candidates = preferences.candidates()
    top_candidate = min(candidates, key=lambda c: preferences.get_preference(c, agent))
    return top_candidate


def scoring_rule(preferences, score_vector, tie_break):
    """
    Implements a general scoring rule voting system.
    Each candidate receives a score based on a predefined scoring vector applied
    to their ranks in each voter's preferences.

    :param preferences: Preference object containing voter rankings.
    :param score_vector: List of scores corresponding to candidate ranks.
    :param tie_break: The tie-breaking agent to resolve ties.
    :return: The winning candidate.
    :raises ValueError: If the score vector length does not match the number of candidates.
    """
    # Get the list of candidates and voters
    candidates = preferences.candidates()
    voters = preferences.voters()

    score_vector = sorted(score_vector, reverse=True)
    # Check if the score vector length matches the number of candidates
    if len(score_vector) != len(candidates):
        raise ValueError("Score vector length does not match the number of candidates.")

    # Initialize a score dictionary
    scores = {candidate: 0 for candidate in candidates}

    # Calculate scores for each candidate based on all voters
    for voter in voters:
        for candidate in candidates:
            rank = preferences.get_preference(candidate, voter)
            scores[candidate] += score_vector[rank]

    # Find the candidate(s) with the highest score
    max_score = max(scores.values())
    top_candidates = [c for c in candidates if scores[c] == max_score]

    # Use tie-breaking if necessary
    if len(top_candidates) > 1:
        # Tie-break using the tie_break agent's preferences
        return min(
            top_candidates, key=lambda c: preferences.get_preference(c, tie_break)
        )

    # Return the winner
    return top_candidates[0]


def plurality(preferences, tie_break):
    """
    Implements the Plurality voting rule.
    The candidate with the most first-place votes wins.

    :param preferences: Preference object containing voter rankings.
    :param tie_break: The tie-breaking agent to resolve ties.
    :return: The winning candidate.
    """
    # Get the list of candidates and voters
    candidates = preferences.candidates()
    voters = preferences.voters()

    # Count first-place votes
    first_place_votes = {candidate: 0 for candidate in candidates}
    for voter in voters:
        top_candidate = min(
            candidates, key=lambda c: preferences.get_preference(c, voter)
        )
        first_place_votes[top_candidate] += 1

    # Find the candidate(s) with the most votes
    max_votes = max(first_place_votes.values())
    top_candidates = [c for c in candidates if first_place_votes[c] == max_votes]

    # Use tie-breaking if necessary
    if len(top_candidates) > 1:
        # Tie-break using the tie_break agent's preferences
        return min(
            top_candidates, key=lambda c: preferences.get_preference(c, tie_break)
        )

    # Return the winner
    return top_candidates[0]


def veto(preferences, tie_break):
    """
    Implements the Veto voting rule.
    Each voter awards points to all candidates except their least-preferred one.

    :param preferences: Preference object containing voter rankings.
    :param tie_break: The tie-breaking agent to resolve ties.
    :return: The winning candidate.
    """
    # Get the list of candidates and voters
    candidates = preferences.candidates()
    voters = preferences.voters()

    # Initialize scores
    scores = {candidate: 0 for candidate in candidates}

    # Assign points based on veto rule
    for voter in voters:
        least_preferred = max(
            candidates, key=lambda c: preferences.get_preference(c, voter)
        )
        for candidate in candidates:
            if candidate != least_preferred:
                scores[candidate] += 1

    # Find the candidate(s) with the highest score
    max_score = max(scores.values())
    top_candidates = [c for c in candidates if scores[c] == max_score]

    # Use tie-breaking if necessary
    if len(top_candidates) > 1:
        # Tie-break using the tie_break agent's preferences
        return min(
            top_candidates, key=lambda c: preferences.get_preference(c, tie_break)
        )

    # Return the winner
    return top_candidates[0]


def borda(preferences, tie_break):
    """
    Implements the Borda Count voting rule.
    Each candidate receives points based on their position in each voter's ranking.

    :param preferences: Preference object containing voter rankings.
    :param tie_break: The tie-breaking agent to resolve ties.
    :return: The winning candidate.
    """
    # Get the list of candidates and voters
    candidates = preferences.candidates()
    voters = preferences.voters()

    # Initialize scores
    scores = {candidate: 0 for candidate in candidates}

    # Assign Borda scores
    for voter in voters:
        for candidate in candidates:
            rank = preferences.get_preference(candidate, voter)
            scores[candidate] += len(candidates) - 1 - rank

    # Find the candidate(s) with the highest score
    max_score = max(scores.values())
    top_candidates = [c for c in candidates if scores[c] == max_score]

    # Use tie-breaking if necessary
    if len(top_candidates) > 1:
        # Tie-break using the tie_break agent's preferences
        return min(
            top_candidates, key=lambda c: preferences.get_preference(c, tie_break)
        )

    # Return the winner
    return top_candidates[0]


def STV(preferences, tie_break):
    """
    Implements the Single Transferable Vote (STV) rule.
    Candidates with the fewest first-choice votes are sequentially eliminated.
    If a tie occurs, it is resolved using the tie-breaking agent.

    :param preferences: Preference object containing voter rankings.
    :param tie_break: The tie-breaking agent to resolve ties.
    :return: The winning candidate.
    """
    winners = list(preferences.candidates())
    voters = preferences.voters()  # List of all voters
    while len(winners) > 1:
        score = {candidate: 0 for candidate in winners}
        for voter in voters:
            for candidate in winners:
                if preferences.get_preference(candidate, voter) == 0:
                    score[candidate] += 1
        if min(score.values()) != max(score.values()):
            for candidate in winners:
                if score[candidate] == min(score.values()):
                    winners.remove(candidate)
        else:
            return min(winners, key=lambda c: preferences.get_preference(c, tie_break))
    return winners[0]
