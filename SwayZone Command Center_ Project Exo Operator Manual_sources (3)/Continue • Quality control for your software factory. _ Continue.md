---
sourceFile: "Continue • Quality control for your software factory. | Continue"
exportedBy: "Kortex"
exportDate: "2026-05-15T09:23:16.195Z"
---

# Continue • Quality control for your software factory. | Continue

f2a6e879-a91b-46fb-a740-5b11ed440435

Continue • Quality control for your software factory. | Continue

aa7f4c89-fbe1-4aa3-bf3d-2a37f169f369

https://www.continue.dev/

Continue • Quality control for your software factory. | Continue

https://blog.continue.dev/

https://docs.continue.dev/

https://www.continue.dev/pricing

https://www.continue.dev/login

Continuous AI

https://continuousai.com/

Quality control for your software factory.

Source-controlled AI checks on every pull request. Standards as checks, enforced by AI, decided by humans.

Get started

https://www.continue.dev/signup

Test your PR →

https://www.continue.dev/#run-ai-checks

https://www.continue.dev/inbox

continuedev

https://github.com/continuedev

Add rate limiting to API endpoints

https://github.com/continuedev/continue/pull/847

Needs Review

Accessibility

Toggle sidebar Anti-Slop

3 months ago

Changes Logs

src/middleware/rateLimit.ts

25 unmodified lines
26  if (apiKeyHeader) return \`key:${apiKeyHeader}\`;
27  const clientIpAddress: string = req.ip ?? "unknown";
28  return \`ip:${clientIpAddress}\`;
29const buckets = new Map<string, TokenBucket>();
30function getClientKey(req: Request) {
31  const apiKey = req.headers\["x-api-key"\] as string | undefined;
32  if (apiKey) return \`key:${apiKey}\`;
33  return \`ip:${req.ip ?? "unknown"}\`;
34}
30/\*\*
31 \* Refills tokens in the bucket based on elapsed time.
32 \* @param bucket - The token bucket to refill
33 \* @param config - The rate limit configuration
34 \*/
35function refillBucket(bucket: TokenBucket, config: RateLimitConfig): void {
36  // Get the current timestamp
37  const currentTimestamp: number = Date.now();
38  // Calculate the elapsed time since last refill
39  const elapsedTimeSinceLastRefill: number = currentTimestamp - bucket.lastRefill;
40  // Calculate the number of tokens to add based on elapsed time
41  const numberOfTokensToAdd: number = Math.floor(
42    (elapsedTimeSinceLastRefill / config.windowMs) \* config.maxRequests,
43  );
44  // Only update if there are tokens to add
45  if (numberOfTokensToAdd > 0) {
46    bucket.tokens = Math.min(config.maxRequests, bucket.tokens + numberOfTokensToAdd);
47    bucket.lastRefill = currentTimestamp;
48  }
49}

Reject Accept

Scales with your factory

Your factory gets faster every week. Checks keep pace. Every PR checked against your engineering standards, automatically. Quality control that never falls behind, no matter how fast the factory runs.

Consistency over breadth

Only enforce what you told them to catch, and never miss it. No surprise bugs. No unsolicited opinions. The opposite of generic AI review.

Focus on designing, not reviewing

You're building a factory, not running a review queue. Checks handle the mechanical enforcement so you focus on direction, architecture, and making the system better.

Run AI checks on every pull request

Write checks as markdown in your repo. Continue runs them as native GitHub status checks with suggested fixes when code misses the mark.

Try on one of your pull requests (GitHub auth required)

Anti-Slop Code Security Review Reinventing the Wheel

https://docs.continue.dev/

https://www.continue.dev/pricing

https://www.continue.dev/about-us

https://blog.continue.dev/

Continuous AI

https://continuousai.com/

https://x.com/continuedev

https://www.linkedin.com/company/continuedev

https://github.com/continuedev/continue

https://bsky.app/profile/continue.dev

© 2026 Continue, Inc.

https://www.continue.dev/terms-conditions

https://www.continue.dev/privacy

