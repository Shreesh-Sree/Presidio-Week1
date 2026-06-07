INSERT INTO developers VALUES
(1, 'Anika Rao', 'anika-rao', 'Platform', '2026-01-08'),
(2, 'Mateo Chen', 'mateochen', 'Developer Experience', '2026-01-12'),
(3, 'Priya Shah', 'priyashah', 'Analytics', '2026-02-01'),
(4, 'Noah Williams', 'noahw', 'Platform', '2026-02-18'),
(5, 'Isha Menon', 'ishamenon', 'Developer Experience', '2026-03-02');

INSERT INTO repositories VALUES
(1, 'devinsight-api', 'Platform', '2026-03-01'),
(2, 'devinsight-analytics', 'Analytics', '2026-03-04'),
(3, 'devinsight-web', 'Developer Experience', '2026-03-08');

INSERT INTO commits VALUES
(1, 1, 1, 'a1c9f2', 'Add activity ingestion endpoint', 120, 12, '2026-06-01 09:30:00'),
(2, 1, 2, 'b42e10', 'Validate pull request payloads', 84, 5, '2026-06-01 10:15:00'),
(3, 2, 3, 'f8d331', 'Implement review aggregation job', 170, 22, '2026-06-02 11:00:00'),
(4, 2, 1, 'c02a77', 'Tune analytics query builder', 95, 31, '2026-06-02 13:40:00'),
(5, 3, 5, 'd903ac', 'Create productivity dashboard layout', 210, 44, '2026-06-03 09:10:00'),
(6, 1, 4, 'e72bd0', 'Add repository health checks', 61, 9, '2026-06-03 15:25:00'),
(7, 3, 2, 'ab3491', 'Connect dashboard to review metrics', 132, 18, '2026-06-04 10:30:00'),
(8, 2, 3, 'ff92bc', 'Add cache-aware metric refresh', 77, 16, '2026-06-04 16:45:00'),
(9, 1, 1, '19bd01', 'Refactor commit event parser', 54, 41, '2026-06-05 08:55:00');

INSERT INTO pull_requests VALUES
(1, 1, 1, 'Add GitHub event ingestion API', 'MERGED', '2026-06-01 09:45:00', '2026-06-01 17:00:00'),
(2, 2, 3, 'Aggregate review cycle metrics', 'APPROVED', '2026-06-02 11:30:00', NULL),
(3, 3, 5, 'Build dashboard summary cards', 'OPEN', '2026-06-03 09:25:00', NULL),
(4, 1, 4, 'Add health check endpoint', 'MERGED', '2026-06-03 15:50:00', '2026-06-04 09:00:00'),
(5, 3, 2, 'Wire review metrics into UI', 'CLOSED', '2026-06-04 11:00:00', NULL);

INSERT INTO reviews VALUES
(1, 1, 2, 'APPROVED', 'API contract is clear and testable.', '2026-06-01 14:10:00'),
(2, 1, 3, 'COMMENTED', 'Consider storing raw webhook payload for audit.', '2026-06-01 15:20:00'),
(3, 2, 1, 'CHANGES_REQUESTED', 'Metric names need consistency with dashboard labels.', '2026-06-02 14:00:00'),
(4, 2, 4, 'APPROVED', 'Aggregation shape looks production ready.', '2026-06-02 16:30:00'),
(5, 3, 2, 'COMMENTED', 'Card spacing should match the design system.', '2026-06-03 13:00:00'),
(6, 4, 1, 'APPROVED', 'Health checks are small and reliable.', '2026-06-03 18:00:00'),
(7, 5, 5, 'CHANGES_REQUESTED', 'Dashboard state handling needs a loading path.', '2026-06-04 14:45:00');

