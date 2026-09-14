-- Sanctions Screening & Compliance Analytics
-- 1 Potential matches
SELECT * FROM sanctions_screening_alerts ORDER BY screening_risk_score DESC;
-- 2 True matches
SELECT * FROM sanctions_screening_alerts WHERE disposition='True Match';
-- 3 False positives
SELECT * FROM sanctions_screening_alerts WHERE disposition='False Positive';
-- 4 Escalations
SELECT * FROM sanctions_screening_alerts WHERE disposition='Escalated';
-- 5 High match scores
SELECT * FROM sanctions_screening_alerts WHERE name_match_score >= 85 ORDER BY name_match_score DESC;
-- 6 Country mismatch review
SELECT * FROM sanctions_screening_alerts WHERE country_match=0 AND name_match_score >= 80;
-- 7 Programs
SELECT sanctions_program, COUNT(*) alerts FROM sanctions_screening_alerts GROUP BY sanctions_program ORDER BY alerts DESC;
-- 8 Country exposure
SELECT screened_country, COUNT(*) alerts, SUM(flagged_amount) flagged_amount FROM sanctions_screening_alerts GROUP BY screened_country ORDER BY flagged_amount DESC;
-- 9 False-positive rate
SELECT disposition, COUNT(*) alerts FROM sanctions_screening_alerts GROUP BY disposition;
-- 10 Screening volume by counterparty
SELECT counterparty_id, screening_volume, flagged_amount FROM sanctions_screening_alerts ORDER BY flagged_amount DESC;
-- 11 High-risk queue
SELECT * FROM sanctions_screening_alerts WHERE risk_level IN ('High','Critical') ORDER BY screening_risk_score DESC;
-- 12 Monthly trend
SELECT DATE_TRUNC('month', alert_date) month, COUNT(*) alerts FROM sanctions_screening_alerts GROUP BY DATE_TRUNC('month',alert_date) ORDER BY month;
