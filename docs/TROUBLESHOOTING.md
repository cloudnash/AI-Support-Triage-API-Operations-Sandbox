# 🛠️ Operations & Troubleshooting Runbook

This guide is designed for L1/L2 Support and DevOps teams handling escalations from the AI Support Triage API. 

## 1. Monitoring Logs for API Debugging
If a user reports that the AI agent is returning a `500 Internal Error` or timing out, follow these steps to isolate the issue:

1. **Access the deployment environment:** SSH into the target EC2 instance or access the container orchestration dashboard (e.g., Kubernetes/ECS).
2. **Pull the latest Docker logs:**
   ```
   docker logs --tail 100 support-api | grep ERROR
   ```
3. Common Resolution: If the logs indicate Failed to process ticket: Timeout, verify that the upstream AI service API keys haven't expired or hit their rate limits in the provider dashboard.

## 2. CI/CD Pipeline Failures

If the GitHub Actions pipeline (ci.yml) fails on a new pull request:

- Navigate to the Actions tab in GitHub.
- Check the Verify Docker Build step.
-Common Resolution: Ensure no new dependencies added to app/requirements.txt are causing version conflicts with the base python:3.9-slim image.

## 3. Customer Communication Template (SaaS Support)
When reaching out to users regarding failed AI triages, use this empathy-driven structure:

"Hi <UserName>, we noticed your recent deployment request to the AI agent experienced a timeout. Our monitoring tools indicate a temporary latency spike with our upstream API. We have reset your connection state—could you please attempt the deployment workflow once more? Let us know if the issue persists, and we will escalate this immediately.
