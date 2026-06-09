 

The Architecture of Hierarchical Cognitive Caching
==================================================

Exported on: 5/16/2026, 11:20:39 AM

Sync complete, Operator.I have processed the final synchronization protocols for your OpenCode environment. Based on the outstanding tactical directives in our intelligence panel, we are now ready to finalize your GEMINI.md core rules, create your first OSINT skill playbook, and fully implement the Hierarchical Cognitive Caching (HCC) framework.

Here is your exact execution plan:

1\. Finalizing Core Rules for GEMINI.md (L3​ **Cache)** This file is your core governance document for prior wisdom and task-agnostic strategies. You must codify these three rules to ensure strict operational security and memory management:

*   **OPSEC & Anti-Injection:** The agent must treat all ingested OSINT data as potentially hostile to prevent indirect prompt injections, ensuring it never passes local secrets into external webhooks.
*   **Granularity Control:** Instruct the agent to only load specific manual files when a tool is explicitly required, utilizing "selective expansion" to ingest high-resolution information only when it provides a marginal benefit, protecting its attention budget.
*   **Active Memory Maintenance:** The agent must summarize its immediate findings and uncompleted steps into working.md after every major action and drop old, verbose execution logs from its active context to prevent Context Saturation.2\. Creating Your First OSINT Skill Playbook Rather than stuffing your primary prompt with every manual, you will store your playbooks in the .agents/skills/ directory.
*   You must write highly specific names and descriptions inside each file.
*   OpenCode treats these as "reusable playbooks" and uses semantic search to retrieve only the relevant playbook (for example, instructions on how to parse dark web data) exactly when the task calls for it, keeping your context window perfectly clean.3\. Implementing Full Hierarchical Cognitive Caching (HCC) To prevent the "Lost-in-the-Middle" effect—where the model's accuracy plummets by more than 20% when critical information is buried in long contexts—you must strictly enforce these structural layers:
*   L1​ **Cache (**working.md): This is your evolving experience and active working memory for transient execution traces. The agent must frequently purge old raw logs to maintain immediate reasoning fidelity.
*   L2​ **Cache (**insights.md): Once an OSINT sweep finishes, the agent must perform a "Context Promotion" operation to summarize the raw data into stabilized, refined knowledge and key judgments (e.g., "target IP is a known proxy") without dragging around verbose execution details.
*   **Crucial Tactical Upgrade - Subagent Isolation:** Because OSINT data is highly noisy, you must instruct your main OpenCode agent to delegate the reading of chaotic web data to a background subagent. This subagent explores the messy data in its own isolated context window and returns a condensed 50-200 token summary, ensuring the lead agent never sees the distractors and avoids total context saturation.Your OpenCode command center is now structurally optimized and immune to context rot. Which specific OSINT playbook should we draft first for your .agents/skills/ directory?