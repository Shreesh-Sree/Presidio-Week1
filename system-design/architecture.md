# Developer Productivity Analytics Platform

DevInsight-Lab started as a simple idea: collect GitHub activity and show useful engineering metrics. Initially I only had users, APIs, a database, and a cache in mind. After reviewing `qz.pdf`, I decided to make the design a little more realistic by adding webhook ingestion, async processing, audit logs, RBAC, and observability.

This is still a Week-1 design, so I am not pretending every component is implemented. The goal is to show how I would think about the system if this learning project grew into a real platform.

## Design Goals

- Ingest GitHub events for commits, pull requests, reviews, branches, and CI checks.
- Process events asynchronously so GitHub webhooks receive fast acknowledgements.
- Provide dashboards for team productivity, review quality, contributor activity, and repository health.
- Preserve auditability for raw events and derived analytics.
- Keep the system scalable, secure, observable, and fault tolerant.

## Assumptions

- GitHub is the first source of activity data.
- PostgreSQL is enough for Week-1 because the data is relational.
- Redis is used for cache and queue-like workflows in the design, although a production system might use a dedicated message broker.
- Metrics can be a few seconds delayed. I chose this tradeoff because async processing makes ingestion more reliable.

## High-Level Architecture

```text
                    +-----------------------------+
                    | Users                       |
                    | Developers / Leads / Mentors|
                    +--------------+--------------+
                                   |
                                   v
                    +-----------------------------+
                    | Edge Layer                  |
                    | DNS / WAF / Load Balancer   |
                    +--------------+--------------+
                                   |
                                   v
                    +-----------------------------+
                    | API Gateway                 |
                    | Rate Limits / Routing       |
                    +------+----------------------+
                           |
          +----------------+----------------+
          |                                 |
          v                                 v
+-------------------+            +------------------------+
| Dashboard API     |            | Webhook Ingestion API  |
| Query Metrics     |            | GitHub Event Receiver  |
+---------+---------+            +-----------+------------+
          |                                  |
          v                                  v
+-------------------+            +------------------------+
| Auth + RBAC       |            | Signature Validator    |
| Tenant Access     |            | Idempotency Check      |
+---------+---------+            +-----------+------------+
          |                                  |
          |                                  v
          |                       +------------------------+
          |                       | Event Queue            |
          |                       | Redis Streams / Jobs   |
          |                       +-----------+------------+
          |                                   |
          v                                   v
+-------------------+            +------------------------+
| Cache             |<-----------| Analytics Engine       |
| Hot Dashboards    |            | Aggregations / Scoring |
+---------+---------+            +-----------+------------+
          |                                  |
          v                                  v
+-------------------+            +------------------------+
| PostgreSQL        |            | Observability          |
| System of Record  |            | Logs / Metrics / Traces|
+-------------------+            +------------------------+
```

## Layered Architecture

| Layer | Responsibility |
| --- | --- |
| Client Layer | Web dashboard, mentor review views, API consumers |
| Edge Layer | DNS, WAF, DDoS protection, load balancing |
| Authentication Layer | JWT validation, GitHub OAuth, RBAC for teams and repositories |
| Control Plane | Dashboard API, repository configuration, organization settings |
| Ingestion Layer | GitHub webhook receiver, HMAC validation, event normalization |
| Async Processing Layer | Queue-based processing for commits, PRs, reviews, and CI events |
| Analytics Layer | Aggregates productivity metrics and stores dashboard-ready summaries |
| Data Layer | PostgreSQL, Redis cache, audit/event storage |
| Observability Layer | Metrics, logs, traces, alerts, and audit reports |

## Core Services

### Dashboard API

Serves read-heavy views:

- `GET /teams/{team_id}/activity`
- `GET /repositories/{repository_id}/health`
- `GET /developers/{developer_id}/productivity`
- `GET /pull-requests/review-cycle`

### Webhook Ingestion API

Receives GitHub webhook events and returns quickly. It validates HMAC signatures, stores raw event payloads, applies idempotency keys, and publishes normalized events to the queue.

I decided to separate ingestion from analytics because webhook endpoints should not do heavy work. If GitHub sends many events quickly, the API can still accept them and workers can process them at their own pace.

### Analytics Engine

Consumes queue events and updates metrics:

- Commits per developer
- Pull requests opened, approved, merged, and closed
- Average reviews per PR
- Review turnaround time
- Repository review load
- CI pass/fail rate
- Open PR aging buckets

### Policy Service

Controls access to productivity metrics. For example, an intern can view their own metrics, a mentor can view assigned interns, and an engineering lead can view team-level summaries.

I added this because productivity data can be sensitive. Not every user should see every developer's detailed metrics.

### Audit Log

Stores raw webhook event references, metric recalculation events, role changes, and dashboard export activity. Auditability matters because productivity data can influence performance conversations.

## Event Processing Sequence

```text
GitHub
  |
  | POST /webhooks/github
  v
Webhook Ingestion API
  |
  | Verify HMAC signature
  | Check delivery ID for idempotency
  | Store raw payload
  v
Event Queue
  |
  | Worker consumes event
  v
Analytics Engine
  |
  | Update normalized tables
  | Recompute affected aggregates
  | Refresh cache keys
  v
Dashboard API
  |
  | Serve latest productivity metrics
  v
Users
```

## Data Flow

```text
GitHub Event JSON
      |
      v
Raw Event Store ----------------------+
      |                               |
      v                               v
Normalized Tables              Audit Log
developers                     event_id
repositories                   actor
commits                        action
pull_requests                  timestamp
reviews                        checksum
      |
      v
Analytics Tables
daily_developer_metrics
repository_review_metrics
pull_request_cycle_metrics
      |
      v
Redis Cache
      |
      v
Dashboard
```

## Database Design Fit

The SQL project already defines the core operational tables:

- `developers`
- `repositories`
- `commits`
- `pull_requests`
- `reviews`

In a larger production version, the platform would add:

- `raw_events` for immutable webhook payload records
- `ci_checks` for build status analytics
- `daily_developer_metrics` for precomputed dashboard summaries
- `audit_logs` for sensitive access and recalculation history

## Caching Strategy

Redis caches expensive read models:

- Team activity for the last 7, 14, and 30 days
- Top contributors by repository
- Review decision distribution
- Pull request aging buckets
- Repository health summaries

Cache keys should include tenant, repository, metric name, and time range:

```text
tenant:42:repo:devinsight-api:metric:review-summary:range:30d
```

Cache invalidation happens when related GitHub events are processed.

One issue with caching is freshness. I am assuming it is acceptable if dashboard data is slightly delayed after a commit or review event.

## Scalability Strategy

- Keep API servers stateless and horizontally scalable.
- Return `202 Accepted` from webhook ingestion after validation and enqueueing.
- Use queue depth to autoscale analytics workers.
- Partition high-volume event tables by month.
- Add read replicas for dashboard-heavy workloads.
- Precompute common analytics instead of recomputing every dashboard request.

## Security Strategy

The PDF emphasized defense in depth; DevInsight-Lab applies that principle to engineering analytics:

- HMAC verification for GitHub webhooks
- OAuth or SSO for dashboard users
- RBAC at organization, team, and repository level
- Row-level authorization for sensitive developer metrics
- Encrypted database storage and secrets management
- Audit logs for metric exports and permission changes
- Rate limiting to prevent API abuse

I did not include advanced sandbox execution in the main design because this platform is mostly reading and aggregating GitHub activity. If future versions allow custom scripts or plugins, sandboxing would become more important.

## Observability

The platform should expose:

- Webhook request latency and failure rate
- Queue depth and worker lag
- Analytics job duration
- Dashboard API p95 latency
- Cache hit ratio
- Database query latency
- Failed event processing count

Logs, metrics, and traces should share correlation IDs so one GitHub delivery can be followed from ingestion to dashboard update.

## Fault Tolerance

- Webhook events are stored before async processing.
- Analytics workers are idempotent and can retry failed jobs.
- Dead-letter queues preserve events that fail repeatedly.
- Cache failure degrades performance but does not corrupt data.
- Database backups protect historical metrics.
- Read replicas reduce the impact of dashboard traffic spikes.

## High Availability

```text
                 +-------------------+
                 | Global Load       |
                 | Balancer          |
                 +---------+---------+
                           |
        +------------------+------------------+
        |                  |                  |
        v                  v                  v
+---------------+  +---------------+  +---------------+
| AZ-1 API +    |  | AZ-2 API +    |  | AZ-3 API +    |
| Worker Nodes  |  | Worker Nodes  |  | Worker Nodes  |
+-------+-------+  +-------+-------+  +-------+-------+
        |                  |                  |
        +------------------+------------------+
                           |
                           v
                 +-------------------+
                 | PostgreSQL Primary|
                 | + Read Replicas   |
                 +-------------------+
```

Recovery goals for a production version:

- RPO: near zero for committed database transactions
- RTO: under 30 minutes for regional failover
- Graceful degradation: dashboards can show last computed metrics if workers are delayed

## CI/CD Architecture

```text
Developer
   |
   v
GitHub Push / Pull Request
   |
   v
GitHub Actions
   |
   +--> Repository structure validation
   +--> Python syntax checks
   +--> SQL linting in future iteration
   +--> Unit tests in future iteration
   |
   v
Merge to main after review
```

In a production deployment, the pipeline would add dependency scanning, container builds, image signing, staging deployment, smoke tests, and production promotion.

## Basic System Design Tradeoffs

| Decision | Benefit | Tradeoff |
| --- | --- | --- |
| Async webhook processing | Fast GitHub acknowledgement and better reliability | More moving parts |
| PostgreSQL as source of truth | Strong joins and relational integrity | Needs indexing and query tuning |
| Redis cache | Fast dashboard reads | Cache invalidation complexity |
| Precomputed metrics | Stable dashboard performance | Delayed freshness by seconds or minutes |
| RBAC on analytics | Safer productivity data access | More authorization logic |

## What I Would Improve Next

- Add a small working webhook receiver.
- Store raw events in the SQL schema.
- Add a `ci_checks` table for build pass/fail analytics.
- Add a dashboard wireframe.
- Compare Redis Streams with a dedicated queue like Kafka or SQS.
- Add concrete API request and response examples.

## Final Design Summary

After testing the idea against the PDF reference, I noticed the design became much stronger once I treated GitHub events as a real ingestion pipeline instead of just static data. The final design combines GitHub ingestion, async analytics, relational storage, caching, observability, CI/CD, and access control. It is not production complete, but it is a realistic direction for a Week-1 system design project.
