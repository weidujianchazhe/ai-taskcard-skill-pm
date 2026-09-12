# Report generation spec (report\)

> Data pull and format for daily / weekly reports. Generated on demand; the output settles under the existing protocol.

## 1. Data sources

| Report element | Source |
|---|---|
| Current progress | STATE (human-read zone + current progress) |
| What was done today/this week | reports\ (by date range) + INDEX (recent rows) |
| Details | the corresponding reports files (along the INDEX handoff column) |
| Next step / risks | STATE decision points + task card Key points |

## 2. Format (concise)

### Daily report

```
Date / what was done / result / next step / risks (one line each)
```

### Weekly report

```
This week's summary (progress/completed items/decisions) + next week's plan (task cards) + risks and items to be confirmed
```

## 3. Conventions

- A report does not copy the full handoff text, only a summary (data pull + aggregation)
- After generation register it in INDEX (`[done]` or `[handoff]`), and store it in reports\ when necessary
- Frequency and trigger: per the manager's need or schedule\ scheduled tasks
