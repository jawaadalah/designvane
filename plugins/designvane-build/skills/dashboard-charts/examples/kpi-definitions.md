# Gold standard — KPI definitions excerpt

## Active subscribers
- Definition: accounts with a paid plan at 00:00 UTC today, excluding trials
  and accounts in dunning > 7 days.
- Display: value + delta vs 30 days ago. Up is good.
- Source: billing.subscriptions (daily snapshot).

## Churn risk
- Definition: % of active subscribers with no login in 21+ days.
- Display: percentage to 1 decimal + count. Up is BAD — delta shown in
  danger color only when rising, with the word "worse" in the label.
- Empty state (new product, < 30 days of data): "Not enough history yet —
  this card activates after 30 days of snapshots."
