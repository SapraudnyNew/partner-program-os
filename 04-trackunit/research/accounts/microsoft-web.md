# Microsoft (web digest, scoped: marketplace/ISV, Dynamics 365 FS + F&O, Manufacturing & Mobility, Copilot agents)

Researched: 2026-07-03. Scope: what a construction-IoT ISV like Trackunit (IrisX, credit consumption metric) can plug into.

## Snapshot

- Microsoft Corporation, HQ Redmond, WA, USA. Public (NASDAQ: MSFT), ~228,000 employees (per FY2025 filings).
- FY2025 revenue (fiscal year ended June 30, 2025): $281.7B, up 15%. Operating income $128.5B. Azure surpassed $75B revenue, up 34%.
- Partner-facing structure that matters here: the commercial marketplace and ISV programs sit under the Global Partner Solutions organization; Dynamics 365 Field Service and Finance & Operations under Business Applications engineering; construction adjacency lives in the Manufacturing & Mobility industry cloud team.

## Why now signals

- Marketplace unification (Sept 2025): Azure Marketplace and AppSource merged into a single "Microsoft Marketplace" with one Partner Center listing flow and 6M+ monthly unique visitors. A dedicated "AI Apps" category launched in 2026 for AI-native applications.
- App Accelerate (announced Ignite Nov 2025, launching 2026): unifies ISV Success, Marketplace Rewards, and co-sell resources into one pathway, with early co-sell access no longer gated only by the $100K revenue threshold.
- 2026 MACC expansion: more marketplace purchase types count toward customers' Azure committed spend, enlarging the buyer pool for ISV listings. Multiparty private offers (MPO, selling with channel partners) are GA.
- Dynamics 365 2026 release wave 1 (Apr-Sep 2026) is explicitly agentic: AI agents across sales, service, finance, supply chain. Notably, D365 Finance adds support for rental-based business models (tracking rental assets, revenue, related processes). Inference: this is directly relevant to Trackunit's rental-company customer base and to work-order/billing data flows IrisX could feed.
- D365 Field Service wave 1 2026: Scheduling Operations Agent (AI resource-to-work matching), mobile technician improvements, deeper ties to Finance & Operations and Project Operations.
- Manufacturing & Mobility team is pushing "agentic era" messaging (Mar 2026 blog: simulations, AI agents, physical AI in supply chain; Factory Operations Agent on Azure AI; manufacturing data solutions in Microsoft Fabric). Construction is not called out as a separate industry cloud; it is folded into Manufacturing & Mobility (inference from Microsoft's industry site structure).
- Copilot monetization shifted to consumption: custom agents billed via Copilot Credits; M365 E7 suite (GA May 2026) bundles Agent 365 seats. Inference: Microsoft's credit-consumption model for agents mirrors Trackunit's IrisX credit metric, making a co-sell narrative easy to align.

## Hiring signals

- Microsoft careers and LinkedIn show a steady pipeline of ISV Partner Development Manager roles inside Global Partner Solutions: "Partner Development Manager - ISV", "ISV Partner Development Manager, Data & AI" (posted 2025), "ISV Partner Development Manager (Strategic Recruit)", "Partner Development Manager (ISV Business Applications)", and regional PDM ISV roles. Pattern: dedicated motions for recruiting strategic ISVs, with Data & AI and Business Applications as named specializations.
- Certification signal: the D365 Field Service Functional Consultant cert (MB-240) retired June 30, 2026, replaced by AI-focused certifications. Inference: Microsoft is reskilling the Field Service ecosystem toward agents rather than classic configuration.
- No public evidence of a construction-specific industry team hiring; construction ISV engagement would route through Manufacturing & Mobility industry PDMs and the ISV Success/App Accelerate programs (inference).

## Integration-relevant facts

- Entry points for Trackunit: (1) Microsoft Marketplace listing (transactable offer, MACC-eligible after unification) via ISV Success / App Accelerate; (2) a Dynamics 365 Field Service integration (work orders, assets, IoT alerts); (3) a Copilot agent or MCP server surfaced in the M365 Agent Store.
- Connected Field Service (IoT-to-work-order): Azure IoT Hub remains the out-of-box path; Azure Time Series Insights retired July 2024, and several legacy Field Service integrations were deprecated after Oct 30, 2025. Field Service supports custom IoT providers, i.e. third-party telematics platforms can push device events that trigger work orders. Inference: the deprecations create whitespace for a construction telematics ISV to be the equipment-data provider into Field Service.
- MCP support is now mainstream: GA in Copilot Studio (agents can consume MCP servers through connector infrastructure with VNet, DLP, auth controls), GA for declarative agents in M365 Copilot, and MCP support documented for finance and operations apps. Build 2026 added remote MCP servers, agent-to-agent (A2A) GA, computer-using agents GA. Trackunit already positions IrisX so AI agents (Copilot named explicitly, alongside Claude/GPT/Gemini) can access construction data; an IrisX MCP server consumable by Copilot Studio is the natural technical bridge (inference on the bridge, fact on both sides existing).
- Agent Store in M365 Copilot is the distribution surface for partner agents; ISV agents are billed via Copilot Credits (consumption), which requires publishing through Partner Center.
- No Trackunit listing found on AppSource/Azure Marketplace and no formal Trackunit-Microsoft partnership announcement found (checked; Trackunit runs its own marketplace of ~third-party ConTech integrations instead).
- Program names to reference: ISV Success, App Accelerate, Marketplace Rewards, Azure IP co-sell, multiparty private offers, MACC eligibility, Copilot Studio + MCP connectors, Agent Store, Microsoft Cloud for Manufacturing (Manufacturing data solutions in Fabric, Factory Operations Agent).

## Sources

- https://techcommunity.microsoft.com/blog/marketplace-blog/your-next-big-move-thriving-in-the-reimagined-microsoft-marketplace/4470199
- https://www.automatum.io/blog-posts/microsoft-marketplace-2026-changes
- https://learn.microsoft.com/en-us/partner-center/membership/faq-isvsuccess
- https://www.microsoft.com/en-us/dynamics-365/blog/business-leader/2026/03/18/2026-release-wave-1-plans-for-microsoft-dynamics-365-microsoft-power-platform-and-copilot-studio-offerings/
- https://learn.microsoft.com/en-us/dynamics365/release-plan/2026wave1/
- https://learn.microsoft.com/en-us/dynamics365/release-plan/2026wave1/enterprise-resource-planning/dynamics365-finance/
- https://www.hubsite365.com/en-ww/crm-pages/power-tips-dynamics-365-field-service-2026-release-wave-1.htm
- https://learn.microsoft.com/en-us/dynamics365/field-service/deprecations-field-service
- https://learn.microsoft.com/en-us/dynamics365/field-service/cfs-custom-iot-provider
- https://learn.microsoft.com/en-us/industry/release-plan/2025wave1/cloud-manufacturing/
- https://www.microsoft.com/en-us/industry/blog/manufacturing-and-mobility/2026/03/24/supply-chain-2-0-how-microsoft-is-powering-simulations-ai-agents-and-physical-ai/
- https://www.microsoft.com/en-us/microsoft-copilot/blog/copilot-studio/model-context-protocol-mcp-is-now-generally-available-in-microsoft-copilot-studio/
- https://devblogs.microsoft.com/microsoft365dev/build-declarative-agents-for-microsoft-365-copilot-with-mcp/
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/copilot/copilot-mcp
- https://learn.microsoft.com/en-us/microsoft-365/copilot/copilot-agent-store
- https://blog.cloudfactorygroup.com/posts/microsoft-build-2026-recap-ai-agents-and-the-new-partner-opportunity
- https://jobs.careers.microsoft.com/global/en/job/1817264 (ISV PDM Data & AI; plus roles 1801926, 1471475, 1368306)
- https://www.microsoft.com/en-us/investor/earnings/fy-2025-q4/performance
- https://trackunit.com/irisx/integrations/
- https://trackunit.com/marketplace/
