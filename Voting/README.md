# Voting Rules Assignment

A Python exercise to implement a suite of voting rules based on a `Preference` object. This assignment is divided into two parts: implementation of voting rule functions (Part 1) and peer feedback (Part 2).

## Requirements

- Implement the following functions in `voting.py`, each taking a `Preference` object (with methods `candidates()`, `voters()`, `get_preference(candidate, voter)`) and relevant parameters:
  - **`dictatorship(preferences, agent) -> int`**
  - **`scoring_rule(preferences, score_vector, tie_break) -> int`**
  - **`plurality(preferences, tie_break) -> int`**
  - **`veto(preferences, tie_break) -> int`**
  - **`borda(preferences, tie_break) -> int`**
  - **`STV(preferences, tie_break) -> int`**
- Tie-breaking: use the specified agent’s ranking to break score ties
- Error handling:
  - Invalid dictator agent → `ValueError`
  - Wrong-length score vector → `ValueError`
- Protect any test code within an `if __name__ == "__main__":` guard so import into CodeGrade tests works correctly


## Plagiarism & Integrity

- Follow University of Liverpool academic integrity guidelines
- Complete the Academic Integrity Tutorial and Quiz
- CodeGrade will check submissions for plagiarism and collusion

## Disclaimer

This project was developed as a homework assignment for a University of Liverpool class. Do not redistribute or represent as original work.

